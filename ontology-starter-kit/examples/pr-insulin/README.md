# PR Insulin Distributors, Inc.: the storm test

PR Insulin Distributors is a fictional distributor in Puerto Rico. Every name, number, and record is invented. The rules in `pr-insulin-ontology.yaml` are the company's internal policies, not regulations, and not legal or clinical guidance.

- 3 distribution centers: Carolina, Ponce, Mayagüez
- 42 customers, including 9 dialysis centers
- 16 products, including insulin; 7 suppliers; 12 routes; 28 contracts; 22 open deals
- The ontology: 19 entities in five lanes, each with a schema.org type or marked company-defined; 9 rules, Rule-01 to Rule-09, each with an owner

## Run it yourself

1. Create two projects in Claude, ChatGPT, or Copilot. Load the nine files in `data/` into both.
2. Add `pr-insulin-ontology.yaml` to the second project only, with the instruction line from `docs/share-it.md`.

### Warm-up question

```
Can Carolina DC take the controlled stock from Ponce?
```

Without the ontology, the AI says yes: Carolina has the most vault space and 120 hours of fuel. It guesses that `lic_st = 40` means licensed. With the ontology, it says no: 40 means renewal pending, so Carolina cannot receive controlled products [Rule-03]. Send it to Mayagüez.

### The storm question

```
It is Tuesday, October 20, 6:00 a.m. A hurricane warning is in effect for the south coast. Landfall is forecast in 48 hours. What is our business continuity plan, and what do we need to do in the next 48 hours?
```

Español:

```
Es martes 20 de octubre, 6:00 a.m. Hay un aviso de huracán para la costa sur. Se pronostica que toque tierra en 48 horas. ¿Cuál es nuestro plan de continuidad del negocio y qué tenemos que hacer en las próximas 48 horas?
```

## What to look for

Without the ontology, the plan reads well and breaks two rules:

- It keeps the insulin in Ponce and tops off the generator. Ponce has 36 hours of fuel. That breaks Rule-02, "Insulin stays cold."
- It delivers the dialysis orders on their Wednesday due date. The mountain routes close Wednesday at 6:00 a.m. Five mountain dialysis centers get nothing before landfall. That breaks Rule-06.

With the ontology, the answer is a timed plan with rule IDs:

| By | Action | Rule |
|---|---|---|
| Now | Hold 20% of Ponce's life-critical stock for the south municipal health network | Rule-04 |
| Tue 6:00 p.m. | Force-majeure notices on 6 hospital contracts, or up to $186K in penalties stand | Rule-05 |
| Wed 6:00 a.m. | Insulin, cold-chain, and controlled stock out of Ponce, to Mayagüez, not Carolina | Rule-02, Rule-03 |
| Wed 6:00 a.m. | Dialysis orders to all 9 centers, the 5 mountain centers first | Rule-01, Rule-06 |

## Two more questions, same map

- "What does this storm do to our Q4 commit?" Expected: $4.2M reported, $2.8M after Rule-07 to Rule-09, $2.3M after the storm.
- "What do we reorder first, and from whom?" Expected: epoetin and dialysate first, from suppliers that ship through San Juan. Morphine goes to Mayagüez only.

`pr-insulin-ontology.mmd` is the same map as a diagram.

## Check the numbers

`check/answer_key.py` applies the rules to the data and asserts every number above. Run it from the `check` folder: `python3 answer_key.py` (needs pandas). `check/build_data.py` regenerates the CSV files.
