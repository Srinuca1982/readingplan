"""HTML template for the unified single-file planner.

Tabs are per-subject: Restructuring, Ind AS, IT Act 2025, Internal Audit,
Labour Codes, Auditing, English, Notebook. Each subject tab shows the same
kind of sections inline — roadmap, topics/concepts, deep-dive notes, books
and online sources — with restructuring also showing case-law materials and
a cross-statute matrix.
"""

CSS = r"""
:root {
  --bg: #faf7f0;
  --bg-tint: #fdfbf6;
  --paper: #ffffff;
  --paper-2: #fbf8f1;
  --paper-3: #f7f2e6;
  --ink: #2c2a28;
  --ink-soft: #5a554c;
  --ink-mute: #9c968a;
  --accent: #a05661;
  --accent-deep: #7e3d49;
  --accent-soft: #d6a8b0;
  --accent-tint: #f7e8eb;
  --gold: #b48854;
  --gold-soft: #e0c194;
  --gold-tint: #f8efdb;
  --sage: #7d9484;
  --sage-tint: #e6ede8;
  --border: #ede4d0;
  --border-soft: #f4ecd9;
  --code-bg: #f7ecd4;
  --shadow-sm: 0 1px 2px rgba(160, 130, 90, 0.08);
  --shadow: 0 2px 4px rgba(160, 130, 90, 0.06), 0 6px 18px rgba(160, 130, 90, 0.08);
  --shadow-lg: 0 4px 8px rgba(160, 130, 90, 0.08), 0 16px 36px rgba(160, 130, 90, 0.10);
}

* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }

body {
  background: var(--bg);
  background-image:
    radial-gradient(at 20% 0%, var(--accent-tint) 0%, transparent 35%),
    radial-gradient(at 90% 100%, var(--sage-tint) 0%, transparent 45%);
  background-attachment: fixed;
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 16px;
  line-height: 1.65;
  -webkit-font-smoothing: antialiased;
  letter-spacing: 0.005em;
}

.container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 40px 28px 80px;
}

a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }

/* === Header === */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 28px;
  padding: 28px 32px;
  margin-bottom: 28px;
  background: var(--paper);
  border: 1px solid var(--border-soft);
  border-radius: 16px;
  box-shadow: var(--shadow);
}
.header-text { flex: 1; min-width: 280px; }
.eyebrow {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 8px;
  display: inline-block;
  background: var(--accent-tint);
  padding: 4px 10px;
  border-radius: 12px;
}
h1 {
  font-size: clamp(1.8rem, 4vw, 2.3rem);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.15;
  color: var(--ink);
}
.subtitle {
  margin-top: 8px;
  font-size: 0.98rem;
  color: var(--ink-soft);
  max-width: 620px;
  line-height: 1.55;
}
.progress-card {
  background: linear-gradient(135deg, var(--gold-tint), var(--accent-tint));
  border: 1px solid var(--border-soft);
  padding: 16px 22px;
  min-width: 200px;
  border-radius: 12px;
  box-shadow: var(--shadow-sm);
}
.progress-card .label {
  font-size: 10px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--ink-soft);
  margin-bottom: 4px;
  font-weight: 600;
}
.progress-card .value {
  font-size: 1.8rem;
  font-weight: 700;
  color: var(--ink);
  letter-spacing: -0.02em;
}
.progress-card .pct { color: var(--accent); margin-left: 2px; font-size: 1rem; }
.progress-bar {
  margin-top: 8px;
  height: 6px;
  background: rgba(255, 255, 255, 0.65);
  border-radius: 4px;
  overflow: hidden;
}
.progress-bar-fill {
  height: 100%;
  width: 0;
  background: linear-gradient(90deg, var(--gold), var(--accent));
  border-radius: 4px;
  transition: width 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}
.progress-card .meta {
  margin-top: 6px;
  font-size: 11px;
  color: var(--ink-mute);
}

/* === Tabs === */
.tabs {
  display: flex;
  gap: 8px;
  margin-bottom: 28px;
  padding: 6px;
  background: var(--paper);
  border: 1px solid var(--border-soft);
  border-radius: 14px;
  box-shadow: var(--shadow-sm);
  overflow-x: auto;
  flex-wrap: wrap;
}
.tab {
  background: transparent;
  border: 1px solid transparent;
  padding: 9px 16px;
  font-size: 0.92rem;
  font-weight: 500;
  color: var(--ink-soft);
  cursor: pointer;
  border-radius: 9px;
  white-space: nowrap;
  font-family: inherit;
  transition: all 0.18s ease;
  letter-spacing: 0.01em;
}
.tab:hover {
  color: var(--ink);
  background: var(--paper-2);
}
.tab.active {
  color: var(--accent);
  background: var(--accent-tint);
  border-color: var(--accent-soft);
  font-weight: 600;
}

.tab-panel { display: none; }
.tab-panel.active { display: block; animation: fade 0.3s cubic-bezier(0.16, 1, 0.3, 1); }
@keyframes fade { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: none; } }

/* === Area header === */
.area-intro {
  margin-bottom: 24px;
  padding: 24px 28px;
  background: linear-gradient(135deg, var(--accent-tint) 0%, var(--paper) 60%);
  border: 1px solid var(--border-soft);
  border-radius: 14px;
  box-shadow: var(--shadow-sm);
}
.area-intro h2 {
  font-size: 1.6rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--ink);
  margin-bottom: 4px;
}
.area-intro .subtitle-line {
  font-size: 0.98rem;
  color: var(--accent-deep);
  margin-bottom: 8px;
  font-weight: 500;
}
.area-intro .area-summary {
  font-size: 0.95rem;
  color: var(--ink-soft);
  max-width: 760px;
  line-height: 1.6;
}

/* === Table of contents === */
.toc-box {
  background: linear-gradient(180deg, var(--paper) 70%, var(--paper-2));
  border: 1px solid var(--border-soft);
  border-radius: 14px;
  box-shadow: var(--shadow);
  margin-bottom: 24px;
  overflow: hidden;
}
.toc-box > summary {
  list-style: none;
  cursor: pointer;
  padding: 18px 24px;
  display: flex;
  align-items: center;
  gap: 14px;
  border-bottom: 1px solid transparent;
  transition: background 0.15s;
}
.toc-box[open] > summary { border-bottom-color: var(--border-soft); }
.toc-box > summary::-webkit-details-marker { display: none; }
.toc-box > summary:hover { background: var(--paper-2); }
.toc-title {
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  color: var(--accent);
  font-weight: 700;
}
.toc-hint {
  font-size: 12px;
  color: var(--ink-mute);
  flex: 1;
}
.toc-list {
  list-style: none;
  padding: 14px 24px 18px;
  margin: 0;
  column-count: 1;
}
@media (min-width: 720px) { .toc-list { column-count: 2; column-gap: 36px; } }
.toc-row {
  break-inside: avoid;
  margin-bottom: 10px;
}
.toc-chapter {
  display: inline-block;
  font-size: 0.98rem;
  font-weight: 600;
  color: var(--ink);
  text-decoration: none;
  margin-bottom: 4px;
}
.toc-chapter:hover { color: var(--accent); text-decoration: none; }
.toc-num {
  display: inline-block;
  min-width: 28px;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 0.86em;
  color: var(--accent);
  font-weight: 700;
}
.toc-count {
  font-weight: 400;
  color: var(--ink-mute);
  font-size: 0.88em;
}
.toc-subs {
  list-style: none;
  padding: 0 0 0 28px;
  margin: 4px 0 0 0;
}
.toc-subs li { margin: 2px 0; }
.toc-subs a {
  font-size: 0.88rem;
  color: var(--ink-soft);
  text-decoration: none;
  line-height: 1.4;
}
.toc-subs a:hover { color: var(--accent); }
.toc-subs .toc-num {
  min-width: 32px;
  font-size: 0.78em;
}
.toc-more {
  font-size: 0.82rem;
  color: var(--ink-mute);
  font-style: italic;
  padding-left: 32px;
}

/* === Chapter number labels === */
.chapter-num {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--accent);
  background: var(--accent-tint);
  padding: 3px 9px;
  border-radius: 10px;
  margin-right: 10px;
  white-space: nowrap;
}
.chapter-sub-num {
  display: inline-block;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 0.78em;
  font-weight: 700;
  color: var(--accent);
  background: var(--accent-tint);
  padding: 2px 7px;
  border-radius: 8px;
  margin-right: 6px;
  white-space: nowrap;
}
.book-num {
  position: absolute;
  top: 14px;
  right: 16px;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 0.78em;
  font-weight: 700;
  color: var(--gold);
  background: var(--gold-tint);
  padding: 2px 8px;
  border-radius: 8px;
}
.book-card { position: relative; }

.section-top-link {
  margin-top: 18px;
  padding-top: 12px;
  border-top: 1px dashed var(--border-soft);
  text-align: right;
}
.section-top-link a {
  font-size: 0.85rem;
  color: var(--ink-mute);
  text-decoration: none;
}
.section-top-link a:hover { color: var(--accent); }

/* === Section accordion === */
.content-section {
  margin-bottom: 14px;
  background: var(--paper);
  border: 1px solid var(--border-soft);
  border-radius: 12px;
  box-shadow: var(--shadow-sm);
  overflow: hidden;
  transition: box-shadow 0.2s;
}
.content-section[open] { box-shadow: var(--shadow); }
.content-section > summary {
  list-style: none;
  cursor: pointer;
  padding: 18px 26px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  position: relative;
  transition: background 0.15s;
}
.content-section > summary::-webkit-details-marker { display: none; }
.content-section > summary:hover { background: var(--paper-2); }
.section-title {
  display: flex;
  align-items: center;
  gap: 14px;
  flex: 1;
}
.section-title-text {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--ink);
  letter-spacing: -0.005em;
}
.section-count {
  display: inline-block;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.06em;
  color: var(--ink-soft);
  background: var(--paper-3);
  padding: 3px 10px;
  border-radius: 10px;
  border: 1px solid var(--border-soft);
}
.section-chevron {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--accent-tint);
  color: var(--accent);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.05rem;
  font-weight: 600;
  line-height: 1;
  transition: transform 0.25s ease;
}
.content-section[open] .section-chevron { transform: rotate(180deg); }
.section-chevron::before { content: "▾"; }
.section-body {
  padding: 6px 26px 28px;
  border-top: 1px solid var(--border-soft);
}

/* === Week cards === */
.weeks-grid { display: grid; gap: 12px; }
.week-card {
  background: var(--paper-2);
  border: 1px solid var(--border-soft);
  border-radius: 10px;
  padding: 18px 22px;
  position: relative;
  transition: all 0.2s ease;
}
.week-card::before {
  content: "";
  position: absolute;
  left: 0;
  top: 16px;
  bottom: 16px;
  width: 3px;
  background: var(--border);
  border-radius: 0 3px 3px 0;
  transition: background 0.2s;
}
.week-card:hover {
  background: var(--paper);
  box-shadow: var(--shadow-sm);
}
.week-card:hover::before { background: var(--accent-soft); }
.week-card.complete {
  background: linear-gradient(135deg, var(--gold-tint), var(--paper));
  border-color: var(--gold-soft);
}
.week-card.complete::before { background: var(--gold); }
.week-card.complete::after {
  content: "✓ COMPLETE";
  position: absolute;
  top: 18px;
  right: 22px;
  font-size: 10px;
  letter-spacing: 0.14em;
  color: var(--gold);
  font-weight: 700;
}
.week-head {
  display: flex;
  align-items: baseline;
  gap: 12px;
  margin-bottom: 6px;
  flex-wrap: wrap;
}
.week-tag {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  background: var(--accent-tint);
  padding: 4px 10px;
  border-radius: 10px;
  border: 1px solid var(--accent-soft);
}
.week-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--ink);
}
.week-focus {
  font-size: 0.95rem;
  color: var(--ink-soft);
  font-style: italic;
  margin-bottom: 10px;
}
.tasks { list-style: none; }
.task {
  display: flex;
  gap: 10px;
  align-items: flex-start;
  padding: 7px 0;
  cursor: pointer;
  font-size: 0.94rem;
  color: var(--ink-soft);
  border-bottom: 1px dashed var(--border-soft);
}
.task:last-child { border-bottom: none; }
.task:hover { color: var(--ink); }
.task input[type="checkbox"] {
  appearance: none;
  -webkit-appearance: none;
  width: 16px;
  height: 16px;
  border: 1.5px solid var(--ink-mute);
  border-radius: 3px;
  margin-top: 3px;
  flex-shrink: 0;
  cursor: pointer;
  position: relative;
}
.task input[type="checkbox"]:checked {
  background: var(--accent);
  border-color: var(--accent);
}
.task input[type="checkbox"]:checked::after {
  content: "";
  position: absolute;
  left: 4px;
  top: 1px;
  width: 4px;
  height: 9px;
  border: solid #fff;
  border-width: 0 1.5px 1.5px 0;
  transform: rotate(45deg);
}
.task.done { color: var(--ink-mute); text-decoration: line-through; }

/* === Concept cards (restructuring) === */
.concept {
  background: var(--paper-2);
  border: 1px solid var(--border-soft);
  border-radius: 10px;
  padding: 18px 22px;
  margin-bottom: 10px;
  transition: all 0.18s;
}
.concept:hover { background: var(--paper); box-shadow: var(--shadow-sm); }
.concept[open] { background: var(--paper); box-shadow: var(--shadow-sm); }
.concept summary {
  cursor: pointer;
  list-style: none;
  outline: none;
  position: relative;
  padding-right: 30px;
}
.concept summary::-webkit-details-marker { display: none; }
.concept summary::after {
  content: "+";
  position: absolute;
  right: 0;
  top: -2px;
  font-size: 1.4rem;
  color: var(--accent);
  font-weight: 300;
  line-height: 1;
}
.concept[open] summary::after { content: "−"; }
.concept-tag {
  display: inline-block;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--sage);
  background: var(--sage-tint);
  padding: 4px 10px;
  border-radius: 10px;
  margin-bottom: 8px;
}
.concept-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--ink);
  margin-bottom: 4px;
}
.concept-summary {
  font-size: 0.95rem;
  color: var(--ink-soft);
  font-style: italic;
}
.concept-body {
  margin-top: 14px;
  padding-top: 14px;
  border-top: 1px solid var(--border-soft);
  font-size: 0.96rem;
  color: var(--ink-soft);
}
.concept-body h4 {
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--gold);
  margin: 14px 0 6px;
  font-weight: 700;
}
.concept-body h4:first-child { margin-top: 0; }
.concept-body p { margin-bottom: 8px; }
.concept-body .example {
  background: var(--paper-2);
  border-left: 3px solid var(--gold);
  padding: 12px 16px;
  margin: 10px 0;
  border-radius: 0 4px 4px 0;
}
.concept-body code, .concept-body .sec {
  background: var(--code-bg);
  padding: 1px 6px;
  border-radius: 3px;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 0.88em;
  color: var(--ink);
}

/* === Topics list === */
.topics-list {
  columns: 2;
  column-gap: 28px;
  margin-left: 18px;
}
.topics-list li {
  margin-bottom: 5px;
  font-size: 0.95rem;
  color: var(--ink-soft);
  break-inside: avoid;
}
@media (max-width: 720px) {
  .topics-list { columns: 1; }
}

/* === Deep-dive note (now rendered as inline article inside its dropdown) === */
.deep-dive-body {
  background: var(--paper-2);
  padding: 24px 28px;
  border-radius: 10px;
  font-size: 0.98rem;
  line-height: 1.7;
  color: var(--ink-soft);
}

/* Article body shared styles — used by deep-dive AND material-item bodies */
.article-body h2 {
  font-size: 1.22rem;
  color: var(--ink);
  margin: 22px 0 8px;
  font-weight: 700;
  letter-spacing: -0.005em;
}
.article-body h2:first-child { margin-top: 0; }
.article-body h3 {
  font-size: 1.05rem;
  color: var(--ink);
  margin: 18px 0 6px;
  font-weight: 700;
}
.article-body h4 {
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--accent);
  margin: 16px 0 6px;
  font-weight: 700;
}
.article-body p { margin-bottom: 8px; }
.article-body ul, .article-body ol { margin: 0 0 10px 22px; }
.article-body li { margin-bottom: 3px; }
.article-body code, .article-body .sec {
  background: var(--code-bg);
  padding: 1px 6px;
  border-radius: 3px;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 0.86em;
  color: var(--ink);
}
.article-body blockquote {
  border-left: 3px solid var(--gold);
  background: var(--paper);
  padding: 10px 16px;
  margin: 10px 0;
  font-style: italic;
  color: var(--ink-soft);
  border-radius: 0 4px 4px 0;
}
.article-body .callout {
  border-left: 3px solid var(--accent);
  background: rgba(122, 43, 52, 0.05);
  padding: 12px 16px;
  margin: 14px 0;
  border-radius: 0 4px 4px 0;
}
.article-body .callout strong { color: var(--accent); }
.article-body table {
  width: 100%;
  min-width: 0;
  margin: 12px 0;
  border-collapse: collapse;
  font-size: 0.9rem;
}
.article-body table th {
  background: var(--paper);
  text-align: left;
  padding: 10px 12px;
  border-bottom: 2px solid var(--accent);
  border-right: 1px solid var(--border-soft);
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--accent);
  font-weight: 700;
}
.article-body table td {
  padding: 10px 12px;
  border-bottom: 1px solid var(--border-soft);
  border-right: 1px solid var(--border-soft);
  vertical-align: top;
}
.article-body table th:last-child,
.article-body table td:last-child { border-right: none; }

/* === Material items (restructuring's notes/cheat sheets/case digests) === */
.materials-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 14px;
}
.materials-filter {
  background: var(--paper-2);
  border: 1px solid var(--border-soft);
  border-radius: 16px;
  padding: 6px 14px;
  font: inherit;
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 0.03em;
  color: var(--ink-soft);
  cursor: pointer;
  transition: all 0.15s;
}
.materials-filter:hover { border-color: var(--accent-soft); color: var(--ink); background: var(--accent-tint); }
.materials-filter.active {
  background: var(--accent);
  color: #fff;
  border-color: var(--accent);
}
.material-group { margin-bottom: 22px; }
.material-group-head {
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: var(--accent);
  font-weight: 700;
  margin-bottom: 10px;
}
.material-item {
  background: var(--paper-2);
  border: 1px solid var(--border-soft);
  border-radius: 10px;
  margin-bottom: 8px;
  overflow: hidden;
  transition: all 0.15s;
}
.material-item:hover { background: var(--paper); }
.material-item[open] { background: var(--paper); box-shadow: var(--shadow-sm); }
.material-item summary {
  list-style: none;
  cursor: pointer;
  padding: 12px 20px;
  position: relative;
  padding-right: 50px;
  transition: background 0.15s;
}
.material-item summary::-webkit-details-marker { display: none; }
.material-item summary:hover { background: var(--paper-2); }
.material-item summary::after {
  content: "+";
  position: absolute;
  top: 10px;
  right: 20px;
  font-size: 1.4rem;
  color: var(--accent);
  font-weight: 300;
  line-height: 1;
}
.material-item[open] summary::after { content: "−"; }
.material-item-title {
  font-size: 1rem;
  font-weight: 700;
  color: var(--ink);
  margin-bottom: 2px;
}
.material-item-summary {
  font-size: 0.9rem;
  color: var(--ink-soft);
  font-style: italic;
}
.material-item-body {
  border-top: 1px solid var(--border-soft);
  padding: 22px 28px 26px;
  background: var(--paper);
  font-size: 0.97rem;
  line-height: 1.7;
  color: var(--ink-soft);
}

/* === Books === */
.books-grid {
  display: grid;
  gap: 14px;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
}
.book-card {
  background: linear-gradient(180deg, var(--paper) 60%, var(--gold-tint) 100%);
  border: 1px solid var(--border-soft);
  border-radius: 12px;
  padding: 18px 20px;
  display: flex;
  flex-direction: column;
  position: relative;
  transition: all 0.2s ease;
}
.book-card::before {
  content: "";
  position: absolute;
  left: 0;
  top: 18px;
  bottom: 18px;
  width: 3px;
  background: var(--gold);
  border-radius: 0 3px 3px 0;
}
.book-card:hover { transform: translateY(-2px); box-shadow: var(--shadow); }
.book-priority {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 6px;
}
.book-title {
  font-size: 1rem;
  font-weight: 700;
  color: var(--ink);
  margin-bottom: 2px;
  line-height: 1.25;
}
.book-author {
  font-size: 0.92rem;
  color: var(--ink-soft);
  font-style: italic;
  margin-bottom: 2px;
}
.book-publisher {
  font-size: 11px;
  color: var(--ink-mute);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: 8px;
}
.book-why {
  font-size: 0.92rem;
  color: var(--ink-soft);
  margin-bottom: 12px;
  flex: 1;
}
.book-toggle {
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--ink-mute);
  cursor: pointer;
  padding-top: 10px;
  border-top: 1px solid var(--border-soft);
  display: flex;
  align-items: center;
  gap: 8px;
  user-select: none;
}
.book-toggle input { display: none; }
.toggle-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  border: 1.5px solid var(--ink-mute);
}
.book-toggle input:checked + .toggle-dot { background: var(--gold); border-color: var(--gold); }
.book-toggle input:checked ~ .toggle-label { color: var(--gold); }

/* === Sources === */
.sources-list { display: grid; gap: 10px; }
.source-card {
  background: var(--paper-2);
  border: 1px solid var(--border-soft);
  border-radius: 10px;
  padding: 14px 20px;
  display: block;
  color: var(--ink);
  position: relative;
  transition: all 0.18s ease;
}
.source-card::before {
  content: "";
  position: absolute;
  left: 0;
  top: 14px;
  bottom: 14px;
  width: 3px;
  background: var(--sage);
  border-radius: 0 3px 3px 0;
  opacity: 0.6;
  transition: opacity 0.18s;
}
.source-card:hover {
  background: var(--paper);
  box-shadow: var(--shadow-sm);
  text-decoration: none;
  transform: translateX(2px);
}
.source-card:hover::before { opacity: 1; }
.source-type {
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: var(--sage);
  font-weight: 700;
  margin-bottom: 4px;
}
.source-title { font-size: 1rem; font-weight: 700; color: var(--ink); margin-bottom: 4px; }
.source-desc { font-size: 0.92rem; color: var(--ink-soft); margin-bottom: 4px; }
.source-url { font-size: 11px; color: var(--ink-mute); word-break: break-all; }

/* === Matrix === */
.matrix-wrap {
  overflow-x: auto;
  border: 1px solid var(--border-soft);
  background: var(--paper);
  border-radius: 10px;
}
.matrix-wrap table { width: 100%; border-collapse: collapse; font-size: 0.86rem; min-width: 900px; }
.matrix-wrap th, .matrix-wrap td {
  text-align: left;
  padding: 12px 14px;
  border-bottom: 1px solid var(--border-soft);
  border-right: 1px solid var(--border-soft);
  vertical-align: top;
}
.matrix-wrap th {
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--accent);
  font-weight: 700;
  background: rgba(122, 43, 52, 0.04);
  white-space: nowrap;
}
.matrix-wrap td:first-child {
  font-weight: 700;
  color: var(--ink);
  background: var(--paper-2);
  white-space: nowrap;
}
.matrix-wrap td { color: var(--ink-soft); line-height: 1.5; }
.matrix-wrap tr:last-child td { border-bottom: none; }
.matrix-wrap th:last-child, .matrix-wrap td:last-child { border-right: none; }

/* === Notebook === */
.notes-pad {
  background: var(--paper);
  border: 1px solid var(--border-soft);
  border-radius: 12px;
  box-shadow: var(--shadow-sm);
}
.notes-pad textarea {
  width: 100%;
  min-height: 480px;
  border: none;
  background: transparent;
  padding: 24px 28px;
  font-family: inherit;
  font-size: 1rem;
  line-height: 1.7;
  color: var(--ink);
  resize: vertical;
  outline: none;
}
.notes-meta {
  padding: 10px 28px;
  border-top: 1px solid var(--border-soft);
  font-size: 11px;
  color: var(--ink-mute);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  display: flex;
  justify-content: space-between;
}

/* === Footer === */
.footer {
  margin-top: 56px;
  padding-top: 22px;
  border-top: 1px solid var(--border);
  text-align: center;
  font-size: 11px;
  color: var(--ink-mute);
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

/* === Quiz === */
.quiz-item {
  background: var(--paper-2);
  border: 1px solid var(--border-soft);
  border-radius: 10px;
  padding: 16px 18px 14px;
  margin-bottom: 12px;
}
.quiz-q {
  font-size: 0.98rem;
  font-weight: 600;
  color: var(--ink);
  margin-bottom: 10px;
  line-height: 1.5;
}
.quiz-options {
  display: grid;
  gap: 6px;
}
.quiz-option {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  text-align: left;
  background: var(--paper);
  border: 1px solid var(--border-soft);
  border-radius: 8px;
  padding: 10px 14px;
  font: inherit;
  font-size: 0.94rem;
  color: var(--ink);
  cursor: pointer;
  transition: all 0.15s ease;
  width: 100%;
}
.quiz-option:hover:not(:disabled) {
  border-color: var(--accent-soft);
  background: var(--accent-tint);
}
.quiz-option:disabled { cursor: default; opacity: 0.85; }
.quiz-letter {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: var(--paper-3);
  font-size: 11px;
  font-weight: 700;
  color: var(--ink-soft);
  flex-shrink: 0;
}
.quiz-option.picked { border-color: var(--accent); }
.quiz-option.correct-answer {
  background: var(--sage-tint);
  border-color: var(--sage);
}
.quiz-option.correct-answer .quiz-letter { background: var(--sage); color: #fff; }
.quiz-option.wrong-pick {
  background: rgba(160, 86, 97, 0.08);
  border-color: var(--accent);
}
.quiz-option.wrong-pick .quiz-letter { background: var(--accent); color: #fff; }
.quiz-feedback {
  margin-top: 12px;
  padding: 12px 14px;
  background: var(--paper);
  border: 1px solid var(--border-soft);
  border-radius: 8px;
}
.quiz-verdict {
  font-weight: 700;
  font-size: 0.95rem;
  margin-bottom: 6px;
}
.quiz-explain { font-size: 0.94rem; }
.quiz-source {
  margin-top: 8px;
  padding-top: 8px;
  border-top: 1px solid var(--border-soft);
  font-size: 0.86rem;
  color: var(--ink-mute);
}
.quiz-score {
  padding: 10px 14px;
  background: var(--accent-tint);
  border-radius: 8px;
  border: 1px solid var(--accent-soft);
}

@media (max-width: 720px) {
  .container { padding: 28px 16px 60px; }
  .header { flex-direction: column; align-items: stretch; }
  .progress-card { text-align: left; }
  .material-item summary { padding: 10px 16px; padding-right: 44px; }
  .material-item-body { padding: 18px 16px; }
  .deep-dive summary { padding: 14px 18px; }
  .deep-dive-body { padding: 18px 18px 22px; }
}
"""

