# PR Insulin Distributors, Inc.: storm-test demo data. Fictional company. Every record is invented.
import csv
P = "pr-insulin-"

def write(name, header, rows):
    with open(P + name, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n"); w.writerow(header); w.writerows(rows)
    print(f"{P + name:36s} {len(rows):3d} rows")

sites = [  # site_id, site, town, region, lic_st, gen_h, cold_cap_plt, cold_used_plt, vault_cap_plt, vault_used_plt
    ("CAR", "Carolina DC", "Carolina", "MTR", 40, 120, 48, 30, 30, 12),
    ("PON", "Ponce DC", "Ponce", "S", 10, 36, 20, 9, 12, 4),
    ("MAY", "Mayagüez DC", "Mayagüez", "W", 10, 96, 16, 4, 10, 3),
]
routes = [  # route_id, from_site, serves, mtn, transit_h
    ("RT-PS", "PON", "South coast west: Ponce, Juana Díaz, Yauco, Peñuelas, Coamo", "N", 1.0),
    ("RT-PE", "PON", "South coast east: Santa Isabel, Guayama", "N", 1.5),
    ("RT-PC", "PON", "Central: Utuado, Jayuya, Adjuntas, Orocovis, Barranquitas, Aibonito", "Y", 3.0),
    ("RT-PM", "PON", "Site transfer: Mayagüez DC via PR-2", "N", 1.5),
    ("RT-PK", "PON", "Site transfer: Carolina DC via PR-52", "Y", 2.5),
    ("RT-CM", "CAR", "Metro: San Juan, Carolina, Bayamón", "N", 1.0),
    ("RT-CN", "CAR", "North coast: Dorado, Arecibo", "N", 1.5),
    ("RT-CE", "CAR", "East: Fajardo, Humacao, Caguas", "N", 1.5),
    ("RT-CC", "CAR", "Central via PR-52", "Y", 2.5),
    ("RT-MW", "MAY", "West coast: Mayagüez, Aguadilla, Cabo Rojo, San Germán", "N", 1.0),
    ("RT-MP", "MAY", "Site transfer: Ponce DC via PR-2", "N", 1.5),
    ("RT-MK", "MAY", "Site transfer: Carolina DC via PR-22", "N", 2.5),
]
customers = [  # account_id, account, segment, town, region, home_site, route, reg
    ("C-101", "Hospital Santa Brígida", "HOSP", "Ponce", "S", "PON", "RT-PS", "A"),
    ("C-102", "Hospital Valle Verde", "HOSP", "Juana Díaz", "S", "PON", "RT-PS", "A"),
    ("C-103", "Hospital Brisas de Guayama", "HOSP", "Guayama", "S", "PON", "RT-PE", "A"),
    ("C-104", "Hospital Monte Claro", "HOSP", "Aibonito", "C", "PON", "RT-PC", "A"),
    ("C-105", "Hospital Lomas de Utuado", "HOSP", "Utuado", "C", "PON", "RT-PC", "A"),
    ("C-106", "Hospital Pico Alto", "HOSP", "Barranquitas", "C", "PON", "RT-PC", "A"),
    ("C-111", "Cordillera Renal Utuado", "DIAL", "Utuado", "C", "PON", "RT-PC", "N"),
    ("C-112", "Cordillera Renal Jayuya", "DIAL", "Jayuya", "C", "PON", "RT-PC", "N"),
    ("C-113", "Cordillera Renal Adjuntas", "DIAL", "Adjuntas", "C", "PON", "RT-PC", "N"),
    ("C-114", "Cordillera Renal Orocovis", "DIAL", "Orocovis", "C", "PON", "RT-PC", "N"),
    ("C-115", "Cordillera Renal Barranquitas", "DIAL", "Barranquitas", "C", "PON", "RT-PC", "N"),
    ("C-116", "Costa Renal Ponce", "DIAL", "Ponce", "S", "PON", "RT-PS", "N"),
    ("C-117", "Costa Renal Yauco", "DIAL", "Yauco", "S", "PON", "RT-PS", "N"),
    ("C-118", "Costa Renal Santa Isabel", "DIAL", "Santa Isabel", "S", "PON", "RT-PE", "N"),
    ("C-119", "Costa Renal Guayama", "DIAL", "Guayama", "S", "PON", "RT-PE", "N"),
    ("C-121", "Farmacia Sol de Yauco", "PHARM", "Yauco", "S", "PON", "RT-PS", "L"),
    ("C-122", "Farmacia Las Delicias", "PHARM", "Ponce", "S", "PON", "RT-PS", "A"),
    ("C-123", "Farmacia Coamo Centro", "PHARM", "Coamo", "S", "PON", "RT-PS", "A"),
    ("C-124", "Farmacia La Montaña", "PHARM", "Adjuntas", "C", "PON", "RT-PC", "N"),
    ("C-131", "Clínica Valle Sur", "CLIN", "Juana Díaz", "S", "PON", "RT-PS", "A"),
    ("C-132", "Clínica Peñuelas Salud", "CLIN", "Peñuelas", "S", "PON", "RT-PS", "N"),
    ("C-133", "Clínica Jayuya Familiar", "CLIN", "Jayuya", "C", "PON", "RT-PC", "N"),
    ("C-141", "Red Municipal de Salud del Sur", "GOV", "Ponce", "S", "PON", "RT-PS", "A"),
    ("C-201", "Hospital Bahía Norte", "HOSP", "Carolina", "MTR", "CAR", "RT-CM", "A"),
    ("C-202", "Hospital Los Corales", "HOSP", "Fajardo", "E", "CAR", "RT-CE", "A"),
    ("C-203", "Hospital Paseo Norte", "HOSP", "San Juan", "MTR", "CAR", "RT-CM", "A"),
    ("C-204", "Hospital Arecibo Costa", "HOSP", "Arecibo", "N", "CAR", "RT-CN", "A"),
    ("C-205", "Botica Central Carolina", "PHARM", "Carolina", "MTR", "CAR", "RT-CM", "A"),
    ("C-206", "Farmacia Isla Verde", "PHARM", "Carolina", "MTR", "CAR", "RT-CM", "A"),
    ("C-207", "Farmacia Bayamón Norte", "PHARM", "Bayamón", "MTR", "CAR", "RT-CM", "L"),
    ("C-208", "Clínica Dorado Familiar", "CLIN", "Dorado", "N", "CAR", "RT-CN", "N"),
    ("C-209", "Clínica Humacao Salud", "CLIN", "Humacao", "E", "CAR", "RT-CE", "N"),
    ("C-210", "Red de Salud Municipal Norte", "GOV", "Arecibo", "N", "CAR", "RT-CN", "A"),
    ("C-211", "Consorcio de Salud del Este", "GOV", "Humacao", "E", "CAR", "RT-CE", "A"),
    ("C-212", "Centro Renal Metro", "DIAL", "Bayamón", "MTR", "CAR", "RT-CM", "N"),
    ("C-213", "Centro Renal Valle de Caguas", "DIAL", "Caguas", "E", "CAR", "RT-CE", "N"),
    ("C-301", "Hospital Puesta del Sol", "HOSP", "Mayagüez", "W", "MAY", "RT-MW", "A"),
    ("C-302", "Hospital Bahía Oeste", "HOSP", "Aguadilla", "W", "MAY", "RT-MW", "A"),
    ("C-303", "Farmacia Cabo Rojo", "PHARM", "Cabo Rojo", "W", "MAY", "RT-MW", "A"),
    ("C-304", "Clínica San Germán Salud", "CLIN", "San Germán", "W", "MAY", "RT-MW", "N"),
    ("C-305", "Centro Renal Mayagüez", "DIAL", "Mayagüez", "W", "MAY", "RT-MW", "N"),
    ("C-306", "Red de Salud Municipal Oeste", "GOV", "Mayagüez", "W", "MAY", "RT-MW", "A"),
]
suppliers = [  # supplier_id, supplier, port, lead_d
    ("S01", "Arrecife Renal Supply", "PON", 3), ("S02", "Atalaya Pharma", "SJU", 4), ("S03", "Ceiba MedSurg", "SJU", 2),
    ("S04", "Puerto Sur Biologics", "PON", 3), ("S05", "Vigía Specialty Rx", "SJU", 5), ("S06", "Norte Renal Direct", "SJU", 6),
    ("S07", "Polar Cold Chain", "SJU", 5),
]
products = [  # sku, product, line, stor, crit, supplier_id, alt_supplier_id, rop
    ("D-100", "Dialysate concentrate, case", "MSS", "AMB", "L1", "S01", "S06", 300),
    ("D-110", "Dialyzer, high-flux, box of 24", "MSS", "AMB", "L1", "S01", "S06", 100),
    ("D-120", "Bloodline set, box of 24", "MSS", "AMB", "L1", "S01", "S06", 120),
    ("H-200", "Heparin 1,000 u/mL, box", "RX", "AMB", "L1", "S02", "", 100),
    ("E-400", "Epoetin alfa vials, box", "RX", "CLD", "L1", "S04", "S07", 80),
    ("I-300", "Insulin glargine pens, box", "RX", "CLD", "L1", "S04", "S07", 100),
    ("I-310", "Insulin regular vials, box", "RX", "CLD", "L1", "S02", "S07", 60),
    ("V-500", "Sodium chloride 0.9% IV 1 L, case", "MSS", "AMB", "L1", "S03", "", 400),
    ("A-600", "Amoxicillin 500 mg, case", "RX", "AMB", "L2", "S02", "", 100),
    ("K-610", "Ceftriaxone 1 g vials, box", "RX", "AMB", "L2", "S02", "", 80),
    ("T-700", "Tetanus-diphtheria vaccine, box", "RX", "CLD", "L2", "S04", "S07", 40),
    ("W-810", "Wound dressing kit, case", "MSS", "AMB", "L2", "S03", "", 150),
    ("M-900", "Morphine sulfate 10 mg/mL, box", "SRX", "CTL", "L2", "S05", "", 40),
    ("Y-910", "Hydromorphone 2 mg/mL, box", "SRX", "CTL", "L2", "S05", "", 30),
    ("L-920", "Lorazepam 2 mg/mL, box", "SRX", "CTL", "L2", "S05", "", 30),
    ("G-800", "Nitrile exam gloves, case", "MSS", "AMB", "L3", "S03", "", 500),
]
inventory = [
    ("LP-1001","D-100","PON",200,5,"2027-08-31","ARS-55120"),("LP-1002","D-110","PON",60,2,"2028-01-31","ARS-55311"),
    ("LP-1003","D-120","PON",50,2,"2028-03-31","ARS-55402"),("LP-1004","H-200","PON",40,1,"2027-05-31","ATP-8812"),
    ("LP-1005","E-400","PON",50,2,"2027-02-28","PSB-2207"),("LP-1006","I-300","PON",60,3,"2027-04-30","PSB-2291"),
    ("LP-1007","I-310","PON",30,2,"2027-03-31","ATP-8930"),("LP-1008","V-500","PON",150,6,"2028-06-30","CMS-40112"),
    ("LP-1009","A-600","PON",80,2,"2027-11-30","ATP-9014"),("LP-1010","K-610","PON",50,1,"2027-09-30","ATP-9120"),
    ("LP-1011","T-700","PON",25,2,"2027-06-30","PSB-2330"),("LP-1012","W-810","PON",90,3,"2028-12-31","CMS-40207"),
    ("LP-1013","G-800","PON",120,4,"2029-01-31","CMS-40355"),("LP-1014","M-900","PON",20,2,"2027-07-31","VSR-1170"),
    ("LP-1015","Y-910","PON",12,1,"2027-06-30","VSR-1182"),("LP-1016","L-920","PON",10,1,"2027-04-30","VSR-1191"),
    ("LC-2001","D-100","CAR",180,5,"2027-09-30","ARS-55188"),("LC-2002","D-110","CAR",90,3,"2028-02-29","ARS-55320"),
    ("LC-2003","D-120","CAR",80,3,"2028-03-31","ARS-55410"),("LC-2004","H-200","CAR",90,2,"2027-06-30","ATP-8840"),
    ("LC-2005","E-400","CAR",40,2,"2027-03-31","PSB-2215"),("LC-2006","I-300","CAR",70,3,"2027-05-31","PSB-2296"),
    ("LC-2007","I-310","CAR",40,2,"2027-04-30","ATP-8941"),("LC-2008","V-500","CAR",300,12,"2028-07-31","CMS-40130"),
    ("LC-2009","A-600","CAR",120,3,"2027-12-31","ATP-9020"),("LC-2010","K-610","CAR",80,2,"2027-10-31","ATP-9133"),
    ("LC-2011","T-700","CAR",30,2,"2027-07-31","PSB-2341"),("LC-2012","W-810","CAR",160,5,"2029-01-31","CMS-40219"),
    ("LC-2013","G-800","CAR",300,10,"2029-02-28","CMS-40360"),("LC-2014","M-900","CAR",25,2,"2027-08-31","VSR-1175"),
    ("LC-2015","Y-910","CAR",20,1,"2027-07-31","VSR-1185"),("LC-2016","L-920","CAR",18,1,"2027-05-31","VSR-1194"),
    ("LM-3001","D-100","MAY",60,2,"2027-08-31","ARS-55131"),("LM-3002","D-110","MAY",30,1,"2028-01-31","ARS-55318"),
    ("LM-3003","D-120","MAY",30,1,"2028-03-31","ARS-55407"),("LM-3004","H-200","MAY",30,1,"2027-05-31","ATP-8816"),
    ("LM-3005","E-400","MAY",15,1,"2027-02-28","PSB-2209"),("LM-3006","I-300","MAY",20,1,"2027-04-30","PSB-2293"),
    ("LM-3007","I-310","MAY",10,1,"2027-03-31","ATP-8933"),("LM-3008","V-500","MAY",80,3,"2028-06-30","CMS-40118"),
    ("LM-3009","A-600","MAY",40,1,"2027-11-30","ATP-9017"),("LM-3010","K-610","MAY",30,1,"2027-09-30","ATP-9126"),
    ("LM-3011","T-700","MAY",10,1,"2027-06-30","PSB-2334"),("LM-3012","W-810","MAY",50,2,"2028-12-31","CMS-40210"),
    ("LM-3013","G-800","MAY",80,3,"2029-01-31","CMS-40357"),("LM-3014","M-900","MAY",8,1,"2027-07-31","VSR-1172"),
    ("LM-3015","Y-910","MAY",6,1,"2027-06-30","VSR-1183"),("LM-3016","L-920","MAY",6,1,"2027-04-30","VSR-1192"),
]
orders = []; n = 5001
home = {c[0]: c[5] for c in customers}
def add(acct, sku, qty, due):
    global n
    orders.append((f"SO-{n}", acct, sku, qty, due, home[acct])); n += 1
for a in ["C-111","C-112","C-113","C-114","C-115","C-116","C-117","C-118","C-119"]:
    add(a,"D-100",12,"2026-10-21"); add(a,"D-110",4,"2026-10-21"); add(a,"E-400",3,"2026-10-21")
add("C-101","A-600",20,"2026-10-21"); add("C-101","G-800",20,"2026-10-22"); add("C-102","W-810",15,"2026-10-21")
add("C-103","K-610",10,"2026-10-22"); add("C-104","G-800",20,"2026-10-21"); add("C-104","W-810",10,"2026-10-22")
add("C-105","A-600",15,"2026-10-21"); add("C-106","K-610",8,"2026-10-21"); add("C-122","M-900",10,"2026-10-21")
add("C-123","A-600",10,"2026-10-22"); add("C-131","W-810",10,"2026-10-21"); add("C-133","G-800",10,"2026-10-21")
for a in ["C-212","C-213","C-305"]:
    add(a,"D-100",12,"2026-10-21"); add(a,"D-110",4,"2026-10-21"); add(a,"E-400",3,"2026-10-21")
add("C-201","V-500",60,"2026-10-21"); add("C-201","G-800",40,"2026-10-22"); add("C-203","V-500",60,"2026-10-22")
add("C-205","M-900",8,"2026-10-22"); add("C-301","G-800",20,"2026-10-21"); add("C-302","A-600",15,"2026-10-22")
contracts = [
    ("CT-01","C-101","SUP","STD-H",420000,"2027-12-31"),("CT-02","C-102","SUP","STD-H",260000,"2027-06-30"),
    ("CT-03","C-103","SUP","STD-H",300000,"2027-09-30"),("CT-04","C-104","SUP","STD-H",280000,"2027-12-31"),
    ("CT-05","C-105","SUP","STD-H",340000,"2028-03-31"),("CT-06","C-106","SUP","STD-H",260000,"2027-06-30"),
    ("CT-07","C-201","SUP","STD-H",610000,"2028-06-30"),("CT-08","C-202","SUP","STD-H",280000,"2027-12-31"),
    ("CT-09","C-203","SUP","STD-H",520000,"2027-12-31"),("CT-10","C-204","SUP","STD-H",300000,"2027-09-30"),
    ("CT-11","C-301","SUP","STD-H",390000,"2028-03-31"),("CT-12","C-302","SUP","STD-H",240000,"2027-06-30"),
]
for i, a in enumerate(["C-111","C-112","C-113","C-114","C-115","C-116","C-117","C-118","C-119","C-212","C-213","C-305"]):
    contracts.append((f"CT-{20+i}", a, "SUP", "STD-D", 90000 + 5000*(i % 4), "2027-12-31"))
contracts += [("CT-40","C-141","EMG","EMG-20",0,"2027-06-30"),("VEH-01","C-306","VEH","VEH",0,"2027-03-31"),
              ("VEH-02","C-210","VEH","VEH",0,"2027-06-30"),("VEH-03","C-211","VEH","VEH",0,"2026-11-30")]
names = {c[0]: c[1] for c in customers}
opps = [
    ("OPP-1004","C-201","MSS","5-PO Pending","Commit",700000,"2026-12-10",5,"J. Rivera",""),
    ("OPP-1007","C-301","RX","4-Negotiate","Commit",450000,"2026-11-20",9,"M. Ortiz",""),
    ("OPP-1009","C-210","MSS","5-PO Pending","Commit",380000,"2026-12-05",8,"L. Santana","VEH-02"),
    ("OPP-1012","C-101","MSS","5-PO Pending","Commit",300000,"2026-11-13",6,"A. Colón",""),
    ("OPP-1015","C-131","RX","4-Negotiate","Commit",200000,"2026-11-18",3,"A. Colón",""),
    ("OPP-1018","C-104","MSS","4-Negotiate","Commit",250000,"2026-12-18",10,"A. Colón",""),
    ("OPP-1021","C-205","SRX","5-PO Pending","Commit",290000,"2026-11-25",7,"J. Rivera",""),
    ("OPP-1027","C-303","RX","4-Negotiate","Commit",230000,"2026-12-01",12,"M. Ortiz",""),
    ("OPP-1030","C-302","MSS","4-Negotiate","Commit",480000,"2026-12-12",28,"M. Ortiz",""),
    ("OPP-1033","C-203","RX","4-Negotiate","Commit",300000,"2026-12-15",35,"J. Rivera",""),
    ("OPP-1036","C-121","SRX","5-PO Pending","Commit",310000,"2026-11-10",4,"A. Colón",""),
    ("OPP-1039","C-211","MSS","5-PO Pending","Commit",310000,"2026-12-15",6,"L. Santana","VEH-03"),
    ("OPP-1041","C-202","MSS","3-Proposal","Best Case",420000,"2026-12-20",11,"J. Rivera",""),
    ("OPP-1043","C-102","RX","3-Proposal","Best Case",260000,"2026-12-08",24,"A. Colón",""),
    ("OPP-1045","C-207","MSS","3-Proposal","Best Case",95000,"2026-11-30",30,"J. Rivera",""),
    ("OPP-1047","C-306","MSS","3-Proposal","Best Case",350000,"2026-12-18",5,"M. Ortiz","VEH-01"),
    ("OPP-1049","C-212","MSS","2-Qualify","Pipeline",180000,"2026-12-22",14,"J. Rivera",""),
    ("OPP-1051","C-116","MSS","2-Qualify","Pipeline",150000,"2026-12-29",7,"A. Colón",""),
    ("OPP-1053","C-124","SRX","2-Qualify","Pipeline",120000,"2026-12-30",9,"A. Colón",""),
    ("OPP-1055","C-204","RX","3-Proposal","Best Case",310000,"2026-12-11",6,"J. Rivera",""),
    ("OPP-1057","C-209","MSS","2-Qualify","Pipeline",90000,"2026-12-31",3,"J. Rivera",""),
    ("OPP-1059","C-305","MSS","3-Proposal","Best Case",200000,"2026-12-04",10,"M. Ortiz",""),
]
if __name__ == "__main__":
    write("sites.csv", ["site_id","site","town","region","lic_st","gen_h","cold_cap_plt","cold_used_plt","vault_cap_plt","vault_used_plt"], sites)
    write("routes.csv", ["route_id","from_site","serves","mtn","transit_h"], routes)
    write("customers.csv", ["account_id","account","segment","town","region","home_site","route","reg"], customers)
    write("suppliers.csv", ["supplier_id","supplier","port","lead_d"], suppliers)
    write("products.csv", ["sku","product","line","stor","crit","supplier_id","alt_supplier_id","rop"], products)
    write("inventory.csv", ["lot_id","sku","site_id","qty","plt","expiry","supplier_lot"], inventory)
    write("orders.csv", ["order_id","account_id","sku","qty","due","site_id"], orders)
    write("contracts.csv", ["contract_id","account_id","type","terms","mvol_usd","end_date"], contracts)
    write("opportunities.csv", ["opp_id","account_id","account","prod_line","stage","fcst","amount_usd","close_date","days_idle","owner","vehicle_id"],
          [(o[0], o[1], names[o[1]], *o[2:]) for o in opps])
