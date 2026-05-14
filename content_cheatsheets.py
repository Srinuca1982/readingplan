"""One-page cheat sheets — focused, printable, desk-reference."""

CHEATSHEETS = [
    {
        "slug": "amalgamation-test",
        "title": "Sec 2(1B) Amalgamation — The Three-Condition Test",
        "summary": "Quick decision card: does your transaction qualify as a tax-neutral amalgamation?",
        "body": """
<h2>The three conditions — ALL must be met</h2>
<table>
  <thead><tr><th>#</th><th>Condition</th><th>Common breach</th></tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td><strong>All property</strong> of amalgamating co. becomes property of amalgamated co.</td>
      <td>Retaining a brand IP or a key contract with the amalgamating co.</td>
    </tr>
    <tr>
      <td>2</td>
      <td><strong>All liabilities</strong> of amalgamating co. become liabilities of amalgamated co.</td>
      <td>Carving out a contingent liability or a disputed tax demand.</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Shareholders holding <strong>≥ 3/4 in value</strong> of shares of amalgamating co. (other than shares held by amalgamated co.) become shareholders of amalgamated co.</td>
      <td>Cashing out minority shareholders pre-amalgamation; insufficient continuity.</td>
    </tr>
  </tbody>
</table>

<div class="callout">
<strong>Drafting test.</strong> If your scheme uses the words "except for", "save and except", or
"other than" when describing the property or liabilities transferred, you have a Condition-1 or
Condition-2 problem. Fix the scheme before filing.
</div>

<h2>The downstream tax benefits that depend on Sec 2(1B)</h2>
<ul>
  <li><span class="sec">Sec 47(vi)</span> — transfer of capital asset is not regarded as a transfer.</li>
  <li><span class="sec">Sec 47(vii)</span> — issue of shares in lieu of amalgamating-co shares is not regarded as a transfer.</li>
  <li><span class="sec">Sec 49(2)</span> — cost of acquisition in the amalgamated co. is the cost in the amalgamating co.</li>
  <li><span class="sec">Sec 72A</span> — carry forward of losses and unabsorbed depreciation (subject to additional industrial-undertaking conditions).</li>
</ul>

<h2>Pre-filing checklist</h2>
<ol>
  <li>Schedule of all assets and liabilities at the appointed date — confirm comprehensiveness.</li>
  <li>Shareholder roll on appointed date — compute the 3/4-by-value continuity.</li>
  <li>List of "carve-outs" — there should be none. If any are commercially needed, restructure as two-step transaction.</li>
  <li>Industrial-undertaking analysis for Sec 72A loss carry-forward (separate test).</li>
  <li>Sec 47A risk register — to monitor 8-year post-merger compliance.</li>
</ol>
""",
    },

    {
        "slug": "demerger-test",
        "title": "Sec 2(19AA) Demerger — The Five-Condition Test",
        "summary": "The most-litigated definition. Each condition independently kills tax neutrality.",
        "body": """
<h2>The five conditions — ALL must be met</h2>
<table>
  <thead><tr><th>#</th><th>Condition</th><th>What it means</th></tr></thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>All <strong>property</strong> of the undertaking transfers to resulting co.</td>
      <td>The "undertaking" must be a self-contained business; nothing related to it can stay back.</td>
    </tr>
    <tr>
      <td>2</td>
      <td>All <strong>liabilities relatable to the undertaking</strong> transfer to resulting co.</td>
      <td>Direct-relatability test. Common liabilities apportioned on a reasonable basis (typically asset ratio).</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Property and liabilities transfer <strong>at values appearing in the books</strong> (without revaluation).</td>
      <td>No mark-to-market; reversal of upward revaluation is acceptable.</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Resulting co. <strong>issues shares to demerged-co shareholders on a proportionate basis</strong>, except where resulting co. is already a shareholder of demerged co.</td>
      <td>Pro-rata only. Cannot issue to a subset of shareholders or in non-proportionate ratios.</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Shareholders holding <strong>≥ 3/4 in value</strong> of shares of demerged co. become shareholders of resulting co.</td>
      <td>Shareholder-continuity test.</td>
    </tr>
  </tbody>
</table>

<h2>Bonus conditions tucked away in the definition</h2>
<ul>
  <li>Transfer must be on a <strong>going-concern basis</strong> (Condition (iv) of the explanation to Sec 2(19AA)).</li>
  <li>The "undertaking" must include <strong>all assets and liabilities</strong> of that business unit; the explanation defines undertaking as "any part of an undertaking, or a unit or division".</li>
  <li>The CBDT has clarified that a single business activity cannot be split — must transfer as a whole.</li>
</ul>

<div class="callout">
<strong>Quick diagnostic.</strong> Demergers fail Sec 2(19AA) most often because of (a) Condition 1
— a non-relatable asset gets transferred or a relatable asset is retained, or (b) Condition 4 —
shares issued in a non-proportionate ratio (e.g., promoters get more). Both are scheme-drafting
issues, fixable at planning stage.
</div>

<h2>Downstream tax effects</h2>
<ul>
  <li><span class="sec">Sec 47(vib)</span> — capital-gains exemption for transferring co.</li>
  <li><span class="sec">Sec 47(vid)</span> — exemption for shareholders receiving resulting-co shares.</li>
  <li><span class="sec">Sec 49(2C) / (2D)</span> — cost-allocation between demerged-co and resulting-co shares.</li>
  <li><span class="sec">Sec 72A(4)</span> — proportionate loss carry-forward to resulting co.</li>
  <li><strong>SEBI Reg. 37</strong> — pre-NCLT approval for listed demerged co.</li>
</ul>

<h2>Cost-allocation formula — Sec 49(2C)</h2>
<blockquote>
Cost of acquisition of resulting-co shares to shareholder<br>
= Cost of original demerged-co shares ×<br>
  (Net book value of assets transferred to resulting co.) ÷ (Net worth of demerged co. before demerger)
</blockquote>
<p>The balance is the cost of remaining demerged-co shares — Sec 49(2D).</p>
""",
    },

    {
        "slug": "fast-track",
        "title": "Sec 233 Fast-Track Merger — Eligibility & Procedure",
        "summary": "3–4 month merger route via RD, bypassing NCLT entirely.",
        "body": """
<h2>Who is eligible (Sec 233(1) read with Rule 25 of CAA Rules 2016)</h2>
<ul>
  <li>Two or more <strong>small companies</strong> (paid-up capital ≤ ₹4 cr AND turnover ≤ ₹40 cr).</li>
  <li>A <strong>holding company and its wholly-owned subsidiary</strong> (any size).</li>
  <li>Two or more <strong>start-up companies</strong> (DPIIT-recognised).</li>
  <li>A <strong>start-up company and a small company</strong>.</li>
  <li>Per MCA notification September 2024: also extended to certain <strong>unlisted public companies</strong> meeting prescribed thresholds, and to <strong>inbound cross-border</strong> fast-track mergers between a foreign WOS and its Indian holding.</li>
</ul>

<h2>Procedure</h2>
<ol>
  <li><strong>Board resolution</strong> in both companies approving the scheme.</li>
  <li><strong>Notice (Form CAA-9)</strong> inviting objections from ROC, OL and persons affected, with the proposed scheme. Time given: 30 days.</li>
  <li><strong>Declaration of solvency (Form CAA-10)</strong> by each company.</li>
  <li><strong>General meeting</strong>: approval by members representing <strong>90% of total shares</strong>.</li>
  <li><strong>Meeting of creditors</strong>: approval by <strong>creditors representing 9/10 in value</strong> of total debts. (May be dispensed with by written consent.)</li>
  <li><strong>Filing of scheme (Form CAA-11)</strong> with the Regional Director via the ROC, accompanied by the company's solvency declaration, creditor consents, and the scheme.</li>
  <li>If RD has no objections — or if objections received are not substantive — RD passes order confirming the scheme (Form CAA-12).</li>
  <li>If RD has reservations, the matter is transferred to NCLT — at which point the standard Sec 230–232 procedure resumes.</li>
  <li>Order filed with ROC; the transferor stands dissolved.</li>
</ol>

<h2>What can the RD examine?</h2>
<ul>
  <li>Whether the eligibility conditions of Sec 233(1) are met.</li>
  <li>Whether the scheme is in the public interest.</li>
  <li>Whether the prescribed meetings/consents have been duly held.</li>
  <li>Whether the accounting treatment is in accordance with applicable accounting standards.</li>
  <li>Tax department, sectoral regulator and other government departments may file objections.</li>
</ul>

<div class="callout">
<strong>Time vs cost.</strong> A Sec 233 merger typically takes 3–4 months end-to-end at a fraction
of the cost of a Sec 230 scheme. The trade-off: lower threshold for the 90% members / 9/10 creditors
consent, and inability to use Sec 233 if creditor universe is too dispersed or one major creditor objects.
</div>

<h2>Tax treatment</h2>
<p>Identical to a regular Sec 230–232 amalgamation — Sec 2(1B), 47(vi)/(vii), 49(2), 72A all apply
provided their independent conditions are met. The RD-route mechanism does not give any tax
preference; it only saves time on the corporate-law side.</p>
""",
    },

    {
        "slug": "cross-border-checklist",
        "title": "Sec 234 Cross-Border Merger — Jurisdiction & Procedure Checklist",
        "summary": "Compliance map across Companies Act, FEMA, NDI/ODI, and tax.",
        "body": """
<h2>Phase 1 — Eligibility</h2>
<ul>
  <li>Foreign company must be incorporated in a <strong>notified jurisdiction</strong> under Rule 25A:
    <ul>
      <li>FATF / IOSCO MMoU member country, OR</li>
      <li>Country with a bilateral arrangement with India.</li>
    </ul>
  </li>
  <li>No prohibition on the sectoral activity of the merging Indian entity (FDI sectoral cap test).</li>
  <li><strong>PN3 screening</strong> — check beneficial ownership for neighbouring-country exposure.</li>
  <li>If parties are listed, SEBI LODR Reg. 37 prior approval required.</li>
</ul>

<h2>Phase 2 — Corporate law</h2>
<ol>
  <li>Board approvals in both companies.</li>
  <li>Valuation report by an independent valuer (internationally recognised, where the foreign entity is involved).</li>
  <li>NCLT petition under Sec 230–232 read with Sec 234 and Rule 25A.</li>
  <li>Meetings of creditors and members (or dispensation order).</li>
  <li>Sanction order from NCLT, with the scheme.</li>
  <li>Filing with ROC; in case of outbound, also with the foreign-jurisdiction authority.</li>
</ol>

<h2>Phase 3 — FEMA (Cross Border Merger Regulations 2018)</h2>
<ul>
  <li><strong>Compliance certificate</strong> — by managing director / WTD / company secretary, certifying compliance with the regulations.</li>
  <li><strong>For inbound</strong>: share issuance to non-resident shareholders → NDI Rules 2019 pricing → FC-GPR within 30 days.</li>
  <li><strong>For outbound</strong>: Indian shareholders receive foreign company shares → ODI Rules 2022 → Form FC + APR.</li>
  <li><strong>2-year window</strong>: dispose of or make compliant any non-FEMA-compliant asset, borrowing or guarantee that comes through the merger.</li>
</ul>

<h2>Phase 4 — Tax</h2>
<ul>
  <li><strong>Sec 47(via)</strong> — amalgamation of foreign co. into Indian co. (inbound): exempt if conditions met.</li>
  <li><strong>Sec 47(vic)</strong> — demerger of foreign co.: exempt if conditions met.</li>
  <li><strong>Sec 47(vicc)</strong> — amalgamation/demerger of two foreign cos. holding shares in Indian co.: exempt subject to ≥ 25% shareholder continuity in the new foreign holding.</li>
  <li><strong>Sec 9(1)(i)</strong> — indirect transfer: even with corporate-law cross-border merger, the indirect-transfer charge can apply to gains on Indian assets unless Sec 47 carve-out applies.</li>
  <li><strong>GAAR</strong> — substance test on the merger's business rationale.</li>
</ul>

<h2>Phase 5 — Other clearances</h2>
<ul>
  <li><strong>CCI approval</strong> if combination thresholds (Sec 5) crossed.</li>
  <li><strong>SEBI</strong> for listed entities — Reg. 37 and Master Circular on Schemes.</li>
  <li><strong>Sectoral regulator</strong> — RBI for banking/NBFC, IRDAI for insurance, etc.</li>
  <li><strong>Foreign-jurisdiction filings</strong> — to be coordinated with foreign counsel.</li>
</ul>

<h2>Common pitfalls</h2>
<ol>
  <li>Treating FEMA compliance as "to be done after NCLT". The compliance certificate must be ready at NCLT-petition stage.</li>
  <li>Forgetting PN3 — Chinese ultimate ownership through Mauritius/Singapore is the most common trap.</li>
  <li>Inheriting overseas non-compliant ECBs through inbound merger; 2-year cleanup window can be tight.</li>
  <li>Ignoring Sec 9(1)(i) indirect-transfer charge even when Sec 47 exemption applies to the merger itself.</li>
</ol>
""",
    },

    {
        "slug": "slump-sale-flow",
        "title": "Sec 50B Slump Sale — Tax Computation Flow",
        "summary": "Step-by-step from lump-sum consideration to taxable capital gain.",
        "body": """
<h2>Pre-test — is it actually a "slump sale"?</h2>
<p>Per Sec 2(42C), four ingredients must coexist:</p>
<ol>
  <li>Transfer of <strong>an undertaking</strong> — i.e., a unit or division capable of being carried on as a separate business.</li>
  <li>By way of <strong>sale</strong> — not exchange, gift, or compulsory acquisition.</li>
  <li>For a <strong>lump-sum consideration</strong> — no value assigned to individual assets.</li>
  <li>Transfer is on a <strong>going-concern basis</strong>.</li>
</ol>
<p>Fail any one and Sec 50B does not apply. The transaction is then taxed as itemised sale —
individual asset-wise capital gains/business income.</p>

<h2>Step 1 — Sale consideration</h2>
<p>The lump-sum consideration received. From AY 2022–23, if the lump sum is less than FMV of the
undertaking under <strong>Rule 11UAE</strong>, the higher value is deemed the sale consideration.</p>

<h2>Step 2 — Compute net worth</h2>
<blockquote>
<strong>Net worth</strong> = aggregate value of total assets of the undertaking − value of liabilities,
appearing in the books of account.
</blockquote>
<p>Adjustments to "aggregate value of total assets":</p>
<ul>
  <li><strong>Depreciable assets</strong> — WDV under Sec 43(6) of the block.</li>
  <li><strong>Capital assets on which 100% deduction allowed</strong> under Sec 35AD — value taken as nil.</li>
  <li><strong>Other assets</strong> — book value (no revaluation effect).</li>
  <li><strong>Self-generated goodwill</strong> — explicitly excluded from net worth (post-FY 2020–21).</li>
</ul>

<h2>Step 3 — Capital gain</h2>
<blockquote>
<strong>Capital gain</strong> = Sale consideration (step 1) − Net worth (step 2)
</blockquote>

<h2>Step 4 — Long-term vs short-term</h2>
<ul>
  <li>If the undertaking is held for <strong>more than 36 months</strong> — long-term capital gain.</li>
  <li>Otherwise — short-term.</li>
  <li><strong>Critical:</strong> indexation benefit is <em>not</em> available for slump-sale long-term gain.</li>
  <li>Long-term gain taxed at <strong>20% + surcharge + cess</strong>; short-term at the company's normal rate.</li>
</ul>

<h2>Step 5 — Compliance</h2>
<ul>
  <li><strong>Form 3CEA</strong> — report by an accountant indicating computation of net worth — to be filed before the due date of return.</li>
  <li>Disclosure in the return of income.</li>
  <li>Where the transferee is a non-resident, Sec 50CA + Sec 56(2)(x) overlay may apply on the share-side if shares are part-consideration.</li>
</ul>

<h2>Worked example</h2>
<table>
  <thead><tr><th>Item</th><th>Amount (₹ cr)</th></tr></thead>
  <tbody>
    <tr><td>Lump-sum consideration received</td><td>500</td></tr>
    <tr><td>FMV under Rule 11UAE</td><td>460</td></tr>
    <tr><td>Sale consideration (higher)</td><td><strong>500</strong></td></tr>
    <tr><td>Aggregate book value of assets</td><td>700</td></tr>
    <tr><td>Less: Liabilities</td><td>400</td></tr>
    <tr><td>Net worth</td><td><strong>300</strong></td></tr>
    <tr><td>Capital gain (long-term)</td><td><strong>200</strong></td></tr>
    <tr><td>Tax @ 20% + surcharge/cess (~23.3%)</td><td><strong>~46.6</strong></td></tr>
  </tbody>
</table>

<div class="callout">
<strong>Watch for.</strong> If self-generated goodwill or revalued assets sit in the balance sheet,
they don't count in net worth. The net worth will be lower than the carrying balance-sheet number,
and the taxable gain higher. Reconcile before pricing the transaction.
</div>
""",
    },

    {
        "slug": "buyback-procedure",
        "title": "Sec 68 Buyback — Procedure Step-by-Step",
        "summary": "Limits, sources, voting, filings — and the October 2024 tax shift.",
        "body": """
<h2>Step 1 — Eligibility & limits</h2>
<ul>
  <li>Articles must authorise the buyback.</li>
  <li>Authorised by board resolution alone if buyback ≤ <strong>10%</strong> of paid-up equity + free reserves.</li>
  <li>Special resolution required if &gt; 10% but ≤ <strong>25%</strong> of paid-up equity + free reserves.</li>
  <li>Within the 25% cap, equity-share buyback in an FY cannot exceed 25% of total paid-up equity capital.</li>
  <li>Debt-to-equity ratio post-buyback ≤ <strong>2:1</strong>.</li>
  <li>Minimum <strong>1 year gap</strong> between two buybacks (Sec 68(2)(d)).</li>
  <li>All shares to be bought back must be <strong>fully paid up</strong>.</li>
</ul>

<h2>Step 2 — Sources of funds (Sec 68(1))</h2>
<ul>
  <li>Free reserves.</li>
  <li>Securities premium account.</li>
  <li>Proceeds of fresh issue of <em>different</em> kind of shares/securities.</li>
  <li>Not permissible: proceeds of an earlier issue of the same kind of shares.</li>
</ul>

<h2>Step 3 — Procedure</h2>
<ol>
  <li>Board meeting — approve buyback; appoint merchant banker (if listed) or determine method (if unlisted).</li>
  <li>If special resolution required → notice + EGM/AGM.</li>
  <li>Declaration of solvency (Form SH-9) — signed by ≥ 2 directors including MD; states that the company is capable of meeting its liabilities post-buyback.</li>
  <li>For listed company: public announcement; SEBI Buyback Regulations 2018 procedure.</li>
  <li>For unlisted company: offer letter to shareholders (Form SH-8); time for acceptance not less than 15 and not more than 30 days.</li>
  <li>Open separate bank account; pay consideration only out of that account.</li>
  <li>Extinguish certificates of shares within 7 days of buyback.</li>
  <li>File Form SH-11 (return of buyback) with ROC within 30 days of completion.</li>
  <li>Maintain register of shares bought back in Form SH-10.</li>
</ol>

<h2>Step 4 — Tax (post-1 October 2024)</h2>

<table>
  <thead><tr><th>Period</th><th>Tax in company</th><th>Tax in shareholder</th></tr></thead>
  <tbody>
    <tr>
      <td>Up to 30 Sep 2024</td>
      <td>20% buyback tax under Sec 115QA (+ surcharge & cess)</td>
      <td>Exempt under Sec 10(34A)</td>
    </tr>
    <tr>
      <td>1 Oct 2024 onwards</td>
      <td>No buyback tax</td>
      <td>Buyback consideration taxed as <strong>deemed dividend under Sec 2(22)</strong>; TDS under Sec 194; slab rate applies</td>
    </tr>
  </tbody>
</table>

<div class="callout">
<strong>Post-October 2024 economics.</strong> Buyback as a cash-return mechanism is now generally
inferior to dividend for non-promoter shareholders (no rate differential), and broadly equivalent for
promoter shareholders (slab rate either way). The case for buyback now rests on signalling, EPS
mechanics, and the capital-loss available on extinguishment of shares — not on tax savings.
</div>

<h2>SEBI Buyback Regulations 2018 (for listed companies)</h2>
<ul>
  <li>Two routes: <strong>tender offer</strong> (open to all shareholders, proportionate acceptance) or <strong>open market</strong> (stock exchange or book-building).</li>
  <li>Reservation for small shareholders (15%) in tender offers.</li>
  <li>Maximum buyback price disclosed up-front.</li>
  <li>Cooling period and reporting framework.</li>
</ul>

<h2>Common pitfalls</h2>
<ol>
  <li>Promoter cannot use buyback proceeds to subscribe to a fresh issue of the same kind of shares — circular flow prohibited.</li>
  <li>Buyback cannot be funded by borrowed money (only free reserves / SP / fresh issue of different securities).</li>
  <li>Post-buyback debt-equity ratio breach — board must verify projected balance sheet, not just historical.</li>
  <li>Open-offer trigger under SAST if promoter's percentage increases beyond 25% post-buyback (creeping acquisition).</li>
</ol>
""",
    },
]
