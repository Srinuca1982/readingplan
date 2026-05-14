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
        "slug": "buyback-shareholder-tax",
        "title": "Buyback tax in shareholder's hands (post-Oct 2024 regime)",
        "subject": "Tax",
        "body": """
<h2>Facts</h2>
<p>Ms. Priya holds 1,000 equity shares of Vantage Ltd. (unlisted), each acquired in 2018 at
₹100. Vantage Ltd. announces a buyback at ₹350 per share on 15 January 2026. Priya tenders
all 1,000 shares.</p>

<h2>Step 1 — Pre-Oct 2024 vs Post-Oct 2024 treatment</h2>
<table>
  <thead><tr><th>Item</th><th>Pre-1 Oct 2024</th><th>Post-1 Oct 2024 (applicable here)</th></tr></thead>
  <tbody>
    <tr><td>Tax in company (115QA)</td><td>20% × (price − issue price)</td><td>NIL (115QA withdrawn)</td></tr>
    <tr><td>Tax in shareholder</td><td>Exempt u/s 10(34A)</td><td>Deemed dividend u/s 2(22); slab rate; TDS u/s 194 @ 10%</td></tr>
  </tbody>
</table>

<h2>Step 2 — Compute shareholder's tax exposure</h2>
<table>
  <tbody>
    <tr><td>Buyback consideration (1,000 × ₹350)</td><td>₹3,50,000</td></tr>
    <tr><td>Deemed dividend under Sec 2(22) — full amount</td><td>₹3,50,000</td></tr>
    <tr><td>Priya's slab (assume highest 30% + 4% cess + surcharge)</td><td>~33.59%</td></tr>
    <tr><td>Income tax on dividend</td><td>~₹1,17,565</td></tr>
    <tr><td>TDS u/s 194 @ 10% (deducted by company)</td><td>₹35,000</td></tr>
    <tr><td>Balance tax payable by Priya at return-filing</td><td>~₹82,565</td></tr>
  </tbody>
</table>

<h2>Step 3 — Capital loss on the bought-back shares</h2>
<p>Cost of acquisition: 1,000 × ₹100 = ₹1,00,000. Since the shares are extinguished and no
capital-gains consideration arises (the proceeds were treated as dividend), Priya is entitled
to a <strong>capital loss of ₹1,00,000</strong>. As long-term (held > 24 months for unlisted),
this is a long-term capital loss that can be set off only against long-term capital gains —
not against the dividend income.</p>

<h2>Step 4 — Net economic impact</h2>
<table>
  <tbody>
    <tr><td>Cash received</td><td>₹3,50,000</td></tr>
    <tr><td>Less: Tax on deemed dividend (33.59%)</td><td>(₹1,17,565)</td></tr>
    <tr><td>Net cash after tax</td><td>₹2,32,435</td></tr>
    <tr><td>Plus: LTCL of ₹1,00,000 to be carried forward and set off against future LTCG (potential future saving @ 12.5%)</td><td>₹12,500 (potential)</td></tr>
    <tr><td><strong>Net post-tax economic value</strong></td><td><strong>~₹2,44,935</strong></td></tr>
  </tbody>
</table>

<div class="callout">
<strong>Comparison with pre-Oct 2024 regime.</strong> Under the old framework, Priya would have
received ₹3,50,000 tax-free at her end (company paid ~₹50,000 buyback tax). Net to her: ₹3,50,000.
The shift to shareholder taxation costs her ~₹1,05,000 in net cash at the same slab rate. The
LTCL provides only partial recovery if she has future LTCG to offset.
</div>
""",
    },

    {
        "slug": "capital-reduction-tax",
        "title": "Capital reduction — deemed dividend vs return of capital",
        "subject": "Tax",
        "body": """
<h2>Facts</h2>
<p>Sigma Ltd. has 1 crore equity shares outstanding (face value ₹10, paid up). It undertakes
a capital reduction under Sec 66 paying ₹40 per share to shareholders. The company's
accumulated profits (free reserves + balance of P&L) as at the reduction date are ₹250 crore.</p>
<p>Aditya holds 1,00,000 shares acquired in 2019 at ₹35 each.</p>

<h2>Step 1 — Deemed dividend portion (Anarkali Sarabhai principle)</h2>
<p>Total payout: 1,00,000 × ₹40 = ₹40,00,000.</p>
<p>Sigma's accumulated profits attributable to Aditya's shareholding: ₹250 cr × (1,00,000 ÷
1,00,00,000) = ₹2,50,000.</p>
<p>Per Sec 2(22)(d) read with <em>Anarkali Sarabhai</em>:</p>
<table>
  <tbody>
    <tr><td>Payout up to attributable accumulated profits</td><td>₹2,50,000 → Deemed dividend</td></tr>
    <tr><td>Balance payout (₹40,00,000 − ₹2,50,000)</td><td>₹37,50,000 → Return of capital</td></tr>
  </tbody>
</table>

<h2>Step 2 — Tax on deemed dividend portion</h2>
<p>Slab rate (assume 30% + cess + surcharge) on ₹2,50,000:</p>
<p>Tax ≈ ₹2,50,000 × 33.59% ≈ <strong>₹83,975</strong>.</p>

<h2>Step 3 — Capital gain on return of capital portion</h2>
<p>The return of capital (₹37,50,000) is set off against the cost of acquisition. If the return
exceeds cost, the excess is a capital gain.</p>
<table>
  <tbody>
    <tr><td>Cost of acquisition (1,00,000 × ₹35)</td><td>₹35,00,000</td></tr>
    <tr><td>Return of capital portion</td><td>₹37,50,000</td></tr>
    <tr><td><strong>Capital gain (long-term — held > 24 months)</strong></td><td><strong>₹2,50,000</strong></td></tr>
  </tbody>
</table>
<p>LTCG on unlisted shares @ 12.5% (no indexation post-Budget 2024): ₹2,50,000 × 12.5% ≈
<strong>₹31,250</strong>.</p>

<h2>Step 4 — Cost of remaining shares (Sec 55(2)(v))</h2>
<p>After capital reduction, the original cost gets reduced by the return-of-capital portion:</p>
<p>Remaining cost = ₹35,00,000 − ₹37,50,000 = NIL (cost exhausted; future sale will have full
consideration as gain).</p>

<h2>Step 5 — Summary</h2>
<table>
  <tbody>
    <tr><td>Total payout received</td><td>₹40,00,000</td></tr>
    <tr><td>Tax on deemed dividend portion</td><td>(₹83,975)</td></tr>
    <tr><td>Tax on capital gain portion</td><td>(₹31,250)</td></tr>
    <tr><td><strong>Net after-tax cash to Aditya</strong></td><td><strong>~₹38,84,775</strong></td></tr>
  </tbody>
</table>

<div class="callout">
<strong>Planning insight.</strong> A capital reduction is significantly more tax-efficient than
a dividend distribution where (a) shareholders' cost basis is high relative to the payout
(absorbing the return-of-capital portion as basis reduction) and (b) the company has limited
accumulated profits. If the same payout were a dividend, the entire ₹40,00,000 would be
deemed dividend — tax exposure ~₹13.4 lakh vs ~₹1.15 lakh in the reduction structure.
</div>
""",
    },

    {
        "slug": "ind-as-21-foreign-currency",
        "title": "Ind AS 21 — Foreign currency monetary & non-monetary items at year-end",
        "subject": "Ind AS",
        "body": """
<h2>Facts</h2>
<p>OmegaTech Ltd. has the following balances in foreign currency as at 31 March 2027:</p>
<table>
  <thead><tr><th>Item</th><th>Currency</th><th>Amount</th><th>Rate when arose</th><th>Closing rate (31 Mar 2027)</th></tr></thead>
  <tbody>
    <tr><td>Trade receivables from US customer</td><td>USD</td><td>2,00,000</td><td>₹82/$</td><td>₹83.50/$</td></tr>
    <tr><td>Trade payable to German supplier</td><td>EUR</td><td>1,00,000</td><td>₹89/€</td><td>₹91/€</td></tr>
    <tr><td>External Commercial Borrowing (ECB)</td><td>USD</td><td>10,00,000</td><td>₹81/$</td><td>₹83.50/$</td></tr>
    <tr><td>Advance paid to supplier (refundable in INR)</td><td>USD-denominated invoice</td><td>50,000</td><td>₹82.50/$</td><td>₹83.50/$</td></tr>
    <tr><td>Inventory purchased in EUR</td><td>EUR</td><td>50,000</td><td>₹87/€</td><td>₹91/€</td></tr>
  </tbody>
</table>

<h2>Step 1 — Classify each item as monetary vs non-monetary</h2>
<table>
  <thead><tr><th>Item</th><th>Type</th><th>Reason</th></tr></thead>
  <tbody>
    <tr><td>Trade receivables</td><td>Monetary</td><td>Right to receive a determined amount of cash</td></tr>
    <tr><td>Trade payable</td><td>Monetary</td><td>Obligation to pay a determined amount of cash</td></tr>
    <tr><td>ECB (foreign currency loan)</td><td>Monetary</td><td>Loan repayable in determined cash</td></tr>
    <tr><td>Refundable advance (INR settlement)</td><td>Non-monetary</td><td>Settlement is in INR; the FX value is irrelevant. Per Ind AS 21, classification depends on settlement currency.</td></tr>
    <tr><td>Inventory</td><td>Non-monetary</td><td>Not a contractual right to cash; held for sale</td></tr>
  </tbody>
</table>

<h2>Step 2 — Retranslate monetary items at closing rate; non-monetary items at historical rate</h2>
<table>
  <thead><tr><th>Item</th><th>At inception (₹)</th><th>At year-end (₹)</th><th>Difference (₹)</th><th>Recognise where</th></tr></thead>
  <tbody>
    <tr><td>Receivables (2,00,000 × $)</td><td>1,64,00,000</td><td>1,67,00,000</td><td>+3,00,000 (gain)</td><td>P&L</td></tr>
    <tr><td>Payables (1,00,000 × €)</td><td>89,00,000</td><td>91,00,000</td><td>(2,00,000) loss</td><td>P&L</td></tr>
    <tr><td>ECB (10,00,000 × $)</td><td>8,10,00,000</td><td>8,35,00,000</td><td>(25,00,000) loss</td><td>P&L (or capitalised if qualifying asset under Ind AS 23)</td></tr>
    <tr><td>Refundable advance</td><td>41,25,000</td><td>41,25,000 (no retranslation)</td><td>NIL</td><td>—</td></tr>
    <tr><td>Inventory</td><td>43,50,000</td><td>43,50,000 (no retranslation)</td><td>NIL</td><td>—</td></tr>
  </tbody>
</table>

<h2>Step 3 — Net P&L impact</h2>
<p>Gain on receivables ₹3,00,000 − Loss on payables ₹2,00,000 − Loss on ECB ₹25,00,000 =
<strong>Net exchange loss ₹24,00,000</strong> in P&L (under "Finance costs / Other expenses").</p>

<h2>Step 4 — Disclosures</h2>
<ul>
  <li>The amount of exchange differences recognised in P&L (and OCI for foreign-operation translation).</li>
  <li>Functional currency, presentation currency.</li>
  <li>If functional currency differs from presentation currency, the rates used and the reason.</li>
</ul>

<div class="callout">
<strong>Common error.</strong> Classifying a foreign-currency-denominated <em>but
INR-settled</em> receivable/payable as monetary. The classification depends on the
<em>settlement currency</em>, not the invoice currency. Always check the contractual
settlement terms.
</div>
""",
    },

    {
        "slug": "internal-audit-p2p-rcm",
        "title": "Internal audit — Risk and Control Matrix for Procure-to-Pay",
        "subject": "Internal Audit",
        "body": """
<h2>Process: Procure-to-Pay (P2P) — abridged RCM</h2>
<p>The Risk and Control Matrix is the foundational internal-audit deliverable for any
process. Below is an abridged RCM for the P2P cycle.</p>

<table>
  <thead><tr><th>Process step</th><th>Risk (What could go wrong)</th><th>Control</th><th>Type</th><th>Frequency</th><th>Test approach</th></tr></thead>
  <tbody>
    <tr>
      <td>1. Vendor master maintenance</td>
      <td>Unauthorised changes to vendor bank details enable diversion of payments</td>
      <td>All vendor master changes require dual approval (request by AP, approve by Finance Head); system logs all changes</td>
      <td>Preventive, manual, key</td>
      <td>Per change</td>
      <td>Sample 25 vendor changes from the year; verify dual approval and bank-detail change rationale</td>
    </tr>
    <tr>
      <td>2. Purchase requisition (PR)</td>
      <td>PR raised without business justification or budget approval</td>
      <td>System-enforced approval matrix (e.g., HOD ≤ ₹10L; CFO ≤ ₹1Cr; CEO > ₹1Cr); budget check at PR creation</td>
      <td>Preventive, automated, key</td>
      <td>Per transaction</td>
      <td>Sample 30 POs across approval levels; verify approver was within delegation and budget existed</td>
    </tr>
    <tr>
      <td>3. PO creation</td>
      <td>PO terms (price, quantity, payment terms) differ from approved PR</td>
      <td>System validates PO against PR; variances flagged for re-approval</td>
      <td>Preventive, automated</td>
      <td>Per transaction</td>
      <td>Review system flag-and-block log; sample 15 flagged exceptions and verify resolution</td>
    </tr>
    <tr>
      <td>4. Goods receipt (GRN)</td>
      <td>Goods/services not received or received in lesser quantity than billed</td>
      <td>Three-way match: PO + GRN + Invoice must reconcile; variances ≤ tolerance auto-approved, above tolerance routed for explanation</td>
      <td>Detective, automated, key</td>
      <td>Per transaction</td>
      <td>Sample 40 invoices; trace to PO and GRN; verify match or rationale for variance</td>
    </tr>
    <tr>
      <td>5. Invoice processing</td>
      <td>Duplicate invoices paid (same invoice number from same vendor)</td>
      <td>System duplicate-invoice check on (vendor ID + invoice number + invoice date)</td>
      <td>Preventive, automated</td>
      <td>Per transaction</td>
      <td>Run CAAT to identify duplicate invoice number-vendor combinations from full year; verify each is genuinely duplicate or appropriately handled</td>
    </tr>
    <tr>
      <td>6. Payment release</td>
      <td>Payment to wrong bank account due to compromised vendor details or social engineering</td>
      <td>Payment confirmation call to vendor on bank-detail changes; segregation between vendor master and payment authorisation</td>
      <td>Preventive, manual + automated</td>
      <td>Per change</td>
      <td>Sample 15 bank-detail changes in past year and confirm the verification call log; check SoD via user access report</td>
    </tr>
    <tr>
      <td>7. TDS deduction</td>
      <td>TDS not deducted, deducted at wrong rate, or not deposited timely → Sec 40(a)(ia) disallowance</td>
      <td>Vendor master tagged with TDS section and rate; automated deduction at payment; monthly TDS reconciliation</td>
      <td>Preventive + detective, automated</td>
      <td>Per transaction</td>
      <td>Sample 25 vendor payments across TDS sections; verify rate, deduction, deposit date and Form 26Q filing</td>
    </tr>
    <tr>
      <td>8. Bank reconciliation</td>
      <td>Unauthorised / unrecorded payments going through the operating bank</td>
      <td>Monthly bank reconciliation by independent person (not the payment authoriser); CFO review</td>
      <td>Detective, manual, key</td>
      <td>Monthly</td>
      <td>Inspect 6 months of bank reconciliations; verify all open items investigated; CFO review evidence</td>
    </tr>
  </tbody>
</table>

<div class="callout">
<strong>Practical tip.</strong> Build the RCM in a spreadsheet with the columns above plus an
"observation" and "rating" column populated during fieldwork. The RCM becomes both the test
plan AND the findings report. One unified working paper per process.
</div>
""",
    },

    {
        "slug": "labour-wage-impact",
        "title": "Labour codes — wage definition impact on PF / gratuity",
        "subject": "Labour",
        "body": """
<h2>Facts</h2>
<p>Mr. Karthik draws a CTC of ₹12,00,000 per annum at Acme Pvt. Ltd. The current CTC
structure is:</p>
<table>
  <tbody>
    <tr><td>Basic Salary</td><td>₹3,00,000 (25% of CTC)</td></tr>
    <tr><td>HRA</td><td>₹1,50,000</td></tr>
    <tr><td>Special Allowance</td><td>₹4,50,000</td></tr>
    <tr><td>LTA, Telephone, Books etc.</td><td>₹1,80,000</td></tr>
    <tr><td>Employer PF (12% on Basic only)</td><td>₹36,000</td></tr>
    <tr><td>Employer Gratuity (4.81% on Basic)</td><td>₹14,430</td></tr>
    <tr><td>Other</td><td>~₹69,570</td></tr>
    <tr><td><strong>Total CTC</strong></td><td><strong>₹12,00,000</strong></td></tr>
  </tbody>
</table>

<h2>Step 1 — Identify the issue under Code on Wages</h2>
<p>Section 2(y) of Code on Wages 2019 mandates that the "wages" (broadly basic + DA + retaining
allowance) must be at least 50% of the total remuneration. Where excluded allowances (HRA,
LTA, special allowance, etc.) exceed 50% of remuneration, the excess is <strong>added back to
wages</strong> for statutory contributions.</p>

<h2>Step 2 — Apply the 50% test</h2>
<table>
  <tbody>
    <tr><td>Total remuneration (CTC excluding employer contributions)</td><td>₹10,80,000</td></tr>
    <tr><td>Basic (current)</td><td>₹3,00,000 (27.8%)</td></tr>
    <tr><td>50% floor required</td><td>₹5,40,000</td></tr>
    <tr><td>Add-back to "wages"</td><td>₹2,40,000 (5,40,000 − 3,00,000)</td></tr>
    <tr><td><strong>Effective wages for PF/gratuity computation</strong></td><td><strong>₹5,40,000</strong></td></tr>
  </tbody>
</table>

<h2>Step 3 — Recompute statutory contributions under the new wage definition</h2>
<table>
  <thead><tr><th></th><th>Current (Basic-only)</th><th>Post-Codes (50% floor)</th><th>Increase</th></tr></thead>
  <tbody>
    <tr><td>Employer PF (12%)</td><td>₹36,000</td><td>₹64,800</td><td>+₹28,800</td></tr>
    <tr><td>Employee PF (12%)</td><td>₹36,000</td><td>₹64,800</td><td>+₹28,800</td></tr>
    <tr><td>Gratuity provision (4.81%)</td><td>₹14,430</td><td>₹25,974</td><td>+₹11,544</td></tr>
    <tr><td><strong>Total cost increase per employee</strong></td><td></td><td></td><td><strong>~₹69,144 / year (5.8% of CTC)</strong></td></tr>
  </tbody>
</table>

<h2>Step 4 — Karthik's take-home impact</h2>
<table>
  <tbody>
    <tr><td>Current net take-home (after Employee PF ₹36,000)</td><td>₹10,44,000 gross less tax</td></tr>
    <tr><td>Post-Codes net take-home (after Employee PF ₹64,800)</td><td>₹10,15,200 gross less tax</td></tr>
    <tr><td><strong>Reduction in take-home</strong></td><td><strong>₹28,800 / year (~₹2,400 / month)</strong></td></tr>
  </tbody>
</table>

<h2>Step 5 — Restructuring CTC to mitigate</h2>
<p>Options for the employer:</p>
<ul>
  <li><strong>Status quo</strong> — absorb the 5.8% increase as compliance cost.</li>
  <li><strong>Restructure CTC</strong> — keep total CTC at ₹12 lakh but increase basic to 50% (₹6 lakh) and reduce allowances proportionately. Same compliance cost but full transparency.</li>
  <li><strong>Cap PF at threshold</strong> — many employers will opt to contribute PF only up to the statutory wage ceiling (₹15,000/month = ₹1.8 lakh/year), shifting the burden away. Requires careful drafting in offer letter.</li>
  <li><strong>Pass through</strong> — increase gross CTC by ~5.8% to maintain take-home.</li>
</ul>

<div class="callout">
<strong>Drafting consideration.</strong> When restructuring offer letters, distinguish between
"Basic + DA" (subject to 50% test) and "wages" (the broader definition used by the Codes for
PF/gratuity computation). Employee retention can be sensitive — communicate the change
transparently before implementation. Most large employers are running the impact in HR
modelling tools before State Rules are notified.
</div>
""",
    },

    {
        "slug": "merger-tax-loss-72a",
        "title": "Sec 72A — Carry-forward of business loss on amalgamation",
        "subject": "Tax",
        "body": """
<h2>Facts</h2>
<p>Sunrise Mfg. Ltd. (an industrial undertaking) has accumulated business loss of ₹500 cr and
unabsorbed depreciation of ₹200 cr as of 31 March 2026. Skyline Ltd., a profitable industrial
unit, is acquiring Sunrise via amalgamation effective 1 April 2026.</p>
<p>Both companies have been engaged in their respective businesses for over 5 years. Sunrise
has held its industrial assets for 4 years (book value ₹600 cr) and continues to operate at
60% capacity.</p>

<h2>Step 1 — Eligibility conditions under Sec 72A(1)</h2>
<table>
  <thead><tr><th>Condition</th><th>Sunrise (amalgamating)</th><th>Skyline (amalgamated)</th></tr></thead>
  <tbody>
    <tr><td>Industrial undertaking?</td><td>✓ Mfg</td><td>✓ Mfg</td></tr>
    <tr><td>Engaged in business for ≥ 3 yrs</td><td>✓ (5+ years)</td><td>—</td></tr>
    <tr><td>Held ≥ 3/4 of fixed assets for ≥ 2 yrs</td><td>✓ (4 years; assumed met)</td><td>—</td></tr>
    <tr><td>Continue business for ≥ 5 years post-amalgamation</td><td>—</td><td>Will continue (commitment)</td></tr>
    <tr><td>Hold ≥ 3/4 of acquired fixed assets for ≥ 5 yrs</td><td>—</td><td>Will hold (commitment)</td></tr>
    <tr><td>Achieve ≥ 50% of installed capacity within 4 yrs</td><td>—</td><td>Currently at 60% (already met)</td></tr>
  </tbody>
</table>
<p>All conditions satisfied → Skyline is entitled to carry forward Sunrise's losses.</p>

<h2>Step 2 — Compute available loss carry-forward</h2>
<table>
  <tbody>
    <tr><td>Sunrise's accumulated business loss (deemed Skyline's)</td><td>₹500 cr</td></tr>
    <tr><td>Sunrise's unabsorbed depreciation (deemed Skyline's)</td><td>₹200 cr</td></tr>
    <tr><td><strong>Total carry-forward to Skyline</strong></td><td><strong>₹700 cr</strong></td></tr>
  </tbody>
</table>

<h2>Step 3 — Skyline's projected tax benefit</h2>
<p>Assume Skyline expects post-merger taxable profit (before set-off) of ₹150 cr per annum
for next 5 years.</p>
<table>
  <thead><tr><th>Year</th><th>Profit before set-off</th><th>Set-off</th><th>Taxable</th><th>Loss remaining</th></tr></thead>
  <tbody>
    <tr><td>FY27</td><td>150</td><td>150</td><td>0</td><td>550</td></tr>
    <tr><td>FY28</td><td>150</td><td>150</td><td>0</td><td>400</td></tr>
    <tr><td>FY29</td><td>150</td><td>150</td><td>0</td><td>250</td></tr>
    <tr><td>FY30</td><td>150</td><td>150</td><td>0</td><td>100</td></tr>
    <tr><td>FY31</td><td>150</td><td>100</td><td>50</td><td>0</td></tr>
  </tbody>
</table>
<p>Total set-off realised: ₹700 cr. Tax saved (assuming 25.168% effective rate): 700 × 25.168%
= <strong>~₹176 cr</strong> over 5 years.</p>

<h2>Step 4 — Compliance and monitoring</h2>
<ul>
  <li>Skyline must hold ≥ 3/4 of fixed assets acquired from Sunrise for 5 years (sale or transfer of significant fixed assets triggers 47A claw-back).</li>
  <li>Skyline must operate at ≥ 50% capacity within 4 years.</li>
  <li>If any condition is breached within 5 years, the loss carry-forward is withdrawn under Sec 47A and the unutilised portion becomes immediately taxable as income of the year of breach.</li>
  <li>Audit firm should maintain a Sec 72A monitoring memo for each subsequent year confirming compliance.</li>
</ul>

<div class="callout">
<strong>Note for non-industrial businesses.</strong> Sec 72A only applies to "industrial
undertakings" as defined in Sec 72A(7) — manufacturing, processing, hotels (defined classes),
operation of ships/aircraft. Pure trading and most services are <em>not eligible</em> for
loss carry-forward via amalgamation. For services businesses, alternative structures (e.g.,
asset acquisition with separate compensation, IBC-route Sec 79(2)(c)) must be considered.
</div>
""",
    },

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
