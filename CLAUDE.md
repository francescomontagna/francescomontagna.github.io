# CLAUDE.md

You are an agent generating code for Francesco Montagna's personal website, which has a professional part and a personal part.

## Project overview

A static personal website, built by a small custom Python static-site generator (Jinja2 + Markdown + YAML front matter). The output is plain HTML/CSS/JS, meant for static hosting (e.g. GitHub Pages).

The site has two sections:

| Section | URL path | Content dir | Purpose |
|---|---|---|---|
| **Francesco in the Profession** | `/profession/` | `content/profession/` | Research, publications, CV, talks |
| **Francesco in the Wild** | `/wild/` | `content/wild/` | Non-professional life: hobbies, travel, writing |

The two sections share a base layout but may have distinct visual identities. Keep them clearly separated in content, templates and assets.

## Repository layout

```
content/profession/   Markdown pages (with YAML front matter) for the professional section
content/wild/         Markdown pages for the wild section
templates/shared/     Base layout and partials used by both sections
templates/profession/ Templates specific to the professional section
templates/wild/       Templates specific to the wild section
static/               CSS, JS, images, copied as-is into the build
  img/profession/     Images for the professional section
  img/wild/           Images for the wild section
site/                 Build output (git-ignored, never edit by hand)
requirements.txt      Python dependencies
```

## Environment

- Python 3.12, virtual environment in `.venv/` (git-ignored).
- Set up with:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```
- Run tools through the venv (`.venv/bin/python ...`) rather than the system Python.
- Node.js is **not** installed. Do not introduce Node-based tooling without asking.

## Conventions

- Content goes in Markdown under `content/<section>/`, not hardcoded in templates.
- Templates extend `templates/shared/` base layouts; section templates hold only what differs.
- Keep dependencies minimal. Add any new package to `requirements.txt` with a version lower bound.
- Prefer plain CSS and vanilla JS. No heavy frameworks unless agreed.
- Pages must be responsive (work at phone width) and accessible (semantic HTML, alt text, sufficient contrast).
- Never commit `site/`, `.venv/`, or secrets.

## Workflow

- Only commit when asked. Use clear, imperative commit messages.
- Before reporting work as done, build the site and check that the output renders.
- Ask before making large structural changes (new sections, new frameworks, hosting changes).
