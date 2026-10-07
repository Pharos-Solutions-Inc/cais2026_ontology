# Why an ontology, and not just a context file?

A context file is a note. An ontology is a contract.

| | Context file | Ontology |
|---|---|---|
| Form | Prose. "Carolina is renewing its license, be careful." | Typed entities, connections, codes, and rules |
| Vocabulary | Your words, read differently by every tool | schema.org types every AI tool already knows |
| Connections | Buried in sentences | Explicit: "Site holds License" |
| Rules | Advice | An ID, a condition, an action, and an owner |
| Answers | "Probably avoid Carolina" | "No. Rule-03. Owner: Compliance." |
| Quality control | None. A typo reaches the answer. | A schema check rejects a bad file before any AI reads it |
| Change | Anyone edits, nobody approves | Pull request, owner approval, changelog |

## Use a shared vocabulary

schema.org is a free, open vocabulary founded by Google, Microsoft, Yahoo, and Yandex, and used across the web. When your ontology says a site is a `schema:Place`, a license is a `schema:GovernmentPermit`, a product is a `schema:Drug`, and a customer is a `schema:Hospital`, every AI tool, partner, and developer starts from the same definitions.

Use a schema.org type where one exists. Write `company-defined` where it doesn't. In the PR Insulin example, 13 of 19 entities map to schema.org; contracts, routes, opportunities, and forecasts are company-defined.

## Check it like code

Store the file in a repo. Add a schema check to your pull requests (JSON Schema or LinkML both work on YAML). A wrong code, a missing owner, or a broken rule ID fails the check. The mistake never reaches an answer.

## When you need more

The same file maps to JSON-LD, so you can load it into a knowledge graph later. Microsoft Fabric IQ, Palantir Foundry, and the Apache Ossie semantic interchange (formerly OSI) all work from the same idea: a shared, governed map of the business. Start with a text file.
