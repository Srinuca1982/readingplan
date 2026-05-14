"""Worked numerical examples — drill the calculation muscle.

Each example is self-contained, with the data, the working, the answer and a
short interpretation. Organised by subject; meant to be solved alongside the
corresponding study note.
"""

EXAMPLES = [
    # ----------------------------------------------------------------------
    # Ind AS — Revenue (Ind AS 115)
    # ----------------------------------------------------------------------
    {
        "slug": "ind-as-115-revenue",
        "title": "Ind AS 115 — Multi-element software contract (full 5-step walk-through)",
        "subject": "Ind AS",
        "body": """
<h2>Facts</h2>
<p>On 1 April 2026, Acme Software Ltd. enters into a 3-year contract with Beta Bank
for:</p>
<ul>
  <li>(i) A perpetual software licence — stand-alone selling price (SSP) ₹60 lakh</li>
  <li>(ii) Customisation services to integrate with Beta's core banking system — SSP ₹40 lakh</li>
  <li>(iii) 3 years of post-go-live support and updates — SSP ₹10 lakh per year (i.e., ₹30 lakh total)</li>
</ul>
<p>Total SSPs = ₹60 + ₹40 + ₹30 = ₹130 lakh.</p>
<p>Contract price: ₹110 lakh (a 15.4% bundle discount). Payment: ₹40 lakh upfront, ₹40 lakh on
go-live (expected 30 Sept 2026), ₹10 lakh per year for 3 years thereafter.</p>

<h2>Step 1 — Identify the contract</h2>
<p>Written contract, identifiable rights and obligations, payment terms, commercial substance,
collectibility probable. ✓ Valid contract.</p>

<h2>Step 2 — Identify performance obligations</h2>
<p>Three candidates. Test each for "distinct":</p>
<ul>
  <li><strong>Licence</strong> — Capable of being distinct? Yes (off-shelf usable). Distinct in
the context of the contract? Yes — Acme could sell to others without customisation.
<strong>= Distinct.</strong></li>
  <li><strong>Customisation</strong> — significantly modifies the licence; integrated with core
banking. Capable of being distinct (in theory, another vendor could do it) but in the context
of Beta's contract, customisation is what makes the bundle useful. Per Ind AS 115 para 29(a),
if the entity provides a significant service of integrating, the goods/services are not
distinct in the context of the contract. <strong>However</strong>, where the customisation
is a discrete deliverable (project ends with a "go-live" event) and the licence is usable
without customisation, treat as <strong>distinct</strong>. Acme determines customisation is
distinct.</li>
  <li><strong>Support and updates</strong> — clearly distinct (separately priced; standalone
service). <strong>= Distinct.</strong></li>
</ul>
<p>→ <strong>3 performance obligations.</strong></p>

<h2>Step 3 — Determine transaction price</h2>
<p>Fixed: ₹110 lakh. No variable consideration. No financing component (payments are not
significantly delayed beyond performance — straightforward).</p>

<h2>Step 4 — Allocate transaction price using relative SSPs</h2>
<table>
  <thead><tr><th>Obligation</th><th>SSP (₹ lakh)</th><th>Weight</th><th>Allocated (₹ lakh)</th></tr></thead>
  <tbody>
    <tr><td>Licence</td><td>60</td><td>60/130 = 46.15%</td><td>50.77</td></tr>
    <tr><td>Customisation</td><td>40</td><td>40/130 = 30.77%</td><td>33.85</td></tr>
    <tr><td>Support (3 yrs)</td><td>30</td><td>30/130 = 23.08%</td><td>25.38</td></tr>
    <tr><td><strong>Total</strong></td><td><strong>130</strong></td><td><strong>100%</strong></td><td><strong>110.00</strong></td></tr>
  </tbody>
</table>

<h2>Step 5 — Recognise revenue when (or as) each obligation is satisfied</h2>
<ul>
  <li><strong>Licence (perpetual)</strong> — point in time when control transfers (delivery
of licence keys / right to use). If on contract date (1 April 2026): recognise <strong>₹50.77
lakh on 1 April 2026</strong>.</li>
  <li><strong>Customisation</strong> — over time as work performed (assuming Acme has
enforceable right to payment for work-to-date — per Ind AS 115 para 35(c)). Use input method
(cost incurred / total expected cost). If as at year-end 31 Mar 2027 customisation is 75%
complete: recognise <strong>₹33.85 × 75% = ₹25.39 lakh</strong> in FY 2026-27, balance
₹8.46 lakh in FY 2027-28.</li>
  <li><strong>Support (3 yrs)</strong> — straight-line over 3 years from go-live (30 Sept 2026).
FY 2026-27 covers 30 Sept 2026 to 31 Mar 2027 = 6 months. Recognise <strong>₹25.38 × 6/36 =
₹4.23 lakh</strong> in FY 2026-27.</li>
</ul>

<h2>Summary — FY 2026-27 P&L revenue</h2>
<table>
  <thead><tr><th>Obligation</th><th>Revenue recognised (₹ lakh)</th></tr></thead>
  <tbody>
    <tr><td>Licence (point in time, 1 Apr 2026)</td><td>50.77</td></tr>
    <tr><td>Customisation (over time, 75% complete)</td><td>25.39</td></tr>
    <tr><td>Support (6 months of 36)</td><td>4.23</td></tr>
    <tr><td><strong>Total FY 26-27 revenue</strong></td><td><strong>80.39</strong></td></tr>
  </tbody>
</table>

<div class="callout">
<strong>Why this matters.</strong> If Acme had not separated the three obligations and just
recognised cash as billed, the FY 26-27 revenue would have been ₹80 lakh (₹40 + ₹40) — same
magnitude but wrong reasoning, with the support revenue rolled into year 1 instead of
deferred. NCAA audit-finding territory. The 5-step model is what produces a defensible
allocation.
</div>
""",
    },

    # ----------------------------------------------------------------------
    # Ind AS 12 — Deferred Tax
    # ----------------------------------------------------------------------
    {
        "slug": "ind-as-12-deferred-tax",
        "title": "Ind AS 12 — Deferred tax on temporary differences",
        "subject": "Ind AS",
        "body": """
<h2>Facts</h2>
<p>As at 31 March 2027 (FY 26-27 year-end), Crest Manufacturing Ltd. has the following
items in its books vs tax records:</p>
<table>
  <thead><tr><th>Item</th><th>Carrying amount (book)</th><th>Tax base</th><th>Temporary difference</th><th>Type</th></tr></thead>
  <tbody>
    <tr><td>PP&E (gross)</td><td>500</td><td>400</td><td>100 (book higher)</td><td>Taxable (DTL)</td></tr>
    <tr><td>Provision for warranty</td><td>(80)</td><td>0</td><td>80 (book lower)</td><td>Deductible (DTA)</td></tr>
    <tr><td>Accrued expenses (disallowed u/s 43B)</td><td>(60)</td><td>0</td><td>60 (book lower)</td><td>Deductible (DTA)</td></tr>
    <tr><td>Brought-forward business loss</td><td>—</td><td>(120)</td><td>120</td><td>Deductible (DTA)</td></tr>
    <tr><td>Fair-value gain on FVTOCI investments (in equity)</td><td>40</td><td>0</td><td>40</td><td>Taxable (DTL, in OCI)</td></tr>
  </tbody>
</table>
<p>Tax rate: 25.168% (corporate rate + surcharge + cess for FY 26-27, normal regime).</p>

<h2>Step 1 — Compute deferred tax line by line</h2>
<table>
  <thead><tr><th>Item</th><th>Temp diff (₹ lakh)</th><th>Tax rate</th><th>DTA/DTL (₹ lakh)</th><th>Recognise in</th></tr></thead>
  <tbody>
    <tr><td>PP&E</td><td>100</td><td>25.168%</td><td>(25.17) DTL</td><td>P&L</td></tr>
    <tr><td>Warranty provision</td><td>80</td><td>25.168%</td><td>20.13 DTA</td><td>P&L</td></tr>
    <tr><td>43B accruals</td><td>60</td><td>25.168%</td><td>15.10 DTA</td><td>P&L</td></tr>
    <tr><td>B/f business loss</td><td>120</td><td>25.168%</td><td>30.20 DTA</td><td>P&L</td></tr>
    <tr><td>FVTOCI gain</td><td>40</td><td>25.168%</td><td>(10.07) DTL</td><td>OCI</td></tr>
  </tbody>
</table>

<h2>Step 2 — Apply DTA recognition test</h2>
<p>Per Ind AS 12 para 24, a DTA is recognised <strong>only to the extent it is probable that
future taxable profit will be available</strong> against which the deductible difference can be
utilised. Crest forecasts taxable profit of ₹200 lakh for FY 27-28 and FY 28-29 each based on
its 5-year plan.</p>

<p>Total DTAs claimed = 20.13 + 15.10 + 30.20 = <strong>₹65.43 lakh</strong>. This represents
₹260 lakh of deductible differences which can be set off against forecast taxable profits of
₹400 lakh over 2 years. Recovery probable → <strong>recognise full DTA</strong>.</p>

<p>Brought-forward business loss carry-forward is limited to 8 years under Sec 79 (assume
Crest is within window). ✓ Recoverable. Recognised.</p>

<h2>Step 3 — Net deferred tax balance</h2>
<table>
  <thead><tr><th></th><th>Through P&L (₹ lakh)</th><th>Through OCI (₹ lakh)</th></tr></thead>
  <tbody>
    <tr><td>DTAs</td><td>65.43</td><td>—</td></tr>
    <tr><td>DTLs</td><td>(25.17)</td><td>(10.07)</td></tr>
    <tr><td><strong>Net DTA / (DTL)</strong></td><td><strong>40.26 DTA</strong></td><td><strong>(10.07) DTL</strong></td></tr>
  </tbody>
</table>

<h2>Step 4 — Journal entries (assuming opening balances nil)</h2>
<blockquote>
<p>Dr. Deferred Tax Asset ₹40.26 lakh<br>
Cr. Deferred Tax Income (P&L) ₹40.26 lakh</p>
<p>Dr. OCI ₹10.07 lakh<br>
Cr. Deferred Tax Liability ₹10.07 lakh</p>
</blockquote>

<div class="callout">
<strong>The 3 things auditors check.</strong> (1) Have you reassessed unrecognised DTAs every
year (para 37)? (2) Have you recognised the OCI portion in OCI, not P&L (the FVTOCI gain
example)? (3) Are tax-base values calculated consistently — for PP&E, WDV under Sec 43(6),
not depreciation as per books? Mistakes here are the most common Ind AS audit finding in
NFRA reports.
</div>
""",
    },

    # ----------------------------------------------------------------------
    # Ind AS 109 — Expected Credit Loss
    # ----------------------------------------------------------------------
    {
        "slug": "ind-as-109-ecl",
        "title": "Ind AS 109 — Expected Credit Loss on a portfolio of trade receivables (simplified approach)",
        "subject": "Ind AS",
        "body": """
<h2>Facts</h2>
<p>DeltaCo, an Ind AS preparer, has trade receivables ₹5,000 lakh as at 31 Mar 2027. The
company uses the <strong>simplified approach</strong> under Ind AS 109 para 5.5.15 (always
lifetime ECL — no need for stage migration logic for trade receivables).</p>

<p>Ageing analysis and historical default rates (last 3 years average):</p>
<table>
  <thead><tr><th>Ageing bucket</th><th>Receivables ₹ lakh</th><th>Historical default rate</th></tr></thead>
  <tbody>
    <tr><td>Current (0 days)</td><td>3,000</td><td>0.5%</td></tr>
    <tr><td>1–30 days past due</td><td>1,200</td><td>2%</td></tr>
    <tr><td>31–60 days past due</td><td>500</td><td>5%</td></tr>
    <tr><td>61–90 days past due</td><td>200</td><td>15%</td></tr>
    <tr><td>91–180 days past due</td><td>80</td><td>40%</td></tr>
    <tr><td>> 180 days past due</td><td>20</td><td>90%</td></tr>
  </tbody>
</table>

<h2>Step 1 — Forward-looking adjustment</h2>
<p>Per Ind AS 109 para B5.5.51, historical loss rates must be adjusted for current and forecast
economic conditions. DeltaCo's economist forecasts a mild recession in FY 27-28 → uplift
historical rates by 1.25x. Apply to the higher-ageing buckets (61+ days) where macro
sensitivity is greater.</p>

<table>
  <thead><tr><th>Ageing</th><th>Historical</th><th>Forward-adjusted</th></tr></thead>
  <tbody>
    <tr><td>Current</td><td>0.5%</td><td>0.5%</td></tr>
    <tr><td>1–30</td><td>2%</td><td>2%</td></tr>
    <tr><td>31–60</td><td>5%</td><td>5%</td></tr>
    <tr><td>61–90</td><td>15%</td><td>18.75% (×1.25)</td></tr>
    <tr><td>91–180</td><td>40%</td><td>50% (×1.25)</td></tr>
    <tr><td>> 180</td><td>90%</td><td>100% (cap)</td></tr>
  </tbody>
</table>

<h2>Step 2 — Compute ECL per bucket</h2>
<table>
  <thead><tr><th>Bucket</th><th>Receivables</th><th>Adj. rate</th><th>ECL ₹ lakh</th></tr></thead>
  <tbody>
    <tr><td>Current</td><td>3,000</td><td>0.5%</td><td>15</td></tr>
    <tr><td>1–30</td><td>1,200</td><td>2%</td><td>24</td></tr>
    <tr><td>31–60</td><td>500</td><td>5%</td><td>25</td></tr>
    <tr><td>61–90</td><td>200</td><td>18.75%</td><td>37.5</td></tr>
    <tr><td>91–180</td><td>80</td><td>50%</td><td>40</td></tr>
    <tr><td>> 180</td><td>20</td><td>100%</td><td>20</td></tr>
    <tr><td><strong>Total ECL</strong></td><td><strong>5,000</strong></td><td></td><td><strong>161.5</strong></td></tr>
  </tbody>
</table>

<h2>Step 3 — Compare with opening provision and book the difference</h2>
<p>Opening ECL provision (as at 1 Apr 2026): ₹120 lakh.<br>
Closing required: ₹161.5 lakh.<br>
Top-up needed: <strong>₹41.5 lakh</strong>.</p>

<h2>Journal entry</h2>
<blockquote>
<p>Dr. Impairment loss on trade receivables (P&L) ₹41.5 lakh<br>
Cr. Loss allowance for trade receivables ₹41.5 lakh</p>
</blockquote>

<h2>Disclosure under Ind AS 107</h2>
<ul>
  <li>The provision matrix (the table above) must be disclosed.</li>
  <li>Forward-looking adjustment methodology must be disclosed.</li>
  <li>Credit-risk concentrations (top 5 customers / sector concentrations).</li>
  <li>Movement in ECL allowance: opening 120 + charge 41.5 - written off [if any] = closing 161.5.</li>
</ul>

<div class="callout">
<strong>Audit hotspots.</strong> (1) Where did the 1.25x come from? Auditors will challenge —
need an economist's report or a documented sensitivity to GDP. (2) Why uplift only some
buckets and not all? Justify the differential. (3) Are write-offs being booked when truly
uncollectible, or are they staying in the > 180 bucket inflating the gross trade-receivable
number? Sec 36(1)(vii) requires actual write-off for tax deduction.
</div>
""",
    },

    # ----------------------------------------------------------------------
    # Ind AS 19 — Gratuity (actuarial)
    # ----------------------------------------------------------------------
    {
        "slug": "ind-as-19-gratuity",
        "title": "Ind AS 19 — Gratuity defined-benefit actuarial valuation",
        "subject": "Ind AS",
        "body": """
<h2>Facts</h2>
<p>EpsilonTech Ltd. has 200 employees on permanent rolls. Gratuity is a defined-benefit plan
(unfunded). At 31 March 2027:</p>
<ul>
  <li>Opening DBO (1 Apr 2026): ₹220 lakh (actuarial valuation as at FY 25-26)</li>
  <li>Plan assets: nil (unfunded)</li>
  <li>Current service cost (computed by actuary for FY 26-27): ₹38 lakh</li>
  <li>Interest cost: discount rate 7.2% on opening DBO ₹220 lakh = ₹15.84 lakh</li>
  <li>Benefits paid during FY 26-27: ₹18 lakh</li>
  <li>Actuarial loss on remeasurement: ₹12 lakh (driven by lower-than-expected attrition + 1% upward salary revision assumption)</li>
</ul>

<h2>Step 1 — Roll-forward of DBO</h2>
<table>
  <tbody>
    <tr><td>Opening DBO (1 Apr 2026)</td><td>220.00</td></tr>
    <tr><td>+ Current service cost</td><td>38.00</td></tr>
    <tr><td>+ Interest cost (7.2% × 220)</td><td>15.84</td></tr>
    <tr><td>− Benefits paid</td><td>(18.00)</td></tr>
    <tr><td>+ Actuarial loss (remeasurement)</td><td>12.00</td></tr>
    <tr><td><strong>Closing DBO (31 Mar 2027)</strong></td><td><strong>267.84</strong></td></tr>
  </tbody>
</table>

<h2>Step 2 — Components by where they go (P&L vs OCI)</h2>
<table>
  <thead><tr><th>Component</th><th>P&L (₹ lakh)</th><th>OCI (₹ lakh)</th></tr></thead>
  <tbody>
    <tr><td>Current service cost (employee benefits expense)</td><td>38.00</td><td>—</td></tr>
    <tr><td>Net interest cost (finance cost)</td><td>15.84</td><td>—</td></tr>
    <tr><td>Actuarial loss — remeasurement (not reclassified)</td><td>—</td><td>12.00</td></tr>
    <tr><td><strong>Total impact on FY 26-27</strong></td><td><strong>53.84</strong></td><td><strong>12.00</strong></td></tr>
  </tbody>
</table>

<h2>Step 3 — Journal entries</h2>
<blockquote>
<p>Dr. Employee benefits expense (P&L) ₹38.00 lakh<br>
Dr. Finance cost (P&L) ₹15.84 lakh<br>
Dr. OCI — Actuarial losses ₹12.00 lakh<br>
Cr. Gratuity liability ₹65.84 lakh</p>
<p>(For provision charged during the year before benefits paid)</p>
<br>
<p>Dr. Gratuity liability ₹18.00 lakh<br>
Cr. Cash / Bank ₹18.00 lakh</p>
<p>(For benefits paid)</p>
</blockquote>

<h2>Step 4 — Balance-sheet presentation</h2>
<ul>
  <li>Non-current liability: gratuity portion expected to be paid after 12 months (per actuary's schedule).</li>
  <li>Current liability: portion expected to be paid within 12 months.</li>
  <li>The split is provided by the actuary in the valuation report.</li>
</ul>

<h2>Key disclosures (Ind AS 19 para 135–147)</h2>
<ol>
  <li>Reconciliation of opening to closing DBO (Step 1 table above).</li>
  <li>Key actuarial assumptions: discount rate 7.2%, salary escalation 8%, mortality table (IALM 2012-14), attrition rate 12%, retirement age 60.</li>
  <li>Sensitivity analysis: ± 1% change in discount rate, salary escalation — show impact on DBO.</li>
  <li>Maturity profile of expected payments (next year, year 2-5, year 6-10, > 10 years).</li>
  <li>Weighted average duration of the obligation.</li>
</ol>

<div class="callout">
<strong>Common audit findings.</strong> (1) Discount rate not aligned with high-quality bond
yields of similar duration. (2) Salary escalation assumption inconsistent with the company's
own compensation policy. (3) Mortality table outdated. (4) Sensitivity disclosure missing.
(5) Treating the actuarial gain/loss in P&L instead of OCI — basic error that still appears.
</div>
""",
    },

    # ----------------------------------------------------------------------
    # Restructuring — Slump sale (more elaborate than the cheat sheet)
    # ----------------------------------------------------------------------
    {
        "slug": "slump-sale-rule-11uae",
        "title": "Slump sale — net-worth vs FMV (Rule 11UAE) interplay",
        "subject": "Restructuring",
        "body": """
<h2>Facts</h2>
<p>Zenith Ltd. is selling its "Logistics" undertaking to Nimbus Ltd. on 1 May 2026.</p>
<p>Lump-sum consideration: ₹420 crore.</p>
<p>Net worth of the undertaking (per books, after Sec 50B adjustments): ₹250 crore.</p>
<p>FMV per Rule 11UAE: ₹480 crore (includes premium for the customer book and trained workforce).</p>

<h2>Step 1 — Determine the deemed sale consideration</h2>
<p>Per Sec 50B(2) read with Rule 11UAE: <strong>sale consideration = higher of (a) actual
lump-sum consideration OR (b) FMV under Rule 11UAE</strong>.</p>
<p>Higher of ₹420 cr (actual) or ₹480 cr (FMV) → <strong>deemed sale consideration = ₹480 cr</strong>.</p>

<h2>Step 2 — Compute capital gain</h2>
<table>
  <tbody>
    <tr><td>Deemed sale consideration</td><td>480</td></tr>
    <tr><td>Less: Net worth of undertaking</td><td>(250)</td></tr>
    <tr><td><strong>Long-term capital gain (held > 36 months)</strong></td><td><strong>230</strong></td></tr>
  </tbody>
</table>

<h2>Step 3 — Tax liability on the gain</h2>
<p>LTCG on slump sale taxed at 20% + surcharge + cess (no indexation available even though
long-term). Effective rate ~23.296% (with 12% surcharge + 4% cess).</p>
<p><strong>Tax = ₹230 cr × 23.296% ≈ ₹53.58 cr</strong></p>

<h2>Step 4 — What if the FMV were lower than actual?</h2>
<p>If FMV were ₹400 cr (less than ₹420 cr actual): deemed consideration = ₹420 cr (higher).
Capital gain = ₹420 - ₹250 = ₹170 cr. Tax = ₹170 × 23.296% = ₹39.60 cr.</p>

<h2>Step 5 — Form 3CEA</h2>
<p>The CA's report u/s 50B in Form 3CEA must independently substantiate:</p>
<ul>
  <li>The net worth computation (asset-by-asset, with WDV for depreciable assets, book value for others, NIL for self-generated goodwill);</li>
  <li>The lump-sum nature of the consideration (no asset-wise allocations);</li>
  <li>The Rule 11UAE FMV computation;</li>
  <li>The going-concern certification.</li>
</ul>

<div class="callout">
<strong>Planning note.</strong> If you expect FMV to materially exceed the negotiated price
(e.g., undervalued business sold to a related party), the Rule 11UAE deeming kicks in. Best
to align consideration with FMV at the deal-table — paying a discount that gets clawed back
as tax leaves the seller worse off than a fair-price negotiation would have.
</div>
""",
    },

    # ----------------------------------------------------------------------
    # Demerger cost-allocation (Sec 49(2C)/(2D))
    # ----------------------------------------------------------------------
    {
        "slug": "demerger-cost-allocation",
        "title": "Demerger — cost allocation in shareholder's hands (Sec 49(2C)/(2D))",
        "subject": "Restructuring",
        "body": """
<h2>Facts</h2>
<p>Sigma Holdings is demerged: the FMCG undertaking transfers to a new "Sigma FMCG" company;
the residual industrial business remains in Sigma Holdings.</p>
<p>You hold <strong>10,000 equity shares</strong> of Sigma Holdings, originally acquired for
₹150 each (Total cost = ₹15,00,000).</p>
<p>As part of the demerger you receive <strong>10,000 equity shares</strong> of Sigma FMCG (1:1
proportionate).</p>
<p>From the company's records:</p>
<ul>
  <li>Net book value of assets transferred to Sigma FMCG: ₹400 crore</li>
  <li>Net worth of Sigma Holdings before demerger: ₹1,000 crore</li>
</ul>

<h2>Step 1 — Cost of Sigma FMCG shares in your hands (Sec 49(2C))</h2>
<blockquote>
Cost of Sigma FMCG shares = Cost of original Sigma Holdings shares × (NBV of assets transferred ÷ Net worth before demerger)
</blockquote>
<p>= ₹15,00,000 × (400 ÷ 1,000)<br>
= ₹15,00,000 × 0.40<br>
= <strong>₹6,00,000</strong></p>
<p>Per share cost of Sigma FMCG = ₹6,00,000 ÷ 10,000 = ₹60.</p>

<h2>Step 2 — Cost of remaining Sigma Holdings shares (Sec 49(2D))</h2>
<blockquote>
Cost of remaining Sigma Holdings shares = Original cost minus cost allocated to Sigma FMCG shares
</blockquote>
<p>= ₹15,00,000 − ₹6,00,000<br>
= <strong>₹9,00,000</strong></p>
<p>Per share cost = ₹9,00,000 ÷ 10,000 = ₹90.</p>

<h2>Step 3 — Holding period for capital-gains computation on future sale</h2>
<p>For Sigma FMCG shares received in demerger: per Sec 2(42A) Explanation 1(g), <strong>holding
period includes the period for which the original Sigma Holdings shares were held</strong>.
So you have not "restarted" the clock — the FMCG shares inherit the original acquisition date.</p>

<h2>Step 4 — Tax-neutrality on receipt</h2>
<p>The issuance of Sigma FMCG shares to you is not regarded as a transfer (Sec 47(vid)) and
Sec 56(2)(x) does not apply because the demerger satisfies Sec 2(19AA). You have no tax
liability today.</p>

<h2>Step 5 — When you later sell, say, the Sigma FMCG shares</h2>
<p>If you sell all 10,000 Sigma FMCG shares on 30 June 2028 for ₹120 each:</p>
<table>
  <tbody>
    <tr><td>Sale consideration (10,000 × 120)</td><td>12,00,000</td></tr>
    <tr><td>Less: Cost of acquisition (per Sec 49(2C))</td><td>(6,00,000)</td></tr>
    <tr><td><strong>Long-term capital gain</strong></td><td><strong>6,00,000</strong></td></tr>
  </tbody>
</table>
<p>Long-term because original acquisition date (let's say 1 Jan 2023) is more than 12 months
before sale. Subject to LTCG @ 12.5% (post-Budget 2024 rate, no indexation on listed equity).</p>
<p>Tax = ₹6,00,000 × 12.5% = ₹75,000 (above ₹1.25 lakh exemption threshold; this is the gain
exceeding the threshold portion).</p>

<div class="callout">
<strong>Practical note.</strong> The company is required to communicate the "net book value
of assets transferred / net worth before demerger" ratio to all shareholders for cost
allocation. This is usually published in the corporate communication around demerger record
date. Save that disclosure — your CA will need it when computing capital gains on later sale.
</div>
""",
    },

    # ----------------------------------------------------------------------
    # MAT (Sec 115JB)
    # ----------------------------------------------------------------------
    {
        "slug": "mat-115jb",
        "title": "MAT computation under Sec 115JB (Ind AS company)",
        "subject": "Tax",
        "body": """
<h2>Facts</h2>
<p>OmegaCorp, an Ind AS preparer, has the following P&L items for FY 26-27:</p>
<table>
  <tbody>
    <tr><td>Profit before tax (per Ind AS P&L)</td><td>1,000</td></tr>
    <tr><td>Add: Income tax provision (current + deferred)</td><td>300</td></tr>
    <tr><td>Add: Net actuarial loss in OCI (Ind AS 19)</td><td>20</td></tr>
    <tr><td>Less: Fair value gain on FVTOCI investments (in OCI, not reclassified)</td><td>(50)</td></tr>
    <tr><td>Add: Provision for diminution in value of investments</td><td>40</td></tr>
    <tr><td>Less: Depreciation per books</td><td>(150)</td></tr>
    <tr><td>Add: Depreciation per Sec 115JB Explanation 1 (excluding revaluation effect)</td><td>140</td></tr>
    <tr><td>Less: Brought-forward business loss / unabsorbed depreciation (lower of)</td><td>(80)</td></tr>
  </tbody>
</table>
<p>(All amounts in ₹ crore.)</p>

<h2>Step 1 — Compute book profit under Sec 115JB</h2>
<p>Starting from PBT, apply Explanation 1 to Sec 115JB (additions and deductions):</p>
<table>
  <tbody>
    <tr><td>Profit before tax</td><td>1,000</td></tr>
    <tr><td>Add: Income tax (current + deferred)</td><td>300</td></tr>
    <tr><td>Add: Provision for diminution (covered under Explanation 1(g))</td><td>40</td></tr>
    <tr><td>Add: Net actuarial loss in OCI (for Ind AS companies — Explanation to s115JB(2A))</td><td>20</td></tr>
    <tr><td>Less: FVTOCI gain (not reclassified — included in book profit for Ind AS co.)</td><td>(50)</td></tr>
    <tr><td>Net depreciation adjustment</td><td>(150) + 140 = (10)</td></tr>
    <tr><td>Sub-total: adjusted book profit</td><td>1,300</td></tr>
    <tr><td>Less: B/f loss or depreciation (lower of)</td><td>(80)</td></tr>
    <tr><td><strong>Book profit under Sec 115JB</strong></td><td><strong>1,220</strong></td></tr>
  </tbody>
</table>

<h2>Step 2 — Compute MAT</h2>
<p>MAT rate: 15% + surcharge (12% if income > ₹10 cr) + cess (4%).</p>
<p>Effective MAT rate ≈ 17.472%.</p>
<p>MAT = ₹1,220 × 17.472% ≈ <strong>₹213.16 cr</strong></p>

<h2>Step 3 — Compare with normal tax</h2>
<p>Normal corporate tax (assume normal regime): 25.168%.</p>
<p>Suppose normal taxable income is ₹600 cr (after various tax adjustments).</p>
<p>Normal tax = ₹600 × 25.168% ≈ ₹151.01 cr.</p>

<h2>Step 4 — Final tax liability</h2>
<p>Higher of normal tax (₹151.01 cr) or MAT (₹213.16 cr) → <strong>pay MAT ₹213.16 cr</strong>.</p>
<p>MAT credit carried forward = ₹213.16 − ₹151.01 = <strong>₹62.15 cr</strong> (can be utilised
against normal tax in future years for up to 15 AYs).</p>

<h2>Step 5 — Ind AS-specific adjustment items to remember</h2>
<p>For Ind AS preparers, Sec 115JB(2A) adds further book-profit adjustments:</p>
<ul>
  <li>Items in OCI that will not be reclassified to P&L (actuarial gains/losses, FVTOCI gains/losses on equity instruments) — included in book profit, but spread over 5 years for transition items.</li>
  <li>Demerger / amalgamation accounting under Ind AS 103 — capital reserve / goodwill on bargain purchase treated specifically.</li>
  <li>Service-concession arrangements, financial instrument adjustments — specific carve-outs.</li>
</ul>

<div class="callout">
<strong>Practical tip.</strong> If your company is eligible for the concessional regime under
Sec 115BAA (22%) or 115BAB (15%), MAT does <em>not</em> apply. Run the comparison before
default-electing the normal regime: MAT at effective 17.5% on book profit could be higher than
22% on taxable income for capital-intensive Ind AS companies with large depreciation gaps.
</div>
""",
    },
]
