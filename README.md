# Business ontology starter kit

**A map of your business your AI can read.** One text file that tells every AI tool, and every person, what your business tracks, how it connects, and which rules it follows.

Caribbean AI Summit 2026 · Pharos Solutions · Free to use and adapt.

## Start here

| You have | Do this | Time |
|---|---|---|
| Claude, ChatGPT, or Copilot | Paste `prompts/01-draft-it.md`, then `prompts/02-draw-it.md` | 5 minutes |
| A real domain to map | Paste `prompts/03-interview.md`. The AI asks the questions, one at a time. | 30 minutes |
| Claude Code | Clone this repo, open it, run `/ontology-interview` | 30 minutes |
| Codex | Clone this repo, open it, say "Run the ontology interview." | 30 minutes |

Every path ends with the same three things: version 1.0 of `ontology/ontology.yaml`, a diagram for human review, and three test questions.

## Then

- **Why not a context file?** `docs/why-an-ontology.md`. Shared schema.org vocabulary, rules with IDs and owners, checked like code.
- **Share it:** `docs/share-it.md`. Claude and ChatGPT projects, Copilot agents, Claude Code, Codex.
- **Test it:** `prompts/04-test-it.md`. Same question, with and without the file.
- **Start Monday:** `docs/monday-morning.md`. One domain, ten terms, three rules.

## Examples

- `examples/pr-insulin/`: the storm test from the talk. A fictional distributor, nine data files, 19 entities, 9 rules.
- `examples/panaderia-solerno/`: a bakery, built from two prompts.

## What's in the file

| Section | What it holds |
|---|---|
| entities | The things you track, their schema.org type, their attributes, and what every code means |
| relationships | How the things connect: "Order is placed by Customer" |
| terms | The words your team uses that outsiders get wrong |
| rules | The judgment calls, each with an ID (Rule-01) and an owner |
| changelog | Every change, versioned and approved |

## How this repo works with AI tools

- `AGENTS.md` tells Codex to read the ontology before every task.
- `CLAUDE.md` imports `AGENTS.md` and the ontology, so Claude Code loads both at the start of every session.
- `.claude/skills/` and `.agents/skills/` hold the same interview skill for Claude Code and Codex.

## License

MIT. See `LICENSE`.

All companies and data in `examples/` are fictional.
