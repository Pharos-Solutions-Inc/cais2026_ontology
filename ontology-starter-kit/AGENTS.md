# AGENTS.md

This repository holds a business ontology: the shared map of the things the business tracks, how they connect, and the rules it follows. People and AI tools read the same file.

## Before any task
Read `ontology/ontology.yaml`. Use its terms. Apply every rule that fits the task. When a rule shapes an answer or a change, cite its ID, for example [Rule-02].

## Building or changing the ontology
- To build or extend it, run the `ontology-interview` skill. The same interview is in `prompts/03-interview.md`.
- Never invent a code meaning, a rule, or an owner. Write TODO and ask.
- Give every entity a schema.org type, or "company-defined" when none fits.
- Every change bumps the version and adds a changelog entry in `ontology/ontology.yaml`.
- Redraw `ontology/ontology.mmd` when entities, relationships, or rules change.
- A rule changes only with its owner's approval in the pull request.

## Files
- `ontology/ontology.yaml`: the ontology. Starts as a template.
- `ontology/ontology.mmd`: the diagram for human review.
- `prompts/`: copy-paste prompts for Claude, ChatGPT, and Copilot.
- `docs/`: why an ontology, how to share it, and a one-hour Monday plan.
- `examples/pr-insulin/`: a full worked example with data. Fictional company.
- `examples/panaderia-solerno/`: a small bakery example. Fictional company.
