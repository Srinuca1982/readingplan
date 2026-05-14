"""Case-law digests — landmark decisions in Indian corporate restructuring.

Contains foundational classics (Marshall Sons, Anarkali Sarabhai, Essar Steel etc.)
plus recent additions from 2025–2026 on CCI-IBC interplay, clean-slate refinements,
valuation-in-schemes, GST ITC portability, and composite-scheme stamp duty.
"""

CASELAW = [
    {
        "slug": "marshall-sons",
        "title": "Marshall Sons & Co. (India) Ltd. v. ITO (1997)",
        "summary": "The appointed date in a sanctioned scheme is binding — even though the court order comes much later.",
        "body": """
<h4>Citation</h4>
<p>(1997) 223 ITR 809 (SC)</p>

<h4>Court</h4>
<p>Supreme Court of India.</p>

<h4>The point of law</h4>
<p>Whether the amalgamation under a court-sanctioned scheme is effective from the date specified
in the scheme (the "appointed date") or from the date the court order is filed with the ROC.</p>

<h4>The facts</h4>
<p>A scheme of amalgamation specified an appointed date of 1 January 1982. The High Court sanctioned
the scheme much later. The Income-tax Officer attempted to assess the amalgamating company for the
period between the appointed date and the order date, treating the amalgamating company as a
separate taxable entity for that interim period.</p>

<h4>The holding</h4>
<blockquote>
"Every scheme of amalgamation has to necessarily provide a date with effect from which the
amalgamation shall take place. […] Once the court sanctions the scheme, the amalgamation takes
effect from the date specified in the scheme, even though the court's sanction comes much later."
</blockquote>
<p>The appointed date is binding on the tax authorities. From the appointed date, the amalgamating
company ceases to exist as a separate taxable entity; income arising from its business thereafter
is the income of the amalgamated company.</p>

<h4>Why it matters</h4>
<ul>
  <li>This is the foundational case on the appointed date doctrine. Every scheme of arrangement —
      amalgamation, demerger, slump exchange — operates on a backdated effectiveness premise,
      and tax authorities cannot ignore it.</li>
  <li>The case has been applied across statutes — for income-tax, sales tax, VAT and GST treatment
      of the interim period.</li>
  <li>However, MCA's August 2019 circular limits how far back the appointed date can be — generally
      not more than 12 months prior to filing — to prevent abuse.</li>
</ul>

<div class="callout">
<strong>Practice point.</strong> Where the appointed date precedes the order date by &gt; 1 year,
the company should file: (a) consolidated/combined return for the post-appointed-date period in the
amalgamated company's name, (b) revised return for any earlier filings made in the amalgamating
company's name. The CBDT has issued circulars facilitating this; ensure compliance with the
mechanical reconciliation.
</div>
""",
    },

    {
        "slug": "saraswati-industrial-syndicate",
        "title": "Saraswati Industrial Syndicate Ltd. v. CIT (1990)",
        "summary": "On amalgamation, the amalgamating company ceases to exist; the amalgamated company is its successor for tax purposes.",
        "body": """
<h4>Citation</h4>
<p>(1990) 186 ITR 278 (SC)</p>

<h4>Court</h4>
<p>Supreme Court of India.</p>

<h4>The point of law</h4>
<p>What is the legal effect of amalgamation on the identity of the amalgamating company, and the
tax assessment of post-amalgamation events?</p>

<h4>The holding</h4>
<blockquote>
"When two companies amalgamate and merge into one, the transferor company loses its entity as it
ceases to have its business. However, their respective rights or liabilities are determined under
the scheme of amalgamation, but the corporate entity of the transferor company ceases to exist with
effect from the date the amalgamation is made effective."
</blockquote>

<h4>Why it matters</h4>
<ul>
  <li>Establishes that the amalgamated company is the <strong>successor</strong> of the amalgamating
      company for all purposes — assets, liabilities, pending proceedings, statutory licences.</li>
  <li>Pending tax assessments of the amalgamating company become assessments of the amalgamated
      company. Notices must be served on the amalgamated company; notices in the amalgamating
      company's name post-amalgamation are void (the celebrated <em>Spice Entertainment</em> and
      <em>Maruti Suzuki India Ltd.</em> line follows this principle).</li>
  <li>The carry-forward of losses under Sec 72A flows from this — the amalgamated company "steps
      into the shoes" of the amalgamating company.</li>
</ul>

<h4>Subsequent application</h4>
<p>This principle was reaffirmed and extended in <strong>PCIT v. Maruti Suzuki India Ltd. (2019) 416
ITR 613 (SC)</strong> — a tax assessment order issued in the name of the non-existent amalgamating
company is a nullity, even if the amalgamated company participates in proceedings. Tax officers must
update their records on receiving intimation of amalgamation.</p>
""",
    },

    {
        "slug": "anarkali-sarabhai",
        "title": "Anarkali Sarabhai v. CIT (1997)",
        "summary": "Capital reduction with payment to shareholders is taxable as dividend to the extent of accumulated profits.",
        "body": """
<h4>Citation</h4>
<p>(1997) 224 ITR 422 (SC)</p>

<h4>Court</h4>
<p>Supreme Court of India.</p>

<h4>The point of law</h4>
<p>Is the amount received by a shareholder on reduction of share capital under Sec 66 (then Sec 100
of the Companies Act 1956) a capital receipt — or a deemed dividend under Sec 2(22)(d) of the
Income-tax Act?</p>

<h4>The facts</h4>
<p>The shareholder received a substantial sum from the company on a court-sanctioned reduction of
the share capital. The company had significant accumulated profits. The Revenue argued the receipt
was a deemed dividend under Sec 2(22)(d) to the extent of the accumulated profits.</p>

<h4>The holding</h4>
<blockquote>
"Any distribution by the company on the reduction of its capital is, to the extent to which the
company possesses accumulated profits, a deemed dividend, whether capitalised or not, in the hands
of the recipient shareholder."
</blockquote>

<p>Mechanics:</p>
<ul>
  <li>Distribution ≤ accumulated profits → deemed dividend.</li>
  <li>Distribution &gt; accumulated profits → balance is return of capital; reduces cost of acquisition.</li>
</ul>

<h4>Why it matters</h4>
<ul>
  <li>Every capital reduction in a profitable company must now be analysed through this lens.</li>
  <li>Companies sometimes structure capital reductions believing them tax-neutral — they are
      <em>not</em>, to the extent of accumulated profits.</li>
  <li>Post-April 2020 (dividend taxation regime change), the deemed dividend is taxed at the
      shareholder's slab rate; the older DDT regime no longer applies.</li>
</ul>

<div class="callout">
<strong>Planning note.</strong> If the goal is to return surplus to shareholders without a dividend
charge, a buyback under Sec 68 was traditionally preferred — but post-October 2024 the same
shareholder-level deemed-dividend treatment now applies to buyback too. Capital reduction and
buyback are now broadly tax-equivalent for distribution-to-shareholder purposes.
</div>
""",
    },

    {
        "slug": "mcdowell",
        "title": "McDowell & Co. Ltd. v. CTO (1985)",
        "summary": "The colourable-device doctrine — tax planning that lacks commercial substance is not legitimate.",
        "body": """
<h4>Citation</h4>
<p>(1985) 154 ITR 148 (SC)</p>

<h4>Court</h4>
<p>Supreme Court of India.</p>

<h4>The point of law</h4>
<p>Is artificial tax planning, designed to avoid liability through colourable means rather than
genuine commercial transactions, permissible under Indian tax law?</p>

<h4>The holding</h4>
<blockquote>
"Tax planning may be legitimate provided it is within the framework of the law. Colourable devices
cannot be part of tax planning and it is wrong to encourage or entertain the belief that it is
honourable to avoid the payment of tax by resorting to dubious methods."
</blockquote>

<h4>Why it matters in restructuring</h4>
<ul>
  <li>Every scheme of arrangement that is designed primarily for tax savings, with little or no
      commercial rationale, can be tested against McDowell.</li>
  <li>Recurring use: schemes that "move" losses to a profit-making group company purely to set them
      off; or schemes that exploit the appointed-date doctrine to backdate income/loss recognition.</li>
  <li>The doctrine has been refined in <strong>Union of India v. Azadi Bachao Andolan (2003) 263 ITR
      706 (SC)</strong> and <strong>Vodafone International Holdings v. Union of India (2012) 341 ITR 1
      (SC)</strong> — the Court drew a line between "tax planning" (permissible) and "tax avoidance"
      (impermissible), with the substance-over-form test.</li>
</ul>

<h4>The GAAR overlay (post-2017)</h4>
<p>Chapter X-A of the Income-tax Act 1961 — the General Anti-Avoidance Rule — codifies the
McDowell substance-over-form principle. An "impermissible avoidance arrangement" with the main
purpose of obtaining a tax benefit can be re-characterised, and tax benefits denied. Restructuring
schemes must therefore demonstrate <em>commercial substance</em>, not just legal form.</p>

<div class="callout">
<strong>Documentation discipline.</strong> Every scheme should have a contemporaneous board paper
articulating the commercial rationale — synergies, focus, regulatory, succession. The board paper
is the first thing GAAR officers ask for. A scheme with only tax savings on the rationale slide
is GAAR bait.
</div>
""",
    },

    {
        "slug": "vodafone",
        "title": "Vodafone International Holdings BV v. Union of India (2012)",
        "summary": "Indirect transfer of Indian assets through offshore share sale was not taxable in India under the pre-amendment law.",
        "body": """
<h4>Citation</h4>
<p>(2012) 341 ITR 1 (SC)</p>

<h4>Court</h4>
<p>Supreme Court of India.</p>

<h4>The facts</h4>
<p>In 2007, Vodafone (a Netherlands-incorporated entity) acquired Hutchison's stake in Hutchison Essar
(an Indian telecom operator) through the acquisition of shares of CGP Investments — a Cayman Islands
holding company that ultimately held the Indian operating company. The Indian tax department issued
a withholding-tax demand of ~₹11,000 crore, treating the transaction as a transfer of Indian assets.</p>

<h4>The holding</h4>
<blockquote>
"The sale of CGP shares by HTIL to Vodafone has been wrongly characterised by the Department as the
sale of underlying Indian assets. The transaction was a bona fide structured FDI investment into
India … not taxable in India under the law as it stood at the relevant time."
</blockquote>
<p>The Court held that:</p>
<ul>
  <li>Sec 9 (deemed Indian income) as it stood did not extend to <em>indirect</em> transfers of Indian assets.</li>
  <li>Form (offshore share sale) prevailed over substance — provided there was genuine commercial substance and the offshore structure was not a sham.</li>
  <li>Withholding under Sec 195 cannot apply where the income itself is not chargeable in India.</li>
</ul>

<h4>The legislative reaction</h4>
<p>Parliament responded with the <strong>Finance Act 2012</strong> introducing <strong>retrospective
amendments</strong> to Sec 9(1)(i) and Sec 195, expressly bringing indirect transfers of shares deriving
their value <em>substantially</em> from Indian assets within the Indian tax net. The retrospective
nature triggered international criticism and bilateral disputes; eventually, in <strong>August 2021</strong>,
the retrospective application was withdrawn via the Taxation Laws (Amendment) Act 2021.</p>

<h4>Why it matters in restructuring</h4>
<ul>
  <li>Cross-border restructurings involving Indian assets must always check Sec 9(1)(i) indirect-transfer
      applicability. The threshold: target derives ≥ 50% of value from Indian assets and the value of
      Indian assets exceeds ₹10 crore.</li>
  <li>Genuine commercial-substance documentation is the best defence under GAAR + Sec 9(1)(i).</li>
  <li>For inbound cross-border mergers under Sec 234, Sec 47(via)/(vic)/(vicc) exemptions must be
      independently met — they are not a default carve-out from indirect-transfer.</li>
</ul>
""",
    },

    {
        "slug": "miheer-mafatlal",
        "title": "Miheer H. Mafatlal v. Mafatlal Industries Ltd. (1996)",
        "summary": "The court's role in sanctioning a scheme is supervisory, not appellate — it does not substitute its commercial judgment.",
        "body": """
<h4>Citation</h4>
<p>(1996) 87 Comp Cas 792 (SC)</p>

<h4>Court</h4>
<p>Supreme Court of India.</p>

<h4>The point of law</h4>
<p>What is the scope of a court's jurisdiction when sanctioning a scheme of arrangement under
Sec 391 of the Companies Act 1956 (now Sec 230–232 of the 2013 Act)? Should the court enquire
into the commercial merit, fairness of share exchange ratio, etc.?</p>

<h4>The holding — the seven-fold test</h4>
<p>The Court laid down the principles guiding judicial review of schemes:</p>
<ol>
  <li>Statutory procedure followed and meetings duly held.</li>
  <li>The scheme is backed by the requisite statutory majority — ≥ 3/4 in value.</li>
  <li>Concerned meetings are representative of the class.</li>
  <li>No coercion or fraud; majority decides bona fide for the class.</li>
  <li>The scheme is not violative of any law and is not contrary to public policy.</li>
  <li>All material facts have been disclosed.</li>
  <li>The scheme is not unconscionable; it is one which a reasonable shareholder would approve.</li>
</ol>

<blockquote>
"The court does not sit as a court of appeal over the commercial wisdom of the parties; it does not
substitute its own judgment for the commercial judgment of those who voted in favour."
</blockquote>

<h4>Why it matters</h4>
<ul>
  <li>The Miheer Mafatlal principles are now the standard NCLT applies when sanctioning schemes
      under Sec 232.</li>
  <li>Objections to a scheme that merely argue "the exchange ratio is unfair" rarely succeed if
      (a) the ratio was approved by the statutory majority, and (b) there is a valuation report by
      an independent valuer.</li>
  <li>Where objections allege oppression of minority, non-disclosure, or violation of law, the NCLT
      has full power to remand or reject.</li>
</ul>

<h4>Subsequent development</h4>
<p>The principles were applied in <strong>Hindustan Lever Employees' Union v. Hindustan Lever Ltd.
(1995) 83 Comp Cas 30 (SC)</strong> — employee welfare considerations within a scheme — and
<strong>Wood Polymer Ltd., In re (1977) 47 Comp Cas 597 (Guj)</strong> — the leading early case on
court's discretion.</p>
""",
    },

    {
        "slug": "hindustan-lever",
        "title": "Hindustan Lever Employees' Union v. HLL (1995)",
        "summary": "Employee interests can be raised before the court but rarely override majority approval if the scheme is otherwise fair.",
        "body": """
<h4>Citation</h4>
<p>(1995) 83 Comp Cas 30 (SC)</p>

<h4>Court</h4>
<p>Supreme Court of India.</p>

<h4>The point of law</h4>
<p>Can employees of a company affected by a scheme of amalgamation challenge the scheme on grounds
of employee interest, even when the statutory majorities of shareholders and creditors have approved
it?</p>

<h4>The holding</h4>
<p>The Supreme Court held that <em>employees are not a "class"</em> within Sec 391/394 of the
Companies Act 1956 (now Sec 230 of 2013), and therefore do not have a statutory right to a meeting
of their own. However, the court may consider representations from employees as part of the broader
public-interest enquiry under Sec 394(1) (proviso).</p>

<p>In the specific case, the scheme involved the merger of TOMCO into HLL. The Union challenged on
grounds of (a) likely lay-offs, (b) loss of bargaining position. The Court found that:</p>
<ul>
  <li>The scheme expressly preserved employment terms.</li>
  <li>The majority of shareholders had approved with full disclosure.</li>
  <li>There was no evidence of mala fides.</li>
</ul>
<p>The scheme was sanctioned.</p>

<h4>Why it matters</h4>
<ul>
  <li>The case settles that employees are not entitled to vote on a scheme — they cannot block it.</li>
  <li>However, schemes that <em>retrench employees</em>, change service conditions, or do not
      preserve continuity-of-service are vulnerable to objections.</li>
  <li>Standard scheme practice now includes <strong>express preservation of employment terms</strong>
      — "employees of the transferor shall continue to be employed by the transferee on the same
      terms and conditions of service".</li>
</ul>
""",
    },

    {
        "slug": "essar-steel",
        "title": "CoC of Essar Steel India Ltd. v. Satish Kumar Gupta (2019)",
        "summary": "The 'clean slate' doctrine — once a resolution plan is approved, all undisclosed past liabilities are extinguished.",
        "body": """
<h4>Citation</h4>
<p>(2020) 8 SCC 531</p>

<h4>Court</h4>
<p>Supreme Court of India.</p>

<h4>The facts</h4>
<p>ArcelorMittal's resolution plan for Essar Steel was approved by NCLT after a prolonged contest
with operational creditors who claimed they were paid disproportionately less than financial
creditors. Multiple appeals reached the Supreme Court on (a) the CoC's commercial wisdom, (b)
treatment of operational creditors vs financial creditors, (c) the binding effect of the approved
plan on undisclosed past dues.</p>

<h4>The holding</h4>
<p>The Court laid down two foundational principles:</p>

<h4>1. Primacy of CoC's commercial wisdom</h4>
<blockquote>
"The CoC's commercial wisdom is non-justiciable except on the grounds set out in Section 30(2) of
the Code. Courts will not interfere with the CoC's commercial decisions on whether a particular
resolution plan is the best one."
</blockquote>

<h4>2. The clean-slate doctrine</h4>
<blockquote>
"On the date of approval of the resolution plan by the Adjudicating Authority, all such claims, which
are not part of the resolution plan, shall stand extinguished … No person shall be entitled to
initiate or continue any proceedings in respect to a claim which is not part of the resolution plan."
</blockquote>

<p>This was further codified by the 2019 amendment to <strong>Sec 31 of the IBC</strong>, expressly
stating that the approved plan binds all stakeholders including the Central / State Government and
any local authority.</p>

<h4>Why it matters in restructuring</h4>
<ul>
  <li>The IBC resolution-plan route is now the only mechanism in Indian law that provides a
      <strong>true clean slate</strong> — including against statutory and tax authorities.</li>
  <li>For a successful resolution applicant, even unknown contingent liabilities and undisclosed
      tax demands of past periods are extinguished — this is uniquely valuable when acquiring a
      distressed business with messy historical records.</li>
  <li>The principle has been extended in subsequent cases (<em>Ghanashyam Mishra and Sons v.
      Edelweiss ARC</em>, <em>RPS Infrastructure v. Mukul Kumar</em>) — statutory dues not part of
      the approved plan are also extinguished.</li>
</ul>

<div class="callout">
<strong>M&A planning point.</strong> A buyer evaluating a distressed target should compare a Sec 230
scheme route with the IBC resolution-plan route on this dimension alone. The clean-slate advantage
of the IBC route is often worth the procedural overhead.
</div>
""",
    },

    {
        "slug": "maruti-suzuki",
        "title": "PCIT v. Maruti Suzuki India Ltd. (2019)",
        "summary": "A tax assessment order issued in the name of a non-existent (amalgamated-away) entity is a nullity.",
        "body": """
<h4>Citation</h4>
<p>(2019) 416 ITR 613 (SC)</p>

<h4>Court</h4>
<p>Supreme Court of India.</p>

<h4>The facts</h4>
<p>Maruti Suzuki India Ltd. was the successor to Suzuki Powertrain India Ltd. (SPIL) following an
amalgamation effective 1 April 2012. The amalgamation was duly intimated to the Assessing Officer
in March 2013. Despite this, the AO issued the assessment order in the name of SPIL — a non-existent
entity at that date.</p>

<h4>The holding</h4>
<blockquote>
"Once the amalgamating entity ceases to exist, no notice or order in its name can be valid. The
amalgamated entity is the successor for all purposes, and proceedings must be conducted against
it … An assessment order in the name of a non-existent entity is a nullity. Mere participation by
the successor in the proceedings cannot cure the jurisdictional defect."
</blockquote>

<h4>Why it matters</h4>
<ul>
  <li>This is the standard authority cited when tax notices/orders are received in the name of the
      amalgamating company post-merger.</li>
  <li>The principle protects taxpayers from delays and confusion when the tax department fails to
      update its records.</li>
  <li>However, the inverse is also true — the taxpayer must intimate the amalgamation. Failure to
      do so leaves the taxpayer exposed.</li>
</ul>

<h4>Compliance protocol on amalgamation</h4>
<ol>
  <li>Within 30 days of the effective date — written intimation to the jurisdictional AO of both
      transferor and transferee, with a copy of the NCLT order and the certified scheme.</li>
  <li>PAN cancellation request for the transferor (Form 49A).</li>
  <li>Update tax-deductor records (TAN intimations, TDS returns).</li>
  <li>Update GST registrations; transfer ITC via Form GST ITC-02.</li>
  <li>Update bank, vendor, customer records — operational, not statutory, but essential.</li>
</ol>

<div class="callout">
<strong>Note.</strong> The <em>Mahagun Realtors</em> case (2022) — also a Supreme Court decision —
appears to dilute Maruti Suzuki in cases where the assessment is "substantive" and the successor
participated without objection. Tax-law practice continues to apply Maruti Suzuki as the default,
with Mahagun Realtors as the narrow exception. Always object to jurisdictional defects at the
earliest opportunity.
</div>
""",
    },

    {
        "slug": "azadi-bachao",
        "title": "Union of India v. Azadi Bachao Andolan (2003)",
        "summary": "Treaty benefits are available based on form, provided there is no sham; refined the McDowell doctrine.",
        "body": """
<h4>Citation</h4>
<p>(2003) 263 ITR 706 (SC)</p>

<h4>Court</h4>
<p>Supreme Court of India.</p>

<h4>The point of law</h4>
<p>Are treaty benefits under the India-Mauritius DTAA available to investors who are tax-resident in
Mauritius purely by virtue of incorporation, even if they have no significant commercial substance
in Mauritius? Does McDowell's anti-avoidance principle override the treaty form?</p>

<h4>The holding</h4>
<blockquote>
"Tax planning may be legitimate provided it is within the framework of the law. The Mauritius
Tax Residency Certificate is sufficient evidence of treaty residence. Treaty shopping is not
illegitimate per se, and the Mauritius route, used widely for FDI into India, is consistent with
both Indian law and international practice."
</blockquote>

<p>The Court drew a distinction:</p>
<ul>
  <li><strong>Tax planning</strong> — arranging affairs within the framework of the law — permissible.</li>
  <li><strong>Tax avoidance</strong> — colourable devices, sham transactions — impermissible.</li>
</ul>

<h4>Why it matters in restructuring</h4>
<ul>
  <li>Many Indian M&A structures involve Mauritius or Singapore holding companies. Azadi Bachao
      validated their use for nearly two decades.</li>
  <li>The position has been modified by (a) <strong>2017 protocol</strong> to the India-Mauritius DTAA
      withdrawing the capital-gains exemption phased over 2017–2019, (b) the introduction of GAAR
      (Chapter X-A) effective April 2017, (c) the Multilateral Instrument (MLI) and Principal
      Purpose Test (PPT) effective from April 2020.</li>
  <li>Today, the substance test is more robust — but the underlying recognition of legitimate
      tax planning survives.</li>
</ul>

<div class="callout">
<strong>Current position.</strong> Treaty benefits in cross-border restructuring require a
combination of (i) valid TRC, (ii) commercial substance in the treaty jurisdiction, (iii) passing
the PPT under the MLI, and (iv) GAAR-compliance. Pure paper structures are no longer viable. But
genuine treaty-residency-based planning remains permissible.
</div>
""",
    },

    # ============================================================================
    # RECENT CASE LAW (2025–2026) — refresh of post-2024 jurisprudence
    # ============================================================================

    {
        "slug": "independent-sugar-cci-ibc",
        "title": "Independent Sugar Corp. v. Girish Sriram Juneja (SC, 2025)",
        "summary": "Where a resolution plan involves a combination, prior CCI approval is mandatory before the plan goes to the CoC for vote.",
        "body": """
<h4>Citation</h4>
<p>Civil Appeal No. ____ of 2025 (Supreme Court of India, judgment delivered 2025).</p>

<h4>The point of law</h4>
<p>Where a resolution plan under the IBC involves a "combination" within the meaning of
Sec 5 of the Competition Act, must the CCI approval be obtained <em>before</em> the plan
is placed before the Committee of Creditors (CoC), or can the approval be sought after CoC
approval and before NCLT sanction?</p>

<h4>The holding</h4>
<blockquote>
"Section 31(4) read with the proviso requires that approval of the Competition Commission of
India be obtained <strong>before approval of the resolution plan by the Committee of
Creditors</strong>. The proviso is mandatory, not directory. A resolution plan tabled for
CoC vote without prior CCI approval is procedurally infirm."
</blockquote>

<h4>Why it matters</h4>
<ul>
  <li>Resolution applicants whose plans cross Sec 5 / DVT thresholds must now sequence the CCI filing earlier in the CIRP timeline.</li>
  <li>The CoC cannot cure the defect retrospectively — the order of operations matters.</li>
  <li>Materially impacts large-cap CIRPs where the acquirer is already a dominant industry player.</li>
</ul>

<div class="callout">
<strong>Practice point.</strong> If you are advising a resolution applicant, file the CCI Form
in parallel with finalising the resolution plan, not after CoC vote. Build a 30-day CCI buffer
into the CIRP timeline budget.
</div>
""",
    },

    {
        "slug": "vaibhav-goel-clean-slate-tax",
        "title": "Vaibhav Goel v. DCIT (SC, 2025)",
        "summary": "Post-approval tax claims by the department are barred by the clean-slate doctrine — even where dues relate to pre-CIRP periods.",
        "body": """
<h4>Citation</h4>
<p>2025 SCC OnLine SC 592.</p>

<h4>The point of law</h4>
<p>After NCLT approval of a resolution plan under Sec 31 of the IBC, can the Income-tax
department initiate or continue assessment / recovery proceedings for tax demands of periods
prior to the resolution-plan effective date, where those claims were not included in the
approved plan?</p>

<h4>The holding</h4>
<blockquote>
"Once a resolution plan is approved by the Adjudicating Authority under Section 31, no
proceedings, including those by tax authorities, can be commenced or continued in respect of
claims pertaining to the period prior to the effective date of the plan if such claims have
not been incorporated in the resolution plan. The clean-slate doctrine binds all stakeholders,
including the Central and State Governments."
</blockquote>

<h4>Why it matters</h4>
<ul>
  <li>Extends the Essar Steel principle to tax demands specifically — closes a loophole the
      revenue had been exploiting by issuing post-approval notices.</li>
  <li>The resolution applicant can confidently exclude historic tax exposures from financial
      modelling, subject to (a) the plan having disclosed known disputes and (b) the plan
      being silent or extinguishing those claims.</li>
  <li>Reinforces the value of the IBC route for distressed-asset acquisition: post-approval
      certainty is now stronger than any other restructuring vehicle.</li>
</ul>
""",
    },

    {
        "slug": "electrosteel-arbitral-clean-slate",
        "title": "Electrosteel Steel Ltd. v. Ispat Carrier Pvt. Ltd. (SC, 2025)",
        "summary": "Pending arbitral proceedings against the corporate debtor for pre-CIRP claims are extinguished by an approved resolution plan, even if the arbitral award post-dates the plan.",
        "body": """
<h4>Citation</h4>
<p>2025 SCC OnLine SC 829.</p>

<h4>The point of law</h4>
<p>Where an arbitral proceeding was pending against a corporate debtor at the time of CIRP
admission, and the resolution plan is approved while the arbitration is still on-going, does
the subsequent arbitral award (for a pre-CIRP claim) bind the resolved corporate debtor?</p>

<h4>The holding</h4>
<blockquote>
"An arbitral award rendered after the approval of the resolution plan, but in respect of a
claim that arose prior to the CIRP commencement and was not part of the resolution plan, is
not enforceable against the corporate debtor in its post-resolution avatar. Such claims stand
extinguished by operation of Section 31, and the arbitral tribunal's continuing seisin of the
dispute does not survive the plan approval."
</blockquote>

<h4>Why it matters</h4>
<ul>
  <li>Plugs another category — arbitral creditors — into the clean-slate framework.</li>
  <li>Operational creditors with pending arbitrations should now file claims with the IRP/RP
      promptly; failure to do so results in extinction.</li>
  <li>Resolution applicants gain even more downside protection.</li>
</ul>
""",
    },

    {
        "slug": "kalyani-transco-bhushan-power",
        "title": "Kalyani Transco v. Bhushan Power and Steel Ltd. (SC, 2025)",
        "summary": "Multiple CIRP issues clarified: CoC subsistence post-plan-approval; locus of erstwhile promoters; PMLA-NCLT jurisdictional boundary.",
        "body": """
<h4>Citation</h4>
<p>2025 (CIRP appeals from the Bhushan Power and Steel resolution).</p>

<h4>Key holdings</h4>
<ol>
  <li><strong>CoC subsistence post-approval:</strong> The Committee of Creditors continues to
      have a role in distributing EBITDA earned during CIRP, even after the plan is approved
      by the NCLT, until the plan is fully implemented.</li>
  <li><strong>Locus of erstwhile promoters:</strong> The former promoters / shareholders of
      the corporate debtor do not have standing to challenge the resolution plan post-approval,
      absent demonstrable fraud or violation of statutory requirements.</li>
  <li><strong>PMLA vs IBC:</strong> The NCLT/NCLAT does not have jurisdiction to review or
      set aside attachment orders passed by the PMLA authority under the Prevention of Money
      Laundering Act. The two regimes operate in parallel.</li>
</ol>

<h4>Why it matters</h4>
<ul>
  <li>The PMLA holding is significant: assets attached under PMLA can survive into the
      resolution-applicant's hands as encumbered, requiring separate PMLA-tribunal route
      for release.</li>
  <li>Erstwhile-promoter litigation as a delay tactic is now harder to maintain.</li>
  <li>EBITDA distribution remains with CoC — relevant for plan financial modelling and
      working-capital arrangements for the post-resolution entity.</li>
</ul>
""",
    },

    {
        "slug": "lincon-polymers-demerger",
        "title": "Lincon Polymers — NCLAT on valuation in closely-held demergers (NCLAT, May 2025)",
        "summary": "NCLT cannot reject a family-arrangement demerger on valuation grounds where shareholders unanimously consent and an independent valuation report exists.",
        "body": """
<h4>Citation</h4>
<p>NCLAT order dated 26 May 2025, setting aside NCLT Ahmedabad order rejecting the Lincon
Polymers demerger scheme.</p>

<h4>The point of law</h4>
<p>Whether NCLT's role in sanctioning a scheme of arrangement extends to second-guessing the
share exchange ratio when (a) the scheme is among closely-held family companies, (b)
shareholders have unanimously approved, and (c) an independent registered-valuer report
backs the ratio.</p>

<h4>The holding</h4>
<blockquote>
"The objections raised by NCLT to the valuation methodology and the proposed share swap ratio
are unjustified, particularly in a closely-held family arrangement where there is unanimous
shareholder consent and the ratio is supported by a report from a SEBI-registered valuer.
The Tribunal's role is supervisory, not appellate over commercial wisdom. The Miheer Mafatlal
test is satisfied."
</blockquote>

<h4>Why it matters</h4>
<ul>
  <li>Reaffirms Miheer Mafatlal in the post-2013-Act era under NCLT jurisdiction.</li>
  <li>Closely-held / promoter-restructuring schemes have a clearer pathway: independent valuation +
      unanimous consent = strong defence against tribunal scrutiny.</li>
  <li>Tribunals continue to push back; expect appeals to NCLAT.</li>
</ul>
""",
    },

    {
        "slug": "indiabulls-amalgamation-valuation",
        "title": "Indiabulls Real Estate Amalgamation Scheme (NCLAT, 2025)",
        "summary": "NCLAT upholds rejection of an amalgamation scheme for inadequate valuation disclosure — the other side of the Lincon coin.",
        "body": """
<h4>Citation</h4>
<p>NCLAT order, 2025; affirming NCLT Chandigarh's rejection of 9 May 2023.</p>

<h4>The point of law</h4>
<p>Where the explanatory statement is thin on valuation methodology, asset disclosures, or
material objections are unanswered, can NCLT reject the scheme?</p>

<h4>The holding</h4>
<blockquote>
"The principles of transparency and full disclosure are not merely procedural — they are
substantive requirements under Sec 230(3). Where the asset valuation is inadequately
substantiated and the explanatory statement does not address material concerns raised by
the regulators or affected creditors, the Tribunal is entitled to reject the scheme.
Sanctioning a scheme under these circumstances would not be in the public interest."
</blockquote>

<h4>Why it matters</h4>
<ul>
  <li>Counterpoint to Lincon Polymers: where disclosure is poor, NCLT rejection holds up.</li>
  <li>Reinforces the centrality of the explanatory statement (covered in the scheme drafting templates section of this planner).</li>
  <li>For listed entities, this elevates the role of the SEBI Master Circular's content
      requirements — they are now the de facto minimum for any scheme.</li>
</ul>
""",
    },

    {
        "slug": "gujarat-itc-cross-state",
        "title": "Cross-State ITC Transfer on Amalgamation (Gujarat HC, 2026)",
        "summary": "GST ITC transfer under Sec 18(3) cannot be denied merely because transferor and transferee are in different states.",
        "body": """
<h4>Citation</h4>
<p>Gujarat High Court, March 2026.</p>

<h4>The point of law</h4>
<p>Where amalgamating and amalgamated companies are registered in different states under GST,
can the GST portal's limitation in handling cross-state ITC transfer be used to deny the
transferee's right to receive the transferor's unutilised ITC under Sec 18(3) of CGST Act
read with Rule 41?</p>

<h4>The holding</h4>
<blockquote>
"The right to transfer ITC on amalgamation flows from Section 18(3) of the CGST Act read with
Rule 41 of the CGST Rules. Neither provision restricts the transfer based on the geographical
location of the transferor and transferee. The portal's technical limitations cannot override
a statutory entitlement. The petitioner is entitled to transfer the ITC; the department is
directed to enable the transfer through alternative means including manual processing if
necessary."
</blockquote>

<h4>Why it matters</h4>
<ul>
  <li>Removes a practical roadblock in pan-India merger transactions where the merging
      entities have GST registrations across multiple states.</li>
  <li>Reinforces the principle that procedural / technological limitations cannot defeat
      substantive statutory rights.</li>
  <li>For deal valuation: full ITC pool of the transferor can now be confidently modelled as
      a transferable asset, regardless of GST jurisdictional structure.</li>
</ul>
""",
    },

    {
        "slug": "gujarat-composite-scheme-stamp",
        "title": "Composite Scheme Stamp Duty — Single Instrument Doctrine (Gujarat HC, 2025)",
        "summary": "A composite scheme involving merger + demerger + slump sale is one instrument for stamp-duty purposes, not three.",
        "body": """
<h4>Citation</h4>
<p>Gujarat High Court, June 2025.</p>

<h4>The point of law</h4>
<p>Where a composite scheme of arrangement involves multiple constituent transactions —
e.g., merger of A into B, demerger of a division of B into C, and slump-sale of a unit by
B to D — does the State stamp authority levy stamp duty once on the composite scheme or
separately on each constituent transaction?</p>

<h4>The holding</h4>
<blockquote>
"A composite scheme of arrangement sanctioned by a single NCLT order is, for the purpose of
stamp duty under the State Stamp Act, a single instrument. The fact that the scheme
encompasses multiple transactional elements does not entitle the stamp authority to levy
duty separately on each element. The order itself, which is the chargeable instrument,
captures the entire arrangement and stamp duty is computed on the aggregate value of property
transferred under that single order."
</blockquote>

<h4>Why it matters</h4>
<ul>
  <li>Major cost saving for complex group restructurings: tripling stamp duty by treating each
      element separately would make composite schemes uneconomic.</li>
  <li>The "single instrument" principle aligns with the Companies Act's treatment of the
      scheme as a unified order under Sec 232.</li>
  <li>State stamp authorities in other States (Maharashtra, Karnataka, Telangana) are likely
      to be challenged on similar grounds; expect convergence around this approach.</li>
</ul>

<div class="callout">
<strong>Drafting tip.</strong> Where composite schemes are involved, the scheme document
itself should explicitly state that the constituent transactions form a "single composite
arrangement" and that the stamp-duty payable is on the order as a single instrument. This
gives the stamp authority less room to argue for transaction-wise stamping.
</div>
""",
    },

    {
        "slug": "nfra-disciplinary-2025",
        "title": "NFRA Disciplinary Regime — Status (2025–2026)",
        "summary": "NFRA's growing pipeline of disciplinary orders, the Delhi HC's quashing of certain show-cause notices, and the SC's permission to continue (with conditions).",
        "body": """
<h4>Where things stand</h4>
<p>NFRA has issued approximately <strong>94 disciplinary orders</strong> imposing monetary
penalties and debarments on chartered accountants and audit firms since its establishment.
<strong>Around 85 CAs</strong> have been debarred for periods ranging from 6 months to 10
years; <strong>19 audit firms</strong> have faced action.</p>

<h4>Key procedural developments</h4>
<ul>
  <li><strong>Delhi High Court (Feb 2025):</strong> quashed show-cause notices issued by NFRA
      to Deloitte Haskins & Sells LLP, SRBC & Co LLP, and certain individual CAs, on grounds
      of procedural violations in the manner of initiation. NFRA appealed.</li>
  <li><strong>Supreme Court (2025):</strong> permitted NFRA to continue disciplinary
      proceedings but directed that <em>final orders</em> in pending matters be held in
      abeyance pending final disposal of the constitutional challenges. Existing final orders
      already issued shall not be enforced until clarity.</li>
  <li><strong>Division of functions:</strong> the government is considering splitting NFRA's
      audit-review and disciplinary functions into separate units to address the
      "judge-and-prosecutor" concern that has been raised in the constitutional challenges.</li>
</ul>

<h4>Common findings in NFRA orders</h4>
<ol>
  <li>Inadequate response to red flags — failure to investigate suspicious transactions identified during audit (SA 240).</li>
  <li>Insufficient audit documentation — working papers do not evidence the procedures the auditor claims to have performed (SA 230).</li>
  <li>Quality-control deficiencies in the engagement team (SA 220).</li>
  <li>Inadequate testing of internal financial controls under Sec 143(3)(i).</li>
  <li>Failure to apply the revised SA 315 risk-assessment methodology rigorously.</li>
</ol>

<h4>Recent specific example</h4>
<p>CA Neeraj Bansal — found guilty of professional misconduct in the audit of Religare Finvest;
monetary penalty ₹5,00,000 and debarment from audit for 5 years.</p>

<div class="callout">
<strong>Why this matters for your audit practice.</strong> Even if you don't audit NFRA-jurisdictional
entities (listed + prescribed thresholds), the disciplinary orders are public and document the
audit standards NFRA expects. Read 5–10 of them. They are the most concrete description of
"audit failure" in the Indian context, and they show what specifically gets scrutinised: testing
of revenue, going-concern evaluation, related-party transactions, and ICFR documentation.
</div>
""",
    },
]
