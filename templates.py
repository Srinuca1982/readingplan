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

const STORAGE_KEY = "structuring_planner_v1";
const state = JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
state.tasks = state.tasks || {};
state.books = state.books || {};
state.notes = state.notes || "";

function save() { localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); }

function escapeHTML(s) {
  return String(s == null ? "" : s).replace(/[&<>"']/g, c => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[c]));
}

let materialFilter = "all";

function taskId(area, wi, ti) {
  return area.task_prefix + wi + "_t" + ti;
}

function sectionShell(title, count, body, open) {
  const openAttr = open ? " open" : "";
  const countHTML = count != null ? '<span class="section-count">' + escapeHTML(count) + '</span>' : "";
  return '<details class="content-section"' + openAttr + '>' +
    '<summary>' +
      '<span class="section-title">' +
        '<span class="section-title-text">' + escapeHTML(title) + '</span>' +
        countHTML +
      '</span>' +
      '<span class="section-chevron"></span>' +
    '</summary>' +
    '<div class="section-body">' + body + '</div>' +
  '</details>';
}

// ----- per-subject section renderers -----

function renderWeeksSection(area) {
  const rows = area.weeks.map((w, wi) => {
    const tasks = w.tasks.map((t, ti) => {
      const id = taskId(area, wi, ti);
      const done = !!state.tasks[id];
      return '<li class="task ' + (done ? 'done' : '') + '">' +
        '<input type="checkbox" data-id="' + escapeHTML(id) + '" ' + (done ? 'checked' : '') + '>' +
        '<span>' + escapeHTML(t) + '</span></li>';
    }).join("");
    const allDone = w.tasks.length > 0 && w.tasks.every((_, ti) => state.tasks[taskId(area, wi, ti)]);
    return '<article class="week-card ' + (allDone ? 'complete' : '') + '">' +
      '<div class="week-head">' +
        '<span class="week-tag">Week ' + escapeHTML(w.week) + '</span>' +
        '<span class="week-title">' + escapeHTML(w.title) + '</span>' +
      '</div>' +
      '<p class="week-focus">' + escapeHTML(w.focus) + '</p>' +
      '<ul class="tasks">' + tasks + '</ul></article>';
  }).join("");
  const count = area.weeks.length + " weeks";
  return sectionShell("Roadmap", count, '<div class="weeks-grid">' + rows + '</div>', true);
}

function renderConceptsSection(area) {
  if (!area.concepts || !area.concepts.length) return "";
  const html = area.concepts.map(c => {
    const example = c.example ? '<h4>Example</h4><div class="example">' + c.example + '</div>' : '';
    const hooks = c.hooks ? '<h4>Statutory hooks</h4><p>' + c.hooks + '</p>' : '';
    const pitfalls = c.pitfalls ? '<h4>Common pitfalls</h4><p>' + c.pitfalls + '</p>' : '';
    return '<details class="concept">' +
      '<summary>' +
        '<span class="concept-tag">' + escapeHTML(c.tag) + '</span>' +
        '<div class="concept-title">' + escapeHTML(c.title) + '</div>' +
        '<div class="concept-summary">' + escapeHTML(c.summary) + '</div>' +
      '</summary>' +
      '<div class="concept-body">' +
        '<h4>The idea</h4><p>' + c.body + '</p>' +
        example + hooks + pitfalls +
      '</div></details>';
  }).join("");
  return sectionShell("Concepts & Examples", area.concepts.length, html, false);
}

function renderTopicsSection(area) {
  if (!area.topics || !area.topics.length) return "";
  const items = area.topics.map(t => '<li>' + escapeHTML(t) + '</li>').join("");
  return sectionShell("Key Topics", area.topics.length, '<ul class="topics-list">' + items + '</ul>', false);
}

function renderDeepDiveSection(area) {
  if (!area.note_body) return "";
  const body = '<div class="deep-dive-body article-body">' + area.note_body + '</div>';
  return sectionShell("Deep-Dive Study Note", null, body, false);
}

function renderMaterialsSection(area) {
  if (!area.materials || !area.materials.length) return "";
  const filters = ['<button class="materials-filter ' + (materialFilter === "all" ? "active" : "") + '" data-filter="all">All</button>',
                   '<button class="materials-filter ' + (materialFilter === "Study Note" ? "active" : "") + '" data-filter="Study Note">Study Notes</button>',
                   '<button class="materials-filter ' + (materialFilter === "Cheat Sheet" ? "active" : "") + '" data-filter="Cheat Sheet">Cheat Sheets</button>',
                   '<button class="materials-filter ' + (materialFilter === "Case Digest" ? "active" : "") + '" data-filter="Case Digest">Case Law</button>'].join("");

  const groups = { "Study Note": [], "Cheat Sheet": [], "Case Digest": [] };
  area.materials.forEach(m => { if (groups[m.kind]) groups[m.kind].push(m); });
  const order = ["Study Note", "Cheat Sheet", "Case Digest"];
  const labels = { "Study Note": "Study Notes", "Cheat Sheet": "Cheat Sheets", "Case Digest": "Case Digests" };

  const groupsHTML = order.filter(k => groups[k].length && (materialFilter === "all" || materialFilter === k)).map(k => {
    const items = groups[k].map(m =>
      '<details class="material-item" id="mat-' + escapeHTML(m.slug) + '">' +
        '<summary>' +
          '<div class="material-item-title">' + escapeHTML(m.title) + '</div>' +
          '<div class="material-item-summary">' + escapeHTML(m.summary) + '</div>' +
        '</summary>' +
        '<div class="material-item-body article-body">' + m.body + '</div>' +
      '</details>'
    ).join("");
    return '<div class="material-group"><div class="material-group-head">' + escapeHTML(labels[k]) + '</div>' + items + '</div>';
  }).join("");

  const body = '<div class="materials-controls">' + filters + '</div>' +
               '<div id="materials-' + escapeHTML(area.slug) + '">' + groupsHTML + '</div>';
  return sectionShell("Notes, Cheat Sheets & Case Law", area.materials.length, body, false);
}

function renderBooksSection(area) {
  if (!area.books || !area.books.length) return "";
  const cards = area.books.map((b, i) => {
    const id = "book_" + area.slug + "_" + i;
    const owned = !!state.books[id];
    const priority = b.priority || "";
    const publisher = b.publisher || "";
    return '<article class="book-card">' +
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
  return sectionShell("Books", area.books.length, '<div class="books-grid">' + cards + '</div>', false);
}

function renderSourcesSection(area) {
  if (!area.sources || !area.sources.length) return "";
  const cards = area.sources.map(s =>
    '<a class="source-card" href="' + escapeHTML(s.url) + '" target="_blank" rel="noopener">' +
      (s.type ? '<div class="source-type">' + escapeHTML(s.type) + '</div>' : "") +
      '<div class="source-title">' + escapeHTML(s.name) + ' →</div>' +
      '<div class="source-desc">' + escapeHTML(s.description) + '</div>' +
      '<div class="source-url">' + escapeHTML(s.url) + '</div>' +
    '</a>'
  ).join("");
  return sectionShell("Online Sources", area.sources.length, '<div class="sources-list">' + cards + '</div>', false);
}

function renderMatrixSection(area) {
  if (!area.matrix) return "";
  const m = area.matrix;
  const headers = ["Mode"].concat(m.columns);
  const head = '<thead><tr>' + headers.map(h => '<th>' + escapeHTML(h) + '</th>').join("") + '</tr></thead>';
  const body = '<tbody>' + m.rows.map(r =>
    '<tr>' + r.map(c => '<td>' + escapeHTML(c) + '</td>').join("") + '</tr>'
  ).join("") + '</tbody>';
  return sectionShell("Cross-Statute Matrix", m.rows.length + " modes", '<div class="matrix-wrap"><table>' + head + body + '</table></div>', false);
}

// ----- top-level renderers -----

function renderTabs() {
  const tabs = document.getElementById("tabs");
  let html = AREAS.map((a, i) =>
    '<button class="tab ' + (i === 0 ? "active" : "") + '" data-target="panel-' + escapeHTML(a.slug) + '">' +
      escapeHTML(a.title) +
    '</button>'
  ).join("");
  html += '<button class="tab" data-target="panel-notebook">Notebook</button>';
  tabs.innerHTML = html;
}

function renderPanels() {
  const panels = document.getElementById("panels");
  let html = AREAS.map((a, i) => {
    return '<section class="tab-panel ' + (i === 0 ? "active" : "") + '" id="panel-' + escapeHTML(a.slug) + '">' +
      '<div class="area-intro">' +
        '<h2>' + escapeHTML(a.title) + '</h2>' +
        '<p class="subtitle-line">' + escapeHTML(a.subtitle) + '</p>' +
        (a.summary ? '<p class="area-summary">' + escapeHTML(a.summary) + '</p>' : "") +
      '</div>' +
      renderWeeksSection(a) +
      renderConceptsSection(a) +
      renderTopicsSection(a) +
      renderDeepDiveSection(a) +
      renderMaterialsSection(a) +
      renderBooksSection(a) +
      renderSourcesSection(a) +
      renderMatrixSection(a) +
    '</section>';
  }).join("");

  // Notebook panel
  html += '<section class="tab-panel" id="panel-notebook">' +
    '<div class="area-intro">' +
      '<h2>Notebook</h2>' +
      '<p class="subtitle-line">A scratchpad for case-law digests, section numbers and questions. Saves automatically in this browser.</p>' +
    '</div>' +
    '<div class="notes-pad">' +
      '<textarea id="notes-text" placeholder="Begin writing — your notes are saved locally in this browser…"></textarea>' +
      '<div class="notes-meta">' +
        '<span>Auto-saved locally</span>' +
        '<span id="word-count">0 words</span>' +
      '</div>' +
    '</div>' +
  '</section>';

  panels.innerHTML = html;
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
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  });

  // Task checkboxes
  document.querySelectorAll('.task input[type="checkbox"]').forEach(cb => {
    cb.addEventListener("change", () => {
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
      state.books[cb.dataset.book] = cb.checked;
      save();
      renderPanels();
      attachHandlers();
    });
  });

  // Material filters
  document.querySelectorAll('.materials-filter').forEach(btn => {
    btn.addEventListener("click", () => {
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

// Restore active tab from hash, if any
function restoreFromHash() {
  if (location.hash) {
    const slug = location.hash.replace("#", "");
    const tab = document.querySelector('[data-target="panel-' + slug + '"]');
    if (tab) tab.click();
  }
}

// Boot
renderTabs();
renderPanels();
attachHandlers();
updateProgress();
restoreFromHash();
</script>
</body>
</html>
"""

PLANNER_HTML = PLANNER_HTML.replace("__CSS__", CSS)
