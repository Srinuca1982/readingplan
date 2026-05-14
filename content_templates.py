"""Drafting templates — skeletons you can lift, paste and adapt.

Each template includes inline notes [in brackets] explaining what to fill in
and the source of the requirement. These are starting points only — always
verify against the latest law / SEBI circulars / NCLT practice.
"""

TEMPLATES = [
    {
        "slug": "scheme-explanatory-statement",
        "title": "Explanatory Statement for a Scheme of Arrangement",
        "summary": "The disclosure document accompanying the notice of meeting under Sec 230(3) — read by NCLT and dispositive in 70% of cases.",
        "body": """
<h2>Structure (CAA Rule 6 + Sec 230(3))</h2>
<p>The Explanatory Statement is the single most important document in a scheme. NCLT reads
it carefully — the quality of the statement is the strongest predictor of whether the scheme
is sanctioned cleanly. Use this skeleton, replacing the bracketed placeholders.</p>

<h2>Skeleton</h2>
<blockquote>
<h3>1. Details of the Transferor and Transferee Companies</h3>
<p>1.1 [Transferor Co. Name] (CIN: [____]), incorporated on [date] under the Companies Act
[1956/2013], having its registered office at [address]. Authorised capital: ₹[__]; paid-up:
₹[__]; main objects: [in brief, 3–4 lines from MOA].</p>

<p>1.2 [Transferee Co. Name] (CIN: [____]), incorporated on [date]... [same details].</p>

<p>1.3 Both companies are part of the [____] group. [Promoter family / parent details].</p>

<h3>2. Rationale of the Scheme</h3>
<p>The proposed Scheme is being undertaken with a view to:</p>
<ul>
  <li><strong>Operational consolidation</strong> — [describe synergies: scale, common procurement, shared management bandwidth, regulatory simplification, etc.]</li>
  <li><strong>Strategic focus</strong> — [why separating / combining serves the long-term strategy]</li>
  <li><strong>Capital-structure rationalisation</strong> — [if applicable]</li>
  <li><strong>Compliance simplification</strong> — [reducing intra-group transactions / multiple ROC filings]</li>
</ul>
<p>The Scheme is expected to result in [quantified or qualitative benefit]. <strong>It is not
intended for or expected to result in any tax benefit not otherwise available under law</strong>
[critical GAAR-deflecting language].</p>

<h3>3. Salient features of the Scheme</h3>
<p>Appointed date: [DD-MMM-YYYY] (within 12 months of filing per MCA Circular dated 21 Aug 2019).</p>
<p>Effective date: the date on which the certified copy of the NCLT order is filed with the ROC.</p>
<p>Share exchange ratio: [N] equity shares of ₹[X] each of [Transferee] for every [M] equity
shares of ₹[Y] each of [Transferor]. The ratio has been determined by [Valuer Firm Name] vide
their report dated [date] and confirmed fair by [Merchant Banker Name] vide fairness opinion
dated [date].</p>

<h3>4. Treatment of property, liabilities, contracts and employees</h3>
<p>All property, rights, powers, liabilities, duties, contracts, agreements, schemes, deeds,
licences, permits, approvals, registrations and all other interests of every kind whatsoever
of the Transferor Company shall, by operation of the order under Section 232 read with Section
230, stand transferred to and vested in the Transferee Company, without any further act or
deed.</p>
<p>Employees of the Transferor Company shall become employees of the Transferee Company on
the same terms and conditions of service, with continuity of service preserved (no break,
no fresh probation).</p>

<h3>5. Capital structure pre- and post-Scheme</h3>
<table>
  <thead><tr><th></th><th>Transferor (pre)</th><th>Transferee (pre)</th><th>Transferee (post)</th></tr></thead>
  <tbody>
    <tr><td>Authorised capital</td><td>₹[__]</td><td>₹[__]</td><td>₹[__]</td></tr>
    <tr><td>Issued capital</td><td>₹[__]</td><td>₹[__]</td><td>₹[__]</td></tr>
    <tr><td>Paid-up capital</td><td>₹[__]</td><td>₹[__]</td><td>₹[__]</td></tr>
    <tr><td>No. of equity shares</td><td>[__]</td><td>[__]</td><td>[__]</td></tr>
  </tbody>
</table>

<h3>6. Shareholding pattern pre- and post-Scheme</h3>
<p>[Promoter / public / institutional break-up for both companies before and after]</p>

<h3>7. Effect on creditors</h3>
<p>The Scheme will not adversely affect the rights of creditors. All known creditors as on
[date] have been listed in Annexure [__]. Aggregate liabilities of the Transferor Company stand
at ₹[__] crore as at [date], all of which will be assumed by the Transferee Company. The
Transferee Company's net worth is ₹[__] crore, sufficient to discharge the combined
liabilities.</p>

<h3>8. Auditor's certificate on accounting treatment</h3>
<p>The accounting treatment proposed in the Scheme is in accordance with [Ind AS 103 / AS 14]
and Section 133 of the Companies Act 2013. A certificate to this effect from the statutory
auditor of the Transferee Company is annexed as Annexure [__].</p>

<h3>9. Disclosures specific to listed company (if applicable)</h3>
<ul>
  <li>Confirmation that the Scheme is in compliance with SEBI LODR Regulation 37, SEBI Master Circular on Schemes of Arrangement, and the relevant SEBI Takeover Regulations.</li>
  <li>Confirmation of receipt of stock exchange in-principle approval dated [____].</li>
  <li>Fairness opinion of [SEBI-registered merchant banker name] dated [____] is annexed.</li>
  <li>Audit Committee resolution dated [____] is annexed.</li>
  <li>Committee of Independent Directors resolution dated [____] is annexed.</li>
</ul>

<h3>10. Pending investigations, prosecutions or proceedings</h3>
<p>There are no investigations or proceedings against the Transferor Company under [the Companies Act, IBC, SEBI Act, IT Act] except [list with details, or "Nil"].</p>

<h3>11. Material interests of directors, KMPs and their relatives</h3>
<p>[List of directors / KMPs of both companies and their shareholdings, with statement that no director has any other material interest in the Scheme except as a shareholder.]</p>

<h3>12. Effect on shareholders and minority protection</h3>
<p>[Specific discussion: how minority shareholders are protected; whether the Scheme requires majority-of-minority approval; whether dissenting shareholders have exit rights.]</p>

<h3>13. Compliance certifications</h3>
<p>[Compliance with Sec 232(3)(i); Sec 232(3)(b); Sec 232(5) — certificate of the Income-tax department confirming no objection / no pending demand; FEMA compliance certificate if cross-border; CCI approval status.]</p>

<h3>14. Reasons why creditors / members should approve</h3>
<p>[Pull the key economic / strategic benefits from Section 2 into a concise final pitch.]</p>

<p><em>Place: [____], Date: [____]; For [Transferor/Transferee Co.]; Director / Company Secretary signature</em></p>
</blockquote>

<div class="callout">
<strong>The 3 things NCLT always asks.</strong> (1) Is the rationale commercial, not tax? (2)
Is the exchange ratio backed by independent valuation? (3) Are creditors protected? Address
all three explicitly and clearly. If you can't, restructure the deal — don't try to hide it
in the explanatory statement.
</div>
""",
    },

    {
        "slug": "bta-recital",
        "title": "Business Transfer Agreement (BTA) — Recitals & Key Clauses",
        "summary": "Slump-sale BTA opening recitals and the half-dozen clauses that decide whether Sec 50B applies.",
        "body": """
<h2>BTA recital structure</h2>
<p>The recitals frame the transaction. Sec 50B applies only if the transfer is a 'slump sale'
under Sec 2(42C) — recitals that fail this characterisation cost the seller indexation, the
buyer cost stepping-up, and create a tax dispute.</p>

<h2>Skeleton — opening</h2>
<blockquote>
<p><strong>THIS BUSINESS TRANSFER AGREEMENT</strong> is made and entered into on this [__]
day of [____], 2026 (the "<strong>Execution Date</strong>")</p>

<p><strong>BETWEEN</strong></p>

<p>(1) <strong>[Seller Co. Name]</strong>, a company incorporated under the Companies Act,
2013 / 1956, having its CIN [____] and its registered office at [address] (hereinafter
referred to as the "<strong>Seller</strong>" or "<strong>Transferor</strong>", which
expression shall, unless repugnant to the context, include its successors and permitted
assigns), of the FIRST PART;</p>

<p><strong>AND</strong></p>

<p>(2) <strong>[Buyer Co. Name]</strong>, a company incorporated... (hereinafter referred to
as the "<strong>Buyer</strong>" or "<strong>Transferee</strong>"...), of the SECOND PART.</p>

<p>The Seller and the Buyer are individually referred to as a "<strong>Party</strong>" and
collectively as the "<strong>Parties</strong>".</p>

<p><strong>WHEREAS:</strong></p>

<p><strong>A.</strong> The Seller is engaged in the business of [describe — be specific
enough that the "undertaking" is identifiable] (the "<strong>Business</strong>") and is
desirous of transferring the Business as a whole and on a going concern basis to the Buyer.</p>

<p><strong>B.</strong> The Business comprises an identifiable undertaking of the Seller,
capable of being carried on independently and includes, without limitation, all assets,
liabilities, employees, contracts, licences, permits, intellectual property rights and
business records exclusively pertaining to the Business (collectively, the "<strong>Transferred
Undertaking</strong>"), more particularly described in <strong>Schedule I</strong>.</p>

<p><strong>C.</strong> The Buyer is desirous of acquiring the Transferred Undertaking from
the Seller on a <strong>going concern basis</strong> by way of a <strong>slump sale</strong>
within the meaning of Section 2(42C) of the Income-tax Act for a <strong>lump-sum
consideration</strong> as set out in Clause [__] hereof, <strong>without values being
assigned to the individual assets and liabilities</strong> comprising the Transferred
Undertaking.</p>

<p><strong>D.</strong> The Parties have, after due deliberation and on the basis of mutual
representations, warranties, covenants and assurances contained herein, agreed to enter into
this Agreement on the terms and conditions set forth below.</p>

<p><strong>NOW, THEREFORE</strong>, in consideration of the mutual covenants and agreements
herein contained, the Parties hereby agree as follows:</p>
</blockquote>

<h2>Critical clauses — the ones that make-or-break Sec 50B</h2>

<h3>Clause 2 — Sale of Undertaking</h3>
<blockquote>
<p>The Seller hereby agrees to sell, transfer, convey, assign and deliver to the Buyer, and
the Buyer hereby agrees to purchase and acquire from the Seller, the <strong>entirety</strong>
of the Transferred Undertaking, <strong>as a going concern, by way of a slump sale</strong>,
<strong>without values being assigned to the individual assets and liabilities</strong>
comprising the Transferred Undertaking, for the Lump-Sum Consideration set out in Clause 3.</p>
</blockquote>

<h3>Clause 3 — Lump-Sum Consideration</h3>
<blockquote>
<p>In consideration of the sale, transfer and assignment of the Transferred Undertaking, the
Buyer shall pay to the Seller a <strong>lump-sum consideration of ₹[____] crore</strong> (the
"<strong>Consideration</strong>"), payable in the manner set out in Schedule II. <strong>The
Consideration represents the price for the Transferred Undertaking as a whole; no values are
attributed to any individual asset or liability comprising the Transferred Undertaking.</strong></p>
</blockquote>

<h3>Clause 4 — Closing Conditions</h3>
<p>[Standard CPs: corporate approvals, regulatory approvals (CCI if applicable), third-party
consents, no MAC, accuracy of warranties.]</p>

<h3>Clause 5 — Employees</h3>
<blockquote>
<p>All Employees forming part of the Transferred Undertaking shall, with effect from the
Closing Date, become employees of the Buyer on terms and conditions of service no less
favourable than those obtaining immediately prior to the Closing Date. <strong>Continuity of
service shall be preserved</strong> for all statutory purposes including gratuity, leave
encashment, provident fund and notice periods.</p>
</blockquote>

<h3>Clause 6 — Liabilities Assumed</h3>
<blockquote>
<p>The Buyer shall assume and discharge, with effect from the Closing Date, <strong>all
liabilities and obligations of every nature</strong> (whether actual or contingent, known or
unknown, accrued or to accrue) pertaining to the Transferred Undertaking, as listed in
<strong>Schedule III</strong>, <em>provided that</em> liabilities specifically excluded
(Excluded Liabilities) shall remain with the Seller.</p>
</blockquote>

<h3>Clause 7 — Representations and Warranties</h3>
<p>[Standard reps + slump-sale-specific: (a) the Transferred Undertaking is capable of being
carried on independently; (b) Schedule I lists ALL property comprising the undertaking; (c)
there are no allocations of consideration to individual assets in any side document.]</p>

<h3>Clause 8 — Tax Matters</h3>
<blockquote>
<p>The Parties acknowledge that the transfer is intended to be a slump sale within the meaning
of Section 2(42C) of the Income-tax Act and that the gain, if any, arising to the Seller
shall be computed under Section 50B of the Income-tax Act. The Seller shall obtain a report
in Form 3CEA from an accountant in respect of the computation of net worth and the capital
gain on the slump sale, and shall furnish a copy to the Buyer at Closing.</p>
</blockquote>

<div class="callout">
<strong>Three drafting traps that kill Sec 50B.</strong>
(1) Any line in the BTA or its annexures that assigns a value to a specific asset = no slump
sale. <em>Especially watch:</em> separate land-and-building valuations bundled into the BTA.
(2) Carving out one significant asset from the Transferred Undertaking weakens the "undertaking"
characterisation — risks the buyer arguing it's an itemised sale.
(3) "Sale of business" language without explicitly invoking slump-sale-going-concern can be
recharacterised by the AO. Use the magic words.
</div>
""",
    },

    {
        "slug": "fairness-opinion",
        "title": "Fairness Opinion — Structure (SEBI Master Circular)",
        "summary": "What a SEBI-registered merchant banker's fairness opinion must contain for a listed-company scheme.",
        "body": """
<h2>When required</h2>
<p>Mandatory under the SEBI Master Circular on Schemes of Arrangement for every scheme
involving a listed company, unless the scheme is between a listed company and its
wholly-owned subsidiary (or vice versa) where simplified procedure applies.</p>

<h2>Skeleton</h2>
<blockquote>

<p>[Letterhead of SEBI-registered Merchant Banker]<br>
[Date]<br><br>
To,<br>
The Board of Directors<br>
[Listed Company Name]<br>
[Address]</p>

<p><strong>Subject:</strong> Fairness Opinion on the Share Exchange Ratio under the proposed
Scheme of Arrangement between [Transferor Co.] and [Transferee Co.] and their respective
shareholders and creditors</p>

<h3>1. Engagement</h3>
<p>1.1 [Merchant Banker Name] ("we", "MB"), a Category I Merchant Banker registered with SEBI
(Registration No. INM00[____]), has been engaged by the Board of Directors of [Listed Co.]
vide engagement letter dated [____] to provide an opinion on the fairness of the share
exchange ratio (the "<strong>Exchange Ratio</strong>") set out in the proposed Scheme.</p>

<p>1.2 The Exchange Ratio as recommended in the valuation report dated [____] by [Independent
Valuer Name] (Registered Valuer Reg. No. [____]) (the "<strong>Valuation Report</strong>") is:</p>
<p><em>[N] equity shares of ₹[X] each fully paid-up of [Transferee Co.] for every [M] equity
shares of ₹[Y] each fully paid-up of [Transferor Co.] held as on the Record Date.</em></p>

<h3>2. Scope of opinion</h3>
<p>Our opinion is limited to the fairness, from a financial point of view, of the Exchange
Ratio to the equity shareholders of [Listed Co.]. Our opinion does not address:</p>
<ul>
  <li>The underlying business decision of the Company to enter into the Scheme;</li>
  <li>The relative merits of the Scheme vis-à-vis alternative transactions;</li>
  <li>Any legal, accounting, regulatory or tax aspects of the Scheme;</li>
  <li>The prices at which the Company's shares may trade following the Scheme.</li>
</ul>

<h3>3. Information reviewed</h3>
<p>In arriving at our opinion we have reviewed, among other things:</p>
<ul>
  <li>The draft Scheme dated [____];</li>
  <li>The Valuation Report and supporting workings;</li>
  <li>Audited and unaudited financial statements of both companies for the [3] most recent financial periods;</li>
  <li>Management projections for the [Business] for [FY27 – FY29];</li>
  <li>Stock exchange data for [Listed Co.] for the 6 / 12 / 24 months preceding [date];</li>
  <li>Industry reports and listed-company comparables;</li>
  <li>Such other data, discussions and analyses as we considered relevant.</li>
</ul>

<h3>4. Valuation methodologies considered</h3>
<p>We have evaluated the Valuation Report's use of the following methodologies and have
ourselves applied them, where relevant, in arriving at independent indicative ranges:</p>
<ul>
  <li><strong>Market Price method</strong> — based on volume-weighted average market price (VWAP) of the listed share over [60 trading days] preceding [date];</li>
  <li><strong>Comparable Companies' Quoted Multiples (CCM)</strong> — peer-group EV/EBITDA, P/E, P/B multiples;</li>
  <li><strong>Discounted Cash Flow (DCF)</strong> — explicit period of [5] years + terminal value, WACC [__]%, terminal growth [__]%;</li>
  <li><strong>Net Asset Value (NAV)</strong> — for asset-heavy / unlisted entity;</li>
  <li><strong>Comparable Transactions Multiples</strong> — recent precedent deals in the sector.</li>
</ul>

<h3>5. Assumptions and limitations</h3>
<p>This opinion is based on financial, economic, market and other conditions as in effect on,
and the information made available to us as of, the date hereof. We assume no responsibility
for updating or revising this opinion. We have assumed and relied upon the accuracy and
completeness of the information furnished to us by the Company and its representatives and
have not independently verified the same.</p>

<h3>6. Opinion</h3>
<p>Based on and subject to the foregoing, and such other factors as we have considered
relevant, <strong>we are of the opinion that the Exchange Ratio as set out in the draft
Scheme is fair, from a financial point of view, to the equity shareholders of [Listed
Co.]</strong> as on the date of this opinion.</p>

<h3>7. Confidentiality and use</h3>
<p>This opinion is provided solely for the use of the Board of Directors of [Listed Co.] in
connection with its evaluation of the Scheme. It may be reproduced in full in any
communication to shareholders, the Stock Exchanges, SEBI, the NCLT or any other regulatory
authority as required for the Scheme proceedings, but may not be otherwise reproduced or
referred to without our prior written consent.</p>

<p>Yours faithfully,<br><br>
For [Merchant Banker Name]<br><br>
________________________<br>
Authorised Signatory<br>
SEBI Registration No.: INM00[____]<br>
Place: [____]<br>
Date: [____]</p>
</blockquote>

<div class="callout">
<strong>What SEBI specifically wants.</strong> The opinion must explicitly cover: (a) why the
chosen valuation methodologies are appropriate for this transaction; (b) the weights assigned
to each method and why; (c) sensitivity analysis on key assumptions; (d) a clear statement
that the ratio is fair to the equity shareholders of the listed entity (not just "the
parties"); (e) compliance with the SEBI Master Circular's content requirements.
</div>
""",
    },

    {
        "slug": "form-3cd-line-items",
        "title": "Form 3CD — High-impact Line Items Explained",
        "summary": "The clauses of the tax-audit report that consume 80% of audit time and 100% of penalty risk.",
        "body": """
<h2>Where the time goes</h2>
<p>Form 3CD has 44 clauses. About 10 of them carry real reporting risk (penalty exposure under
Sec 271J if mis-stated) and consume most of the audit team's time. Master these first.</p>

<h2>Clause 11 — Books of account and method of accounting</h2>
<p>Report: (a) whether books are kept at the principal place of business or elsewhere (with
addresses); (b) the method of accounting employed (cash / mercantile) and any change from
preceding year. <strong>Trap:</strong> changes in method of accounting under AS 5 / Ind AS 8
must be flagged here AND in clause 13 — easy to miss the second mention.</p>

<h2>Clause 13 — Method of valuation of closing stock; deviations and adjustments</h2>
<p>Disclose: method (FIFO, weighted average, specific identification); deviation from Sec 145A
(GST inclusive vs exclusive — Sec 145A mandates inclusive); deviation from ICDS. <strong>Most
common error:</strong> closing-stock valuation under Ind AS uses 'net realisable value' (NRV)
but for ICDS purposes you may need a different valuation.</p>

<h2>Clause 14 — Method of valuation of capital assets converted into stock</h2>
<p>Report if any capital asset was converted into stock-in-trade during the year and the
method of valuation. Triggers Sec 45(2) deemed transfer.</p>

<h2>Clause 16 — Amounts not credited to P&L but assessable</h2>
<p>Report:</p>
<ul>
  <li>16(a) — Items falling under proviso to Sec 28 (e.g., notional rent on closely-held co. assets).</li>
  <li>16(b) — Performa credits / drawbacks not credited.</li>
  <li>16(c) — Escalation claims accepted.</li>
  <li>16(d) — Any other income.</li>
  <li>16(e) — Capital receipts not in P&L (with nature).</li>
</ul>

<h2>Clause 17 — Property transferred at less than stamp value (Sec 43CA / 50C / 56(2)(x))</h2>
<p>Per-property table — actual consideration vs stamp duty value vs FMV. Material if business
is real-estate or has significant immovable-property transactions.</p>

<h2>Clause 18 — Depreciation</h2>
<p>The big one. Per-block table: opening WDV, additions (with date), deductions, dep claimed,
closing WDV. <strong>Watch:</strong> (a) additions in second half get half-year rate; (b)
ineligible items (goodwill post Apr 2021); (c) Sec 32(1)(iia) additional depreciation eligibility
for manufacturing.</p>

<h2>Clause 21(a) — Items not allowed under Sec 36 / 37 / 40 / 40A</h2>
<p>The substantive disallowances. Includes:</p>
<ul>
  <li>21(b) — CSR expenditure (Sec 37(1) Explanation 2 — not allowed).</li>
  <li>21(d) — Sec 40(a) — TDS defaults, Sec 40(a)(ii) — tax paid on assessment, etc.</li>
  <li>21(e) — Sec 40(b) / 40(ba) — partner remuneration, AOP/BOI members.</li>
  <li>21(f) — Sec 14A — disallowance for exempt income (use Rule 8D).</li>
  <li>21(g) — Sec 14A disallowance under MAT (Ind AS 12 / 115JB Explanation).</li>
</ul>

<h2>Clause 22 — Sec 23 of the MSMED Act / Sec 43B(h)</h2>
<p>Effective from FY 2023-24: amounts due to micro/small enterprises exceeding the prescribed
payment timeline (15 or 45 days) are disallowed unless paid in the year. <strong>Highest-risk
clause</strong> for FY 2025-26 audits. Requires vendor-master tagging of MSME status.</p>

<h2>Clause 26 — Sec 43B items (actual-payment basis)</h2>
<p>Per-section table — opening balance, additions during year, paid during year (with cheque
numbers / payment dates), unpaid balance. Sections: 43B(a) tax / duty, (b) employee contribution,
(c) interest on loan, (d) bonus / leave encashment, (e) PF deduction from employees, (f)
railway services, (g) goods sold by State Trading entities, (h) MSMED — added FY 2023-24.</p>

<h2>Clause 27 — Sec 41 — Cessation / remission of liability</h2>
<p>Liabilities written back to P&L. Sec 41(1) brings into tax any allowance / deduction in a
prior year whose corresponding liability was remitted in the current year. Common in IBC
resolution-plan write-backs.</p>

<h2>Clause 31 — TDS / TCS</h2>
<p>Per-section TDS table — section, payment, TDS deducted, TDS remitted, late deduction /
remittance (with interest u/s 201(1A)). Heavy data collection; usually automated from the
ERP.</p>

<h2>Clause 32(a) — Brought-forward losses available for set-off</h2>
<p>Year-wise table of business loss, unabsorbed depreciation, speculation loss, capital loss
(STCL / LTCL), house property loss — current AY's available figure after applicable carry-
forward period.</p>

<h2>Clause 32(b) — Sec 79 restriction on closely-held companies</h2>
<p>If 51%+ shareholding changed, losses lapse — except IBC cases under Sec 79(2)(c).
<strong>Critical for post-acquisition assessments.</strong></p>

<h2>Clause 34 — Specified Financial Transactions (SFT)</h2>
<p>Has the assessee complied with SFT reporting under Sec 285BA? Report any SFT that exceeded
threshold and was reported / not reported.</p>

<h2>Clause 36A — Sec 56(2)(x) deemed gift</h2>
<p>Receipt of money / property without or for inadequate consideration. Per-instance table.
Common for shares received in restructuring at less than FMV.</p>

<h2>Clause 41 — Audit reports under any other Act</h2>
<p>Whether the assessee was required to obtain a report under any other law (GST audit, FCRA,
state-VAT etc.). Cross-reference between Form 3CD and statutory audit findings on these.</p>

<div class="callout">
<strong>Day-to-day audit tip.</strong> Build a single spreadsheet at the start of the engagement
with one row per Form 3CD clause and three columns: data source, working-paper reference,
status. This becomes your task list and your evidence file. The 10 high-impact clauses above
should each get a dedicated tab in the file with the raw data, the workings, and the final
Form 3CD entry that's pulled from the workings.
</div>
""",
    },
]
