# Francesco Montagna — Personal Website

A static personal website, generated with a small Python build (Jinja2 + Markdown).

It has two sections:

| Section | Path | Content |
|---|---|---|
| **Francesco in the Profession** | `/profession/` | Research, publications, CV, talks |
| **Francesco in the Wild** | `/wild/` | Everything non-professional |

## Layout

```
content/
  profession/   Markdown pages for the professional section
  wild/         Markdown pages for the non-professional section
templates/
  shared/       Base layout and partials used by both sections
  profession/   Templates specific to the professional section
  wild/         Templates specific to the wild section
static/         CSS, JS, images (copied as-is into the build)
site/           Build output (git-ignored)
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Build

```bash
.venv/bin/python build.py           # writes site/
.venv/bin/python build.py --serve   # build + preview at http://localhost:8000
```

## Editing content

- `content/site.yaml` — name, photo, contact links, "last updated", and the navigation for both sections.
- `content/<section>/<page>.md` — one Markdown file per page. The YAML front matter sets `title`, an optional
  `template`, and any structured data the template needs:
  - `profession/index.md` → `glance` (the "At a glance" box) and `menu`
  - `profession/research.md` → `groups` of papers (`title`, `venue`, `tldr`, `links`, optional `papers`)
  - `profession/cv.md` → `blocks` of timeline `entries` (`when`, `where`, `role`)
- To add a page to the nav, create the `.md` file and list it under the section's `nav` in `site.yaml`.
