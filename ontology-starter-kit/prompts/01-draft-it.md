# Prompt 1: Draft it

Five minutes. Any AI tool. Paste the prompt, replace the part in << >>, and send.

## English

```
You are helping me write a business ontology: a plain-text map of my business that people and AI tools can read.

My business:
<<Describe it in 3 to 6 sentences: what you sell, to whom, from where, which systems hold the data, and what goes wrong.>>

Write the ontology in YAML with these sections:
1. entities: the 6 to 10 things the business tracks. For each one: its schema.org type (for example schema:Organization, schema:Product, schema:Order, schema:Place), or "company-defined" when none fits; what it means; its key attributes; and where the data lives. Spell out every code.
2. relationships: one line each, in the form "Entity verb Entity".
3. terms: the words my team uses that an outsider would get wrong.
4. rules: 3 to 5 judgment calls. Each has an id (Rule-01, Rule-02...), when, then, why, and owner.
5. changelog: version 1.0.0 with today's date.

Use only what I told you. When you must assume something, add "# ASSUMED" at the end of that line so I can check it.
Keep it under 100 lines.
```

## Español

```
Ayúdame a escribir la ontología de mi negocio: un mapa en texto que las personas y las herramientas de IA puedan leer.

Mi negocio:
<<Descríbelo en 3 a 6 oraciones: qué vendes, a quién, desde dónde, en qué sistemas están los datos y qué sale mal.>>

Escribe la ontología en YAML con estas secciones:
1. entities: las 6 a 10 cosas que el negocio controla. Para cada una: su tipo de schema.org (por ejemplo schema:Organization, schema:Product, schema:Order, schema:Place), o "company-defined" si ninguno aplica; qué significa; sus atributos principales; y dónde están los datos. Explica cada código.
2. relationships: una línea por relación, en la forma "Entidad verbo Entidad".
3. terms: las palabras que usa mi equipo y que alguien de afuera entendería mal.
4. rules: de 3 a 5 decisiones de criterio. Cada una con id (Rule-01, Rule-02...), when, then, why y owner.
5. changelog: versión 1.0.0 con la fecha de hoy.

Usa solo lo que te dije. Cuando tengas que suponer algo, añade "# ASSUMED" al final de esa línea para que yo lo verifique.
Que no pase de 100 líneas.
```

The YAML keys stay in English in both versions. Every tool parses them the same way, and your team can still write the meanings in Spanish.