PLANNER_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex,nofollow">
<meta name="googlebot" content="noindex,nofollow">
<title>Study Planner — Restructuring &amp; Mastery</title>
<style>__CSS__</style>
</head>
<body>
<div class="container">

  <header class="header">
    <div class="header-text">
      <div class="eyebrow">Study Planner</div>
      <h1>Restructuring &amp; Six Mastery Areas</h1>
      <p class="subtitle">One self-contained companion for restructuring law plus Ind AS, IT Act 2025, Internal Audit, Labour Codes, Auditing and English.</p>
    </div>
    <div class="progress-card">
      <div class="label">Overall Progress</div>
      <div class="value"><span id="pct">0</span><span class="pct">%</span></div>
      <div class="progress-bar"><div class="progress-bar-fill" id="bar"></div></div>
      <div class="meta"><span id="done-count">0</span> / <span id="total-count">0</span> tasks</div>
    </div>
  </header>

  <nav class="tabs" id="tabs"></nav>

  <main id="panels"></main>

  <footer class="footer">Local Study Companion · single-file · v3</footer>
</div>

<script>
const AREAS = __AREAS__;
const GLOSSARY = __GLOSSARY__;

const STORAGE_KEY = "structuring_planner_v1";
const state = JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
state.tasks = state.tasks || {};
state.books = state.books || {};
state.notes = state.notes || "";
state.stats = state.stats || {};
state.stats.tabOpens = state.stats.tabOpens || {};
state.stats.sectionOpens = state.stats.sectionOpens || {};
state.stats.lastVisit = state.stats.lastVisit || {};
state.quiz = state.quiz || {};  // shape: state.quiz[areaSlug][qIndex] = { picked, correct }

