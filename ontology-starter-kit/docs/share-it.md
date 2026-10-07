# Share it: one file, every tool

Write the ontology once. Every person and every AI tool reads the same file.

## The instruction line

Wherever you load the file, add this instruction:

```
Read ontology.yaml before you answer any question about our business. Use its terms. Apply every rule that fits and cite the rule ID, for example [Rule-02].
```

Español:

```
Lee ontology.yaml antes de contestar cualquier pregunta sobre nuestro negocio. Usa sus términos. Aplica cada regla que corresponda y cita el ID de la regla, por ejemplo [Rule-02].
```

## In a chat project

| Tool | Where the file goes | Where the instruction goes |
|---|---|---|
| Claude | Project knowledge | Project instructions |
| ChatGPT | Project files | Project instructions |
| Microsoft 365 Copilot | An agent's knowledge | The agent's instructions |

Every chat inside the project starts with the map. Nobody re-explains the business.

## In a code repo

| Tool | What to add |
|---|---|
| Claude Code | `CLAUDE.md` at the repo root with the line `@ontology/ontology.yaml`. Claude Code loads the file at the start of every session. |
| Codex | `AGENTS.md` at the repo root that says: "Read ontology/ontology.yaml before any task." |

This kit ships both files. Claude Code reads `CLAUDE.md`, not `AGENTS.md`, so `CLAUDE.md` imports `AGENTS.md` with `@AGENTS.md`. One set of instructions serves both tools.

## Keep it alive

- Store the file in a repo or a shared drive with version history.
- Change it through review. A rule changes only with its owner's approval.
- Bump the version and log every change in the changelog section.
- Redraw the diagram when the map changes.
