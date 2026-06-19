# AGENTS.md

## Objective

Read all `.docx` files inside `faq/` and produce a single unified JSON file with this format:
```json
[
  {
    "question": "string",
    "answer": "string (may contain HTML)"
  }
]
```
The json name is faq.json
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

## Structure

```
faq/              ← 12 Word .docx files (Spanish)
package.json      ← placeholder only (no deps, no scripts)
```

## Rules

- All source documents are **Spanish-language `.docx` binary files** — use `python-docx` or equivalent to extract text.
- The output must be a **single JSON array** merging all 12 files.
- No README, no CI, no linters, no formatters, no tests in this repo.
- Single commit on `master` with no branching convention.