function save() { localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); }

function escapeHTML(s) {
  return String(s == null ? "" : s).replace(/[&<>"']/g, c => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[c]));
}

let materialFilter = "all";
let glossaryFilter = "";

function taskId(area, wi, ti) {
  return area.task_prefix + wi + "_t" + ti;
}

function sectionShell(title, count, body, open, anchorId, chapterNum) {
  const openAttr = open ? " open" : "";
  const idAttr = anchorId ? ' id="' + anchorId + '"' : "";
  const countHTML = count != null ? '<span class="section-count">' + escapeHTML(count) + '</span>' : "";
  const chapterLabel = chapterNum != null
    ? '<span class="chapter-num">Chapter ' + chapterNum + '</span> '
    : "";
  const topLink = anchorId
    ? '<div class="section-top-link"><a href="#toc-' + anchorId + '">↑ Back to contents</a></div>'
    : "";
  return '<details class="content-section"' + idAttr + openAttr + '>' +
    '<summary>' +
      '<span class="section-title">' +
        chapterLabel +
        '<span class="section-title-text">' + escapeHTML(title) + '</span>' +
        countHTML +
      '</span>' +
      '<span class="section-chevron"></span>' +
    '</summary>' +
    '<div class="section-body">' + body + topLink + '</div>' +
  '</details>';
}

function buildChapters(area) {
  const chs = [];
  if (area.weeks && area.weeks.length) {
    chs.push({ kind: 'roadmap', title: 'Roadmap', count: area.weeks.length + ' weeks',
      items: area.weeks.map((w, i) => ({ idx: i, label: 'Week ' + w.week + ' — ' + w.title })) });
  }
  if (area.concepts && area.concepts.length) {
    chs.push({ kind: 'concepts', title: 'Concepts & Examples', count: area.concepts.length,
      items: area.concepts.map((c, i) => ({ idx: i, label: c.title })) });
  }
  if (area.topics && area.topics.length) {
    chs.push({ kind: 'topics', title: 'Key Topics', count: area.topics.length, items: [] });
  }
  if (area.note_body) {
    chs.push({ kind: 'note', title: 'Deep-Dive Study Note', count: null, items: [] });
  }
  if (area.examples && area.examples.length) {
    chs.push({ kind: 'examples', title: 'Worked Examples', count: area.examples.length,
      items: area.examples.map((e, i) => ({ idx: i, label: e.title })) });
  }
  if (area.quiz && area.quiz.length) {
    chs.push({ kind: 'quiz', title: 'Self-Test (MCQs)', count: area.quiz.length,
      items: area.quiz.map((q, i) => ({ idx: i, label: 'Q' + (i + 1) })) });
  }
  if (area.faqs && area.faqs.length) {
    chs.push({ kind: 'faqs', title: 'FAQ (official sources)', count: area.faqs.length,
      items: area.faqs.map((f, i) => ({ idx: i, label: f.q.length > 70 ? f.q.substring(0, 67) + '…' : f.q })) });
  }
  if (area.materials && area.materials.length) {
    chs.push({ kind: 'materials', title: 'Notes, Cheat Sheets & Case Law', count: area.materials.length,
      items: area.materials.map((m, i) => ({ idx: i, label: m.title })) });
  }
  if (area.templates && area.templates.length) {
    chs.push({ kind: 'templates', title: 'Drafting Templates', count: area.templates.length,
      items: area.templates.map((t, i) => ({ idx: i, label: t.title })) });
  }
  if (area.books && area.books.length) {
    chs.push({ kind: 'books', title: 'Books', count: area.books.length,
      items: area.books.map((b, i) => ({ idx: i, label: b.title })) });
  }
  if (area.sources && area.sources.length) {
    chs.push({ kind: 'sources', title: 'Online Sources', count: area.sources.length,
      items: area.sources.map((s, i) => ({ idx: i, label: s.name })) });
  }
  if (area.matrix) {
    chs.push({ kind: 'matrix', title: 'Cross-Statute Matrix', count: area.matrix.rows.length + ' modes', items: [] });
  }
  chs.forEach((c, i) => { c.num = i + 1; c.anchorId = area.slug + '-ch' + c.num; });
  return chs;
}

function chapterItemAnchorId(area, chapter, itemIdx) {
  return area.slug + '-ch' + chapter.num + '-' + (itemIdx + 1);
}

function renderTOC(area, chapters) {
  if (!chapters.length) return "";
  const rows = chapters.map(c => {
    let subs = "";
    if (c.items && c.items.length) {
      // Cap visible sub-items per chapter to keep TOC scannable; show first 8 + "more…"
      const maxShown = 8;
      const visible = c.items.slice(0, maxShown);
      subs = '<ul class="toc-subs">' + visible.map((it, i) =>
        '<li><a href="#' + escapeHTML(chapterItemAnchorId(area, c, i)) + '">' +
          '<span class="toc-num">' + c.num + '.' + (it.idx + 1) + '</span> ' +
          escapeHTML(it.label) + '</a></li>'
      ).join("") +
      (c.items.length > maxShown
        ? '<li class="toc-more">… and ' + (c.items.length - maxShown) + ' more</li>'
        : "")
      + '</ul>';
    }
    return '<li class="toc-row">' +
      '<a class="toc-chapter" href="#' + escapeHTML(c.anchorId) + '" id="toc-' + escapeHTML(c.anchorId) + '">' +
        '<span class="toc-num">' + c.num + '.</span> ' +
        escapeHTML(c.title) +
        (c.count != null ? ' <span class="toc-count">(' + escapeHTML(c.count) + ')</span>' : '') +
      '</a>' +
      subs +
    '</li>';
  }).join("");
  return '<details class="toc-box" open id="toc-' + escapeHTML(area.slug) + '">' +
    '<summary>' +
      '<span class="toc-title">Contents</span>' +
      '<span class="toc-hint">' + chapters.length + ' chapters · click any heading to jump</span>' +
      '<span class="section-chevron"></span>' +
    '</summary>' +
    '<ol class="toc-list">' + rows + '</ol>' +
  '</details>';
}

// ----- per-subject section renderers -----

function renderWeeksSection(area, chapter) {
  const rows = area.weeks.map((w, wi) => {
    const tasks = w.tasks.map((t, ti) => {
      const id = taskId(area, wi, ti);
      const done = !!state.tasks[id];
      return '<li class="task ' + (done ? 'done' : '') + '">' +
        '<input type="checkbox" data-id="' + escapeHTML(id) + '" ' + (done ? 'checked' : '') + '>' +
        '<span>' + escapeHTML(t) + '</span></li>';
    }).join("");
    const allDone = w.tasks.length > 0 && w.tasks.every((_, ti) => state.tasks[taskId(area, wi, ti)]);
    const anchor = chapterItemAnchorId(area, chapter, wi);
    return '<article class="week-card ' + (allDone ? 'complete' : '') + '" id="' + escapeHTML(anchor) + '">' +
      '<div class="week-head">' +
        '<span class="chapter-sub-num">' + chapter.num + '.' + (wi + 1) + '</span>' +
        '<span class="week-tag">Week ' + escapeHTML(w.week) + '</span>' +
        '<span class="week-title">' + escapeHTML(w.title) + '</span>' +
      '</div>' +
      '<p class="week-focus">' + escapeHTML(w.focus) + '</p>' +
      '<ul class="tasks">' + tasks + '</ul></article>';
  }).join("");
  const count = area.weeks.length + " weeks";
  return sectionShell("Roadmap", count, '<div class="weeks-grid">' + rows + '</div>', true, chapter.anchorId, chapter.num);
}

function renderConceptsSection(area, chapter) {
  if (!area.concepts || !area.concepts.length) return "";
  const html = area.concepts.map((c, i) => {
    const example = c.example ? '<h4>Example</h4><div class="example">' + c.example + '</div>' : '';
    const hooks = c.hooks ? '<h4>Statutory hooks</h4><p>' + c.hooks + '</p>' : '';
    const pitfalls = c.pitfalls ? '<h4>Common pitfalls</h4><p>' + c.pitfalls + '</p>' : '';
    const anchor = chapterItemAnchorId(area, chapter, i);
    return '<details class="concept" id="' + escapeHTML(anchor) + '">' +
      '<summary>' +
        '<span class="chapter-sub-num">' + chapter.num + '.' + (i + 1) + '</span> ' +
        '<span class="concept-tag">' + escapeHTML(c.tag) + '</span>' +
        '<div class="concept-title">' + escapeHTML(c.title) + '</div>' +
        '<div class="concept-summary">' + escapeHTML(c.summary) + '</div>' +
      '</summary>' +
      '<div class="concept-body">' +
        '<h4>The idea</h4><p>' + c.body + '</p>' +
        example + hooks + pitfalls +
      '</div></details>';
  }).join("");
  return sectionShell("Concepts & Examples", area.concepts.length, html, false, chapter.anchorId, chapter.num);
}

function renderTopicsSection(area, chapter) {
  if (!area.topics || !area.topics.length) return "";
  const items = area.topics.map(t => '<li>' + escapeHTML(t) + '</li>').join("");
  return sectionShell("Key Topics", area.topics.length, '<ul class="topics-list">' + items + '</ul>', false, chapter.anchorId, chapter.num);
}

function renderDeepDiveSection(area, chapter) {
  if (!area.note_body) return "";
  const body = '<div class="deep-dive-body article-body">' + area.note_body + '</div>';
  return sectionShell("Deep-Dive Study Note", null, body, false, chapter.anchorId, chapter.num);
}

function renderMaterialsSection(area, chapter) {
  if (!area.materials || !area.materials.length) return "";
  const filters = ['<button class="materials-filter ' + (materialFilter === "all" ? "active" : "") + '" data-filter="all">All</button>',
                   '<button class="materials-filter ' + (materialFilter === "Study Note" ? "active" : "") + '" data-filter="Study Note">Study Notes</button>',
                   '<button class="materials-filter ' + (materialFilter === "Cheat Sheet" ? "active" : "") + '" data-filter="Cheat Sheet">Cheat Sheets</button>',
                   '<button class="materials-filter ' + (materialFilter === "Case Digest" ? "active" : "") + '" data-filter="Case Digest">Case Law</button>'].join("");

  const groups = { "Study Note": [], "Cheat Sheet": [], "Case Digest": [] };
  // Build a flat-index map so each material gets the same subsection number across filters
  const flatIndex = new Map();
  area.materials.forEach((m, i) => { flatIndex.set(m.slug, i); if (groups[m.kind]) groups[m.kind].push(m); });
  const order = ["Study Note", "Cheat Sheet", "Case Digest"];
  const labels = { "Study Note": "Study Notes", "Cheat Sheet": "Cheat Sheets", "Case Digest": "Case Digests" };

  const groupsHTML = order.filter(k => groups[k].length && (materialFilter === "all" || materialFilter === k)).map(k => {
    const items = groups[k].map(m => {
      const i = flatIndex.get(m.slug);
      const anchor = chapterItemAnchorId(area, chapter, i);
      return '<details class="material-item" id="' + escapeHTML(anchor) + '">' +
        '<summary>' +
          '<div class="material-item-title"><span class="chapter-sub-num">' + chapter.num + '.' + (i + 1) + '</span> ' + escapeHTML(m.title) + '</div>' +
          '<div class="material-item-summary">' + escapeHTML(m.summary) + '</div>' +
        '</summary>' +
        '<div class="material-item-body article-body">' + m.body + '</div>' +
      '</details>';
    }).join("");
    return '<div class="material-group"><div class="material-group-head">' + escapeHTML(labels[k]) + '</div>' + items + '</div>';
  }).join("");

  const body = '<div class="materials-controls">' + filters + '</div>' +
               '<div id="materials-' + escapeHTML(area.slug) + '">' + groupsHTML + '</div>';
  return sectionShell("Notes, Cheat Sheets & Case Law", area.materials.length, body, false, chapter.anchorId, chapter.num);
}

function renderBooksSection(area, chapter) {
  if (!area.books || !area.books.length) return "";
  const cards = area.books.map((b, i) => {
    const id = "book_" + area.slug + "_" + i;
    const owned = !!state.books[id];
    const priority = b.priority || "";
    const publisher = b.publisher || "";
    const anchor = chapterItemAnchorId(area, chapter, i);
    return '<article class="book-card" id="' + escapeHTML(anchor) + '">' +
      '<div class="book-num">' + chapter.num + '.' + (i + 1) + '</div>' +
      (priority ? '<div class="book-priority">' + escapeHTML(priority) + '</div>' : "") +
      '<div class="book-title">' + escapeHTML(b.title) + '</div>' +
      '<div class="book-author">' + escapeHTML(b.author) + '</div>' +
      '<div class="book-publisher">' + escapeHTML(publisher) + '</div>' +
      '<p class="book-why">' + escapeHTML(b.why) + '</p>' +
      '<label class="book-toggle">' +
        '<input type="checkbox" data-book="' + escapeHTML(id) + '" ' + (owned ? "checked" : "") + '>' +
        '<span class="toggle-dot"></span>' +
        '<span class="toggle-label">' + (owned ? "In library" : "Mark acquired") + '</span>' +
      '</label></article>';
  }).join("");
  return sectionShell("Books", area.books.length, '<div class="books-grid">' + cards + '</div>', false, chapter.anchorId, chapter.num);
}

function renderSourcesSection(area, chapter) {
  if (!area.sources || !area.sources.length) return "";
  const cards = area.sources.map((s, i) => {
    const anchor = chapterItemAnchorId(area, chapter, i);
    return '<a class="source-card" id="' + escapeHTML(anchor) + '" href="' + escapeHTML(s.url) + '" target="_blank" rel="noopener">' +
      (s.type ? '<div class="source-type">' + escapeHTML(s.type) + '</div>' : "") +
      '<div class="source-title"><span class="chapter-sub-num">' + chapter.num + '.' + (i + 1) + '</span> ' + escapeHTML(s.name) + ' →</div>' +
      '<div class="source-desc">' + escapeHTML(s.description) + '</div>' +
      '<div class="source-url">' + escapeHTML(s.url) + '</div>' +
    '</a>';
  }).join("");
  return sectionShell("Online Sources", area.sources.length, '<div class="sources-list">' + cards + '</div>', false, chapter.anchorId, chapter.num);
}

function renderMatrixSection(area, chapter) {
  if (!area.matrix) return "";
  const m = area.matrix;
  const headers = ["Mode"].concat(m.columns);
  const head = '<thead><tr>' + headers.map(h => '<th>' + escapeHTML(h) + '</th>').join("") + '</tr></thead>';
  const body = '<tbody>' + m.rows.map(r =>
    '<tr>' + r.map(c => '<td>' + escapeHTML(c) + '</td>').join("") + '</tr>'
  ).join("") + '</tbody>';
  return sectionShell("Cross-Statute Matrix", m.rows.length + " modes", '<div class="matrix-wrap"><table>' + head + body + '</table></div>', false, chapter.anchorId, chapter.num);
}

function renderTemplatesSection(area, chapter) {
  if (!area.templates || !area.templates.length) return "";
  const items = area.templates.map((t, i) => {
    const anchor = chapterItemAnchorId(area, chapter, i);
    return '<details class="material-item" id="' + escapeHTML(anchor) + '">' +
      '<summary>' +
        '<div class="material-item-title"><span class="chapter-sub-num">' + chapter.num + '.' + (i + 1) + '</span> ' + escapeHTML(t.title) + '</div>' +
        '<div class="material-item-summary">' + escapeHTML(t.summary) + '</div>' +
      '</summary>' +
      '<div class="material-item-body article-body">' + t.body + '</div>' +
    '</details>';
  }).join("");
  return sectionShell("Drafting Templates", area.templates.length, items, false, chapter.anchorId, chapter.num);
}

function renderQuizSection(area, chapter) {
  if (!area.quiz || !area.quiz.length) return "";
  const items = area.quiz.map((q, i) => {
    const optsHTML = q.options.map((opt, oi) =>
      '<button class="quiz-option" data-area="' + escapeHTML(area.slug) + '" data-q="' + i + '" data-opt="' + oi + '">' +
        '<span class="quiz-letter">' + String.fromCharCode(65 + oi) + '</span>' +
        '<span class="quiz-opt-text">' + opt + '</span>' +
      '</button>'
    ).join("");
    const anchor = chapterItemAnchorId(area, chapter, i);
    return '<div class="quiz-item" data-correct="' + q.correct + '" id="' + escapeHTML(anchor) + '">' +
      '<div class="quiz-q"><span class="chapter-sub-num">' + chapter.num + '.' + (i + 1) + '</span> ' + q.q + '</div>' +
      '<div class="quiz-options">' + optsHTML + '</div>' +
      '<div class="quiz-feedback" style="display:none;">' +
        '<div class="quiz-verdict"></div>' +
        '<div class="quiz-explain article-body">' + q.explain + '</div>' +
        '<div class="quiz-source"><strong>Source:</strong> ' + escapeHTML(q.source) + '</div>' +
      '</div>' +
    '</div>';
  }).join("");
  const score = '<div class="quiz-score" data-area="' + escapeHTML(area.slug) + '" style="margin-bottom:12px;font-size:0.95rem;color:var(--ink-soft);"></div>';
  return sectionShell("Self-Test (MCQs)", area.quiz.length, score + items, false, chapter.anchorId, chapter.num);
}

function renderFAQSection(area, chapter) {
  if (!area.faqs || !area.faqs.length) return "";
  const items = area.faqs.map((f, i) => {
    const anchor = chapterItemAnchorId(area, chapter, i);
    return '<details class="material-item" id="' + escapeHTML(anchor) + '">' +
      '<summary>' +
        '<div class="material-item-title"><span class="chapter-sub-num">' + chapter.num + '.' + (i + 1) + '</span> ' + escapeHTML(f.q) + '</div>' +
        '<div class="material-item-summary">' + escapeHTML(f.source) + (f.ref ? ' &middot; ' + escapeHTML(f.ref) : '') + '</div>' +
      '</summary>' +
      '<div class="material-item-body article-body">' + f.a + '</div>' +
    '</details>';
  }).join("");
  return sectionShell("FAQ (from official sources)", area.faqs.length, items, false, chapter.anchorId, chapter.num);
}

function renderExamplesSection(area, chapter) {
  if (!area.examples || !area.examples.length) return "";
  const items = area.examples.map((ex, i) => {
    const anchor = chapterItemAnchorId(area, chapter, i);
    return '<details class="material-item" id="' + escapeHTML(anchor) + '">' +
      '<summary>' +
        '<div class="material-item-title"><span class="chapter-sub-num">' + chapter.num + '.' + (i + 1) + '</span> ' + escapeHTML(ex.title) + '</div>' +
        '<div class="material-item-summary">' + escapeHTML(ex.subject) + ' &middot; worked example</div>' +
      '</summary>' +
      '<div class="material-item-body article-body">' + ex.body + '</div>' +
    '</details>';
  }).join("");
  return sectionShell("Worked Examples", area.examples.length, items, false, chapter.anchorId, chapter.num);
}

// ----- top-level renderers -----

function renderTabs() {
  const tabs = document.getElementById("tabs");
  let html = AREAS.map((a, i) =>
    '<button class="tab ' + (i === 0 ? "active" : "") + '" data-target="panel-' + escapeHTML(a.slug) + '">' +
      escapeHTML(a.title) +
    '</button>'
  ).join("");
  html += '<button class="tab" data-target="panel-glossary">Glossary</button>';
  html += '<button class="tab" data-target="panel-notebook">Notebook</button>';
  tabs.innerHTML = html;
}

function renderPanels() {
  const panels = document.getElementById("panels");
  const renderers = {
    'roadmap': renderWeeksSection,
    'concepts': renderConceptsSection,
    'topics': renderTopicsSection,
    'note': renderDeepDiveSection,
    'examples': renderExamplesSection,
    'quiz': renderQuizSection,
    'faqs': renderFAQSection,
    'materials': renderMaterialsSection,
    'templates': renderTemplatesSection,
    'books': renderBooksSection,
    'sources': renderSourcesSection,
    'matrix': renderMatrixSection,
  };
  let html = AREAS.map((a, i) => {
    const chapters = buildChapters(a);
    const chaptersHTML = chapters.map(c => {
      const fn = renderers[c.kind];
      return fn ? fn(a, c) : "";
    }).join("");
    return '<section class="tab-panel ' + (i === 0 ? "active" : "") + '" id="panel-' + escapeHTML(a.slug) + '">' +
      '<div class="area-intro">' +
        '<h2>' + escapeHTML(a.title) + '</h2>' +
        '<p class="subtitle-line">' + escapeHTML(a.subtitle) + '</p>' +
        (a.summary ? '<p class="area-summary">' + escapeHTML(a.summary) + '</p>' : "") +
      '</div>' +
      renderTOC(a, chapters) +
      chaptersHTML +
    '</section>';
  }).join("");

  // Glossary panel
  html += '<section class="tab-panel" id="panel-glossary">' +
    '<div class="area-intro">' +
      '<h2>Glossary</h2>' +
      '<p class="subtitle-line">Every term that has a precise legal or professional meaning, with the section/standard that defines it.</p>' +
      '<p class="area-summary">' + GLOSSARY.length + ' terms. Use the search box to filter by term, definition or tag (Restructuring, Tax, Ind AS, FEMA, SEBI, Audit, Internal Audit, Labour, English).</p>' +
    '</div>' +
    '<section class="content-section" open style="background:transparent;border:none;box-shadow:none;">' +
      '<div class="section-body" style="padding:0;border:none;">' +
        '<input id="glossary-search" type="search" placeholder="Search terms…" value="' + escapeHTML(glossaryFilter) + '" ' +
          'style="width:100%;padding:12px 16px;border:1px solid var(--border-soft);border-radius:10px;font:inherit;background:var(--paper);margin-bottom:14px;outline:none;" />' +
        '<div id="glossary-list"></div>' +
      '</div>' +
    '</section>' +
  '</section>';

  // Notebook panel
  html += '<section class="tab-panel" id="panel-notebook">' +
    '<div class="area-intro">' +
      '<h2>Notebook &amp; Utilities</h2>' +
      '<p class="subtitle-line">A scratchpad plus your local study stats and progress backup tools.</p>' +
    '</div>' +

    sectionShell("Notebook", null,
      '<div class="notes-pad">' +
        '<textarea id="notes-text" placeholder="Begin writing — your notes are saved locally in this browser…"></textarea>' +
        '<div class="notes-meta">' +
          '<span>Auto-saved locally</span>' +
          '<span id="word-count">0 words</span>' +
        '</div>' +
      '</div>', true) +

    sectionShell("Your Study Stats (local, private)", null,
      '<div id="stats-body" style="font-size:0.95rem;color:var(--ink-soft);"></div>', false) +

    sectionShell("Backup &amp; Restore Progress", null,
      '<p style="margin-bottom:12px;">Your progress (task checkboxes, books, notes, stats) lives in this browser&rsquo;s storage. Download it as a JSON file to back up or move to another browser/device.</p>' +
      '<div style="display:flex;gap:10px;flex-wrap:wrap;">' +
        '<button id="btn-export" class="materials-filter active" style="border-radius:8px;padding:9px 16px;">Download progress.json</button>' +
        '<label class="materials-filter" style="border-radius:8px;padding:9px 16px;cursor:pointer;">Import from file' +
          '<input id="btn-import" type="file" accept="application/json" style="display:none;" />' +
        '</label>' +
        '<button id="btn-reset" class="materials-filter" style="border-radius:8px;padding:9px 16px;">Reset all progress…</button>' +
      '</div>' +
      '<div id="import-status" style="margin-top:10px;font-size:0.9rem;color:var(--ink-mute);"></div>', false) +

  '</section>';

  panels.innerHTML = html;
}

function flushPendingNotes() {
  const notesEl = document.getElementById("notes-text");
  if (notesEl && state.notes !== notesEl.value) {
    state.notes = notesEl.value;
    save();
  }
}

function updateQuizScore(areaSlug) {
  const scoreEl = document.querySelector('.quiz-score[data-area="' + areaSlug + '"]');
  if (!scoreEl) return;
  const area = AREAS.find(a => a.slug === areaSlug);
  if (!area || !area.quiz) return;
  const total = area.quiz.length;
  const answered = state.quiz[areaSlug] ? Object.keys(state.quiz[areaSlug]).length : 0;
  let correctCount = 0;
  if (state.quiz[areaSlug]) {
    Object.values(state.quiz[areaSlug]).forEach(r => { if (r.correct) correctCount++; });
  }
  if (answered === 0) {
    scoreEl.innerHTML = '<em>No answers yet. Pick an option below to begin.</em>';
  } else {
    const pct = Math.round((correctCount / answered) * 100);
    scoreEl.innerHTML = '<strong>Score:</strong> ' + correctCount + ' / ' + answered + ' answered (' + pct + '%) &middot; ' + (total - answered) + ' remaining';
  }
}

function trackTabOpen(slug) {
  state.stats.tabOpens[slug] = (state.stats.tabOpens[slug] || 0) + 1;
  state.stats.lastVisit[slug] = new Date().toISOString();
  save();
}

function todayKey() { return new Date().toISOString().slice(0, 10); }
function weekKey() {
  const d = new Date();
  const onejan = new Date(d.getFullYear(), 0, 1);
  const week = Math.ceil(((d - onejan) / 86400000 + onejan.getDay() + 1) / 7);
  return d.getFullYear() + "-W" + week;
}

function renderGlossary() {
  const container = document.getElementById("glossary-list");
  if (!container) return;
  const searchEl = document.getElementById("glossary-search");
  if (searchEl) glossaryFilter = searchEl.value;
  const filter = glossaryFilter.trim().toLowerCase();
  const sorted = [...GLOSSARY].sort((a, b) => a.term.localeCompare(b.term));
  const filtered = filter
    ? sorted.filter(g =>
        g.term.toLowerCase().includes(filter) ||
        g.definition.toLowerCase().includes(filter) ||
        (g.tags || []).some(t => t.toLowerCase().includes(filter)) ||
        (g.source || "").toLowerCase().includes(filter))
    : sorted;
  if (!filtered.length) {
    container.innerHTML = '<p style="padding:12px;color:var(--ink-mute);font-style:italic;">No matches.</p>';
    return;
  }
  container.innerHTML = filtered.map(g => {
    const tags = (g.tags || []).map(t =>
      '<span style="display:inline-block;font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--sage);background:var(--sage-tint);padding:2px 8px;border-radius:8px;margin-right:4px;">' + escapeHTML(t) + '</span>'
    ).join("");
    return '<div class="material-item" style="background:var(--paper-2);padding:14px 18px;">' +
      '<div style="display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:10px;margin-bottom:4px;">' +
        '<strong style="color:var(--ink);font-size:1rem;">' + escapeHTML(g.term) + '</strong>' +
        '<span style="font-size:11px;color:var(--ink-mute);font-family:ui-monospace,monospace;">' + escapeHTML(g.source) + '</span>' +
      '</div>' +
      '<p style="font-size:0.93rem;color:var(--ink-soft);margin-bottom:6px;">' + escapeHTML(g.definition) + '</p>' +
      '<div>' + tags + '</div>' +
    '</div>';
  }).join("");
}

function renderStats() {
  const container = document.getElementById("stats-body");
  if (!container) return;
  const tabs = state.stats.tabOpens || {};
  const entries = Object.entries(tabs).sort((a, b) => b[1] - a[1]);
  const totalOpens = entries.reduce((s, [, n]) => s + n, 0);
  const top = entries[0];
  const slugToTitle = {};
  AREAS.forEach(a => slugToTitle[a.slug] = a.title);
  slugToTitle["glossary"] = "Glossary";
  slugToTitle["notebook"] = "Notebook";
  if (!entries.length) {
    container.innerHTML = '<p style="font-style:italic;color:var(--ink-mute);">No activity tracked yet. Open tabs to start.</p>';
    return;
  }
  let html = '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px;margin-bottom:16px;">';
  html += '<div style="padding:12px 14px;background:var(--accent-tint);border-radius:8px;"><div style="font-size:11px;text-transform:uppercase;letter-spacing:0.1em;color:var(--accent-deep);font-weight:600;">Total tab opens</div><div style="font-size:1.4rem;font-weight:700;">' + totalOpens + '</div></div>';
  if (top) {
    html += '<div style="padding:12px 14px;background:var(--gold-tint);border-radius:8px;"><div style="font-size:11px;text-transform:uppercase;letter-spacing:0.1em;color:var(--gold);font-weight:600;">Most visited</div><div style="font-size:1rem;font-weight:700;">' + escapeHTML(slugToTitle[top[0]] || top[0]) + '</div><div style="font-size:0.85rem;color:var(--ink-mute);">' + top[1] + ' opens</div></div>';
  }
  html += '</div>';
  html += '<table style="width:100%;border-collapse:collapse;font-size:0.93rem;">' +
    '<thead><tr><th style="text-align:left;padding:8px;border-bottom:1px solid var(--border-soft);font-size:11px;text-transform:uppercase;letter-spacing:0.08em;color:var(--ink-soft);">Subject</th>' +
    '<th style="text-align:right;padding:8px;border-bottom:1px solid var(--border-soft);font-size:11px;text-transform:uppercase;letter-spacing:0.08em;color:var(--ink-soft);">Opens</th>' +
    '<th style="text-align:left;padding:8px;border-bottom:1px solid var(--border-soft);font-size:11px;text-transform:uppercase;letter-spacing:0.08em;color:var(--ink-soft);">Last visit</th></tr></thead><tbody>';
  entries.forEach(([slug, n]) => {
    const last = state.stats.lastVisit[slug];
    const lastTxt = last ? new Date(last).toLocaleString() : "—";
    html += '<tr><td style="padding:8px;border-bottom:1px solid var(--border-soft);">' + escapeHTML(slugToTitle[slug] || slug) +
      '</td><td style="padding:8px;text-align:right;border-bottom:1px solid var(--border-soft);font-variant-numeric:tabular-nums;">' + n +
      '</td><td style="padding:8px;border-bottom:1px solid var(--border-soft);color:var(--ink-mute);font-size:0.85rem;">' + escapeHTML(lastTxt) + '</td></tr>';
  });
  html += '</tbody></table>';
  container.innerHTML = html;
}

function exportProgress() {
  const data = JSON.stringify({
    exportedAt: new Date().toISOString(),
    version: 1,
    state: state,
  }, null, 2);
  const blob = new Blob([data], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "study-planner-progress-" + todayKey() + ".json";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

function importProgress(file) {
  const status = document.getElementById("import-status");
  const reader = new FileReader();
  reader.onload = e => {
    try {
      const payload = JSON.parse(e.target.result);
      if (!payload || !payload.state) throw new Error("File does not contain valid progress data.");
      Object.assign(state, payload.state);
      state.tasks = state.tasks || {};
      state.books = state.books || {};
      state.notes = state.notes || "";
      state.stats = state.stats || { tabOpens: {}, sectionOpens: {}, lastVisit: {} };
      save();
      status.style.color = "var(--sage)";
      status.textContent = "✓ Imported successfully. Refreshing…";
      setTimeout(() => location.reload(), 800);
    } catch (err) {
      status.style.color = "var(--accent)";
      status.textContent = "✗ Import failed: " + err.message;
    }
  };
  reader.readAsText(file);
}

function resetProgress() {
  if (!confirm("This will delete ALL your progress (checkboxes, books, notes, stats). This cannot be undone unless you previously exported a backup. Continue?")) return;
  localStorage.removeItem(STORAGE_KEY);
  location.reload();
}

function attachHandlers() {
  // Tab switching
  document.querySelectorAll(".tab").forEach(tab => {
    tab.addEventListener("click", () => {
      document.querySelectorAll(".tab").forEach(t => t.classList.remove("active"));
      document.querySelectorAll(".tab-panel").forEach(p => p.classList.remove("active"));
      tab.classList.add("active");
      const target = document.getElementById(tab.dataset.target);
      if (target) target.classList.add("active");
      // Track tab open for stats
      const slug = (tab.dataset.target || "").replace(/^panel-/, "");
      if (slug) trackTabOpen(slug);
      // Refresh stats / glossary if relevant
      if (slug === "notebook") renderStats();
      if (slug === "glossary") renderGlossary();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  });

  // Task checkboxes
  document.querySelectorAll('.task input[type="checkbox"]').forEach(cb => {
    cb.addEventListener("change", () => {
      flushPendingNotes();
      state.tasks[cb.dataset.id] = cb.checked;
      save();
      renderPanels();
      attachHandlers();
      updateProgress();
    });
  });

  // Book toggles
  document.querySelectorAll('input[data-book]').forEach(cb => {
    cb.addEventListener("change", () => {
      flushPendingNotes();
      state.books[cb.dataset.book] = cb.checked;
      save();
      renderPanels();
      attachHandlers();
    });
  });

  // Material filters
  document.querySelectorAll('.materials-filter').forEach(btn => {
    btn.addEventListener("click", () => {
      flushPendingNotes();
      materialFilter = btn.dataset.filter;
      renderPanels();
      attachHandlers();
    });
  });

  // Notebook
  const notesEl = document.getElementById("notes-text");
  const wcEl = document.getElementById("word-count");
  if (notesEl) {
    notesEl.value = state.notes;
    const wordCount = t => t.trim() ? t.trim().split(/\s+/).length : 0;
    if (wcEl) wcEl.textContent = wordCount(notesEl.value) + " words";
    let saveTimer;
    notesEl.addEventListener("input", () => {
      state.notes = notesEl.value;
      if (wcEl) wcEl.textContent = wordCount(notesEl.value) + " words";
      clearTimeout(saveTimer);
      saveTimer = setTimeout(save, 350);
    });
  }

  // Export / Import / Reset
  const exportBtn = document.getElementById("btn-export");
  if (exportBtn) exportBtn.addEventListener("click", exportProgress);
  const importInput = document.getElementById("btn-import");
  if (importInput) importInput.addEventListener("change", e => {
    if (e.target.files && e.target.files[0]) importProgress(e.target.files[0]);
  });
  const resetBtn = document.getElementById("btn-reset");
  if (resetBtn) resetBtn.addEventListener("click", resetProgress);

  // Glossary search
  const glossarySearch = document.getElementById("glossary-search");
  if (glossarySearch) glossarySearch.addEventListener("input", renderGlossary);

  // Quiz option clicks
  document.querySelectorAll('.quiz-option').forEach(btn => {
    btn.addEventListener("click", () => {
      const area = btn.dataset.area;
      const qIdx = parseInt(btn.dataset.q, 10);
      const optIdx = parseInt(btn.dataset.opt, 10);
      const item = document.getElementById("quiz-" + area + "-" + qIdx);
      const correct = parseInt(item.dataset.correct, 10);
      const isCorrect = optIdx === correct;
      // Record state
      state.quiz[area] = state.quiz[area] || {};
      state.quiz[area][qIdx] = { picked: optIdx, correct: isCorrect };
      save();
      // Visual feedback
      item.querySelectorAll('.quiz-option').forEach((b, bi) => {
        b.disabled = true;
        b.classList.remove("picked", "correct-answer", "wrong-pick");
        if (bi === correct) b.classList.add("correct-answer");
        if (bi === optIdx && !isCorrect) b.classList.add("wrong-pick");
        if (bi === optIdx) b.classList.add("picked");
      });
      const fb = item.querySelector('.quiz-feedback');
      const verdict = item.querySelector('.quiz-verdict');
      verdict.textContent = isCorrect ? "✓ Correct" : "✗ Not quite — see below.";
      verdict.style.color = isCorrect ? "var(--sage)" : "var(--accent)";
      fb.style.display = "block";
      // Update score widget for this area
      updateQuizScore(area);
    });
  });
  // Initial: restore answered state visually + score
  AREAS.forEach(a => {
    if (!a.quiz || !a.quiz.length) return;
    if (state.quiz[a.slug]) {
      Object.keys(state.quiz[a.slug]).forEach(qIdxStr => {
        const qIdx = parseInt(qIdxStr, 10);
        const rec = state.quiz[a.slug][qIdx];
        const item = document.getElementById("quiz-" + a.slug + "-" + qIdx);
        if (!item) return;
        const correct = parseInt(item.dataset.correct, 10);
        item.querySelectorAll('.quiz-option').forEach((b, bi) => {
          b.disabled = true;
          if (bi === correct) b.classList.add("correct-answer");
          if (bi === rec.picked && !rec.correct) b.classList.add("wrong-pick");
          if (bi === rec.picked) b.classList.add("picked");
        });
        const fb = item.querySelector('.quiz-feedback');
        const verdict = item.querySelector('.quiz-verdict');
        if (fb && verdict) {
          verdict.textContent = rec.correct ? "✓ Correct" : "✗ Not quite — see below.";
          verdict.style.color = rec.correct ? "var(--sage)" : "var(--accent)";
          fb.style.display = "block";
        }
      });
    }
    updateQuizScore(a.slug);
  });

  // First-load population for glossary/stats so a direct hash link works
  renderGlossary();
  renderStats();
}

function updateProgress() {
  let total = 0, done = 0;
  AREAS.forEach(a => {
    a.weeks.forEach((w, wi) => {
      total += w.tasks.length;
      done += w.tasks.filter((_, ti) => state.tasks[taskId(a, wi, ti)]).length;
    });
  });
  const pct = total ? Math.round((done / total) * 100) : 0;
  document.getElementById("pct").textContent = pct;
  document.getElementById("bar").style.width = pct + "%";
  document.getElementById("done-count").textContent = done;
  document.getElementById("total-count").textContent = total;
}

// Open every <details> ancestor of an element so the element is visible.
function openAncestors(el) {
  let p = el && el.parentElement;
  while (p) {
    if (p.tagName && p.tagName.toLowerCase() === 'details') p.open = true;
    p = p.parentElement;
  }
}

// Navigate to a hash anchor — switch to the right tab if needed, expand
// ancestor details, scroll smoothly to the element.
function navigateToAnchor(anchor) {
  if (!anchor) return false;
  // Try direct tab slug first (e.g. "ind-as")
  const directTab = document.querySelector('[data-target="panel-' + anchor + '"]');
  if (directTab) { directTab.click(); return true; }
  // Otherwise, treat as deep anchor — find matching area slug as prefix
  const knownSlugs = AREAS.map(a => a.slug).concat(['notebook', 'glossary']);
  // Sort longer slugs first to handle overlaps (none currently, but safe)
  knownSlugs.sort((a, b) => b.length - a.length);
  const matchedSlug = knownSlugs.find(s => anchor === s || anchor.startsWith(s + '-'));
  if (!matchedSlug) return false;
  const tab = document.querySelector('[data-target="panel-' + matchedSlug + '"]');
  if (tab) tab.click();
  setTimeout(() => {
    const el = document.getElementById(anchor);
    if (el) {
      // Open the element itself if it is a <details>
      if (el.tagName && el.tagName.toLowerCase() === 'details') el.open = true;
      openAncestors(el);
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }, 80);
  return true;
}

function restoreFromHash() {
  if (!location.hash) return;
  navigateToAnchor(location.hash.substring(1));
}

// Global click handler for in-page anchor links (TOC + "↑ Back to contents")
document.addEventListener('click', e => {
  const a = e.target.closest('a[href^="#"]');
  if (!a) return;
  const hash = a.getAttribute('href').substring(1);
  if (!hash) return;
  if (navigateToAnchor(hash)) {
    e.preventDefault();
    history.replaceState(null, '', '#' + hash);
  }
});

// Boot
renderTabs();
renderPanels();
attachHandlers();
updateProgress();
// Track the initial tab open (Restructuring, unless hash navigation overrides below)
if (AREAS && AREAS.length) trackTabOpen(AREAS[0].slug);
restoreFromHash();
</script>
</body>
</html>
"""

PLANNER_HTML = PLANNER_HTML.replace("__CSS__", CSS)
