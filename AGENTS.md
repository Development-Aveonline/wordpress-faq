# AGENTS.md

## Objective

Read all `.docx` files inside `faq/` and produce one JSON file per `.docx` inside a `json/` folder, with this format:
```json
[
  {
    "question": "string",
    "answer": "string (may contain HTML)"
  }
]
```
Each JSON file is named after its source `.docx` but with `.json` extension (e.g. `FAQ Alianza Alegra.docx` → `json/FAQ Alianza Alegra.json`).
Important in answer:
The urls have to have this format: 
<a href="url"><span style="font-weight: 400">url</span></a>
The list have to have this format: 
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
    <li>Item 4</li>
    ...
</ul>
Replace [NOMBRE_MUNICIPIO] by {{nombre_municipio}}

## Structure

```
faq/              ← 12 Word .docx files (Spanish)
json/             ← 12 JSON files (one per .docx)
package.json      ← placeholder only (no deps, no scripts)
```

## Rules

- All source documents are **Spanish-language `.docx` binary files** — use `python-docx` or equivalent to extract text.
- The output must be **one JSON file per `.docx`**, all placed inside a `json/` directory.
- No README, no CI, no linters, no formatters, no tests in this repo.
- Single commit on `master` with no branching convention.
