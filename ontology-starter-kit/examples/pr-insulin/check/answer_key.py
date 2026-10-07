# Applies PR Insulin Distributors' rules to the CSVs and asserts every outcome the deck shows (slides 15, 18, 19)
# plus the finance and procurement follow-up questions.
import pandas as pd
from datetime import datetime, timedelta
R = lambda f: pd.read_csv("../data/pr-insulin-" + f, keep_default_na=False)
sites, routes, cust = R("sites.csv"), R("routes.csv"), R("customers.csv")
sup, prod, inv = R("suppliers.csv"), R("products.csv"), R("inventory.csv")
orders, con, opp = R("orders.csv"), R("contracts.csv"), R("opportunities.csv")
NOW = datetime(2026, 10, 20, 6, 0); LANDFALL = NOW + timedelta(hours=48); ZONE = {"S"}
fmt = lambda t: t.strftime("%a %b %d, %I:%M %p").replace(" 0", " ")
out = []; P = out.append
s = sites.set_index("site_id")
zone_sites = {i for i, r in zip(sites.site_id, sites.region) if r in ZONE}; assert zone_sites == {"PON"}
pi = inv.merge(prod, on="sku"); pon = pi[pi.site_id == "PON"]
cold = pon[pon.stor == "CLD"]; ctl = pon[pon.stor == "CTL"]

P("SLIDE 15: Can Carolina DC receive the controlled stock from Ponce?")
free = lambda i: s.loc[i, "vault_cap_plt"] - s.loc[i, "vault_used_plt"]
assert s.loc["CAR", "lic_st"] == 40 and s.loc["MAY", "lic_st"] == 10
assert free("CAR") == 18 and free("MAY") == 7 and ctl.plt.sum() == 4 and s.loc["CAR", "gen_h"] == 120
P(f"  Bare trap: Carolina has the most vault space ({free('CAR')} pallets free) and {s.loc['CAR','gen_h']} hours of fuel.")
P(f"  With the ontology: No. Carolina lic_st=40, renewal pending [Rule-03]. Mayagüez lic_st=10, {free('MAY')} vault pallets free, needs {ctl.plt.sum()}.")

P("\nSTORM TEST: What is our business continuity plan, and what do we need to do in the next 48 hours?")
P(f"  Now {fmt(NOW)} | Landfall {fmt(LANDFALL)}")
# Rule-05 notice or pay
d05 = LANDFALL - timedelta(hours=36)
c = con.merge(cust, on="account_id")
r05 = c[(c.terms == "STD-H") & ((c.home_site.isin(zone_sites)) | (c.region.isin(ZONE)))]
assert len(r05) == 6 and d05 == NOW + timedelta(hours=12)
cap = 0.10 * r05.mvol_usd.sum(); assert cap == 186000
P(f"  Rule-05 notices due {fmt(d05)} on {len(r05)} STD-H contracts: " + ", ".join(f"{x.contract_id} {x.account}" for _, x in r05.iterrows()))
P(f"     Penalty exposure if notices miss (10% cap): ${cap:,.0f}")
# Rule-02 insulin stays cold
assert list(sites[sites.gen_h < 72].site_id) == ["PON"] and s.loc["PON", "gen_h"] == 36
d02 = LANDFALL - timedelta(hours=24)
insulin = cold[cold["product"].str.contains("Insulin")]
assert set(insulin.sku) == {"I-300", "I-310"} and insulin.plt.sum() == 5
cold_free = lambda i: s.loc[i, "cold_cap_plt"] - s.loc[i, "cold_used_plt"]
assert cold.plt.sum() == 9 and cold_free("MAY") == 12
P(f"  Rule-02 Insulin stays cold. Ponce has {s.loc['PON','gen_h']} hours of fuel. Move by {fmt(d02)}: cold {cold.plt.sum()} plt ({', '.join(cold.sku)}; insulin {insulin.plt.sum()} plt), controlled {ctl.plt.sum()} plt ({', '.join(ctl.sku)})")
# Rule-03 licensed destination
ok_ctl = [i for i in ["CAR","MAY"] if s.loc[i,"lic_st"] == 10 and s.loc[i,"gen_h"] >= 72 and free(i) >= ctl.plt.sum()]
assert ok_ctl == ["MAY"]
P(f"  Rule-03 controlled stock to Mayagüez only (Carolina lic_st=40). Mayagüez takes all of it: cold {cold_free('MAY')} plt free for {cold.plt.sum()}, vault {free('MAY')} free for {ctl.plt.sum()}")
# Rule-06 / Rule-01 dialysis before the mountain routes close
rt = dict(zip(routes.route_id, routes.mtn))
assert rt["RT-PK"] == "Y" and rt["RT-PM"] == "N"
o = orders.merge(prod[["sku","crit","stor"]], on="sku").merge(cust[["account_id","account","segment","route"]], on="account_id")
l1 = o[(o.site_id == "PON") & (o.crit == "L1")]
assert set(l1.segment) == {"DIAL"} and l1.account_id.nunique() == 9 and set(l1.due) == {"2026-10-21"}
mtn = l1[l1.route.map(rt) == "Y"].account.unique(); assert len(mtn) == 5
P(f"  Rule-01 + Rule-06 L1 orders from Ponce: {len(l1)} lines to 9 dialysis centers, all due Wed Oct 21.")
P(f"     Mountain routes close {fmt(d02)}. The 5 mountain centers go first: {', '.join(mtn)}")
P(f"     Bare-plan failure: delivering on the Wednesday due date reaches the mountains after the routes close.")
# Rule-04 reserve
l1_pon = pon[pon.crit == "L1"].groupby("sku").qty.sum(); reserve = (l1_pon * 0.20).round().astype(int)
need = l1.groupby("sku").qty.sum()
for k in l1_pon.index: assert l1_pon[k] - need.get(k, 0) >= reserve[k]
P("  Rule-04 hold for Red Municipal de Salud del Sur (CT-40): " + ", ".join(f"{k} {v}" for k, v in reserve.items()))

