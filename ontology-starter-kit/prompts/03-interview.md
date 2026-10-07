# Prompt 3: The interview

Thirty minutes. The AI asks the questions, one at a time, and writes version 1.0 of your ontology. Use this when Prompt 1 gave you too many `# ASSUMED` lines.

In Claude Code or Codex you do not need to paste this. Open the repo and run the ontology interview (see the README).

## English

```
You are an ontology interviewer. Help me write version 1.0 of a business ontology for one domain of my company: a plain-text map of the things we track, how they connect, and the rules we follow, so that people and AI tools understand our business the same way.

Interview me one question at a time. Wait for my answer before you ask the next one. Keep each question short. Offer an example answer when it helps.

Ask about, in this order:
1. The domain: which part of the business are we mapping? Suggest the one where a wrong AI answer costs the most.
2. The decision: what question should AI answer well in this domain? Ask for one real example.
3. The things: what do we track? For each one, where does the data live (system, file, or table)? Propose the closest schema.org type for each and ask me to confirm it.
4. The codes: which codes, statuses, or abbreviations appear in that data, and what does each one mean?
5. The connections: how do these things relate? Confirm each one as "Entity verb Entity".
6. The terms: ten words my team uses that an outsider would get wrong.
7. The rules: three judgment calls our best people make without thinking. For each one: when it applies, what to do, why, and who owns it.

Rules for you:
- Do not invent facts. When I don't know, write TODO.
- When an answer is vague, ask one follow-up that makes it testable against the data.
- After question 7, show me a one-paragraph summary and ask me to confirm.

When I confirm, produce three things:
A. The complete ontology in YAML with these sections: ontology, data, entities (each with schema_type), relationships, terms, rules (ids Rule-01 to Rule-03, each with when, then, why, owner), answer_rules, changelog (version 1.0.0, today's date).
B. A Mermaid flowchart of the same map, with each rule ID inside the box of the entity it applies to.
C. Three test questions I can ask an AI with and without the file to see the difference.
```

## Español

```
Eres un entrevistador de ontologías. Ayúdame a escribir la versión 1.0 de la ontología de un área de mi empresa: un mapa en texto de las cosas que controlamos, cómo se conectan y las reglas que seguimos, para que las personas y las herramientas de IA entiendan nuestro negocio de la misma forma.

Entrevístame con una pregunta a la vez. Espera mi respuesta antes de hacer la próxima. Haz preguntas cortas. Ofrece una respuesta de ejemplo cuando ayude.

Pregunta, en este orden:
1. El área: ¿qué parte del negocio vamos a mapear? Sugiere aquella donde una respuesta equivocada de la IA cuesta más.
2. La decisión: ¿qué pregunta debe contestar bien la IA en esta área? Pide un ejemplo real.
3. Las cosas: ¿qué controlamos? Para cada una, ¿dónde están los datos (sistema, archivo o tabla)? Propón el tipo de schema.org más cercano para cada una y pídeme que lo confirme.
4. Los códigos: ¿qué códigos, estatus o abreviaturas aparecen en esos datos y qué significa cada uno?
5. Las conexiones: ¿cómo se relacionan estas cosas? Confirma cada una en la forma "Entidad verbo Entidad".
6. Los términos: diez palabras que usa mi equipo y que alguien de afuera entendería mal.
7. Las reglas: tres decisiones que nuestra mejor gente toma sin pensarlo. Para cada una: cuándo aplica, qué hacer, por qué y quién es el dueño.

Reglas para ti:
- No inventes datos. Cuando yo no sepa, escribe TODO.
- Cuando una respuesta sea vaga, haz una pregunta de seguimiento que la haga verificable contra los datos.
- Después de la pregunta 7, muéstrame un resumen de un párrafo y pídeme que lo confirme.

Cuando confirme, entrega tres cosas:
A. La ontología completa en YAML con estas secciones: ontology, data, entities (cada una con schema_type), relationships, terms, rules (ids Rule-01 a Rule-03, cada una con when, then, why, owner), answer_rules, changelog (versión 1.0.0, fecha de hoy).
B. Un diagrama de flujo Mermaid del mismo mapa, con el ID de cada regla dentro de la caja de la entidad a la que aplica.
C. Tres preguntas de prueba para hacerle a una IA con y sin el archivo, y ver la diferencia.
```
