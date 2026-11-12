#!/usr/bin/env python3
"""Build the static site: content/**/*.md + templates/ + static/  ->  site/.

Usage:
    .venv/bin/python build.py            # build into site/
    .venv/bin/python build.py --serve    # build, then serve on http://localhost:8000
    .venv/bin/python build.py --watch    # rebuild whenever content/templates/static change
    .venv/bin/python build.py --serve --watch   # both: live preview while editing

Each Markdown file may start with a YAML front-matter block delimited by '---'.
Recognised keys (all optional):
    title     page title (used in <title> and as the page heading)
    template  template to render with, relative to templates/
              (default: '<section>/page.html')
Any other front-matter keys are passed to the template as `page.<key>`.

content/<section>/foo.md is written to site/<section>/foo.html.
All internal links are relative (via the `root` template variable), so the
output works when opened from disk, from a GitHub Pages project site, or from
a custom domain.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from markupsafe import Markup

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
OUT = ROOT / "site"

SECTIONS = ("profession", "wild")
MD_EXTENSIONS = ["extra", "smarty", "sane_lists"]


def parse(path: Path) -> tuple[dict, str]:
    """Split a Markdown file into (front matter dict, markdown body)."""
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        return (yaml.safe_load(fm) or {}), body
    return {}, text


def md_block(text: str | None) -> Markup:
    return Markup(markdown.markdown(text or "", extensions=MD_EXTENSIONS))


def md_inline(text: str | None) -> Markup:
    """Render a short Markdown snippet without the wrapping <p>."""
    html = markdown.markdown(text or "", extensions=MD_EXTENSIONS).strip()
    if html.startswith("<p>") and html.endswith("</p>") and html.count("<p>") == 1:
        html = html[3:-4]
    return Markup(html)


def make_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=True,
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["md"] = md_block
    env.filters["mdi"] = md_inline
    return env


def build() -> int:
    site = yaml.safe_load((CONTENT / "site.yaml").read_text(encoding="utf-8"))
    env = make_env()

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(STATIC, OUT / "static", ignore=shutil.ignore_patterns(".gitkeep"))

    count = 0
    for section in SECTIONS:
        for src in sorted((CONTENT / section).glob("*.md")):
            meta, body = parse(src)
            rel = f"{section}/{src.stem}.html"
            tpl = env.get_template(meta.get("template", f"{section}/page.html"))
            html = tpl.render(
                site=site,
                page=meta,
                content=md_block(body),
                section=section,
                url=rel,
                root="../",
            )
            dest = OUT / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(html, encoding="utf-8")
            count += 1

    # Site root: send visitors to the professional home page.
    root_html = env.get_template("shared/root.html").render(site=site, target="profession/index.html")
    (OUT / "index.html").write_text(root_html, encoding="utf-8")
    (OUT / ".nojekyll").touch()  # stop GitHub Pages from running Jekyll

    print(f"Built {count} pages into {OUT.relative_to(ROOT)}/")
    return count


def serve(port: int, background: bool = False) -> None:
    import functools
    import http.server
    import threading

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(OUT))
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    print(f"Serving on http://localhost:{port}/  (Ctrl+C to stop)")
    if background:
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
    else:
        with httpd:
            httpd.serve_forever()


WATCHED = (CONTENT, TEMPLATES, STATIC)


def snapshot() -> dict[Path, float]:
    """Modification time of every file under the watched directories."""
    return {
        f: f.stat().st_mtime
        for d in WATCHED
        for f in d.rglob("*")
        if f.is_file()
    }


def watch(interval: float = 0.5) -> None:
    """Poll the source directories and rebuild when anything is added, removed or changed."""
    import time

    print("Watching content/, templates/ and static/ for changes (Ctrl+C to stop)")
    last = snapshot()
    while True:
        time.sleep(interval)
        current = snapshot()
        if current == last:
            continue
        last = current
        print(f"[{time.strftime('%H:%M:%S')}] Change detected, rebuilding...")
        try:
            build()
        except Exception as exc:  # keep watching after a broken edit
            print(f"Build failed: {type(exc).__name__}: {exc}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--serve", action="store_true", help="serve site/ after building")
    ap.add_argument("--watch", action="store_true", help="rebuild when source files change")
    ap.add_argument("--port", type=int, default=8000)
    args = ap.parse_args()
    if args.watch:
        try:
            build()
        except Exception as exc:
            print(f"Build failed: {type(exc).__name__}: {exc}")
        try:
            if args.serve:
                serve(args.port, background=True)
            watch()
        except KeyboardInterrupt:
            print("\nStopped.")
    else:
        build()
        if args.serve:
            serve(args.port)
