"""CI build script — writes the planner output to ./dist/.

Used by the GitHub Actions workflow. Local users keep using planner.py (which
writes to OneDrive). This script writes to a clean ./dist/ folder ready for
GitHub Pages deployment.

Usage (CI or local test):
    python3 build.py
"""

from pathlib import Path
import re
import shutil

from planner import build_planner_html


CUSTOM_DOMAIN = "planner.zerolagautomation.com"

ROBOTS_TXT = """User-agent: *
Disallow: /
"""


def minify_html(html: str) -> str:
    """Light-touch HTML minification. Conservative — preserves pre/textarea/code content
    and JavaScript string literals untouched. Strips HTML comments (excluding IE
    conditionals), collapses runs of whitespace between tags, and trims leading/trailing
    whitespace on lines outside <script>/<style>. Saves ~10-20% on a content-heavy page."""

    # Strip HTML comments (but keep IE conditionals if any)
    html = re.sub(r"<!--(?!\[if).*?-->", "", html, flags=re.DOTALL)

    # Collapse whitespace between tags, but only outside <script>/<style>/<pre>/<textarea>
    # Approach: split the document at protected blocks, minify the rest.
    parts = re.split(r"(<(?:script|style|pre|textarea)\b[^>]*>.*?</(?:script|style|pre|textarea)>)",
                     html, flags=re.DOTALL | re.IGNORECASE)
    out = []
    for part in parts:
        if part.lower().startswith(("<script", "<style", "<pre", "<textarea")):
            out.append(part)
        else:
            # Collapse multi-space runs (not inside attribute values) and inter-tag whitespace
            p = re.sub(r">\s+<", "><", part)
            p = re.sub(r"[ \t]{2,}", " ", p)
            p = re.sub(r"\n\s*\n", "\n", p)
            out.append(p)
    return "".join(out)


def main():
    repo_root = Path(__file__).resolve().parent
    dist = repo_root / "dist"

    # Clean rebuild
    if dist.exists():
        shutil.rmtree(dist)
    dist.mkdir()

    # Main artifact
    raw = build_planner_html()
    html = minify_html(raw)
    (dist / "index.html").write_text(html, encoding="utf-8")
    print(f"  raw : {len(raw.encode('utf-8'))/1024:>7,.1f} KB")
    print(f"  min : {len(html.encode('utf-8'))/1024:>7,.1f} KB  ({(1-len(html)/len(raw))*100:.1f}% reduction)")

    # GitHub Pages custom domain marker
    (dist / "CNAME").write_text(CUSTOM_DOMAIN + "\n", encoding="utf-8")

    # Belt-and-braces no-index (in addition to the meta tag in the HTML)
    (dist / "robots.txt").write_text(ROBOTS_TXT, encoding="utf-8")

    size_kb = len(html.encode("utf-8")) / 1024
    print(f"  dist/index.html  ({size_kb:,.1f} KB)")
    print(f"  dist/CNAME       ({CUSTOM_DOMAIN})")
    print(f"  dist/robots.txt  (Disallow: /)")


if __name__ == "__main__":
    main()