P("\nFINANCE: What does this storm do to our Q4 commit?")
f = opp.merge(cust[["account_id","segment","reg","home_site"]], on="account_id").merge(
    con[con.type == "VEH"][["contract_id","end_date"]].rename(columns={"contract_id":"vehicle_id"}), on="vehicle_id", how="left")
f["Rule-07"] = (f.amount_usd >= 100000) & (f.days_idle > 21)
f["Rule-08"] = (f.segment == "GOV") & (f.end_date.fillna("") != "") & (f.close_date > f.end_date.fillna("9999"))
f["Rule-09"] = (f.prod_line == "SRX") & (f.reg != "A")
f["rule"] = f["Rule-07"] | f["Rule-08"] | f["Rule-09"]
cm = f[f.fcst == "Commit"]; rep = cm.amount_usd.sum(); radj = cm[~cm.rule].amount_usd.sum()
cut = (LANDFALL + timedelta(days=30)).strftime("%Y-%m-%d")
slip = cm[(~cm.rule) & (cm.home_site.isin(zone_sites)) & (cm.close_date <= cut)]
sadj = radj - slip.amount_usd.sum(); assert (rep, radj, sadj) == (4200000, 2800000, 2300000)
P(f"  Reported ${rep/1e6:.1f}M -> rule-adjusted ${radj/1e6:.1f}M -> storm-adjusted ${sadj/1e6:.1f}M")
for _, x in cm[cm.rule].iterrows():
    P(f"     out {x.opp_id} {x.account} ${x.amount_usd:,} {[k for k in ['Rule-07','Rule-08','Rule-09'] if x[k]]}")
for _, x in slip.iterrows(): P(f"     slip {x.opp_id} {x.account} ${x.amount_usd:,} closes {x.close_date}")

P("\nPROCUREMENT: What do we reorder first, and from whom?")
onhand = inv.groupby("sku").qty.sum(); openq = orders.groupby("sku").qty.sum()
pr = prod.set_index("sku").copy()
pr["avail"] = onhand - openq.reindex(onhand.index).fillna(0) - reserve.reindex(onhand.index).fillna(0)
low = pr[pr.avail < pr.rop].copy(); low["cr"] = low.crit.str[1].astype(int); low["gap"] = low.avail / low.rop
low = low.sort_values(["cr", "gap"]); assert list(low.index) == ["E-400","D-100","V-500","M-900","G-800"]
sp = sup.set_index("supplier_id")
for k, x in low.iterrows():
    use = x.alt_supplier_id if sp.loc[x.supplier_id, "port"] == "PON" else x.supplier_id
    P(f"  {k} {x['product']}: avail {int(x.avail)} < rop {x.rop}. Order from {sp.loc[use,'supplier']} ({sp.loc[use,'port']}). Deliver to {'Mayagüez only [Rule-03]' if x.stor == 'CTL' else 'Carolina or Mayagüez'}")
open("answer-key.txt", "w", encoding="utf-8").write("\n".join(out) + "\n"); print("\n".join(out))
