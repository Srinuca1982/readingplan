"""CI build script — writes the planner output to ./dist/.

Used by the GitHub Actions workflow. Local users keep using planner.py (which
writes to OneDrive). This script writes to a clean ./dist/ folder ready for
GitHub Pages deployment.

Usage (CI or local test):
    python3 build.py
"""

from pathlib import Path
import shutil

from planner import build_planner_html


CUSTOM_DOMAIN = "planner.zerolagautomation.com"

ROBOTS_TXT = """User-agent: *
Disallow: /
"""


def main():
    repo_root = Path(__file__).resolve().parent
    dist = repo_root / "dist"

    # Clean rebuild
    if dist.exists():
        shutil.rmtree(dist)
    dist.mkdir()

    # Main artifact
    html = build_planner_html()
    (dist / "index.html").write_text(html, encoding="utf-8")

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
