"""
Study Planner — single-file edition with per-subject tabs.

Generates one self-contained planner.html with eight top-level tabs:
  Restructuring · Ind AS · IT Act 2025 · Internal Audit ·
  Labour Codes · Auditing · English · Notebook

Each subject tab shows its own roadmap, topics/concepts, deep-dive notes,
books and online sources — laid out consistently across subjects.

Progress saves in browser localStorage. Re-running does not erase it.
"""

import json
import os
import shutil
import webbrowser
from pathlib import Path

from content_roadmap import WEEKS, BOOKS, SOURCES, MATRIX
from content_concepts import CONCEPTS
from content_notes import NOTES
from content_cheatsheets import CHEATSHEETS
from content_caselaw import CASELAW
from content_mastery import AREAS as MASTERY_AREAS
from content_mastery_notes import MASTERY_NOTES
from content_glossary import GLOSSARY
from content_templates import TEMPLATES
from content_examples import EXAMPLES
from templates import PLANNER_HTML


def safe_json(obj):
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


def build_areas():
    """Combine restructuring + 6 mastery areas into one unified list."""
    # Restructuring's "materials" — notes + cheat sheets + case digests
    materials = []
    for n in NOTES:
        materials.append({
            "kind": "Study Note",
            "title": n["title"],
            "summary": n["summary"],
            "body": n["body"],
            "slug": "notes-" + n["slug"],
        })
    for c in CHEATSHEETS:
        materials.append({
            "kind": "Cheat Sheet",
            "title": c["title"],
            "summary": c["summary"],
            "body": c["body"],
            "slug": "cheat-" + c["slug"],
        })
    for c in CASELAW:
        materials.append({
            "kind": "Case Digest",
            "title": c["title"],
            "summary": c["summary"],
            "body": c["body"],
            "slug": "case-" + c["slug"],
        })

    # Worked examples grouped by subject
    examples_by_subject = {}
    for ex in EXAMPLES:
        examples_by_subject.setdefault(ex["subject"], []).append(ex)

    areas = [{
        "slug": "restructuring",
        "title": "Restructuring",
        "subtitle": "12-week curriculum across the Companies Act, Income-tax Act, FEMA, SEBI and allied regimes.",
        "summary": (
            "A staged path through every statute that touches a corporate "
            "restructuring transaction. The 12-week roadmap covers schemes, tax, "
            "FEMA, listed-company specifics and IBC — paired with concepts, "
            "case-law digests, cheat sheets and a cross-statute matrix."
        ),
        "task_prefix": "w",
        "weeks": WEEKS,
        "concepts": CONCEPTS,
        "materials": materials,
        "templates": TEMPLATES,
        "examples": (
            examples_by_subject.get("Restructuring", []) +
            examples_by_subject.get("Tax", [])
        ),
        "matrix": MATRIX,
        "books": BOOKS,
        "sources": SOURCES,
    }]

    notes_by_slug = {n["slug"]: n for n in MASTERY_NOTES}

    # Map mastery slug → which examples subject feeds it
    examples_subject_for = {
        "ind-as": "Ind AS",
        "it-act-2025": "Tax",
    }

    for i, ma in enumerate(MASTERY_AREAS):
        note = notes_by_slug.get(ma["slug"], {})
        subj = examples_subject_for.get(ma["slug"])
        areas.append({
            "slug": ma["slug"],
            "title": ma["title"],
            "subtitle": ma["subtitle"],
            "summary": ma["summary"],
            "task_prefix": f"m{i}_w",
            "weeks": ma["weeks"],
            "topics": ma["topics"],
            "note_body": note.get("body", ""),
            "examples": examples_by_subject.get(subj, []) if subj else [],
            "books": ma["books"],
            "sources": ma["sources"],
        })

    return areas


def build_planner_html():
    return (PLANNER_HTML
            .replace("__AREAS__", safe_json(build_areas()))
            .replace("__GLOSSARY__", safe_json(GLOSSARY)))


def find_target_dir():
    for var in ("OneDrive", "OneDriveConsumer", "OneDriveCommercial"):
        val = os.environ.get(var)
        if val and Path(val).expanduser().exists():
            return Path(val).expanduser() / "Claude" / "readingplan", "onedrive_env"
    home_od = Path.home() / "OneDrive"
    if home_od.exists():
        return home_od / "Claude" / "readingplan", "onedrive_home"
    cloud_storage = Path.home() / "Library" / "CloudStorage"
    if cloud_storage.exists():
        for child in cloud_storage.iterdir():
            if child.name.startswith("OneDrive"):
                return child / "Claude" / "readingplan", "onedrive_cloudstorage"
    return Path.home() / "Claude" / "readingplan", "fallback_home"


SOURCE_FILES = [
    "planner.py",
    "build.py",
    "content_roadmap.py",
    "content_concepts.py",
    "content_notes.py",
    "content_cheatsheets.py",
    "content_caselaw.py",
    "content_mastery.py",
    "content_mastery_notes.py",
    "content_glossary.py",
    "content_templates.py",
    "content_examples.py",
    "templates.py",
]


def main():
    target_dir, status = find_target_dir()
    target_dir.mkdir(parents=True, exist_ok=True)

    here = Path(__file__).resolve().parent
    copied = []
    for name in SOURCE_FILES:
        src = here / name
        dst = target_dir / name
        if src.exists() and src.resolve() != dst.resolve():
            try:
                shutil.copy2(src, dst)
                copied.append(name)
            except Exception as e:
                print(f"  Note: could not copy {name} ({e}).")

    html_path = target_dir / "planner.html"
    html = build_planner_html()
    html_path.write_text(html, encoding="utf-8")

    url = html_path.as_uri()
    size_kb = len(html.encode("utf-8")) / 1024

    bar = "=" * 68
    print(bar)
    print("  Study Planner — Restructuring + 6 Mastery Areas")
    print(bar)
    print(f"  Folder    : {target_dir}")
    print(f"  Status    : {status}")
    if copied:
        print(f"  Copied    : {', '.join(copied)}")
    print(f"  Wrote     : planner.html  ({size_kb:,.1f} KB, fully self-contained)")
    print(f"  Opening   : {url}")
    print()
    print("  Your progress is saved in the browser. Re-running this script")
    print("  does NOT erase it.")
    print(bar)

    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"  Note: could not auto-open browser ({e}).")
        print(f"  Open the file manually: {html_path}")


if __name__ == "__main__":
    main()
