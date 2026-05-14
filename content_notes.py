"""Topic-wise study notes. Each note is a standalone HTML body."""

NOTES = [
    {
        "slug": "companies-schemes",
        "title": "Companies Act — Schemes of Arrangement (Sec 230–232)",
        "summary": "The procedural backbone of every NCLT-sanctioned restructuring.",
        "body": """
<h2>The three sections at a glance</h2>
<ul>
  <li><span class="sec">Sec 230</span> — Compromise or arrangement with creditors and/or members. This is the parent enabling section: any reorganisation that involves classes of creditors/members goes through here.</li>
  <li><span class="sec">Sec 231</span> — Tribunal's powers to enforce the compromise/arrangement; supervise implementation; modify if needed.</li>
  <li><span class="sec">Sec 232</span> — Specific provisions for mergers and amalgamations, including treatment of property, contracts, employees and accounting.</li>
</ul>

<h2>The Sec 230 procedure</h2>
<ol>
  <li><strong>Board approval</strong> of the scheme.</li>
  <li><strong>Application to NCLT</strong> by the company, creditor, member or liquidator. Disclosures required under Rule 6, CAA Rules 2016 — material facts, latest auditor's report, investigation reports, the auditor's certificate on accounting treatment under Ind AS 103 or AS 14.</li>
  <li><strong>Meetings of classes</strong> of creditors and members — convened pursuant to NCLT directions. Approval threshold: <strong>majority in number representing three-fourths in value</strong> of each class present and voting (Sec 230(6)).</li>
  <li><strong>Sanction petition</strong> back to NCLT after meetings. The order is binding on the company, all creditors, members and the liquidator.</li>
  <li><strong>Filing with ROC</strong> within 30 days of the order.</li>
</ol>

<h2>Sec 232 — the merger specifics</h2>
<p>Section 232 layers additional requirements on top of Sec 230 for mergers and amalgamations:</p>
<ul>
  <li>Mandatory documents under <strong>Sec 232(2)</strong>: draft scheme, valuation report by a registered valuer, explanatory statement, latest auditor's report on the books of the transferor.</li>
  <li><strong>Accounting treatment</strong> under <strong>Sec 232(3)(i)</strong>: scheme must conform to accounting standards under Sec 133. Departure invites tribunal's adverse comment.</li>
  <li><strong>Statutory authorities</strong> are entitled to make representations: Central Government (via RD/ROC), Income-tax authorities, RBI, SEBI, CCI, sectoral regulators. Most schemes are decided on the back of the RD/ROC report.</li>
  <li><strong>Appointed date logic</strong> — Sec 232(6): the scheme takes effect from the date specified, which may be a date earlier than the order date. The MCA circular dated 21 August 2019 clarifies that appointed date should generally not be more than 12 months before the date of filing.</li>
</ul>

<h2>CAA Rules 2016 — what to memorise</h2>
<ul>
  <li><strong>Rule 6</strong> — application format; disclosures required in the explanatory statement under Sec 230(3).</li>
  <li><strong>Rule 8</strong> — notice of meeting; advertisement requirements (newspapers, website).</li>
  <li><strong>Rule 15</strong> — petition for sanction after meetings.</li>
  <li><strong>Rule 25</strong> — the fast-track procedure under Sec 233.</li>
  <li><strong>Rule 25A</strong> — cross-border mergers under Sec 234.</li>
</ul>

<div class="callout">
<strong>Drafting tip.</strong> The single best predictor of a sanctioned scheme is the quality of the
explanatory statement. It must cover: business rationale, valuation methodology, share exchange ratio
fairness, treatment of employees, treatment of any pending litigation, and the effect on minority
shareholders. Tribunals routinely reject schemes for thin explanatory statements.
</div>

<h2>What tribunals look for — the rejection grounds</h2>
<ol>
  <li><strong>Undervaluation</strong> — the share exchange ratio favours the dominant shareholder.</li>
  <li><strong>Oppression of minority</strong> — minority shareholders disadvantaged without commensurate benefit.</li>
  <li><strong>Tax avoidance dressed up as commercial</strong> — see <em>Vodafone Essar / In re Sun Pharmaceutical</em> line of reasoning.</li>
  <li><strong>Non-disclosure</strong> of related-party transactions, pending litigation, or material liabilities.</li>
  <li><strong>Wrong appointed date</strong> — too far in the past without justification, or where it conflicts with the FY of audit.</li>
</ol>

<h2>The order — what it does</h2>
<p>The NCLT order under Sec 232 produces, by operation of law, the following effects from the appointed date:</p>
<ul>
  <li>Transfer of <strong>all property, rights and powers</strong> of the transferor to the transferee.</li>
  <li>Transfer of <strong>all liabilities and duties</strong> of the transferor to the transferee.</li>
  <li><strong>Pending legal proceedings</strong> continue against the transferee.</li>
  <li>The <strong>transferor stands dissolved</strong> without winding-up.</li>
  <li>The order is registered with the ROC, who strikes off the transferor.</li>
</ul>
""",
    },

    {
        "slug": "companies-special-routes",
        "title": "Companies Act — Special Routes (Sec 66, 68, 233, 234)",
        "summary": "Capital reduction, buyback, fast-track, and cross-border — the routes outside the standard Sec 230–232 scheme.",
        "body": """
<h2>Sec 66 — Capital reduction</h2>
<p>The legal procedure to reduce paid-up share capital. Common uses: write off accumulated losses
against capital (paper exercise), return surplus capital to shareholders (cash payout), or cancel
shares not represented by available assets.</p>
<ul>
  <li>Special resolution required.</li>
  <li><strong>NCLT approval</strong> mandatory — the tribunal must be satisfied that creditors consent or are secured.</li>
  <li>Creditor protection: representative creditors list to be filed; objections heard.</li>
  <li>Order delivered to ROC; the reduction takes effect on registration.</li>
  <li>Tax: if reduction involves return of accumulated profits to shareholders, treated as <strong>deemed dividend under Sec 2(22)(d)</strong> to that extent (Anarkali Sarabhai principle).</li>
</ul>

<h2>Sec 68–70 — Buyback</h2>
<p>The company purchases its own shares from existing shareholders, thereby reducing capital. Faster
than Sec 66 because no NCLT — only a board / shareholder approval and SH-7/SH-9 filings.</p>

<h3>Sources of funds (Sec 68(1))</h3>
<ul>
  <li>Free reserves.</li>
  <li>Securities premium account.</li>
  <li>Proceeds of any shares or other specified securities — but <em>not</em> from the proceeds of an earlier issue of the same kind of shares.</li>
</ul>

<h3>Quantitative limits</h3>
<ul>
  <li><strong>10% of paid-up equity + free reserves</strong> — buyback authorised by board resolution.</li>
  <li><strong>25% of paid-up equity + free reserves</strong> — buyback authorised by special resolution. Within this, buyback of equity in any FY cannot exceed 25% of total paid-up equity.</li>
  <li><strong>Debt-to-equity ratio</strong> post-buyback cannot exceed 2:1.</li>
  <li><strong>Cooling period</strong> of one year between two buybacks (Sec 68(2)(d)).</li>
</ul>

<h3>Section 67 prohibition</h3>
<p>A company cannot give financial assistance for purchase of its own shares, except in limited
employee-stock-scheme cases. Read alongside Sec 68 to avoid back-door buybacks.</p>

<h3>Tax shift — post-October 2024</h3>
<div class="callout">
<strong>Important.</strong> Until 30 September 2024, buyback was taxed at the <em>company</em> level
at 20%+ under <span class="sec">Sec 115QA</span>. From 1 October 2024, the buyback consideration is
taxed in the hands of the <em>shareholder</em> as a deemed dividend. This fundamentally changes the
post-tax economics — tax neutrality for buyback as a return route is gone for most shareholders.
</div>

<h2>Sec 233 — Fast-track merger</h2>
<p>A streamlined route that bypasses the NCLT entirely. Goes to the <strong>Regional Director (RD)</strong> via the ROC.</p>

<h3>Eligibility (Sec 233(1) read with Rule 25)</h3>
<ul>
  <li>Two or more <strong>small companies</strong>.</li>
  <li>A <strong>holding company and its wholly-owned subsidiary (WOS)</strong>.</li>
  <li><strong>Two or more start-up companies</strong> (post the Feb 2021 amendment).</li>
  <li>A <strong>start-up + a small company</strong>.</li>
  <li>Effective from <strong>September 2024 (MCA notification)</strong> — also extended to certain unlisted public companies meeting prescribed thresholds, and to inbound cross-border mergers within the fast-track ambit.</li>
</ul>

<h3>Procedure</h3>
<ol>
  <li>Both companies issue notice of the scheme to ROC, OL and persons affected; objections invited.</li>
  <li>Both companies hold meetings — <strong>90% of total shares</strong> approval from members; <strong>9/10 in value</strong> approval from creditors.</li>
  <li>Scheme filed with RD via ROC.</li>
  <li>If RD finds no objection (or objections are not substantive), order is passed registering the scheme.</li>
  <li>Order filed with ROC; transferor stands dissolved.</li>
</ol>

<p><strong>Why it matters:</strong> 3–4 months end-to-end vs 12–18 months for a Sec 230–232 scheme. Cost is significantly lower.</p>

<h2>Sec 234 — Cross-border merger</h2>
<p>Permits a foreign company to merge into an Indian company (inbound) or vice versa (outbound), but only with companies in <strong>notified jurisdictions</strong> — generally FATF-compliant countries with whom India has bilateral arrangements.</p>

<h3>Procedure (Rule 25A)</h3>
<ol>
  <li><strong>Prior approval of RBI</strong> is required — though in practice this works through the FEMA Cross Border Merger Regulations 2018 (deemed approval if compliant).</li>
  <li>The Indian company files the scheme with NCLT.</li>
  <li>Valuation report by an internationally recognised valuer where the foreign entity is involved.</li>
  <li>The Sec 230–232 procedural overlay applies — creditor/member meetings, sanction order.</li>
</ol>

<div class="callout">
<strong>Watch for.</strong> Cross-border mergers also need to clear sectoral FDI/ODI rules,
PN3 (neighbouring country) checks, and the 2-year FEMA window to dispose of non-compliant assets.
The Companies Act route is necessary but never sufficient.
</div>
""",
    },

    {
        "slug": "tax-amalgamation-demerger",
        "title": "Income-tax — Amalgamation & Demerger",
        "summary": "Sec 2(1B), 2(19AA), 47, 49, 72A — the tax-neutrality engine of corporate restructuring.",
        "body": """
<h2>Sec 2(1B) — Definition of amalgamation</h2>
<p>For amalgamation to be tax-neutral, three cumulative conditions in Sec 2(1B) must be met:</p>
<ol>
  <li><strong>All the property</strong> of the amalgamating company immediately before amalgamation becomes the property of the amalgamated company.</li>
  <li><strong>All the liabilities</strong> of the amalgamating company immediately before amalgamation become the liabilities of the amalgamated company.</li>
  <li><strong>Shareholders holding ≥ 3/4 in value</strong> of the shares of the amalgamating company (other than shares already held by the amalgamated company or its nominee/subsidiary) become shareholders of the amalgamated company by virtue of the amalgamation.</li>
</ol>

<h2>Sec 2(19AA) — Definition of demerger</h2>
<p>For demerger to be tax-neutral, five cumulative conditions must be met:</p>
<ol>
  <li><strong>All the property</strong> of the undertaking transfers from the demerged company to the resulting company on a going-concern basis.</li>
  <li><strong>All the liabilities</strong> relatable to the undertaking transfer from the demerged company to the resulting company.</li>
  <li>Property and liabilities transfer <strong>at values appearing in the books of account</strong> (no revaluation adjustment, except reversal of upward revaluation).</li>
  <li>The resulting company <strong>issues its shares to the shareholders of the demerged company on a proportionate basis</strong>, except where the resulting company itself is a shareholder of the demerged company.</li>
  <li>Shareholders holding <strong>≥ 3/4 in value</strong> of shares of the demerged company become shareholders of the resulting company.</li>
</ol>

<div class="callout">
<strong>Critical.</strong> Failing any one condition kills the tax neutrality of the entire transaction.
The five-condition test of Sec 2(19AA) is the single most-litigated definition in restructuring tax law.
</div>

<h2>Sec 47 — The exemption</h2>
<h3>Amalgamation</h3>
<ul>
  <li><span class="sec">Sec 47(vi)</span> — transfer of capital asset by amalgamating company to amalgamated company (Indian company) is not regarded as transfer.</li>
  <li><span class="sec">Sec 47(vii)</span> — transfer of shares in amalgamating company by shareholder in consideration of allotment of shares in amalgamated company is not regarded as transfer.</li>
</ul>

<h3>Demerger</h3>
<ul>
  <li><span class="sec">Sec 47(vib)</span> — transfer of capital asset by demerged company to resulting company (Indian company) is not regarded as transfer.</li>
  <li><span class="sec">Sec 47(vid)</span> — issue of shares of resulting company to shareholders of demerged company is not regarded as transfer.</li>
</ul>

<h3>Cross-border</h3>
<ul>
  <li><span class="sec">Sec 47(via)</span>, <span class="sec">(vic)</span>, <span class="sec">(vicc)</span> — exemptions for amalgamation/demerger involving foreign companies, subject to conditions on continuity of business and shareholding.</li>
</ul>

<h2>Sec 49 — Cost of acquisition for the successor</h2>
<ul>
  <li><span class="sec">Sec 49(2)</span> — In hands of the amalgamated company, cost of asset = cost in hands of amalgamating company.</li>
  <li><span class="sec">Sec 49(2C)</span> — Cost of shares of resulting company in shareholder's hands = cost of original shares × (net book value of assets transferred ÷ net worth of demerged company before demerger).</li>
  <li><span class="sec">Sec 49(2D)</span> — Cost of shares of demerged company post-demerger = original cost reduced by the cost allocated to resulting company under Sec 49(2C).</li>
</ul>

<h2>Sec 72A — Carry-forward of losses on amalgamation</h2>
<p>The big tax incentive. The accumulated losses and unabsorbed depreciation of the amalgamating
company are deemed to be those of the amalgamated company — provided strict conditions are met:</p>

<h3>Sec 72A(1) — Amalgamation</h3>
<ul>
  <li>Amalgamation must be of an <strong>"industrial undertaking"</strong> — defined in Sec 72A(7) to include manufacturing, processing of goods, hotels (defined classes), and certain other categories. Pure service or trading is generally outside.</li>
  <li><strong>Amalgamating company conditions:</strong> must have been engaged in the industrial undertaking for ≥ 3 years; must have held ≥ 3/4 in value of its book of fixed assets for ≥ 2 years before amalgamation.</li>
  <li><strong>Amalgamated company conditions:</strong> must continue the business for ≥ 5 years; must hold ≥ 3/4 of fixed assets for ≥ 5 years; must achieve ≥ 50% of installed capacity within 4 years.</li>
</ul>

<h3>Sec 72A(4) — Demerger</h3>
<p>Accumulated losses and unabsorbed depreciation directly relatable to the demerged undertaking
transfer to the resulting company. If not directly relatable, they're apportioned in the proportion
of assets retained vs transferred.</p>

<h2>Sec 47A — Withdrawal of exemption</h2>
<p>If the conditions of Sec 47(vib) (or other relevant sub-clause) are violated within 8 years
of the transfer — e.g., resulting company transfers the undertaking — the originally exempt
transaction is reassessed and capital gains tax becomes payable in the year of breach.</p>

<div class="callout">
<strong>Audit checkpoint.</strong> Sec 47A is checked at every audit for ≥ 8 years after a
demerger. Maintain a memo file recording the post-transaction status of the transferred undertaking,
asset retention, and business continuation — for each year.
</div>

<h2>Sec 56(2)(x) — The anti-abuse overlay</h2>
<p>If shares are received without consideration, or for inadequate consideration, the difference
between FMV and consideration is taxed as "income from other sources" in the recipient's hands.
This applies to shareholders receiving shares in a demerger if the shares are issued at less than
FMV — though Sec 56(2)(x) provides exceptions for amalgamation and demerger meeting Sec 2(1B)/2(19AA).
Verify the exception applies in each fact pattern.</p>
""",
    },

    {
        "slug": "tax-slump-buyback",
        "title": "Income-tax — Slump Sale, Buyback, Capital Reduction",
        "summary": "Sec 50B, 115QA, 2(22)(d), 47A — the non-court tax routes.",
        "body": """
<h2>Sec 2(42C) + Sec 50B — Slump sale</h2>
<p><strong>Slump sale</strong> means the transfer of an undertaking, or one of multiple undertakings,
as a result of the sale, for a <em>lump sum consideration</em>, without values being assigned to
individual assets and liabilities. The transfer must be on a going-concern basis.</p>

<h3>Sec 50B — Computation of capital gain</h3>
<ul>
  <li><strong>Sale consideration</strong> = lump sum received (or, post-amendment, FMV under Rule 11UAE if higher).</li>
  <li><strong>Cost of acquisition</strong> = "net worth" of the undertaking — i.e., aggregate value of total assets reduced by value of liabilities, as appearing in the books, computed without considering revaluation.</li>
  <li><strong>Holding period</strong> — if the undertaking has been owned and held for more than 36 months, gain is long-term; the indexation benefit, however, is <em>not</em> available even for long-term slump sale.</li>
  <li>Result: <strong>Slump sale capital gain</strong> = sale consideration − net worth.</li>
</ul>

<h3>Rule 11UAE — FMV calculation</h3>
<p>FMV of an undertaking = aggregate of:</p>
<ul>
  <li><strong>FMV of capital assets</strong> (book value or stamp duty value, depending on asset class), plus</li>
  <li><strong>FMV of jewellery, archaeological collections, drawings, paintings</strong>, plus</li>
  <li><strong>FMV of unquoted shares</strong>, plus</li>
  <li><strong>Book value of other assets</strong>, less liabilities.</li>
</ul>

<p>Where consideration is less than FMV under Rule 11UAE, the higher value is deemed the sale
consideration — a key anti-abuse mechanism.</p>

<h2>Sec 50CA + Sec 56(2)(x) — Anti-abuse on unquoted shares</h2>
<p>Two layers operate together:</p>
<ul>
  <li><span class="sec">Sec 50CA</span> — if unquoted shares are sold at less than FMV (Rule 11UA), the FMV is deemed the sale consideration in the seller's hands.</li>
  <li><span class="sec">Sec 56(2)(x)</span> — the buyer is taxed on the difference between FMV and consideration as "income from other sources".</li>
</ul>
<p>The same delta is therefore taxed twice in mirror form — once on seller (deemed sale price) and once on buyer (deemed gift). This is the "double-anti-abuse" that catches sham private share transactions.</p>

<h2>Sec 115QA — Buyback tax (the regime shift)</h2>

<h3>Pre-October 2024</h3>
<p>Sec 115QA imposed buyback tax on the <em>company</em> at <strong>20% (plus surcharge and cess)</strong>
on the distributed income (buyback price minus issue price). The buyback receipt in shareholder's hands
was exempt under Sec 10(34A).</p>

<h3>Post-1 October 2024</h3>
<div class="callout">
<strong>Regime change.</strong> Section 115QA has been withdrawn for buybacks on or after 1 October
2024. The buyback consideration is now taxed in the hands of the shareholder as <em>deemed dividend</em>
under Sec 2(22), at the shareholder's applicable slab rate (subject to TDS under Sec 194). The
shareholder's cost in the bought-back shares becomes a capital loss available for set-off.
</div>

<p>This fundamentally changes the post-tax efficiency of buybacks for promoter/large shareholders.
Tender-offer buybacks that made commercial sense pre-Oct 2024 may no longer be the cheapest cash-return
route.</p>

<h2>Sec 2(22)(d) — Capital reduction as deemed dividend</h2>
<p>Distribution by a company on the reduction of its capital is deemed to be a dividend
<strong>to the extent of the accumulated profits</strong> of the company (whether capitalised or not).
This is the <strong>Anarkali Sarabhai principle</strong>: <em>Anarkali Sarabhai v. CIT (1997) 224 ITR 422 (SC)</em>.</p>

<p>Mechanics:</p>
<ul>
  <li>Distribution up to accumulated profits → taxable as dividend in shareholder's hands (slab rate post-Apr 2020).</li>
  <li>Distribution in excess of accumulated profits → return of capital, treated as capital receipt; reduces cost of acquisition of the shares (which may be exhausted or trigger capital gains if reduction exceeds cost).</li>
  <li>Where capital reduction is by way of cancellation of shares without consideration, capital loss may arise to the shareholder.</li>
</ul>

<h2>Sec 47A — Withdrawal of exemption (slump sale variant)</h2>
<p>Where an exemption under Sec 47 was claimed (e.g., for share consideration in lieu of cash in a
slump-exchange transaction), and the conditions are breached within the prescribed period
(generally 8 years), the originally exempt transaction becomes taxable retrospectively in the
year of breach.</p>

<div class="callout">
<strong>Audit pitfall.</strong> Mid-sized clients often do a slump sale, then a few years later
restructure the consideration shares. Section 47A monitoring is rarely automated. The cleanest
control is a static schedule of "exempt-transaction lock-ins" maintained at the CFO's office.
</div>

<h2>Decision matrix — non-court routes</h2>
<table>
  <thead><tr><th>Route</th><th>Tax in company</th><th>Tax in shareholder</th><th>Best when</th></tr></thead>
  <tbody>
    <tr><td>Slump sale</td><td>Capital gain on net consideration − net worth</td><td>Nil at transaction</td><td>Single buyer wants the whole undertaking; cash dominant</td></tr>
    <tr><td>Buyback (post Oct-24)</td><td>Nil under Sec 115QA</td><td>Deemed dividend; slab rate</td><td>Distributing surplus cash to shareholders directly</td></tr>
    <tr><td>Capital reduction</td><td>Nil</td><td>Sec 2(22)(d) deemed dividend to extent of accumulated profits</td><td>Cleaning up reserves; aligning capital structure</td></tr>
    <tr><td>Demerger</td><td>Exempt under Sec 47(vib) if Sec 2(19AA) met</td><td>Exempt under Sec 47(vid)</td><td>Separating businesses; preserving promoter ownership</td></tr>
  </tbody>
</table>
""",
    },

    {
        "slug": "fema-cross-border",
        "title": "FEMA — Cross-Border Merger Regulations 2018",
        "summary": "The deemed-approval framework for inbound and outbound mergers.",
        "body": """
<h2>The regulatory ladder</h2>
<p>Cross-border mergers between an Indian company and a foreign company touch three regimes
simultaneously:</p>
<ol>
  <li><strong>Companies Act Sec 234 + Rule 25A</strong> — the corporate-law route, with NCLT.</li>
  <li><strong>FEMA Cross Border Merger Regulations 2018</strong> — the foreign-exchange route, granting <em>deemed RBI approval</em> where the regulations are complied with.</li>
  <li><strong>Income-tax Sec 47(via)/(vic)/(vicc)</strong> — the tax-neutrality overlay, with its own conditions.</li>
</ol>
<p>Plus sectoral checks: PN3 (neighbouring country investors), FDI sectoral caps, listing rules,
CCI thresholds.</p>

<h2>Two flavours of cross-border merger</h2>

<h3>Inbound merger — foreign company merges into Indian company</h3>
<ul>
  <li>The Indian company is the <strong>resulting</strong> entity.</li>
  <li>Indian company may issue shares to shareholders of the foreign company; FEMA NDI Rules 2019 pricing applies.</li>
  <li>Assets and liabilities of the foreign company transfer to the Indian company. If those assets/liabilities are not FEMA-compliant for Indian holding, a 2-year window is granted to make them compliant or dispose of them.</li>
  <li><strong>Typical use case:</strong> the <em>reverse flip</em> — bringing an offshore-domiciled startup back to India in preparation for a domestic listing.</li>
</ul>

<h3>Outbound merger — Indian company merges into foreign company</h3>
<ul>
  <li>The foreign company is the resulting entity. Foreign jurisdiction must be a <strong>notified jurisdiction</strong>.</li>
  <li>Indian shareholders receive foreign-company shares; ODI Rules 2022 govern this — generally requires automatic route eligibility.</li>
  <li>The Indian company's assets become assets of the foreign company; FEMA permits this only if the transfer complies with the prevailing ODI framework.</li>
  <li><strong>Typical use case:</strong> consolidation under a foreign listed parent.</li>
</ul>

<h2>Notified jurisdictions (Annexure to Rule 25A)</h2>
<p>A foreign company is in a "notified jurisdiction" if it is incorporated in a country whose
securities regulator is a member of IOSCO MMoU, OR whose central bank is a BIS member, OR whose
country is a member of FATF — and which has a notified bilateral agreement with India. Common
examples: USA, UK, Singapore, Mauritius, Netherlands.</p>

<h2>The deemed-approval mechanism</h2>
<p>Reg. 9 of the Cross Border Merger Regulations 2018: a transaction is <strong>deemed to have RBI
approval</strong> if it complies with the regulations. The compliance is evidenced by a
<strong>certificate from the managing director / whole-time director / company secretary</strong>
of the company concerned, certifying that the regulations have been complied with. No formal RBI
approval letter is required — though RBI retains the right to inspect.</p>

<h2>The 2-year compliance window</h2>
<p>Reg. 7: if, after the merger, the resulting company holds any asset, security or
borrowing that is not FEMA-compliant (e.g., overseas direct investment outside the ODI permissible
limits, or borrowings outside the ECB framework), the resulting company has <strong>2 years from
the effective date</strong> to dispose of or make the asset/borrowing compliant. Income earned
during this window is to be repatriated through normal banking channels.</p>

<div class="callout">
<strong>Practical pitfall.</strong> The 2-year window is short. For an inbound merger absorbing
a foreign company that holds overseas subsidiaries or non-compliant borrowings, a clean asset list
must be prepared at due-diligence stage. Surprise non-compliant assets discovered post-merger are a
major operational headache.
</div>

<h2>Pricing</h2>
<ul>
  <li><strong>Inbound</strong>: NDI Rules 2019 pricing applies to any equity issued by the Indian company to non-resident shareholders. For unlisted Indian companies, this is DCF or NAV-based; for listed, SEBI ICDR pricing.</li>
  <li><strong>Outbound</strong>: ODI Rules 2022 pricing — fair value based on internationally accepted valuation methodology.</li>
</ul>

<h2>Reporting</h2>
<ul>
  <li><strong>Inbound merger involving share issue</strong>: FC-GPR within 30 days of share allotment.</li>
  <li><strong>Outbound merger</strong>: ODI Form (Form FC) before the merger; Annual Performance Report (APR) thereafter.</li>
  <li>The compliance certificate from the company is filed alongside the NCLT order with ROC.</li>
</ul>

<h2>Tax overlay — Sec 47(via)/(vic)/(vicc) at a glance</h2>
<ul>
  <li><span class="sec">Sec 47(via)</span> — amalgamation of foreign company into Indian company; exempt subject to conditions.</li>
  <li><span class="sec">Sec 47(vic)</span> — demerger of foreign company; exempt subject to conditions.</li>
  <li><span class="sec">Sec 47(vicc)</span> — amalgamation/demerger of two foreign companies holding shares in Indian company; exempt subject to ≥ 25% shareholder continuity.</li>
  <li><span class="sec">Sec 9(1)(i)</span> — indirect transfer provisions still apply; any transaction in foreign-company shares deriving substantial value from Indian assets remains taxable in India absent specific exemption.</li>
</ul>
""",
    },

    {
        "slug": "fema-ndi-odi",
        "title": "FEMA — NDI Rules 2019 & ODI Rules 2022",
        "summary": "The foreign-exchange overlay on every M&A with a non-resident in the structure.",
        "body": """
<h2>NDI Rules 2019 — Non-Debt Instruments</h2>
<p>The Foreign Exchange Management (Non-Debt Instruments) Rules 2019, notified by the Central
Government under FEMA, are the consolidated framework for foreign investment in Indian companies.
They replaced the earlier FDI/NDI scattering of notifications.</p>

<h3>Scope</h3>
<ul>
  <li>Equity instruments — equity shares, fully and mandatorily convertible preference shares, fully and mandatorily convertible debentures, share warrants.</li>
  <li>Investment in an LLP or an investment vehicle.</li>
  <li>Acquisition through merger/demerger/scheme of arrangement.</li>
  <li>Transfer of equity instruments between residents and non-residents.</li>
</ul>

<h3>Entry route — automatic vs government</h3>
<ul>
  <li><strong>Automatic route</strong> — no prior approval required; sectoral cap and conditions to be met; reporting after the fact.</li>
  <li><strong>Government route</strong> — prior approval through the relevant administrative ministry (FIFP, the Foreign Investment Facilitation Portal). Sectors like print media, broadcasting, defence (above 74%) etc.</li>
</ul>

<h3>Sectoral caps — examples</h3>
<table>
  <thead><tr><th>Sector</th><th>Cap</th><th>Route</th></tr></thead>
  <tbody>
    <tr><td>Manufacturing</td><td>100%</td><td>Automatic</td></tr>
    <tr><td>Insurance</td><td>74%</td><td>Automatic</td></tr>
    <tr><td>Banking — private</td><td>74%</td><td>Automatic up to 49%; Govt 49–74%</td></tr>
    <tr><td>Defence</td><td>74% / 100%</td><td>Automatic up to 74%; Govt beyond</td></tr>
    <tr><td>Telecom</td><td>100%</td><td>Automatic up to 100% post-Sept 2021</td></tr>
    <tr><td>Multi-brand retail</td><td>51%</td><td>Government</td></tr>
  </tbody>
</table>
<p>(Always verify against the consolidated FDI Policy / NDI Schedule I before relying.)</p>

<h3>Pricing guidelines</h3>
<ul>
  <li><strong>Listed company</strong> — SEBI ICDR pricing for preferential allotment; SEBI Takeover pricing for transfers above thresholds.</li>
  <li><strong>Unlisted company</strong> — fair value based on internationally accepted methodology (typically DCF or NAV) by a SEBI-registered Merchant Banker or a Chartered Accountant.</li>
  <li>For issue of shares to non-resident: price must be <strong>not less than</strong> fair value.</li>
  <li>For transfer from non-resident to resident: price must be <strong>not more than</strong> fair value.</li>
</ul>

<h3>PN3 — Press Note 3 of 2020</h3>
<div class="callout">
<strong>Government route mandatory</strong> for any investment by an entity of a country sharing a
land border with India, or where the <em>beneficial owner</em> of the investment is situated in such
a country. India's land neighbours: Bangladesh, Bhutan, China, Myanmar, Nepal, Pakistan, Afghanistan.
Beneficial-ownership tracing through multi-tier structures is required.
</div>

<h3>Key reporting forms</h3>
<ul>
  <li><strong>FC-GPR</strong> — Foreign Currency-Gross Provisional Return — within 30 days of share allotment to non-resident.</li>
  <li><strong>FC-TRS</strong> — for transfer of equity instruments between resident and non-resident; within 60 days.</li>
  <li><strong>FLA</strong> — Annual Return on Foreign Liabilities and Assets — by 15 July each year.</li>
</ul>

<h2>ODI Rules 2022 — Overseas Direct Investment</h2>
<p>The Foreign Exchange Management (Overseas Investment) Rules 2022 + Regulations 2022 + Master
Direction govern outbound investment by Indian residents.</p>

<h3>Structure of permissible ODI</h3>
<ul>
  <li><strong>ODI in foreign entity</strong> — capital contribution / equity investment in a foreign entity engaged in a bona fide business activity.</li>
  <li><strong>Financial commitment (FC)</strong> — broader: includes equity, debt, guarantee. The aggregate FC limit for an Indian party is generally <strong>400% of its net worth</strong> on a non-consolidated basis (lower for certain regulated entities).</li>
</ul>

<h3>Automatic vs approval route</h3>
<ul>
  <li><strong>Automatic route</strong> — within the FC ceiling, into bona fide business in countries other than restricted ones, and the foreign entity meets eligibility (not a shell, not a financial-services entity unless eligible).</li>
  <li><strong>Approval route</strong> — beyond the cap, in restricted countries (e.g., FATF/IOSCO non-cooperative), or for financial-services entities not eligible automatically.</li>
</ul>

<h3>Round-tripping</h3>
<p>The 2022 rules expressly permit <strong>round-tripping</strong> up to two layers — an Indian
party can invest in a foreign entity which holds an Indian subsidiary, subject to (a) bona fide
business reason, (b) two-layer cap, (c) RBI reporting. Pre-2022 the position was unclear; the 2022
rules brought welcome certainty.</p>

<h3>Reporting</h3>
<ul>
  <li><strong>Form FC</strong> — pre-investment intimation/approval.</li>
  <li><strong>APR</strong> — Annual Performance Report — by 31 December each year for every foreign entity in which ODI is held.</li>
</ul>

<div class="callout">
<strong>Reverse-flip planning.</strong> If a startup is migrating from a foreign holding back to
India (the "reverse flip"), the inbound side is governed by the Cross Border Merger Regulations 2018
+ NDI Rules 2019. The outbound exit by the founder shareholders (giving up shares of the foreign
company in exchange for Indian-company shares) must be tested against the ODI framework's exit rules.
</div>
""",
    },

    {
        "slug": "sebi-stamp-competition-gst",
        "title": "SEBI, Stamp, Competition & GST Overlays",
        "summary": "The four parallel regimes most often missed in tax-only treatment.",
        "body": """
<h2>SEBI — when does it apply?</h2>
<p>SEBI's jurisdiction is triggered if <strong>any party to the scheme is listed</strong>, or if
the scheme involves listed securities. Three regulations matter most:</p>

<h3>SAST Regulations 2011 — Takeover Code</h3>
<ul>
  <li><strong>Reg. 3(1)</strong> — acquisition of <strong>25% or more</strong> of voting rights → mandatory open offer.</li>
  <li><strong>Reg. 3(2)</strong> — creeping acquisition: a shareholder holding 25–75% acquiring more than 5% in an FY → mandatory open offer.</li>
  <li><strong>Reg. 4</strong> — <strong>change of control</strong> regardless of percentage → mandatory open offer.</li>
  <li><strong>Reg. 10</strong> — exemptions. Most relevant: <strong>Reg. 10(1)(d)(iii)</strong> — acquisition pursuant to a scheme of arrangement under Sec 230–232 is exempt, subject to conditions.</li>
</ul>

<h3>LODR Reg. 37 — Scheme approval</h3>
<p>A listed company must obtain <strong>prior approval of the stock exchanges</strong> (and, through
them, SEBI) before filing a scheme with NCLT. The application requires:</p>
<ul>
  <li>Fairness opinion from an independent SEBI-registered merchant banker on the share exchange ratio.</li>
  <li>Valuation report by an independent registered valuer.</li>
  <li>Recommendation from the audit committee and the committee of independent directors.</li>
  <li>Declaration on any pending investigations, prosecutions or unresolved SEBI/exchange matters.</li>
  <li>Compliance with the SEBI <strong>Master Circular on Schemes of Arrangement</strong>.</li>
</ul>

<h3>Master Circular on Schemes — what to remember</h3>
<ul>
  <li>If the scheme is between a listed company and its wholly-owned subsidiary (or vice versa), simplified procedure — no fairness opinion required.</li>
  <li>If the scheme involves a related party, <strong>majority of public shareholders (majority of minority)</strong> approval is required — promoters cannot vote.</li>
  <li>Post-scheme, the resulting/transferee company seeks <strong>listing</strong> of its shares; in-principle approval must be obtained before NCLT filing.</li>
</ul>

<h2>Stamp duty — State-specific, the easiest to forget</h2>
<p>Stamp duty on schemes of arrangement is governed by State-level stamp legislation, not the
central Indian Stamp Act. Each State has its own rate and basis.</p>

<table>
  <thead><tr><th>State</th><th>Basis</th><th>Typical rate (verify before relying)</th></tr></thead>
  <tbody>
    <tr><td>Maharashtra</td><td>Higher of consideration or value transferred</td><td>~10% of consideration with cap (5% on movable, 5% on immovable, cap based on FMV)</td></tr>
    <tr><td>Karnataka</td><td>Value of shares allotted + consideration paid</td><td>~3%</td></tr>
    <tr><td>Telangana / AP</td><td>Value of the property transferred</td><td>Ad valorem schedule; check the latest schedule under the AP/Telangana Stamp Act</td></tr>
    <tr><td>Delhi</td><td>NCLT order treated as conveyance; consideration-based</td><td>Ad valorem; varies</td></tr>
  </tbody>
</table>

<div class="callout">
<strong>Watch for.</strong> If immovable property in multiple States is involved, stamp duty is
payable in each State based on the property situated there. Plan the stamping sequence carefully —
some States require stamping <em>before</em> registration of the NCLT order with ROC.
</div>

<h2>Competition Act — Sections 5 and 6</h2>

<h3>Combination thresholds (Sec 5)</h3>
<p>A transaction is a "combination" requiring CCI approval if <strong>any one</strong> of the
following thresholds is crossed (Sec 5 read with Notification S.O. 988(E) dated 7 March 2024):</p>
<ul>
  <li><strong>Combined assets in India ≥ ₹2,500 cr</strong> OR <strong>combined turnover in India ≥ ₹7,500 cr</strong> (parties test); OR</li>
  <li><strong>Group-level assets ≥ ₹10,000 cr in India / ₹4 bn worldwide</strong> OR <strong>turnover ≥ ₹30,000 cr in India / ₹12 bn worldwide</strong> (group test).</li>
</ul>

<h3>Deal Value Threshold — effective September 2024</h3>
<p>A new threshold inserted by the 2023 amendment, in force from <strong>10 September 2024</strong>:
if the deal value exceeds <strong>₹2,000 crore</strong> AND the target has "substantial business
operations in India", CCI notification is required regardless of the asset/turnover thresholds.
This catches large digital/tech deals that historically slipped through.</p>

<h3>Procedure (Sec 6)</h3>
<ul>
  <li>Form I (short form) or Form II (long form) notification to CCI before consummation.</li>
  <li>Standstill obligation — parties cannot consummate until CCI approval or expiry of statutory waiting period.</li>
  <li>Approval typically within 30 working days (Phase I) or extended for Phase II investigation.</li>
  <li>Penalty for gun-jumping (consummating without approval) up to <strong>1% of combined assets or turnover</strong>.</li>
</ul>

<h3>Exemptions</h3>
<ul>
  <li><strong>De minimis</strong> — target with assets ≤ ₹450 cr OR turnover ≤ ₹1,250 cr in India (subject to revision).</li>
  <li>Intra-group acquisitions where common control of ≥ 50% pre-transaction.</li>
  <li>Acquisitions by liquidator under IBC.</li>
</ul>

<h2>GST — the unsung overlay</h2>

<h3>Schedule II + Notification 12/2017</h3>
<p>Under Schedule II of the CGST Act, certain transactions are treated as supplies. However,
<strong>transfer of a business as a going concern</strong>, in whole or independent part, is
<strong>exempt</strong> from GST under Notification 12/2017 (entry 2). Therefore most slump sales
and going-concern business transfers do not attract GST.</p>

<h3>Sec 18(3) — Transfer of ITC</h3>
<p>On amalgamation, merger, demerger, sale, lease or transfer of business with specific provision
for transfer of liabilities, the registered person can transfer unutilised ITC to the transferee/
resulting entity in Form GST ITC-02. Pro rata allocation for demerger; lump-sum for merger.</p>

<h3>Sec 87 — Transferee liability</h3>
<p>If the transferor has unpaid GST dues, the transferee is <strong>jointly and severally</strong>
liable for the dues up to the value of the property transferred. Tax due-diligence must include
unpaid GST and pending GST notices.</p>

<div class="callout">
<strong>Drafting tip.</strong> The BTA or scheme should expressly transfer all GST-related rights
(refunds receivable, ITC, registrations) and obligations (pending dues, ongoing assessments). Standard
clauses cover this; deviations create headaches at the assessment stage.
</div>
""",
    },

    {
        "slug": "ibc-restructuring",
        "title": "IBC as a Restructuring Tool",
        "summary": "Resolution plans, schemes during liquidation, and the tax treatment of write-backs.",
        "body": """
<h2>Why IBC is a restructuring statute</h2>
<p>The Insolvency and Bankruptcy Code 2016 is not just a default-and-recovery framework. Sections 30
and 31 enable the <strong>Resolution Plan</strong> — a binding restructuring of a distressed
corporate debtor that can carry out almost any commercial reorganisation: change of control,
write-off of liabilities, fresh capital infusion, demerger, asset transfer, even cancellation of
shares.</p>

<h2>Sec 30–31 — The Resolution Plan</h2>

<h3>The plan's content (Sec 30(2))</h3>
<ul>
  <li>Payment of <strong>CIRP costs</strong> in priority.</li>
  <li>Payment to <strong>operational creditors</strong> not less than the higher of (a) the amount they'd get in liquidation, (b) the amount payable if the proceeds were distributed in accordance with Sec 53.</li>
  <li>Payment to <strong>dissenting financial creditors</strong> not less than the amount payable in liquidation.</li>
  <li>Provisions for <strong>implementation</strong>, including management.</li>
</ul>

<h3>Approval (Sec 30(4) + Sec 31)</h3>
<ul>
  <li>The Committee of Creditors (CoC) approves the resolution plan by <strong>≥ 66% of voting share</strong>.</li>
  <li>The Resolution Professional submits the plan to the NCLT.</li>
  <li>If NCLT is satisfied that the plan meets all statutory requirements, it issues an order under <strong>Sec 31(1)</strong> approving the plan. The order is binding on the corporate debtor, employees, members, creditors, guarantors, and statutory authorities — including tax authorities.</li>
</ul>

<h2>The "clean slate" doctrine</h2>
<div class="callout">
<strong>Key principle.</strong> <em>Essar Steel (CoC of Essar Steel India Ltd. v. Satish Kumar Gupta — 2019 SC)</em> and a line of subsequent decisions establish that, once the resolution plan is approved, all <em>past</em> liabilities (including statutory dues) not provided for in the plan are <strong>extinguished</strong>. The successful resolution applicant takes over the corporate debtor with a clean slate, free of unknown contingent or undisclosed liabilities.
</div>
<p>This is the <strong>single most powerful</strong> restructuring feature in Indian law — and the
reason resolution plans are increasingly used by financially distressed but operationally viable
companies.</p>

<h2>Sec 230 schemes during liquidation</h2>
<p>If a corporate debtor enters liquidation under Chapter III of the IBC, the liquidator may, under
<strong>Regulation 2B of the Liquidation Process Regulations 2016</strong>, propose a Sec 230 scheme
of arrangement to revive the company instead of selling its assets piecemeal. NCLT must approve
the scheme; the standard CAA procedure applies, adapted to the liquidation context.</p>

<p>This provides a "second window" of restructuring after the CIRP has failed but before the company
is wound up. It has been used successfully in mid-sized cases where a strategic acquirer emerges
late.</p>

<h2>Tax treatment of resolution plans</h2>

<h3>Sec 79(2)(c) — Loss carry-forward relaxation</h3>
<p>Ordinarily, under Sec 79, accumulated losses cannot be carried forward if there's a change in
beneficial shareholding of more than 49%. <strong>Sec 79(2)(c)</strong> relaxes this for cases where
the change in shareholding pursuant to a resolution plan approved under Sec 31 of the IBC has taken
place. This allows the successful resolution applicant to use the corporate debtor's accumulated
losses going forward — a major economic feature of resolution-plan structures.</p>

<h3>Write-back of liabilities — capital or revenue?</h3>
<p>When the resolution plan extinguishes a portion of unsecured creditor liability, the corporate
debtor recognises a credit in the P&L. Two views exist:</p>
<ul>
  <li><strong>Revenue receipt</strong> — Sec 41(1) — if the liability arose from a trading transaction (e.g., trade payables), the remission is taxable as deemed business income.</li>
  <li><strong>Capital receipt</strong> — if the liability was capital in nature (e.g., loan from financial creditor for capex), the remission is a capital receipt not chargeable to tax.</li>
</ul>
<p>The Sec 31 order's "binding on all" language has been invoked to argue that the entire write-back
is a capital receipt — the position is being litigated; safer to provide for tax exposure in the
financial model.</p>

<h3>MAT relief — Sec 115JB</h3>
<p>For Sec 115JB MAT computation, a special carve-out exists for companies undergoing CIRP: the
book profit can be reduced by the lower of unabsorbed depreciation or business loss brought forward
— a more generous adjustment than the normal MAT formula. Verify the current FY's exact text.</p>

<h2>Stamp duty exemption</h2>
<p>Under most State stamp legislations, the transfer of property pursuant to an NCLT-approved
resolution plan is exempt from stamp duty (or charged at a nominal rate). The specific exemption
must be checked under each State's stamp schedule — Maharashtra, Karnataka, Telangana have specific
notifications; Delhi and Tamil Nadu have either explicit exemption or judicial reading-down.</p>

<div class="callout">
<strong>Drafting tip.</strong> The resolution plan should expressly state that the transfer of
assets to the resolution applicant is by operation of the NCLT order under Sec 31 of the IBC, and
invoke the State-specific stamp exemption. Generic language risks the State stamp authority charging
ad valorem.
</div>

<h2>The IBC as a M&A tool — strategic uses</h2>
<ol>
  <li><strong>Distressed acquisition</strong> — Sec 31 approval gives clean-slate ownership.</li>
  <li><strong>Liability write-off</strong> at scale — through the resolution plan.</li>
  <li><strong>Loss carry-forward preservation</strong> under Sec 79(2)(c).</li>
  <li><strong>Avoidance of regulatory consents</strong> that would otherwise be required (the Sec 31 order binds statutory authorities).</li>
  <li><strong>Stamp duty efficiency</strong> on the asset transfer.</li>
</ol>

<p>For these reasons, the resolution-plan route is sometimes <em>cheaper and faster</em> than a Sec 230 scheme
even when the company is not in genuine financial distress — though this is being scrutinised by
NCLT to prevent abuse.</p>
""",
    },
]
