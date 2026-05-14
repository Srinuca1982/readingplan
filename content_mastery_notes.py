"""Detailed study notes for each mastery area.

Each note is a substantial HTML body written into materials/mastery-<slug>.html
when planner.py runs.
"""

MASTERY_NOTES = [
    # ------------------------------------------------------------------
    # 1) Ind AS
    # ------------------------------------------------------------------
    {
        "slug": "ind-as",
        "title": "Ind AS — Comprehensive Study Note",
        "summary": "The standard-by-standard tour. What each Ind AS does and the recognition-measurement core of each.",
        "body": """
<h2>The framework — start here</h2>
<p>The <strong>Conceptual Framework for Financial Reporting under Ind AS</strong> is the foundation
for every standard. Master four building blocks:</p>
<ul>
  <li><strong>Objective</strong> — to provide financial information useful to existing and potential investors, lenders and creditors in making decisions.</li>
  <li><strong>Qualitative characteristics</strong> — relevance, faithful representation (fundamental); comparability, verifiability, timeliness, understandability (enhancing).</li>
  <li><strong>Elements</strong> — asset, liability, equity, income, expense.</li>
  <li><strong>Recognition and measurement bases</strong> — historical cost, current cost, realisable value, present value, fair value.</li>
</ul>

<h2>Standards on presentation</h2>

<h3>Ind AS 1 — Presentation of Financial Statements</h3>
<p>Mandates the complete set: balance sheet, P&L (with comprehensive income), statement of changes
in equity, cash flow statement, notes. Schedule III Division II prescribes the exact format. Key
concepts: <strong>going concern</strong> assumption, <strong>accrual</strong> basis, materiality,
consistency, comparative information.</p>

<h3>Ind AS 8 — Accounting Policies, Changes in Accounting Estimates and Errors</h3>
<ul>
  <li>Change in <strong>accounting policy</strong> → retrospective application (restate comparatives).</li>
  <li>Change in <strong>accounting estimate</strong> → prospective application.</li>
  <li><strong>Prior period errors</strong> → retrospective restatement; note disclosure of the nature and amount.</li>
</ul>

<h3>Ind AS 10 — Events After the Reporting Period</h3>
<ul>
  <li><strong>Adjusting events</strong> — provide evidence of conditions existing at reporting date → adjust the financial statements.</li>
  <li><strong>Non-adjusting events</strong> — conditions arose after the reporting date → disclose only.</li>
  <li>Dividends declared after reporting date — disclose, do not recognise as a liability.</li>
</ul>

<h3>Ind AS 7 — Statement of Cash Flows</h3>
<p>Three categories: operating, investing, financing. Direct or indirect method (indirect is the
Indian convention). <strong>Bank overdrafts</strong> repayable on demand → cash equivalents.
Disclose <strong>changes in liabilities from financing activities</strong>.</p>

<h2>Long-term assets</h2>

<h3>Ind AS 16 — Property, Plant and Equipment</h3>
<ul>
  <li>Recognition: future economic benefits probable AND cost can be measured reliably.</li>
  <li><strong>Component accounting</strong> — significant components with different useful lives are depreciated separately.</li>
  <li>Subsequent measurement — cost model OR revaluation model (entire class).</li>
  <li>Depreciation method — reflects pattern of consumption; reviewed annually; <strong>major spares</strong> with useful life > 12 months → capitalised.</li>
</ul>

<h3>Ind AS 38 — Intangible Assets</h3>
<ul>
  <li>Recognition: identifiable, controlled, future economic benefits probable.</li>
  <li><strong>Research</strong> phase → expensed; <strong>development</strong> phase → capitalised if 6 conditions met (technical feasibility, intention, ability to use/sell, future benefits, resources, reliable cost measurement).</li>
  <li>Finite-life intangible → amortised; indefinite-life intangible → not amortised, tested annually for impairment.</li>
</ul>

<h3>Ind AS 40 — Investment Property</h3>
<p>Property held for rental or capital appreciation (not for use in operations or sale in ordinary
course). Cost model is the only choice for measurement, but <strong>fair value disclosure is
mandatory</strong> even under the cost model.</p>

<h3>Ind AS 36 — Impairment of Assets</h3>
<ul>
  <li>Test when indicators exist; annually for indefinite-life intangibles and goodwill.</li>
  <li><strong>Recoverable amount</strong> = higher of fair value less costs of disposal AND value in use.</li>
  <li>Cash-Generating Unit (CGU) — smallest identifiable group of assets generating largely independent cash flows.</li>
  <li>Impairment loss = carrying amount − recoverable amount.</li>
  <li>Reversal allowed for all assets except goodwill.</li>
</ul>

<h3>Ind AS 23 — Borrowing Costs</h3>
<p>Costs directly attributable to construction/production of a <strong>qualifying asset</strong>
(takes substantial time to be ready for use/sale) → capitalise. Otherwise, expense. Capitalisation
rate = weighted average of borrowing costs.</p>

<h2>Revenue — Ind AS 115 (the 5-step model)</h2>
<ol>
  <li><strong>Identify the contract</strong> — parties, rights, payment terms, commercial substance, collectibility probable.</li>
  <li><strong>Identify performance obligations</strong> — each distinct good/service is a separate obligation. Distinct = capable of being distinct AND distinct in the context of the contract.</li>
  <li><strong>Determine transaction price</strong> — fixed + variable. Variable consideration (discounts, rebates, refunds) → most-likely-amount or expected-value method, constrained for reversal risk.</li>
  <li><strong>Allocate transaction price</strong> — to performance obligations based on relative stand-alone selling prices.</li>
  <li><strong>Recognise revenue</strong> — when (or as) the entity satisfies a performance obligation by transferring control. Control = ability to direct use and obtain substantially all the remaining benefits.</li>
</ol>

<div class="callout">
<strong>Over time vs point in time.</strong> Recognise revenue over time if one of three criteria met
(simultaneous receipt and consumption; entity's performance creates/enhances an asset the customer
controls; entity's performance does not create an asset with alternative use AND entity has
enforceable right to payment for performance to date). Otherwise, point in time.
</div>

<h2>Leases — Ind AS 116</h2>
<p>The big shift: lessees recognise <strong>almost all leases on balance sheet</strong> (right-of-use
asset and lease liability) — eliminating the old operating vs finance lease distinction for lessees.</p>

<h3>Lessee accounting</h3>
<ul>
  <li>At commencement: ROU asset = lease liability + initial direct costs + prepayments − incentives. Lease liability = PV of lease payments.</li>
  <li>Subsequent: ROU depreciated (typically straight-line over lease term); lease liability unwinds with interest expense.</li>
  <li>Exemptions: short-term (≤ 12 months) and low-value (≤ approx. ₹3.5 lakh) leases → P&L expense.</li>
</ul>

<h3>Lessor accounting</h3>
<p>Largely unchanged from old AS 19. Finance lease vs operating lease classification based on whether
substantially all risks and rewards transfer.</p>

<h2>Financial instruments — Ind AS 109, 32, 107</h2>

<h3>Classification under Ind AS 109</h3>
<ul>
  <li><strong>Amortised cost</strong> — financial asset held to collect contractual cash flows that are SPPI (solely payments of principal and interest).</li>
  <li><strong>FVTOCI (Fair Value through Other Comprehensive Income)</strong> — held to collect AND sell; SPPI cash flows.</li>
  <li><strong>FVTPL (Fair Value through Profit and Loss)</strong> — all other cases; default for trading and derivatives.</li>
</ul>

<h3>Expected Credit Loss (ECL) — Ind AS 109</h3>
<ul>
  <li><strong>Stage 1</strong> — no significant increase in credit risk since initial recognition → 12-month ECL.</li>
  <li><strong>Stage 2</strong> — significant increase in credit risk → lifetime ECL.</li>
  <li><strong>Stage 3</strong> — credit-impaired → lifetime ECL on net carrying amount.</li>
  <li><strong>Simplified approach</strong> for trade receivables, contract assets, lease receivables → always lifetime ECL.</li>
</ul>

<h3>Liability vs Equity — Ind AS 32</h3>
<p>An instrument is a financial liability if there is a contractual obligation to deliver cash or
another financial asset. Otherwise, it's equity. <strong>Compound instruments</strong> (e.g.,
convertible debentures) — split into liability and equity components at initial recognition.</p>

<h2>Consolidation framework</h2>

<h3>Ind AS 110 — Consolidated Financial Statements</h3>
<p><strong>Control</strong> = power over the investee + exposure to variable returns + ability to
use power to affect those returns. All three elements required.</p>

<h3>Ind AS 28 — Investments in Associates and Joint Ventures</h3>
<p>Significant influence — presumption at 20–50% holding. Use <strong>equity method</strong>:
investment initially recorded at cost, adjusted for post-acquisition share of profits/losses.</p>

<h3>Ind AS 103 — Business Combinations</h3>
<ul>
  <li>Acquisition method only — no pooling-of-interests (except common-control via Appendix C).</li>
  <li>Identify the acquirer; determine acquisition date; recognise identifiable assets acquired and liabilities assumed at fair value; recognise NCI at fair value or proportionate share of net assets; recognise <strong>goodwill</strong> (excess of consideration over identified net assets) or bargain purchase gain.</li>
  <li>Common-control transactions — outside Ind AS 103 scope; carrying-value method per Appendix C.</li>
</ul>

<h2>Other high-impact standards</h2>

<h3>Ind AS 12 — Income Taxes</h3>
<p><strong>Deferred tax</strong> on temporary differences (carrying amount − tax base). Recognised
in same place as the underlying item (P&L, OCI, or directly in equity). <strong>DTA recognition
limited</strong> to extent it's probable that future taxable profit will be available.</p>

<h3>Ind AS 19 — Employee Benefits</h3>
<p>Defined contribution plans — straightforward (recognise as expense as service rendered). Defined
benefit plans (e.g., gratuity) — actuarial valuation; <strong>service cost</strong> in P&L,
<strong>interest cost</strong> in P&L, <strong>remeasurements (actuarial gains/losses)</strong> in
OCI without reclassification.</p>

<h3>Ind AS 37 — Provisions, Contingent Liabilities, Contingent Assets</h3>
<ul>
  <li>Provision: present obligation + probable outflow + reliable estimate.</li>
  <li>Contingent liability: possible obligation OR present obligation but not probable / not reliably estimable. Disclose only.</li>
  <li>Contingent asset: disclose only when probable; recognise only when virtually certain.</li>
</ul>

<h3>Ind AS 21 — Foreign Currency</h3>
<p>Functional currency = primary economic environment. Monetary items retranslated at closing rate;
exchange differences in P&L. Non-monetary items at historical rate. <strong>Translation of foreign
operations</strong> — assets/liabilities at closing rate, income/expenses at average rate, exchange
differences in OCI.</p>

<h2>How to study Ind AS</h2>
<ol>
  <li><strong>Week 1</strong>: framework + presentation standards (Ind AS 1, 8, 10, 7).</li>
  <li><strong>Week 2–3</strong>: tangible/intangible (16, 38, 40, 36, 23).</li>
  <li><strong>Week 4</strong>: revenue (115) — solve at least 20 case-style questions.</li>
  <li><strong>Week 5</strong>: leases (116) — work through lessee transition examples.</li>
  <li><strong>Week 6</strong>: financial instruments (109, 32, 107) — ECL modelling.</li>
  <li><strong>Week 7</strong>: consolidation (103, 110, 28, 111, 112).</li>
  <li><strong>Week 8</strong>: tax, employee benefits, provisions; segment and disclosure standards.</li>
</ol>

<div class="callout">
<strong>Active learning tip.</strong> Pick any listed company's annual report. For each standard
in this note, find the note disclosure in the financial statements. Reconcile what the company
disclosed to the standard's requirements. This single exercise — done for one company across all
standards — beats reading the bare text.
</div>
""",
    },

    # ------------------------------------------------------------------
    # 2) Income Tax Act 2025
    # ------------------------------------------------------------------
    {
        "slug": "it-act-2025",
        "title": "Income-tax Act 2025 — Study Note",
        "summary": "The new Act's structure, key changes from the 1961 Act, and the mapping you need.",
        "body": """
<h2>The new regime — in force</h2>
<p>The Income-tax Act 2025 came into force on <strong>1 April 2026</strong>, replacing the
Income-tax Act 1961. The 1961 Act now applies only to transactions and assessments that arose on
or before 31 March 2026. For everything from AY 2026–27 onwards, the 2025 Act is the operative law.</p>

<p>After 60+ years of amendments, the 1961 Act had become unwieldy — duplications, inconsistent
numbering, sections inserted out of sequence. The 2025 Act reorganises and modernises the same
substantive law into a smaller, more logical code. The objective was clarity, not substantive
policy change — though some procedural simplifications and codifications (such as faceless
assessment) have been built in.</p>

<div class="callout">
<strong>Reading orientation.</strong> Treat the 2025 Act as a rewriting and renumbering exercise.
Most of your 1961-Act knowledge transfers directly. The work is in the mapping — which 1961
section corresponds to which 2025 section. Always verify the current published text at
<a href="https://www.incometaxindia.gov.in/income-tax-act-2025" target="_blank">incometaxindia.gov.in/income-tax-act-2025</a>.
</div>

<h2>Structural changes — what's new at a high level</h2>
<ul>
  <li>Fewer chapters and sections — the 1961 Act's 800+ sections reduced; sub-section nesting simplified.</li>
  <li>Plain-language drafting — fewer "notwithstandings", clearer cross-references.</li>
  <li>Consolidated rules — what was scattered across the 1962 Income-tax Rules and CBDT circulars is being consolidated.</li>
  <li>Faceless administration codified — what began as procedural reform now sits in the statute.</li>
  <li>Definitions chapter expanded — many terms previously defined in case law or circulars now have statutory definitions.</li>
</ul>

<h2>Basic concepts (Chapter II equivalent)</h2>

<h3>Person and assessee</h3>
<p>Definitions of person (7 categories — individual, HUF, company, firm, AOP/BOI, local authority,
artificial juridical person) and assessee remain. The 2025 Act expands "person" to include
explicitly digital-economy concepts (significant economic presence).</p>

<h3>Previous year and assessment year</h3>
<p>Unchanged — financial year basis. The "previous year" of an income is the financial year
immediately preceding the assessment year.</p>

<h2>Residential status</h2>
<p>For <strong>individuals</strong>:</p>
<ul>
  <li><strong>Resident</strong> if either (a) physically in India for ≥ 182 days during the previous year, OR (b) physically in India for ≥ 60 days during the previous year AND ≥ 365 days during the preceding 4 years (with carve-outs for Indian citizens leaving for employment, and Persons of Indian Origin visiting).</li>
  <li><strong>Resident and Ordinarily Resident (R&OR)</strong> if resident AND has been resident in India for at least 2 out of the preceding 10 years AND was in India for at least 730 days in the preceding 7 years.</li>
  <li><strong>Deemed residency for HNI Indian citizens</strong> (introduced FY 2020-21, continued under 2025 Act) — Indian citizen with total income exceeding ₹15 lakh (excluding foreign source income), and not liable to tax in any other country by reason of domicile/residence, is deemed resident.</li>
</ul>
<p>For <strong>companies</strong>: Indian company is always resident. Foreign company is resident if
its <strong>place of effective management (POEM)</strong> is in India during the year.</p>

<h2>Scope of total income — what gets taxed</h2>
<ul>
  <li><strong>R&OR</strong>: world income (Indian source + foreign source).</li>
  <li><strong>Resident but Not Ordinarily Resident (RNOR)</strong>: Indian source income + foreign income that arises from business controlled from India or profession set up in India.</li>
  <li><strong>Non-resident (NR)</strong>: only Indian source income.</li>
</ul>
<p><strong>Indian source / deemed accrual</strong> — Sec 9 equivalent: income from business connection in India, income through property in India, income from transfer of capital asset in India,
income from indirect transfer of shares deriving substantial value from Indian assets, salary for
services rendered in India, dividend from Indian company, interest payable by Indian government
or resident, royalty/fees-for-technical-services payable by Indian government or resident.</p>

<h2>The five heads of income</h2>

<h3>Salaries</h3>
<ul>
  <li>Basic + DA + allowances + perquisites + profits in lieu.</li>
  <li>Perquisite valuation (Rule 3 equivalent) — rent-free accommodation, car, ESOP, etc.</li>
  <li>Standard deduction — ₹75,000 under new regime; ₹50,000 under old regime (verify current).</li>
  <li>Section 17(2)(vi) equivalent — ESOP taxation; cost = FMV on date of allotment; subsequent gain taxed as capital gain.</li>
</ul>

<h3>House Property</h3>
<ul>
  <li>Annual value = higher of fair rent OR municipal value, but not exceeding standard rent. For let-out: actual rent received if higher.</li>
  <li>Less: municipal taxes paid by owner. = Net Annual Value.</li>
  <li>Less: standard deduction 30% of NAV. Less: interest on borrowed capital (capped at ₹2 lakh for self-occupied).</li>
  <li>Loss from house property capped at ₹2 lakh per year for set-off against other heads.</li>
</ul>

<h3>Profits and Gains of Business or Profession</h3>
<ul>
  <li>Net profit per books, adjusted for tax-inadmissible items and tax-only deductions.</li>
  <li>Depreciation — block of assets concept; rates per Schedule.</li>
  <li>Specific deductions — repairs, taxes, insurance, employee contributions, R&D weighted deductions, etc.</li>
  <li>Specific disallowances — Sec 43B equivalent (actual-payment basis for statutory dues, MSME dues post-Apr 2023), Sec 40(a)(ia) equivalent (TDS default), Sec 14A equivalent (expenses for exempt income).</li>
</ul>

<h3>Capital Gains</h3>
<ul>
  <li><strong>Capital asset</strong>: property of any kind, with specified exclusions (stock-in-trade, personal effects, rural agricultural land, gold deposit bonds).</li>
  <li><strong>Short-term</strong> if held ≤ 24 months for immovable property, ≤ 12 months for listed securities; long-term otherwise.</li>
  <li><strong>Rates post-Budget 2024</strong>: LTCG on listed equity 12.5% (no indexation; ₹1.25 lakh exemption); STCG on listed equity 20%; LTCG on other long-term assets 12.5% (with limited indexation grandfathering).</li>
  <li>Reinvestment exemptions — Sec 54 (residential property), 54F (residential property from sale of other LTCA), 54EC (specified bonds up to ₹50 lakh).</li>
  <li><strong>Indirect transfer</strong> — Sec 9(1)(i) equivalent: transfer of foreign-co shares deriving substantial value (≥ 50%) from Indian assets, where Indian-asset value > ₹10 cr, is taxable in India.</li>
</ul>

<h3>Income from Other Sources</h3>
<ul>
  <li>Dividends — fully taxable in shareholder's hands post-Apr 2020 (DDT abolished).</li>
  <li>Interest, rental from non-let-out, royalties not assessable as business income.</li>
  <li>Sec 56(2)(x) equivalent — receipt of sum/property without/with inadequate consideration, deemed gift.</li>
  <li>Sec 115BBDA equivalent — special rates for casual income (lottery, crossword puzzles): 30%.</li>
</ul>

<h2>Deductions, set-off and computation</h2>

<h3>Old regime vs new regime</h3>
<p>The <strong>new regime is the default</strong> from FY 2023-24 (Sec 115BAC for individuals/HUFs).
Slabs are lower but most Chapter VI-A deductions are unavailable. The old regime is available by
filing Form 10-IEA (verify current procedure).</p>

<h3>Chapter VI-A deductions (only under old regime, with limited exceptions)</h3>
<ul>
  <li>80C — LIC, PPF, ELSS, principal repayment of home loan, etc. — up to ₹1.5 lakh.</li>
  <li>80D — medical insurance premium.</li>
  <li>80G — donations.</li>
  <li>80CCD(2) — employer NPS contribution — <strong>available under new regime too</strong>.</li>
  <li>80TTA, 80TTB — interest on deposits.</li>
</ul>

<h3>Set-off and carry-forward</h3>
<ul>
  <li>Intra-head set-off: subject to specific restrictions (e.g., loss from speculation only against speculation income).</li>
  <li>Inter-head set-off: generally allowed (except house property loss capped at ₹2 lakh; capital loss only against capital gains).</li>
  <li>Carry-forward: business loss 8 years; capital loss 8 years; speculation loss 4 years; house property loss 8 years; unabsorbed depreciation indefinite.</li>
  <li><strong>Sec 79 equivalent</strong> — closely-held company shareholding-change ≥ 51% kills loss carry-forward; exception for IBC-resolution-plan cases.</li>
</ul>

<h2>TDS, TCS and advance tax</h2>
<ul>
  <li>Key TDS sections — salary (192), contract payments (194C), professional fees (194J), rent (194I), interest (194A), dividend (194), purchase of goods (194Q), TDS on benefits in kind (194R), TDS on virtual digital assets (194S).</li>
  <li>TCS on LRS remittances (5%/20%); TCS on sale of goods (Sec 206C(1H)).</li>
  <li>Advance tax — 4 instalments (15%, 45%, 75%, 100%); interest u/s 234B (default in payment), 234C (shortfall in instalments), 234A (return delay).</li>
  <li>Quarterly TDS returns — Form 26Q (residents), 27Q (non-residents), Form 24Q (salaries).</li>
</ul>

<h2>Assessment, penalties, appeals</h2>
<ul>
  <li>Assessment types — Sec 143(1) processing; Sec 143(2) scrutiny; Sec 144 best judgment; Sec 147 reopening (faceless).</li>
  <li>Faceless assessment — codified; National Faceless Assessment Centre (NaFAC); team-based, geographically agnostic.</li>
  <li>Penalty regime — Sec 270A (under-reporting 50%, mis-reporting 200%); Sec 271AAB (search-related); Sec 271J (false certification by professional).</li>
  <li>Appeals — CIT(A) → Faceless Appeal Centre → ITAT → High Court → Supreme Court. Time limits per stage.</li>
</ul>

<h2>GAAR — General Anti-Avoidance Rule</h2>
<p>Chapter X-A equivalent. An "impermissible avoidance arrangement" — an arrangement, the main
purpose of which is to obtain a tax benefit AND which (a) creates rights or obligations not at arm's
length, OR (b) results in misuse/abuse of provisions, OR (c) lacks commercial substance, OR (d) is
conducted in a non-bona-fide manner — may be re-characterised by the AO with approval of the GAAR
Approving Panel. Threshold: tax benefit > ₹3 crore per FY (subject to revision).</p>

<h2>Special provisions</h2>
<ul>
  <li>Sec 115BAA (companies opting for 22% rate, no deductions); Sec 115BAB (new manufacturing companies, 15% rate).</li>
  <li>Sec 115BAC (individual/HUF new regime).</li>
  <li>Sec 115JB — MAT; book profit method; 15% rate; not applicable to companies opting for Sec 115BAA/BAB.</li>
  <li>Special provisions for IFSC, AIFs, REITs/InvITs, foreign portfolio investors.</li>
  <li>Taxation of virtual digital assets — Sec 115BBH (30% flat, no set-off, no deductions except cost).</li>
</ul>

<h2>Tax treaties</h2>
<ul>
  <li>Treaty override per Sec 90 — taxpayer can opt for treaty if more beneficial.</li>
  <li>MLI (Multilateral Instrument) — Principal Purpose Test (PPT), simplified LOB, treaty abuse prevention.</li>
  <li>India-Mauritius and India-Singapore — capital gains exemption phased out post-2017 protocol; transition completed.</li>
</ul>

<div class="callout">
<strong>Build your personal mapping sheet.</strong> Across the eight weeks of this study plan,
build a single Excel/Google Sheet with three columns: "1961 Section" | "2025 Section" | "Change
notes". Add a row for every section you touch in your daily work. By the end of the 8 weeks you'll
have your own bridge document — more useful than any published mapping.
</div>
""",
    },

    # ------------------------------------------------------------------
    # 3) Internal Audit
    # ------------------------------------------------------------------
    {
        "slug": "internal-audit",
        "title": "Internal Audit — Study Note",
        "summary": "The risk-based internal audit framework — IPPF, COSO, SIAs, and the operational core.",
        "body": """
<h2>The mandate</h2>
<p>Internal audit in India draws from two sources:</p>
<ul>
  <li><strong>Statutory</strong> — Section 138 of the Companies Act 2013 read with Rule 13 of the Companies (Accounts) Rules 2014 mandates internal audit for specified companies (listed, public with paid-up capital ≥ ₹50 cr or turnover ≥ ₹200 cr or borrowings ≥ ₹100 cr, etc.). Verify current thresholds before relying.</li>
  <li><strong>Professional</strong> — the Institute of Internal Auditors (IIA) International Professional Practices Framework (IPPF) globally, and ICAI's Standards on Internal Audit (SIAs) in India.</li>
</ul>

<h2>The IIA's IPPF — the four mandatory elements</h2>
<ol>
  <li><strong>Mission</strong> — to enhance and protect organisational value by providing risk-based and objective assurance, advice and insight.</li>
  <li><strong>Core Principles</strong> — 10 principles: demonstrates integrity, demonstrates competence and due professional care, is objective and free from undue influence, aligns with strategies/objectives/risks of the organisation, is appropriately positioned and adequately resourced, demonstrates quality and continuous improvement, communicates effectively, provides risk-based assurance, is insightful/proactive/future-focused, promotes organisational improvement.</li>
  <li><strong>Code of Ethics</strong> — integrity, objectivity, confidentiality, competency.</li>
  <li><strong>Standards</strong> — Attribute Standards (organisational characteristics) + Performance Standards (the work itself) + Implementation Standards (assurance vs consulting).</li>
</ol>

<h2>ICAI Standards on Internal Audit (SIAs) — the 18-standard framework</h2>
<ul>
  <li>SIA 110 — Nature of Assurance</li>
  <li>SIA 120 — Internal Controls</li>
  <li>SIA 130 — Risk Management</li>
  <li>SIA 140 — Governance</li>
  <li>SIA 210 — Managing the Internal Audit Function</li>
  <li>SIA 220 — Conducting Overall Internal Audit Planning</li>
  <li>SIA 230 — Objectives of Internal Audit</li>
  <li>SIA 240 — Using the Work of an Expert</li>
  <li>SIA 250 — Communication with Those Charged with Governance</li>
  <li>SIA 310 — Planning the Internal Audit Engagement</li>
  <li>SIA 320 — Internal Audit Evidence</li>
  <li>SIA 330 — Internal Audit Documentation</li>
  <li>SIA 350 — Internal Audit Sampling</li>
  <li>SIA 370 — Information Technology in an Internal Audit</li>
  <li>SIA 390 — Monitoring and Reporting of Findings (Follow-up)</li>
  <li>SIA 410 — Reporting</li>
  <li>SIA 510 — Internal Audit of Special Areas</li>
  <li>SIA 530 — External Quality Assessment</li>
</ul>
<p>Verify current numbering and additions on the ICAI Internal Audit Standards Board portal —
ICAI has been progressively re-issuing these.</p>

<h2>The Three Lines Model (IIA 2020)</h2>
<p>Replaces the old "Three Lines of Defence" terminology, signalling collaboration rather than
defence:</p>
<ul>
  <li><strong>1st Line</strong> — Management functions that own and manage risks at the operational level.</li>
  <li><strong>2nd Line</strong> — Risk management, compliance, controllership functions that monitor and challenge first-line activities.</li>
  <li><strong>3rd Line</strong> — Internal audit, providing independent assurance to the board on the effectiveness of the first two lines.</li>
</ul>

<h2>COSO Internal Control — Integrated Framework (2013)</h2>
<p>The dominant framework for internal control. Five components, 17 principles:</p>
<ul>
  <li><strong>Control Environment</strong> — tone at top, integrity, competence, accountability (5 principles).</li>
  <li><strong>Risk Assessment</strong> — objectives, risk identification, fraud risk, change management (4 principles).</li>
  <li><strong>Control Activities</strong> — selection, IT controls, policies (3 principles).</li>
  <li><strong>Information and Communication</strong> — internal info, internal comm, external comm (3 principles).</li>
  <li><strong>Monitoring Activities</strong> — ongoing/separate evaluations, deficiency communication (2 principles).</li>
</ul>

<h2>COSO ERM — Enterprise Risk Management (2017)</h2>
<p>Five components, 20 principles. The risk-management counterpart of COSO internal control:</p>
<ul>
  <li><strong>Governance and Culture</strong></li>
  <li><strong>Strategy and Objective-Setting</strong></li>
  <li><strong>Performance</strong> — identify, assess, prioritise, respond, monitor risks</li>
  <li><strong>Review and Revision</strong></li>
  <li><strong>Information, Communication and Reporting</strong></li>
</ul>

<h2>Risk-Based Internal Auditing — RBIA</h2>

<h3>Step 1: Universe definition</h3>
<p>List every auditable entity — business processes, functions, geographies, projects, IT systems.
A typical mid-sized company has 50–150 auditable entities.</p>

<h3>Step 2: Risk assessment</h3>
<p>Score each entity on inherent risk (impact × likelihood, without considering controls) and
residual risk (after considering controls). Common dimensions:</p>
<ul>
  <li>Strategic — competitive, market, regulatory</li>
  <li>Operational — process failures, key-person dependency</li>
  <li>Financial — fraud, reporting accuracy, treasury</li>
  <li>Compliance — statutory, regulatory, contractual</li>
  <li>IT — cybersecurity, system availability, data integrity</li>
</ul>

<h3>Step 3: Audit plan</h3>
<p>Annual / multi-year audit plan covering high-risk entities yearly, medium-risk every 2 years, low-risk every 3–5 years. Approved by audit committee.</p>

<h3>Step 4: Engagement execution</h3>
<p>Per-engagement: planning memo → walk-through → Risk and Control Matrix → fieldwork → findings → reporting.</p>

<h2>Risk and Control Matrix (RCM) — the core deliverable</h2>
<p>For each business process, document:</p>
<ul>
  <li><strong>Process step</strong> — what happens in sequence.</li>
  <li><strong>Risk</strong> — what could go wrong (e.g., unauthorised payment).</li>
  <li><strong>Control</strong> — what mitigates it (e.g., dual approval over ₹1 lakh).</li>
  <li><strong>Control type</strong> — preventive vs detective; manual vs automated; key vs compensating.</li>
  <li><strong>Frequency</strong> — every transaction, daily, monthly.</li>
  <li><strong>Tester</strong> — who tests; what evidence to look at.</li>
  <li><strong>Test results</strong> — design effective? operating effective?</li>
</ul>

<h2>Controls testing — design vs operating effectiveness</h2>

<h3>Test of Design (ToD)</h3>
<p>Is the control, as designed, capable of preventing or detecting the risk? Conducted via
walkthrough — pick 1–2 transactions and trace through the control.</p>

<h3>Test of Operating Effectiveness (ToOE)</h3>
<p>Is the control operating as designed throughout the period? Sample-based testing. Sample sizes
generally:</p>
<ul>
  <li>Daily control: 25–60 samples per year</li>
  <li>Weekly: 5–10</li>
  <li>Monthly: 2–5</li>
  <li>Quarterly: 2</li>
  <li>Annually: 1 (the entire instance)</li>
</ul>

<h2>ICFR — Internal Control over Financial Reporting</h2>
<p>Section 143(3)(i) of the Companies Act 2013 requires the auditor to report on the adequacy and
operating effectiveness of internal financial controls. The ICAI's <strong>Guidance Note on Audit
of Internal Financial Controls Over Financial Reporting</strong> is the bible.</p>

<h3>Top-down risk-based approach</h3>
<ol>
  <li>Identify significant accounts and disclosures (materiality + qualitative factors).</li>
  <li>Identify business processes and significant transaction classes affecting those accounts.</li>
  <li>Identify <strong>Where Could It Go Wrong (WCGW)</strong> at each process step.</li>
  <li>Identify <strong>key controls</strong> mitigating each WCGW.</li>
  <li>Test design and operating effectiveness of key controls.</li>
  <li>Evaluate deficiencies — material weakness, significant deficiency, control deficiency.</li>
  <li>Report.</li>
</ol>

<h2>Audit cycles — what to look at in each</h2>

<h3>Order to Cash (O2C)</h3>
<p>Customer master, credit policy, order entry, pricing, dispatch, invoicing, accounts receivable,
collections, dispute management, write-offs. Key controls: credit limit enforcement, three-way match
on invoicing, dunning workflow, write-off approval.</p>

<h3>Procure to Pay (P2P)</h3>
<p>Vendor master, purchase requisition, PO, goods receipt, invoice receipt, three-way match,
payment. Key controls: vendor master changes log, segregation between vendor master and payment
processing, PO approval limits, three-way match exception escalation.</p>

<h3>Payroll</h3>
<p>Employee master, attendance, leave, salary computation, statutory deductions (PF/ESI/TDS),
payment, full-and-final settlement. Key controls: HR-payroll segregation, attendance system
integration, statutory remittance reconciliation.</p>

<h3>Treasury / Cash & Bank</h3>
<p>Cash collection, bank reconciliation, fund transfers, forex hedging, investment policy
compliance, fixed deposit management. Key controls: bank reconciliation timeliness and review,
authorisation matrix for payments, hedging policy compliance.</p>

<h3>Fixed Assets and Inventory</h3>
<p>Capitalisation, depreciation, physical verification, retirement/disposal. Inventory: receipt,
issue, transfer, physical count, valuation, write-down. Key controls: capitalisation policy,
periodic physical verification, slow-moving inventory analysis.</p>

<h3>IT General Controls (ITGC)</h3>
<p>Change management, logical access (user provisioning, role-based access), backup and recovery,
business continuity, IT operations (job scheduling, incident management). Key controls: SOD
enforcement in user access, change management approval and rollback, periodic access review.</p>

<h2>Reporting — SIA 410</h2>

<h3>Structure of a finding</h3>
<ol>
  <li><strong>Observation</strong> — what is the issue, factually described.</li>
  <li><strong>Risk implication</strong> — what could go wrong as a consequence.</li>
  <li><strong>Root cause</strong> — why is the control absent or failing.</li>
  <li><strong>Recommendation</strong> — what to do to fix it.</li>
  <li><strong>Management response</strong> — what management has agreed to do, with owner and timeline.</li>
  <li><strong>Rating</strong> — Critical / High / Medium / Low based on risk implication and likelihood.</li>
</ol>

<h3>Follow-up</h3>
<p>Per SIA 390 — track open findings; verify closure with evidence; report status to audit
committee periodically.</p>

<h2>Quality Assessment</h2>
<p>Per IIA Standards, every internal audit function must have an <strong>external quality
assessment (EQA)</strong> at least every 5 years. Internal QA is ongoing — peer review, supervisor
review, self-assessment.</p>

<h2>Emerging topics</h2>
<ul>
  <li><strong>Cybersecurity audit</strong> — NIST Cybersecurity Framework; ISO 27001.</li>
  <li><strong>ESG audit</strong> — BRSR for top 1,000 listed Indian companies; ICAI's recent Reporting on Climate-Related Disclosures.</li>
  <li><strong>Data analytics</strong> — Power BI, Tableau, Python, R — moving from sample-based to 100% population testing.</li>
  <li><strong>AI/ML model audit</strong> — bias testing, explainability, governance.</li>
  <li><strong>Third-party risk audit</strong> — vendor risk management; SOC 1 / SOC 2 reports.</li>
  <li><strong>Continuous auditing</strong> — automated transaction monitoring rather than periodic engagements.</li>
</ul>

<div class="callout">
<strong>Career note.</strong> For a CA in internal audit, the global certifications that compound
value: CIA (Certified Internal Auditor, by IIA), CISA (Certified Information Systems Auditor, for
IT audit), CFE (Certified Fraud Examiner). CIA is the foundational one. CISA is essential if you
want to specialise in IT audit. CFE is excellent for forensic and fraud investigation work.
</div>
""",
    },

    # ------------------------------------------------------------------
    # 4) Labour Codes
    # ------------------------------------------------------------------
    {
        "slug": "labor-codes",
        "title": "Four Labour Codes — Study Note",
        "summary": "The biggest labour reform since independence — 29 acts consolidated into 4 codes.",
        "body": """
<h2>The consolidation</h2>
<p>Parliament has enacted four codes consolidating 29 central labour laws:</p>
<ol>
  <li><strong>Code on Wages 2019</strong> — replaces Payment of Wages Act, Minimum Wages Act, Payment of Bonus Act, Equal Remuneration Act.</li>
  <li><strong>Industrial Relations Code 2020</strong> — replaces Industrial Disputes Act, Trade Unions Act, Industrial Employment (Standing Orders) Act.</li>
  <li><strong>Code on Social Security 2020</strong> — replaces EPF Act, ESIC Act, Maternity Benefit Act, Payment of Gratuity Act, Employees' Compensation Act, and 4 others.</li>
  <li><strong>Occupational Safety, Health and Working Conditions Code 2020</strong> — replaces Factories Act, Contract Labour Act, Inter-State Migrant Workmen Act, Mines Act, and 9 others.</li>
</ol>
<p>The codes are notified but their substantive provisions take effect when the relevant State Rules
are notified and the appointed date is published. Check the status state-by-state before relying on
operational change.</p>

<h2>Code on Wages 2019 — the most operationally significant</h2>

<h3>The redefined "wages"</h3>
<p>Sec 2(y) defines wages comprehensively. Key feature: <strong>the inclusive list (basic + DA +
retaining allowance) must be at least 50% of total remuneration</strong>; any excluded allowances
that exceed 50% are added back into the wage base. This is the single biggest practical change.</p>

<h4>What's excluded from wages</h4>
<ul>
  <li>Bonus payable under law.</li>
  <li>Value of accommodation, electricity, water, medical attendance.</li>
  <li>Employer contributions to PF and gratuity (excluding employee's share).</li>
  <li>Conveyance allowance.</li>
  <li>HRA.</li>
  <li>Overtime allowance.</li>
  <li>Commission.</li>
  <li>Special expenses incurred for performance of duty.</li>
  <li>Statutory bonus / ex-gratia / gratuity / retrenchment compensation paid on termination.</li>
</ul>

<p>BUT — if the sum of these excluded allowances exceeds 50% of total remuneration, the excess is
added back into "wages" for PF, gratuity, leave-encashment computation. This forces a structural
shift in CTC design toward higher basic wages.</p>

<div class="callout">
<strong>Compliance impact.</strong> Many companies have CTCs structured at 20–30% basic. Under the
codes, basic + DA must effectively be ~50% to avoid add-back. This increases PF contribution
(12% × higher base), gratuity provisions, leave encashment liability. Run the cost impact analysis
for your client/employer.
</div>

<h3>Minimum wages</h3>
<ul>
  <li>National Floor Wage — set by central government; State minimum wage cannot be below this.</li>
  <li>State minimum wage — fixed by state government for scheduled employments.</li>
  <li>Revised at least once every 5 years.</li>
  <li>Different rates by skill (unskilled, semi-skilled, skilled, highly skilled) and geography (zones).</li>
</ul>

<h3>Bonus</h3>
<ul>
  <li>Sec 26 — applicable to establishments with 20+ employees.</li>
  <li>Eligibility — employees earning up to specified ceiling (₹21,000/month wages, subject to revision).</li>
  <li>Minimum bonus 8.33% of wages (or ₹100, whichever higher); maximum 20%.</li>
  <li>Based on "available surplus" computed under prescribed formula.</li>
</ul>

<h2>Industrial Relations Code 2020</h2>

<h3>Worker vs supervisor/manager</h3>
<ul>
  <li>Worker: anyone employed in any establishment to do skilled, unskilled, technical, operational, clerical or supervisory work for hire or reward.</li>
  <li>Supervisory: wage ceiling raised to ₹18,000/month; above this, excluded from "worker" definition.</li>
  <li>Manager: any person employed as manager or in confidential/managerial capacity — excluded.</li>
</ul>

<h3>Trade unions and negotiating union</h3>
<ul>
  <li>A trade union must have ≥ 10% of workers OR 100 workers (whichever lower) for registration.</li>
  <li><strong>Negotiating union</strong> — a single union with ≥ 51% support of workers; otherwise a <strong>negotiating council</strong> with proportionate representation.</li>
  <li>Standing orders apply to establishments with <strong>300+ workers</strong> (raised from 100). Smaller establishments can voluntarily adopt model standing orders.</li>
</ul>

<h3>Layoff, retrenchment, closure</h3>
<ul>
  <li><strong>Layoff</strong> — Sec 67. Temporary inability to provide work. Compensation = 50% of basic + DA. Applies to factories with ≥ 50 workers.</li>
  <li><strong>Retrenchment</strong> — Sec 70. Permanent termination. One month's notice or pay in lieu. Compensation = 15 days × completed years.</li>
  <li><strong>Closure</strong> — Sec 75. 60-day notice. <strong>Government permission</strong> required for establishments with ≥ 300 workers (raised from 100 — a major change reducing labour court intervention).</li>
</ul>

<h3>Fixed-term employment</h3>
<p>Formalised — workers can be hired for a specified period. Entitled to:</p>
<ul>
  <li>Same statutory benefits as permanent workers, proportionate to period.</li>
  <li>Gratuity after 1 year of continuous service (vs 5 for permanent).</li>
  <li>No additional notice/compensation on expiry of fixed term.</li>
</ul>

<h2>Code on Social Security 2020</h2>

<h3>EPF — provident fund</h3>
<ul>
  <li>Applicable to establishments with ≥ 20 employees.</li>
  <li>Contribution: 12% employer + 12% employee on basic wages (post-code definition).</li>
  <li>Out of employer's 12%: 8.33% to EPS (pension fund up to wage ceiling ₹15,000), balance to EPF.</li>
  <li>Voluntary higher contribution permitted.</li>
  <li>International workers — covered with specific rules on cross-border contribution.</li>
</ul>

<h3>ESI — Employees' State Insurance</h3>
<ul>
  <li>Applicable to establishments with ≥ 10 employees, in notified areas.</li>
  <li>Coverage: employees with wages up to ₹21,000/month (subject to revision).</li>
  <li>Contribution: 3.25% employer + 0.75% employee.</li>
  <li>Benefits: medical, sickness, maternity, disability, dependents' benefit.</li>
</ul>

<h3>Gratuity</h3>
<ul>
  <li>Sec 53 — employee with continuous service of 5 years entitled (lowered to 1 year for fixed-term).</li>
  <li>Computation: 15 days' wages × completed years of service.</li>
  <li>Cap: ₹20 lakh (subject to revision).</li>
  <li>Continuous service includes service under previous employer in case of transfer.</li>
</ul>

<h3>Maternity benefit</h3>
<ul>
  <li>26 weeks paid maternity leave (first two children).</li>
  <li>12 weeks for third+ child or for adopting/commissioning mothers.</li>
  <li>Creche facility for establishments with ≥ 50 employees.</li>
  <li>No dismissal or notice during pregnancy.</li>
</ul>

<h3>Gig and platform workers — landmark inclusion</h3>
<p>Chapter IX of the Social Security Code <strong>statutorily recognises gig and platform workers</strong> for the first time. Definitions:</p>
<ul>
  <li><strong>Gig worker</strong> — person who performs work or participates in a work arrangement and earns from such activities outside of traditional employer-employee relationship.</li>
  <li><strong>Platform worker</strong> — gig worker engaged via online platforms.</li>
  <li><strong>Aggregator</strong> — digital intermediary connecting buyer and seller of services.</li>
</ul>

<p><strong>Contributions:</strong> aggregators required to contribute 1–2% of annual turnover (or 5%
of amount paid to gig workers, whichever lower, capped at industry-prescribed limit) to the social
security fund. Funds finance schemes for gig workers — life and disability cover, health and
maternity, old-age protection.</p>

<h2>OSH Code 2020</h2>

<h3>Coverage</h3>
<ul>
  <li>Manufacturing establishments with 10+ workers (with power) or 20+ (without power) — was 10/20 under old Factories Act with state-level variations.</li>
  <li>Contract labour — registration threshold reduced to 50 workers (was 20 under old act).</li>
  <li>Inter-state migrant workers — threshold reduced to 10 workers.</li>
  <li>Mines, plantations, transport, ports — sector-specific provisions retained.</li>
</ul>

<h3>Working hours and conditions</h3>
<ul>
  <li>Maximum 48 hours per week; daily limit 12 hours (some states allow 12-hour days subject to weekly cap; old limit was 9 hours).</li>
  <li>Overtime double rate.</li>
  <li>Weekly off — 1 day.</li>
  <li>Annual leave — 1 day per 20 days worked (i.e., approximately 18 days for a full year). Minimum 12 days encashable on termination.</li>
</ul>

<h3>Women in the workplace</h3>
<p>Major shift — women may be employed in all establishments and in all shifts (including night
shift), subject to safety provisions:</p>
<ul>
  <li>Safe transportation.</li>
  <li>Adequate lighting and safety measures.</li>
  <li>Consent of the woman worker.</li>
</ul>

<h3>Contract labour</h3>
<ul>
  <li>Contractor licensing for any establishment engaging 50+ contract workers.</li>
  <li>Welfare facilities — canteens, restrooms, drinking water — paid for by principal employer.</li>
  <li>Same statutory benefits as direct workers for similar work.</li>
  <li>If contractor not licensed → workers deemed direct employees of principal employer.</li>
</ul>

<h2>Compliance framework</h2>

<h3>Single registration, single return, single inspection</h3>
<p>Across all four codes, the design philosophy is unified:</p>
<ul>
  <li><strong>Single registration</strong> — one registration per establishment instead of multiple.</li>
  <li><strong>Single return</strong> — quarterly/annual return covering all codes.</li>
  <li><strong>Inspector-cum-Facilitator</strong> — replacing adversarial inspectors. Facilitator role includes advising on compliance, not just policing.</li>
  <li><strong>Compoundable offences</strong> — first-offence warning; option to compound penalties.</li>
</ul>

<h3>Shram Suvidha Portal</h3>
<p>The unified online compliance portal at <code>shramsuvidha.gov.in</code>. Registration, returns,
inspections, grievance redressal — all online.</p>

<h2>State Rules — the critical operational variable</h2>
<p>Each code's substantive provisions take effect when corresponding State Rules are notified.
Major industrial states have varying timelines:</p>
<ul>
  <li>Some states (Madhya Pradesh, Uttar Pradesh, Gujarat) — Rules notified for some codes.</li>
  <li>Other states — still in draft stage.</li>
  <li>Operational implications: until State Rules are notified, the old laws continue.</li>
</ul>

<div class="callout">
<strong>Practical advice.</strong> Build a state-by-state matrix tracking notification status of
rules under each of the 4 codes for the states where your employer/clients operate. Update monthly.
This is the difference between knowing the codes academically and being operationally useful.
</div>

<h2>Saving clauses and transitions</h2>
<ul>
  <li>Pending cases under old acts continue under those acts.</li>
  <li>Registrations granted under old acts deemed valid under new codes (subject to migration).</li>
  <li>Acts repealed by the new codes are listed in each code's schedule — note the date of repeal.</li>
</ul>

<h2>Penalties</h2>
<ul>
  <li>Generally — fines ranging from ₹50,000 to ₹3 lakh per contravention; imprisonment for serious offences.</li>
  <li>First-offence warning concept — many minor offences require a warning before penalty.</li>
  <li>Compounding option for most offences with payment of 50% of maximum fine.</li>
</ul>
""",
    },

    # ------------------------------------------------------------------
    # 5) Auditing — ICAI
    # ------------------------------------------------------------------
    {
        "slug": "auditing",
        "title": "Auditing — Study Note (ICAI SAs, CARO 2020, ICFR)",
        "summary": "The audit framework — Standards on Auditing (SAs), Companies Act audit provisions, and CARO 2020.",
        "body": """
<h2>The audit framework</h2>

<h3>Statutory mandate</h3>
<p>Audit of company financial statements is governed by Sections 139–148 of the Companies Act 2013
read with the Companies (Audit and Auditors) Rules 2014. Key provisions:</p>
<ul>
  <li><strong>Sec 139</strong> — Appointment of auditors. First auditor appointed by board within 30 days of incorporation; subsequent auditors at first AGM for 5-year term.</li>
  <li><strong>Sec 139(2) + Rule 5</strong> — Auditor rotation. Individual auditor: 5-year term, then 5-year cooling-off. Audit firm: 10-year term, then 5-year cooling-off. Applies to listed and prescribed companies.</li>
  <li><strong>Sec 140</strong> — Removal, resignation, casual vacancy.</li>
  <li><strong>Sec 141</strong> — Eligibility, qualifications, disqualifications.</li>
  <li><strong>Sec 142</strong> — Remuneration.</li>
  <li><strong>Sec 143</strong> — Powers and duties; the principal section. Sec 143(3)(i) is the ICFR opinion.</li>
  <li><strong>Sec 144</strong> — Auditor not to render certain services (the "prohibited services" — bookkeeping, internal audit, financial management, actuarial, etc.).</li>
  <li><strong>Sec 145</strong> — Auditor's signature.</li>
  <li><strong>Sec 146</strong> — Auditor's attendance at AGM.</li>
  <li><strong>Sec 147</strong> — Punishment for contraventions.</li>
  <li><strong>Sec 148</strong> — Central government's power to direct cost audit.</li>
</ul>

<h3>The standard-setting architecture</h3>
<p><strong>ICAI Auditing and Assurance Standards Board (AASB)</strong> issues:</p>
<ul>
  <li>Standards on Auditing (SAs) — for audit of historical financial information.</li>
  <li>Standards on Review Engagements (SREs) — for limited assurance reviews.</li>
  <li>Standards on Assurance Engagements (SAEs) — for assurance other than audit/review.</li>
  <li>Standards on Related Services (SRSs) — for compilation and agreed-upon procedures.</li>
  <li>Standards on Quality Control (SQC 1).</li>
  <li>Guidance Notes (GNs).</li>
</ul>
<p>SAs are converged with the International Standards on Auditing (ISAs) issued by IAASB.</p>

<h2>The structure of SAs</h2>
<ul>
  <li>SA 100–199 — Introductory Matters (currently primarily SA 200, SA 220).</li>
  <li>SA 200–299 — General Principles and Responsibilities.</li>
  <li>SA 300–499 — Risk Assessment and Response.</li>
  <li>SA 500–599 — Audit Evidence.</li>
  <li>SA 600–699 — Using the Work of Others.</li>
  <li>SA 700–799 — Audit Conclusions and Reporting.</li>
  <li>SA 800–899 — Specialised Areas.</li>
</ul>

<h2>SA 200 — Overall Objectives</h2>
<p>The fundamental SA. The objectives:</p>
<ul>
  <li>Obtain reasonable assurance that the financial statements as a whole are free from material misstatement.</li>
  <li>Report on the financial statements in accordance with the auditor's findings.</li>
</ul>
<p><strong>Reasonable assurance</strong> = high (not absolute) level of assurance. Acknowledges
inherent limitations: nature of financial reporting (estimates), nature of audit procedures (sampling).</p>

<h2>SA 220 — Quality Control for an Audit</h2>
<p>Engagement-level quality. Combined with <strong>SQC 1</strong> (firm-level quality control) — the
ICAI standard equivalent to international ISQC 1. <strong>ISQM 1 and ISQM 2</strong> are new
international standards on Quality Management (replacing ISQC 1); ICAI is in process of issuing
equivalent SAs.</p>

<h2>Risk assessment — SA 300, 315 (revised), 320, 330</h2>

<h3>SA 315 (Revised) — Identifying and Assessing Risks</h3>
<p>The risk-assessment standard, effective for audits of financial statements for periods commencing
on or after 1 April 2022 in India. Significant changes from the prior version:</p>
<ul>
  <li><strong>Spectrum of inherent risk</strong> — risks are now evaluated along factors: subjectivity, complexity, uncertainty, change, susceptibility to fraud or management bias.</li>
  <li><strong>Five elements of system of internal control</strong> — control environment, risk assessment, monitoring of controls, information system, control activities.</li>
  <li><strong>Significant risks</strong> — defined as risks of material misstatement that are at the higher end of the spectrum of inherent risk OR are required to be treated as significant.</li>
  <li><strong>Stand-back</strong> — after risk identification, evaluate whether the overall risk-identification effort is complete.</li>
</ul>

<h3>SA 320 — Materiality</h3>
<p>Materiality at the financial-statement level (overall materiality) and at the assertion level
(performance materiality, typically 50–75% of overall). Specific materiality for particular accounts
or disclosures if lower thresholds apply.</p>

<h3>SA 330 — Responses to Assessed Risks</h3>
<p>Plan and perform audit procedures responsive to assessed risks. Combination of controls testing
(if reliance is placed on controls) and substantive procedures (test of details and substantive
analytical procedures).</p>

<h2>SA 240 — Fraud</h2>
<p>Auditor's responsibilities relating to fraud. Key concepts:</p>
<ul>
  <li><strong>Fraud triangle</strong> — incentive/pressure + opportunity + rationalisation.</li>
  <li><strong>Presumed significant risk of management override of controls</strong> — every audit, journal-entry testing must be performed.</li>
  <li><strong>Revenue recognition</strong> — presumed significant risk in most cases.</li>
  <li>Mandatory team discussion about fraud risks.</li>
  <li>Specific responses — unpredictable procedures, increased sample sizes, year-end testing rather than interim.</li>
</ul>

<h2>SA 250 — Laws and Regulations</h2>
<p>Two categories:</p>
<ul>
  <li>Laws affecting financial statements (e.g., tax, company law) — auditor must understand and consider effect.</li>
  <li>Other laws material to operations (e.g., environmental, FEMA) — auditor must perform specified procedures.</li>
</ul>
<p><strong>NOCLAR</strong> (Non-compliance with Laws and Regulations) — concept globally; in India,
auditor's response is to communicate with TCWG and assess implications.</p>

<h2>SA 260 + SA 265 — Communication</h2>
<ul>
  <li>SA 260 — Communication with Those Charged with Governance (audit committee). Mandatory communications: audit plan, significant findings, auditor independence.</li>
  <li>SA 265 — Communicating Deficiencies in Internal Control. Significant deficiencies and material weaknesses to be communicated in writing.</li>
</ul>

<h2>Audit evidence — SA 500 series</h2>

<h3>SA 500 — Audit Evidence</h3>
<p>Audit evidence must be <strong>sufficient and appropriate</strong>:</p>
<ul>
  <li>Sufficiency — quantity.</li>
  <li>Appropriateness — quality (relevance + reliability).</li>
</ul>
<p>Reliability hierarchy (from most reliable to least): external + direct corroboration; internal
+ external; internal + good control environment; internal + weak control.</p>

<h3>SA 505 — External Confirmations</h3>
<p>Bank confirmations, trade-receivable confirmations, lawyer's confirmations. <strong>Positive</strong>
(reply expected even if balance is correct) and <strong>negative</strong> (reply expected only if
balance is incorrect).</p>

<h3>SA 530 — Audit Sampling</h3>
<p>Statistical and non-statistical sampling. Two main methods:</p>
<ul>
  <li><strong>Attribute sampling</strong> — for controls testing; estimate failure rate.</li>
  <li><strong>Variables sampling / Monetary Unit Sampling (MUS)</strong> — for substantive testing; estimate monetary misstatement.</li>
</ul>

<h3>SA 540 (Revised) — Auditing Accounting Estimates</h3>
<p>The new SA 540 (effective audits of FS for periods beginning on or after 1 April 2023 in India)
takes a risk-based approach to estimates. Three categories of estimates by complexity:</p>
<ul>
  <li>Simple — straightforward computation (e.g., depreciation on PPE).</li>
  <li>Complex — significant judgment (e.g., expected credit losses, fair value of unlisted investments).</li>
  <li>Highly complex — multiple assumptions, scenarios (e.g., goodwill impairment).</li>
</ul>
<p>Audit response calibrated to complexity.</p>

<h3>SA 550 — Related Parties</h3>
<p>Identify related parties beyond those disclosed by management; understand business rationale of
related-party transactions; evaluate whether they are at arm's length.</p>

<h2>Reporting — SA 700 series</h2>

<h3>SA 700 (Revised) — Forming an Opinion</h3>
<ul>
  <li>Opinion section first (not last).</li>
  <li>Basis for opinion section.</li>
  <li>Going concern section (if applicable).</li>
  <li>Key Audit Matters (for listed entities — SA 701).</li>
  <li>Responsibilities of management and TCWG.</li>
  <li>Auditor's responsibilities (detailed).</li>
  <li>Other Information (SA 720).</li>
  <li>Report on other legal and regulatory requirements (CARO).</li>
</ul>

<h3>SA 701 — Key Audit Matters</h3>
<p>Communication of <strong>matters that were of most significance</strong> in the audit, selected
from those communicated to TCWG. Each KAM has:</p>
<ul>
  <li>Description — the matter.</li>
  <li>Why considered KAM — the auditor's reasoning.</li>
  <li>How addressed — the audit response.</li>
</ul>
<p>Typical KAMs: revenue recognition, ECL, fair valuation, going concern, deferred tax, contingent
liabilities, business combinations.</p>

<h3>SA 705 — Modifications to the Opinion</h3>
<table>
  <thead><tr><th>Nature of misstatement</th><th>Material but not pervasive</th><th>Material AND pervasive</th></tr></thead>
  <tbody>
    <tr><td>Disagreement with management</td><td>Qualified opinion</td><td>Adverse opinion</td></tr>
    <tr><td>Inability to obtain evidence</td><td>Qualified opinion</td><td>Disclaimer of opinion</td></tr>
  </tbody>
</table>

<h3>SA 706 — Emphasis of Matter (EOM) and Other Matter (OM)</h3>
<ul>
  <li><strong>EOM</strong> — draws attention to a matter appropriately disclosed in the FS that is fundamental to user understanding.</li>
  <li><strong>OM</strong> — draws attention to a matter not disclosed in the FS but relevant to user understanding.</li>
</ul>

<h2>Group audits — SA 600 (Revised)</h2>
<p>SA 600 (Revised) — effective for audits of group financial statements for periods commencing on
or after 1 April 2026 in India (verify current effective date). Significant changes:</p>
<ul>
  <li>Component identification based on risks, not just size.</li>
  <li>Component materiality determined by group auditor.</li>
  <li>Direction, supervision and review of component auditor's work — more rigorous documentation.</li>
  <li>Quality management oversight at group level.</li>
</ul>

<h2>CARO 2020 — Companies (Auditor's Report) Order</h2>
<p>The auditor's additional report under Sec 143(11). 21 clauses covering:</p>
<ol>
  <li>Property, Plant and Equipment (PPE register, physical verification, title deeds).</li>
  <li>Inventory (physical verification, working capital limits from banks).</li>
  <li>Loans, investments, guarantees, security given.</li>
  <li>Compliance with Sec 185 and 186 on loans/investments.</li>
  <li>Acceptance of deposits — Sec 73–76.</li>
  <li>Cost records — Sec 148.</li>
  <li>Statutory dues (PF, ESI, GST, income tax) and disputed amounts.</li>
  <li>Income disclosed in tax assessments not recorded in books.</li>
  <li>Default in repayment of loans/borrowings; default in financial creditor (wilful defaulter).</li>
  <li>IPO/Further public offer fund utilisation.</li>
  <li>Fraud reporting — by company, on company, by company officials.</li>
  <li>Nidhi company specifics.</li>
  <li>Sec 177 (audit committee) and Sec 188 (related party transactions) compliance.</li>
  <li>Internal audit system adequacy.</li>
  <li>Non-cash transactions with directors per Sec 192.</li>
  <li>NBFC/RBI registration; CIC.</li>
  <li>Cash losses in financial year.</li>
  <li>Resignation of statutory auditors during year.</li>
  <li>Material uncertainty about meeting liabilities.</li>
  <li>CSR — transfer of unspent amount.</li>
  <li>Reporting of fraud by company on company.</li>
</ol>

<h2>ICFR — Sec 143(3)(i)</h2>
<p>Read with the ICAI Guidance Note on Audit of Internal Financial Controls Over Financial Reporting.
Two-track approach:</p>
<ul>
  <li><strong>Standalone audit report</strong> on adequacy of internal financial controls — for listed and prescribed companies.</li>
  <li><strong>Integrated with financial statement audit</strong> — for non-listed companies that meet thresholds.</li>
</ul>

<h2>Specialised audits</h2>
<ul>
  <li><strong>Tax audit under Sec 44AB</strong> — for businesses with turnover &gt; ₹1 crore (or ₹10 crore if cash transactions &lt; 5%); for professionals with receipts &gt; ₹50 lakh. Form 3CA/3CB + 3CD.</li>
  <li><strong>Transfer pricing audit under Sec 92E</strong> — Form 3CEB.</li>
  <li><strong>GST audit</strong> — for taxpayers with turnover above prescribed threshold (Section 35(5) — though the audit requirement was relaxed; reconciliation statement Form GSTR-9C is now self-certified).</li>
  <li><strong>Bank statutory audit</strong> — annual; appointed by RBI/bank board.</li>
  <li><strong>Bank concurrent audit</strong> — continuous; covering ~50% of business.</li>
  <li><strong>Bank revenue audit</strong> — focus on income leakage.</li>
  <li><strong>Cost audit under Sec 148</strong> — sector-specific notifications.</li>
</ul>

<h2>NFRA</h2>
<p>National Financial Reporting Authority — established under Sec 132 of the Companies Act 2013.
Jurisdiction:</p>
<ul>
  <li>Listed companies.</li>
  <li>Unlisted companies above prescribed thresholds (assets ≥ ₹500 cr; turnover ≥ ₹1,000 cr).</li>
  <li>Banks, insurance, electricity sector entities.</li>
  <li>Subsidiaries of foreign listed entities.</li>
</ul>
<p>NFRA can:</p>
<ul>
  <li>Make recommendations to MCA on standards.</li>
  <li>Monitor and enforce compliance with accounting and auditing standards.</li>
  <li>Conduct inspection of audit firms.</li>
  <li>Take disciplinary action — financial penalties, debarment from auditing for specified period.</li>
</ul>
<p><strong>NFRA inspection reports and disciplinary orders</strong> are public and an excellent source
of learning about common audit failures.</p>

<div class="callout">
<strong>Recent regulatory focus.</strong> Three priority areas for NFRA: (a) audit of internal
financial controls — depth and documentation; (b) related-party transactions — substantive procedures
beyond management disclosure; (c) going concern — robust evaluation of going-concern assumption,
particularly for companies in distress. Calibrate your audit approach to these priorities.
</div>
""",
    },

    # ------------------------------------------------------------------
    # 6) English
    # ------------------------------------------------------------------
    {
        "slug": "english",
        "title": "English Grammar & Spoken Skills — Study Note",
        "summary": "A reference covering grammar, vocabulary and pronunciation — the language layer.",
        "body": """
<h2>Why this matters</h2>
<p>Strong English compounds with every other skill on this plan. Audit reports that are clearer
take less revision time; client emails that are more precise reduce back-and-forth; presentation
fluency builds professional confidence. The investment is small (30 minutes daily) and the return
compounds over a career.</p>

<h2>Grammar fundamentals</h2>

<h3>Parts of speech</h3>
<ul>
  <li><strong>Noun</strong> — person, place, thing, idea. Concrete (chair) vs abstract (justice); proper (Delhi) vs common (city); countable (book/books) vs uncountable (water).</li>
  <li><strong>Pronoun</strong> — replaces a noun. Personal (he, she, they), possessive (his, hers), reflexive (himself, themselves), demonstrative (this, that), interrogative (who, what), relative (who, which, that).</li>
  <li><strong>Verb</strong> — action or state. Transitive (takes object) vs intransitive (doesn't). Finite (with tense) vs non-finite (infinitive, gerund, participle).</li>
  <li><strong>Adjective</strong> — qualifies a noun. Descriptive, demonstrative, possessive, indefinite, numerical, interrogative.</li>
  <li><strong>Adverb</strong> — qualifies verb/adjective/another adverb. Of manner, time, place, frequency, degree.</li>
  <li><strong>Preposition</strong> — relates noun/pronoun to another word. In, on, at, by, with, for, to, of.</li>
  <li><strong>Conjunction</strong> — joins words/phrases/clauses. Coordinating (and, but, or), subordinating (because, although, if), correlative (either…or, neither…nor).</li>
  <li><strong>Interjection</strong> — expresses emotion. Oh!, Alas!, Wow!</li>
</ul>

<h3>Sentence structure</h3>
<p>Every English sentence has at minimum a <strong>subject</strong> and a <strong>predicate</strong>.
Four basic sentence patterns:</p>
<ul>
  <li><strong>S + V</strong> — She sleeps.</li>
  <li><strong>S + V + O</strong> — She reads books.</li>
  <li><strong>S + V + IO + DO</strong> — She gives him books.</li>
  <li><strong>S + V + O + OC</strong> — She painted the wall blue.</li>
</ul>

<h3>Phrases vs clauses</h3>
<p>A <strong>phrase</strong> is a group of words without a subject-verb combination. A
<strong>clause</strong> has a subject and a verb. Independent clauses stand alone; dependent clauses
do not.</p>

<h2>The 12 tenses — the core of spoken accuracy</h2>

<table>
  <thead><tr><th></th><th>Simple</th><th>Continuous</th><th>Perfect</th><th>Perfect Continuous</th></tr></thead>
  <tbody>
    <tr><td>Present</td><td>I write</td><td>I am writing</td><td>I have written</td><td>I have been writing</td></tr>
    <tr><td>Past</td><td>I wrote</td><td>I was writing</td><td>I had written</td><td>I had been writing</td></tr>
    <tr><td>Future</td><td>I will write</td><td>I will be writing</td><td>I will have written</td><td>I will have been writing</td></tr>
  </tbody>
</table>

<h3>When to use each</h3>
<ul>
  <li><strong>Simple present</strong> — habits, general truths, scheduled events. "I commute by metro."</li>
  <li><strong>Present continuous</strong> — actions in progress now, temporary states. "I am working on the audit."</li>
  <li><strong>Present perfect</strong> — past action with present relevance. "I have completed the engagement."</li>
  <li><strong>Present perfect continuous</strong> — action started in past, continuing now. "I have been working since 8 AM."</li>
  <li><strong>Simple past</strong> — completed action at a specific past time. "I finished the report yesterday."</li>
  <li><strong>Past continuous</strong> — action in progress at a past time. "I was writing when she called."</li>
  <li><strong>Past perfect</strong> — action completed before another past action. "I had submitted before the deadline."</li>
  <li><strong>Past perfect continuous</strong> — duration before a past time. "I had been waiting for 30 minutes when he arrived."</li>
  <li><strong>Simple future</strong> — future intention or prediction. "I will finish tomorrow."</li>
  <li><strong>Future continuous</strong> — action in progress at a future time. "I will be presenting at 10 AM."</li>
  <li><strong>Future perfect</strong> — action completed before a future time. "I will have finished by 5 PM."</li>
  <li><strong>Future perfect continuous</strong> — duration up to a future point. "By December, I will have been working here for 5 years."</li>
</ul>

<h2>Articles — the silent killers</h2>
<ul>
  <li><strong>A / An</strong> — indefinite; first mention or one of many. "I saw a movie." Use "an" before vowel sounds (an hour, but a university).</li>
  <li><strong>The</strong> — definite; specific, already mentioned, unique, superlative. "The movie was good."</li>
  <li><strong>Zero article</strong> — generic plural, abstract noun in general sense, proper noun. "Books are valuable." "Tigers are endangered." "Delhi is the capital."</li>
</ul>

<h3>Indian English common errors</h3>
<ul>
  <li>"He is going to <s>the</s> Delhi" — no "the" before city names.</li>
  <li>"I have <s>the</s> headache" — no "the" with personal afflictions.</li>
  <li>"<s>The</s> Mr. Sharma is here" — no "the" before titles.</li>
</ul>

<h2>Prepositions — the most error-prone</h2>

<h3>Time</h3>
<ul>
  <li><strong>At</strong> — specific times. "at 5 PM", "at midnight", "at the weekend (BrE)".</li>
  <li><strong>On</strong> — days, dates. "on Monday", "on 15 June", "on my birthday".</li>
  <li><strong>In</strong> — months, years, decades, longer periods. "in June", "in 2025", "in the 1990s".</li>
</ul>

<h3>Place</h3>
<ul>
  <li><strong>At</strong> — specific point. "at the office", "at the bus stop".</li>
  <li><strong>On</strong> — surface. "on the table", "on the wall".</li>
  <li><strong>In</strong> — enclosed space. "in the room", "in the box", "in the city".</li>
</ul>

<h3>Common verb-preposition collocations</h3>
<ul>
  <li>interested IN, depend ON, suffer FROM, succeed IN, agree WITH (person) / TO (proposal), arrive AT (small place) / IN (big place), apologise FOR (action) / TO (person), congratulate ON, listen TO, look AT/FOR/AFTER, consist OF, accuse OF, blame FOR.</li>
</ul>

<h2>Active and passive voice</h2>
<ul>
  <li>Active: <em>The auditor signed the report.</em> (Subject does the action.)</li>
  <li>Passive: <em>The report was signed by the auditor.</em> (Subject receives the action.)</li>
</ul>
<p>Formation: form of "be" + past participle. Tense determined by "be" form.</p>
<ul>
  <li>Present: am/is/are + V3 → "The report is signed."</li>
  <li>Past: was/were + V3 → "The report was signed."</li>
  <li>Future: will be + V3 → "The report will be signed."</li>
  <li>Perfect: has/had been + V3 → "The report has been signed."</li>
  <li>Continuous: am being / was being + V3 → "The report is being signed."</li>
</ul>

<h3>When to use passive</h3>
<ul>
  <li>When the agent is unknown or unimportant.</li>
  <li>When the focus is on the action or result.</li>
  <li>In formal/scientific writing.</li>
  <li>To avoid blaming a specific person.</li>
</ul>

<h2>Modal verbs</h2>
<ul>
  <li><strong>Can / Could</strong> — ability; permission (could is more polite). "I can play tennis." / "Could I leave early?"</li>
  <li><strong>May / Might</strong> — possibility; permission (may is more formal). "It may rain." / "May I come in?"</li>
  <li><strong>Must / Have to</strong> — obligation. "I must finish today." "Mustn't" = prohibition; "don't have to" = no obligation. Critical distinction.</li>
  <li><strong>Should / Ought to</strong> — advice, weak obligation. "You should rest."</li>
  <li><strong>Will / Would</strong> — future; willingness; polite request; habitual past. "Would you mind…?"</li>
  <li><strong>Shall</strong> — formal future; suggestions. "Shall we go?" (BrE prefers; AmE uses "should" more.)</li>
</ul>

<h2>Direct vs Indirect speech</h2>
<p>Tense back-shift on reporting:</p>
<table>
  <thead><tr><th>Direct</th><th>Indirect</th></tr></thead>
  <tbody>
    <tr><td>"I am tired."</td><td>He said he was tired.</td></tr>
    <tr><td>"I have finished."</td><td>He said he had finished.</td></tr>
    <tr><td>"I finished yesterday."</td><td>He said he had finished the previous day.</td></tr>
    <tr><td>"I will go tomorrow."</td><td>He said he would go the next day.</td></tr>
  </tbody>
</table>
<p>Time and place adverbs also shift: <em>here → there, now → then, today → that day, tomorrow →
the next day, yesterday → the previous day</em>.</p>

<h2>Conditional sentences</h2>
<ul>
  <li><strong>Zero conditional</strong> — general truths. "If you heat water, it boils." (if + present, present)</li>
  <li><strong>First conditional</strong> — real future possibility. "If it rains, I will stay home." (if + present, will + V1)</li>
  <li><strong>Second conditional</strong> — unreal present/future. "If I had time, I would help." (if + past, would + V1)</li>
  <li><strong>Third conditional</strong> — unreal past. "If I had known, I would have come." (if + past perfect, would have + V3)</li>
  <li><strong>Mixed conditional</strong> — past condition + present result. "If I had studied more, I would be a doctor now."</li>
</ul>

<h2>Vocabulary building — the etymological approach</h2>
<p>Norman Lewis's method: learn the root + prefix + suffix and you decode hundreds of words. Examples:</p>

<h3>Common Latin/Greek roots</h3>
<ul>
  <li><strong>BENE</strong> (good) — benefactor, beneficiary, benevolent, benediction.</li>
  <li><strong>MAL</strong> (bad) — malice, malfunction, malevolent, malign.</li>
  <li><strong>VIT/VIV</strong> (life) — vital, vivid, revive, vitamin.</li>
  <li><strong>MORT</strong> (death) — mortal, immortal, mortality, mortician.</li>
  <li><strong>PHON</strong> (sound) — phone, symphony, microphone, euphony.</li>
  <li><strong>GEO</strong> (earth) — geography, geology, geopolitics.</li>
  <li><strong>BIO</strong> (life) — biology, biography, biosphere.</li>
  <li><strong>CHRON</strong> (time) — chronicle, chronological, anachronism.</li>
</ul>

<h3>Common prefixes</h3>
<ul>
  <li>UN-, DIS-, IN-, IM-, IL-, IR- (not, opposite) — unhappy, disagree, inactive, impossible, illegal, irregular.</li>
  <li>RE- (again, back) — return, restart, revise.</li>
  <li>PRE- (before) — preview, predict, prevent.</li>
  <li>POST- (after) — postpone, postscript, postwar.</li>
  <li>MIS- (wrong) — misunderstand, mislead, misuse.</li>
  <li>SUB- (under) — submarine, subway, subordinate.</li>
  <li>SUPER- (over) — superior, superhuman, supervise.</li>
</ul>

<h2>Phrasal verbs — the spoken-English challenge</h2>
<p>Phrasal verbs are verb + preposition/adverb combinations with meanings different from the
individual words. Examples around the verb <em>get</em>:</p>
<ul>
  <li>get up — rise from bed.</li>
  <li>get along (with) — have a good relationship.</li>
  <li>get away — escape.</li>
  <li>get by — manage with limited resources.</li>
  <li>get over — recover from.</li>
  <li>get through — successfully complete OR endure.</li>
  <li>get on — board; succeed.</li>
  <li>get off — leave; finish work.</li>
</ul>

<h2>Pronunciation — IPA basics</h2>
<p>English has 44 phonemes: 24 consonants + 12 pure vowels + 8 diphthongs. Indian speakers
commonly need to work on:</p>
<ul>
  <li><strong>/θ/ and /ð/</strong> — "th" sounds. think, this. Tip of tongue between teeth.</li>
  <li><strong>/v/ vs /w/</strong> — distinct in English (vine vs wine). In some Indian languages both become similar sounds.</li>
  <li><strong>/z/</strong> — voiced "s" sound. <em>amazing</em>, <em>noisy</em>.</li>
  <li><strong>Schwa /ə/</strong> — the most common English vowel; unstressed syllables. <em>about</em>, <em>banana</em>, <em>support</em>.</li>
  <li><strong>Word stress</strong> — different stress changes meaning. RECORD (n.) vs reCORD (v.); PRESENT (n.) vs preSENT (v.).</li>
</ul>

<h2>Sentence stress and intonation</h2>
<p>English is a <strong>stress-timed</strong> language (vs. syllable-timed like Hindi). Content words
(nouns, verbs, adjectives, adverbs) are stressed; function words (articles, prepositions,
auxiliary verbs) are unstressed and reduced.</p>
<p>Compare: "I'm GOING to the OFFICE to MEET the CLIENT." — only capitalised words receive stress.</p>

<h2>Common Indian English errors</h2>
<ul>
  <li>"<s>Discuss about</s>" → discuss (no preposition).</li>
  <li>"<s>Reach to</s> the office" → reach the office.</li>
  <li>"<s>Cope up with</s>" → cope with.</li>
  <li>"<s>Marry with</s>" → marry (no preposition).</li>
  <li>"<s>Order for</s>" → order (transitive).</li>
  <li>"<s>Revert back</s>" → revert (or reply / respond).</li>
  <li>"<s>Prepone</s>" → bring forward; reschedule earlier.</li>
  <li>"<s>Kindly do the needful</s>" → please proceed with the necessary action.</li>
  <li>"<s>I am having</s> a car" (continuous for possession) → I have a car.</li>
  <li>"<s>What is your good name</s>" → What is your name?</li>
</ul>

<h2>Business writing principles</h2>
<ol>
  <li><strong>Lead with the point.</strong> What do you want the reader to do? State it first.</li>
  <li><strong>One idea per paragraph.</strong> Topic sentence first; supporting sentences after.</li>
  <li><strong>Active voice over passive</strong> (with exceptions for diplomatic tone).</li>
  <li><strong>Concrete over abstract.</strong> "The audit will take 6 weeks." not "The engagement will be conducted over a reasonable period."</li>
  <li><strong>Short sentences over long.</strong> Aim for average 15–20 words.</li>
  <li><strong>Edit ruthlessly.</strong> Strunk & White's "omit needless words" — every word should earn its place.</li>
</ol>

<h2>Audit-report language</h2>
<p>Specific to your professional context, audit-report language follows conventions:</p>
<ul>
  <li><strong>Factual, observation-based</strong> — describe what is, without interpretation. "The vendor master had 1,234 active vendors at year-end."</li>
  <li><strong>Specific, not vague</strong> — "12 of 30 sampled vendor records lacked required documentation" beats "several vendor records had documentation gaps".</li>
  <li><strong>Risk-implication language</strong> — "this exposes the company to risk of duplicate or fictitious vendor payments" — concrete consequence, not generic risk.</li>
  <li><strong>Recommendation language</strong> — actionable, with owner and timeline. "Recommendation: Implement quarterly vendor master review by Finance team; target completion by [date]."</li>
  <li><strong>Hedge language to avoid</strong> — "may", "could", "it appears that" — these dilute impact. Use only when genuinely uncertain.</li>
</ul>

<h2>A 30-minute daily practice routine</h2>
<ol>
  <li><strong>10 minutes — Grammar/vocabulary.</strong> 1 chapter of Wren & Martin OR 1 chapter of Norman Lewis; do all exercises.</li>
  <li><strong>10 minutes — Listening.</strong> 1 episode of BBC 6 Minute English OR 1 TED Talk. Take notes; look up unknown words.</li>
  <li><strong>10 minutes — Speaking.</strong> Read aloud a 300-word passage from a quality newspaper (The Hindu, Business Standard). Record yourself. Listen back. Identify pronunciation errors.</li>
</ol>

<div class="callout">
<strong>Consistency over intensity.</strong> 30 minutes daily for 8 weeks compounds far more than
3 hours once a week. Block the time in your calendar. Don't break the streak — even on weekends,
even when busy. The single most important variable is consistency.
</div>
""",
    },
]
