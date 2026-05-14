"""FAQs by subject, sourced from official Indian regulators / standard-setters.

Each FAQ has: question, answer (HTML), source (the authoritative body), and a
ref (the specific section / rule / circular / standard). Sources include MCA,
ICAI, NFRA, CBDT, RBI, SEBI, Ministry of Labour, IIA Global, and recognised
language authorities for English.

Keyed by area slug so the planner can pull the right FAQs into each subject tab.
"""

FAQS = {
    # ------------------------------------------------------------------
    # Restructuring (MCA, ICAI, SEBI, CCI, NCLT)
    # ------------------------------------------------------------------
    "restructuring": [
        {
            "q": "What is the difference between Section 230 and Section 232 of the Companies Act 2013?",
            "a": "<p>Section 230 is the parent enabling provision for compromises or arrangements with creditors or members — the umbrella for mergers, demergers, capital reductions etc. Section 232 layers specific additional requirements for mergers and amalgamations: mandatory valuation report by a registered valuer, accounting treatment conformity, automatic vesting of property and liabilities, and the appointed-date doctrine.</p>",
            "source": "MCA / ICAI",
            "ref": "Sections 230–232, Companies Act 2013",
        },
        {
            "q": "Can the appointed date in a scheme of arrangement be a future date or one in the distant past?",
            "a": "<p>The appointed date may be a calendar date or contingent on a specified event. MCA General Circular 09/2019 dated 21 August 2019 clarifies that the date should generally not be more than 12 months prior to the date of filing with NCLT. A future appointed date is permissible but rare; a back-date beyond 12 months requires strong commercial justification and will be scrutinised.</p>",
            "source": "MCA",
            "ref": "General Circular 09/2019 dated 21 Aug 2019",
        },
        {
            "q": "Is fast-track merger under Section 233 available to a holding company and its wholly-owned subsidiary regardless of size?",
            "a": "<p>Yes. Section 233(1)(b) read with Rule 25 covers any holding company and its wholly-owned subsidiary, irrespective of size or paid-up capital. The fast-track route bypasses NCLT and is decided by the Regional Director via the ROC.</p>",
            "source": "MCA",
            "ref": "Section 233(1)(b) + Rule 25, CAA Rules 2016",
        },
        {
            "q": "Does Section 234 cross-border merger require explicit RBI approval?",
            "a": "<p>Rule 25A mandates prior RBI approval. However, the FEMA (Cross Border Merger) Regulations 2018 provide <strong>deemed RBI approval</strong> if the merger is compliant — evidenced by a compliance certificate from the managing director, whole-time director or company secretary. No separate written RBI approval letter is required in practice for compliant transactions.</p>",
            "source": "MCA + RBI",
            "ref": "Rule 25A CAA Rules 2016; FEMA Cross Border Merger Regs 2018",
        },
        {
            "q": "Can a buyback be financed by a loan from a bank or other lender?",
            "a": "<p>No. Section 68(1) restricts the source of funds for buyback to (i) free reserves, (ii) securities premium account, or (iii) proceeds of a fresh issue of any shares or other specified securities — but <em>not</em> from the proceeds of an earlier issue of the same kind of shares. Borrowed funds are prohibited.</p>",
            "source": "MCA",
            "ref": "Section 68(1), Companies Act 2013",
        },
        {
            "q": "When does CCI approval become mandatory for a scheme of arrangement?",
            "a": "<p>Whenever the parties cross the combination thresholds under Section 5 of the Competition Act (asset / turnover tests) OR the new Deal Value Threshold (deal value > ₹2,000 cr AND target with substantial Indian business operations) effective from 10 September 2024. CCI approval must be obtained <em>before</em> consummation; for IBC resolution plans involving combination, CCI approval must precede the CoC vote (<em>Independent Sugar Corp.</em> SC 2025).</p>",
            "source": "CCI",
            "ref": "Section 5 + Notification S.O. 988(E) dt 7 Mar 2024",
        },
        {
            "q": "When is the SEBI Master Circular on Schemes of Arrangement applicable?",
            "a": "<p>Whenever any party to the scheme is listed. The listed company must obtain stock-exchange in-principle approval before filing with NCLT, accompanied by a fairness opinion from a SEBI-registered merchant banker, valuation report by a registered valuer, audit committee recommendation, committee-of-independent-directors recommendation, and a complete declaration of pending investigations. Simplified procedure applies for schemes between a listed company and its wholly-owned subsidiary.</p>",
            "source": "SEBI",
            "ref": "SEBI LODR Reg. 37 + Master Circular on Schemes of Arrangement",
        },
        {
            "q": "Is stamp duty uniform across States for an NCLT-sanctioned scheme?",
            "a": "<p>No. Stamp duty is a State subject — each State has its own rate and basis. The Gujarat High Court (June 2025) held that a composite scheme involving merger + demerger + slump sale is a <em>single instrument</em> for stamp duty, not separate transactions. The principle is being applied/argued in other States. Always check the State-specific stamp schedule before relying on a particular rate.</p>",
            "source": "State Stamp Acts; Gujarat HC",
            "ref": "Composite Scheme Stamp Duty ruling June 2025",
        },
        {
            "q": "Can promoters vote on a related-party scheme of arrangement?",
            "a": "<p>No. Where the scheme is between a listed company and its related party (typically a promoter group entity), the SEBI Master Circular requires <strong>majority-of-minority approval</strong> — the resolution must be approved by the majority of public (non-promoter) shareholders. Promoters cannot vote on the resolution.</p>",
            "source": "SEBI",
            "ref": "Master Circular on Schemes of Arrangement",
        },
        {
            "q": "What is the procedural sequence for an IBC resolution plan involving a combination?",
            "a": "<p>Per the Supreme Court in <em>Independent Sugar Corp. v. Girish Sriram Juneja</em> (2025), CCI approval must be obtained <strong>before</strong> the resolution plan is placed before the Committee of Creditors for voting. Submitting the plan to the CoC without prior CCI approval is procedurally infirm. This re-ordered the CIRP timeline for combinations.</p>",
            "source": "Supreme Court of India",
            "ref": "Independent Sugar Corp. v. Girish Sriram Juneja (2025)",
        },
    ],

    # ------------------------------------------------------------------
    # Ind AS (MCA, ICAI ITFG, NFRA)
    # ------------------------------------------------------------------
    "ind-as": [
        {
            "q": "Which companies are mandatorily required to apply Ind AS?",
            "a": "<p>Per Rule 4 of the Companies (Indian Accounting Standards) Rules 2015: <strong>all listed companies</strong> (irrespective of net worth); <strong>unlisted companies with net worth ≥ ₹250 crore</strong>; their holding, subsidiary, joint-venture and associate companies. Banks, NBFCs and insurance companies follow separate phased applicability per RBI and IRDAI guidelines.</p>",
            "source": "MCA",
            "ref": "Rule 4, Companies (Indian Accounting Standards) Rules 2015",
        },
        {
            "q": "Can a company that doesn't meet the thresholds voluntarily adopt Ind AS?",
            "a": "<p>Yes — Rule 4(1)(iii) permits voluntary adoption. However, once adopted, the company cannot revert to AS. All Ind AS must be applied in full — selective adoption is not permitted.</p>",
            "source": "MCA + ICAI",
            "ref": "Rule 4(1)(iii); ICAI Educational Material on First-time Adoption",
        },
        {
            "q": "Under Ind AS 116, are short-term and low-value leases exempt from on-balance-sheet recognition?",
            "a": "<p>Yes. Ind AS 116 paragraph 5 allows the lessee to elect, on a lease-by-lease basis for low-value, and on a class-of-asset basis for short-term, not to recognise a right-of-use asset and lease liability. Instead, lease payments are expensed on a straight-line basis. Short-term = ≤12 months. Low-value = generally ≤ ~₹3.5 lakh (based on the new asset's value).</p>",
            "source": "ICAI ITFG",
            "ref": "Ind AS 116, paragraph 5; ITFG Clarification Bulletins",
        },
        {
            "q": "How does Ind AS 115 treat a contract with multiple deliverables (e.g., software licence + customisation + support)?",
            "a": "<p>The entity identifies each <em>distinct</em> performance obligation and allocates the transaction price based on relative stand-alone selling prices. Each obligation is recognised either at a point in time (transfer of control) or over time (per the criteria in para 35). Distinctness is tested in <em>both</em> isolation and in the context of the contract.</p>",
            "source": "ICAI Educational Material",
            "ref": "Ind AS 115, paragraphs 22–30 + Educational Material",
        },
        {
            "q": "How is goodwill from amalgamation treated under Ind AS?",
            "a": "<p>Goodwill arising on a business combination (Ind AS 103) is recognised as an asset and tested for impairment <strong>annually</strong>, regardless of impairment indicators. It is <strong>not amortised</strong>. Bargain purchase (negative goodwill) is recognised as gain in P&L only after a thorough reassessment of identification and measurement of acquired net assets.</p>",
            "source": "ICAI ASB",
            "ref": "Ind AS 103, paragraphs 32–36; Ind AS 36 paragraph 10",
        },
        {
            "q": "Does Ind AS 103 apply to common-control business combinations?",
            "a": "<p>No — common-control transactions are explicitly outside the scope of Ind AS 103 (paragraph 2(c)). Appendix C to Ind AS 103 prescribes the <strong>pooling-of-interests / carrying-value method</strong> for common-control mergers — assets and liabilities of the transferor are recognised at their existing carrying amounts in the transferee, with the difference adjusted to capital reserve.</p>",
            "source": "ICAI ASB",
            "ref": "Ind AS 103 paragraph 2(c) + Appendix C",
        },
        {
            "q": "For Ind AS 109 Expected Credit Loss, when is the simplified approach mandatory vs the general approach?",
            "a": "<p>The <strong>simplified approach</strong> (always lifetime ECL — no stage transition logic) is <em>mandatory</em> for trade receivables and contract assets that do not contain a significant financing component. It is <em>optional</em> for trade receivables/contract assets with a significant financing component and for lease receivables. For all other financial instruments, the <strong>general approach</strong> (12-month or lifetime ECL based on stage) applies.</p>",
            "source": "ICAI / IFRS",
            "ref": "Ind AS 109 paragraph 5.5.15",
        },
        {
            "q": "Are fair value measurements of investment property mandatory under Ind AS 40?",
            "a": "<p>Ind AS 40 permits <em>only the cost model</em> for measurement (unlike IAS 40 which permits a fair value option). However, <strong>fair value disclosure is mandatory</strong> in the notes to financial statements — entities must obtain fair value, typically from a registered valuer, and disclose it even when carrying at cost.</p>",
            "source": "ICAI ASB",
            "ref": "Ind AS 40 paragraphs 30 + 76",
        },
        {
            "q": "What are common Ind AS audit findings from NFRA inspections?",
            "a": "<p>Recurring findings include: (i) inadequate documentation of fair value / impairment / ECL judgments; (ii) insufficient testing of revenue recognition under Ind AS 115 (particularly variable consideration and over-time vs point-in-time); (iii) failure to apply Ind AS 116 to embedded leases in supply or service contracts; (iv) weak related-party disclosures (Ind AS 24); (v) deferred tax on temporary differences computed using book-vs-WDV instead of book-vs-tax-base.</p>",
            "source": "NFRA",
            "ref": "NFRA Annual Reports & Inspection Findings",
        },
        {
            "q": "Are unrealised FVTOCI gains added to book profit for MAT (Section 115JB) computation?",
            "a": "<p>For Ind AS preparers, Section 115JB(2A) adds specific adjustments. Items in OCI that will not be reclassified to P&L (e.g., FVTOCI gains on equity instruments designated at FVTOCI without recycling; actuarial gains/losses on defined benefit plans) are included in book profit at the time of <em>realisation</em>, with transition adjustments spread over 5 years per Section 115JB(2B).</p>",
            "source": "CBDT + ICAI",
            "ref": "Section 115JB(2A) and (2B); ICAI Implementation Guide on Sec 115JB",
        },
    ],

    # ------------------------------------------------------------------
    # IT Act 2025 (CBDT, Income-tax Department)
    # ------------------------------------------------------------------
    "it-act-2025": [
        {
            "q": "When did the Income-tax Act 2025 come into effect?",
            "a": "<p>The Income-tax Act 2025 became operative from <strong>1 April 2026</strong>. The Income-tax Act 1961 now applies only to assessments and transactions pertaining to periods ending on or before 31 March 2026. From AY 2026–27 onwards, the 2025 Act is the operative law.</p>",
            "source": "Income-tax Department / CBDT",
            "ref": "Income-tax Act 2025; CBDT enabling notifications",
        },
        {
            "q": "Is the new (concessional) tax regime under Section 115BAC the default?",
            "a": "<p>Yes. Since AY 2024–25, the new regime is the default for individuals and HUFs. A taxpayer wishing to opt for the old regime (with deductions) must file <strong>Form 10-IEA</strong> on or before the due date of return. The election is reversible for non-business taxpayers; business income earners can switch only once.</p>",
            "source": "CBDT",
            "ref": "Section 115BAC; Form 10-IEA",
        },
        {
            "q": "Who is a 'deemed resident' under Section 6(1A)?",
            "a": "<p>An Indian citizen whose total income (other than foreign-source income) exceeds ₹15 lakh and who is not liable to tax in any other country by reason of domicile, residence or any similar criterion. Such a person is deemed resident and is taxable on world income unless able to establish ordinary residence elsewhere.</p>",
            "source": "CBDT",
            "ref": "Section 6(1A), Income-tax Act",
        },
        {
            "q": "What are the LTCG and STCG rates on listed equity post-Budget 2024?",
            "a": "<p>Long-term capital gains (held > 12 months) on listed equity / equity-oriented MFs: <strong>12.5% without indexation</strong>; ₹1.25 lakh basic exemption. Short-term capital gains (held ≤ 12 months): <strong>20%</strong>. Both rates effective for transfers from 23 July 2024.</p>",
            "source": "CBDT",
            "ref": "Section 112A (LTCG) + Section 111A (STCG); Finance Act 2024",
        },
        {
            "q": "How is buyback taxed from 1 October 2024 onwards?",
            "a": "<p>The shift is fundamental: <strong>buyback tax under Section 115QA has been withdrawn</strong> for buybacks on or after 1 October 2024. The buyback consideration is now treated as a <strong>deemed dividend</strong> in the shareholder's hands under Section 2(22), subject to TDS at applicable rates under Section 194. Cost of acquisition becomes available as capital loss.</p>",
            "source": "CBDT",
            "ref": "Finance (No. 2) Act 2024",
        },
        {
            "q": "What is the GAAR threshold and procedure?",
            "a": "<p>GAAR applies where the aggregate tax benefit from an 'impermissible avoidance arrangement' exceeds <strong>₹3 crore</strong> in a financial year. The AO refers the case to the Principal Commissioner, who then refers to the GAAR Approving Panel (a 3-member body including a HC judge). Only with the Panel's approval can the arrangement be re-characterised.</p>",
            "source": "CBDT",
            "ref": "Sections 95–102 (Chapter X-A); Rule 10U",
        },
        {
            "q": "Can a taxpayer file an updated return after assessment?",
            "a": "<p>Yes — Section 139(8A) permits an updated return within <strong>48 months from the end of the relevant assessment year</strong> (extended from 24 months), subject to additional tax (25% / 50% / 60% of additional tax + interest, depending on when filed). An updated return cannot be used to (i) claim or increase loss, (ii) decrease tax liability, or (iii) claim a refund.</p>",
            "source": "CBDT",
            "ref": "Section 139(8A); Finance Act 2025 amendment",
        },
        {
            "q": "Are payments outstanding to MSMEs beyond 45 days disallowed under Sec 43B(h)?",
            "a": "<p>Yes. From FY 2023–24, amounts payable to micro and small enterprises beyond the prescribed payment period under the MSMED Act (15 days where no agreement; 45 days where agreed) are <strong>disallowed in computing business income</strong> unless paid by the end of the previous year. This is the most material clause of Form 3CD for FY 2025–26 audits.</p>",
            "source": "CBDT",
            "ref": "Section 43B(h); Finance Act 2023",
        },
        {
            "q": "How are virtual digital assets (cryptocurrencies, NFTs) taxed?",
            "a": "<p>Section 115BBH taxes gains from transfer of VDAs at a flat <strong>30%</strong>, with no deduction except the cost of acquisition and no set-off or carry-forward of losses (loss from one VDA cannot offset gain from another). <strong>TDS at 1%</strong> under Section 194S applies on the transferee at the time of payment.</p>",
            "source": "CBDT",
            "ref": "Sections 115BBH + 194S; Finance Act 2022",
        },
        {
            "q": "What is faceless assessment and where is it conducted?",
            "a": "<p>Faceless Assessment is an end-to-end electronic and team-based assessment procedure conducted through the <strong>National Faceless Assessment Centre (NaFAC)</strong>. No face-to-face interaction; case allocation is automated and geographically agnostic. Codified in Section 144B. Applies to scrutiny assessments under Section 143(3) and best-judgment under Section 144.</p>",
            "source": "CBDT",
            "ref": "Section 144B; CBDT Notifications & Instructions",
        },
    ],

    # ------------------------------------------------------------------
    # Internal Audit (IIA Global, ICAI IASB, MCA)
    # ------------------------------------------------------------------
    "internal-audit": [
        {
            "q": "Which companies must mandatorily appoint an internal auditor?",
            "a": "<p>Per Section 138 read with Rule 13: (i) every listed company; (ii) every unlisted public company with paid-up share capital ≥ ₹50 crore OR turnover ≥ ₹200 crore OR outstanding loans/borrowings ≥ ₹100 crore OR outstanding deposits ≥ ₹25 crore; (iii) every private company with turnover ≥ ₹200 crore OR outstanding loans/borrowings ≥ ₹100 crore.</p>",
            "source": "MCA",
            "ref": "Section 138 + Rule 13, Companies (Accounts) Rules 2014",
        },
        {
            "q": "Can the statutory auditor of a company also act as its internal auditor?",
            "a": "<p>No. Section 144 of the Companies Act 2013 prohibits the statutory auditor from providing certain services including internal audit, to maintain auditor independence. The statutory and internal auditor functions must be performed by different persons / firms.</p>",
            "source": "MCA",
            "ref": "Section 144, Companies Act 2013",
        },
        {
            "q": "Are ICAI's Standards on Internal Audit (SIAs) mandatory for CA members?",
            "a": "<p>Per the ICAI Internal Audit Standards Board, members performing internal audit are expected to comply with the SIAs. Non-compliance with SIAs may attract disciplinary action by ICAI. The standards apply whether the engagement is statutory (Section 138) or voluntary.</p>",
            "source": "ICAI Internal Audit Standards Board",
            "ref": "Preface to Standards on Internal Audit; ICAI Code of Ethics",
        },
        {
            "q": "Who appoints the internal auditor — the board or the audit committee?",
            "a": "<p>Per Rule 13(2), the internal auditor is appointed by the <strong>Audit Committee</strong> in companies required to constitute one (Section 177), or by the <strong>Board</strong> in other cases. The audit committee/board also determines the scope, functioning, periodicity and methodology of internal audit.</p>",
            "source": "MCA",
            "ref": "Rule 13(2), Companies (Accounts) Rules 2014",
        },
        {
            "q": "Can internal audit be outsourced to an external CA firm?",
            "a": "<p>Yes. Rule 13(2) explicitly permits the internal auditor to be (i) a chartered accountant (in practice or employed), (ii) a cost accountant, or (iii) such other professional as the board may decide. The function can be in-house, fully outsourced, or co-sourced.</p>",
            "source": "MCA",
            "ref": "Rule 13(2), Companies (Accounts) Rules 2014",
        },
        {
            "q": "What is the difference between the Three Lines of Defence and the new Three Lines Model?",
            "a": "<p>IIA updated the terminology in 2020. The Three Lines Model retains the same three-tier structure (operational management; risk/compliance; internal audit) but emphasises <strong>collaboration and alignment with organisational objectives</strong>, rather than 'defence' against threats. Governance, accountability and assurance are framed positively.</p>",
            "source": "IIA Global",
            "ref": "IIA Three Lines Model, July 2020",
        },
        {
            "q": "What is the difference between a 'significant deficiency' and a 'material weakness' in ICFR?",
            "a": "<p>A <strong>material weakness</strong> is a deficiency, or combination, such that there is a reasonable possibility that a material misstatement of the financial statements will not be prevented or detected on a timely basis. A <strong>significant deficiency</strong> is less severe but important enough to merit attention by those charged with governance. Material weakness leads to an adverse opinion on ICFR; significant deficiency is communicated to TCWG but doesn't preclude an unmodified opinion.</p>",
            "source": "ICAI / PCAOB",
            "ref": "ICAI GN on Audit of IFCFR; PCAOB AS 2201",
        },
        {
            "q": "How often must internal audit be performed?",
            "a": "<p>The Companies Act doesn't prescribe a fixed frequency. Per IIA Standards (Standard 2010) and ICAI SIA 220, internal audit is a continuous function. The frequency of <em>specific engagements</em> follows the risk-based annual plan approved by the audit committee — typically high-risk areas yearly, medium every 2 years, low every 3–5 years.</p>",
            "source": "IIA / ICAI",
            "ref": "IIA Standard 2010 — Planning; ICAI SIA 220",
        },
        {
            "q": "Is internal audit required to follow ICAI's Code of Ethics?",
            "a": "<p>Yes — for CA members. The IIA's own Code of Ethics (integrity, objectivity, confidentiality, competency) is additionally referenced in ICAI SIAs. Threats to independence (e.g., long-term engagement, fee dependency, social relationships) must be assessed and safeguards applied.</p>",
            "source": "ICAI + IIA",
            "ref": "ICAI Code of Ethics; IIA Code of Ethics; SIA 110",
        },
        {
            "q": "Is external quality assessment (EQA) of internal audit mandatory?",
            "a": "<p>Per IIA Standard 1312, an external quality assessment must be conducted <strong>at least once every five years</strong> by a qualified, independent reviewer or review team. ICAI SIA 530 echoes this requirement. The assessment evaluates conformance with the IIA Standards / SIAs and recommends improvements.</p>",
            "source": "IIA / ICAI",
            "ref": "IIA Standard 1312; ICAI SIA 530",
        },
    ],

    # ------------------------------------------------------------------
    # Labour Codes (Ministry of Labour & Employment, EPFO, ESIC)
    # ------------------------------------------------------------------
    "labor-codes": [
        {
            "q": "Are the four Labour Codes fully in force across India?",
            "a": "<p>The codes have been enacted by Parliament but their substantive operation depends on notification of State Rules. As of 2026, the operationalisation status varies State-by-State — some States (Madhya Pradesh, Uttar Pradesh, Gujarat) have notified Rules for several codes; others are still in draft stage. Check labour.gov.in and the relevant State Labour Department for the latest status before relying on any provision.</p>",
            "source": "Ministry of Labour & Employment",
            "ref": "labour.gov.in — Code-wise State Rules tracker",
        },
        {
            "q": "How does the new definition of 'wages' under the Code on Wages 2019 affect PF contributions?",
            "a": "<p>Section 2(y) defines wages with an inclusive list (basic + DA + retaining allowance) and an exclusive list of allowances (HRA, conveyance, overtime, etc.). However, if the <strong>excluded allowances exceed 50% of total remuneration</strong>, the excess is added back into 'wages' for computing PF, gratuity and leave-encashment. This typically increases PF contribution by 10–30% for CTC structures with low basic.</p>",
            "source": "Ministry of Labour + EPFO",
            "ref": "Section 2(y), Code on Wages 2019",
        },
        {
            "q": "Are gig and platform workers now eligible for social security?",
            "a": "<p>Yes — for the first time in Indian law, Chapter IX of the Code on Social Security 2020 recognises gig workers, platform workers and unorganised workers. <strong>Aggregators</strong> (digital platforms connecting service buyers and sellers) must contribute <strong>1–2% of annual turnover</strong> (capped at industry-prescribed limit) to a dedicated social security fund.</p>",
            "source": "Ministry of Labour",
            "ref": "Sections 2(35), 2(60), 113 — Code on Social Security 2020",
        },
        {
            "q": "What is the gratuity service-period requirement under the new codes?",
            "a": "<p>For permanent employees: <strong>5 years</strong> of continuous service (or as prescribed under the existing Payment of Gratuity Act, retained substantively). For <strong>fixed-term employees</strong>: gratuity is payable after <strong>1 year</strong> of continuous service. Computation: 15 days' wages × completed years, cap ₹20 lakh.</p>",
            "source": "Ministry of Labour",
            "ref": "Section 53, Code on Social Security 2020",
        },
        {
            "q": "Can women be employed in night shifts and all sectors under the OSH Code?",
            "a": "<p>Yes. The OSH Code 2020 explicitly permits women in <strong>all establishments and all shifts</strong>, subject to safety provisions: safe transport, adequate lighting, and obtaining the consent of the woman worker. This is a significant change from sector-specific restrictions in earlier laws.</p>",
            "source": "Ministry of Labour",
            "ref": "Section 43, OSH Code 2020",
        },
        {
            "q": "What is the worker threshold for government permission for retrenchment or closure?",
            "a": "<p>Government permission is now required for retrenchment / closure where the establishment has <strong>300 or more workers</strong> (raised from 100 under the old Industrial Disputes Act). Below this threshold, the employer needs only to give 60-day notice and pay statutory compensation (15 days × completed years).</p>",
            "source": "Ministry of Labour",
            "ref": "Sections 70 + 75, Industrial Relations Code 2020",
        },
        {
            "q": "How is fixed-term employment regulated under the new codes?",
            "a": "<p>Fixed-term employment is formally recognised and regulated by the IR Code 2020 and OSH Code 2020. A fixed-term worker is entitled to <em>the same statutory benefits</em> as a permanent worker proportionate to the period worked, including gratuity after 1 year. No retrenchment notice / compensation is required on natural expiry of the term.</p>",
            "source": "Ministry of Labour",
            "ref": "IR Code 2020 + OSH Code 2020",
        },
        {
            "q": "What is the threshold for applicability of EPF under the Code on Social Security?",
            "a": "<p>Establishments with <strong>20 or more employees</strong> are mandatorily covered for EPF (retained from the EPF Act 1952). Voluntary coverage is permitted for smaller establishments. International workers are covered without the threshold limit.</p>",
            "source": "EPFO",
            "ref": "Section 15, Code on Social Security 2020",
        },
        {
            "q": "What is the contract-labour licensing threshold under the OSH Code?",
            "a": "<p>An establishment must obtain a licence to engage contract labour if it engages or proposes to engage <strong>50 or more contract workers</strong> (raised from 20 under the old Contract Labour Act). Welfare facilities (canteens, restrooms, drinking water) remain the principal employer's responsibility regardless of contractor licensing.</p>",
            "source": "Ministry of Labour",
            "ref": "Chapter XI, OSH Code 2020",
        },
        {
            "q": "What is the Shram Suvidha portal?",
            "a": "<p>A unified online compliance portal at <a href='https://shramsuvidha.gov.in/' target='_blank' rel='noopener'>shramsuvidha.gov.in</a> covering all four labour codes. It provides single registration of establishments, consolidated returns, online inspection management, and grievance redressal — replacing multiple disparate compliance interfaces under the old laws.</p>",
            "source": "Ministry of Labour",
            "ref": "shramsuvidha.gov.in",
        },
    ],

    # ------------------------------------------------------------------
    # Auditing (ICAI AASB, NFRA, MCA)
    # ------------------------------------------------------------------
    "auditing": [
        {
            "q": "When is rotation of auditors mandatory?",
            "a": "<p>Per Section 139(2): <strong>individual auditor</strong> — maximum 5-year term, then 5-year cooling-off. <strong>Audit firm</strong> — maximum 10-year term (i.e., one or two terms of 5 years each), then 5-year cooling-off. Applies to: listed companies; unlisted public with paid-up capital ≥ ₹10 cr; private with paid-up capital ≥ ₹50 cr; all companies with public borrowings/deposits ≥ ₹50 cr.</p>",
            "source": "MCA",
            "ref": "Section 139(2) + Rule 5, Companies (Audit and Auditors) Rules 2014",
        },
        {
            "q": "For which entities is Key Audit Matters (KAM) reporting mandatory?",
            "a": "<p>SA 701 requires KAM communication in the auditor's report for audits of complete sets of general-purpose financial statements of <strong>listed entities</strong>. For other entities, KAM communication is voluntary but encouraged. Each KAM has three required elements: description, why the matter was considered significant, and how it was addressed in the audit.</p>",
            "source": "ICAI AASB",
            "ref": "SA 701",
        },
        {
            "q": "When does SA 600 (Revised) on Group Audits become effective?",
            "a": "<p>SA 600 (Revised) — <em>Special Considerations: Audits of Group Financial Statements</em> — is effective for audits of financial statements for periods beginning on or after <strong>1 April 2026</strong> in India. The earlier SA 600 continues to apply to prior period audits. The revised version aligns with ISA 600 (Revised) and significantly elevates the requirements around component auditor work, group materiality and risk assessment.</p>",
            "source": "ICAI AASB",
            "ref": "SA 600 (Revised); ICAI implementation notification",
        },
        {
            "q": "Are CARO 2020 reporting requirements waived for any companies?",
            "a": "<p>Yes — CARO 2020 does NOT apply to: (i) one-person companies; (ii) small companies; (iii) certain charitable companies under Section 8; (iv) banking, insurance, and electricity companies (which have separate sectoral audit requirements). For all other companies covered by Section 143(11), all 21 clauses must be reported.</p>",
            "source": "MCA",
            "ref": "CARO 2020 paragraph 1(2); Section 143(11) Companies Act",
        },
        {
            "q": "Is testing of journal entries mandatory in every audit?",
            "a": "<p>Yes. SA 240 presumes there is always a significant risk of management override of controls, and journal entry testing is one of the required responses. The auditor must (a) make inquiries about journal entries, (b) select journals for testing based on risk criteria (round amounts, period-end entries, unusual accounts, etc.), and (c) consider unusual entries even outside the sample.</p>",
            "source": "ICAI AASB",
            "ref": "SA 240, paragraph 32 and Application Material",
        },
        {
            "q": "What is the applicability of ICFR audit reporting under Section 143(3)(i)?",
            "a": "<p>ICFR reporting applies to: (i) all listed companies; (ii) unlisted public companies with paid-up capital ≥ ₹50 cr OR turnover ≥ ₹50 cr OR outstanding borrowings ≥ ₹25 cr OR outstanding deposits ≥ ₹25 cr; (iii) private companies with similar thresholds. <strong>OPCs, small companies and certain dormant/charitable cos are exempt</strong>. ICAI Guidance Note on Audit of IFCFR is the primary reference.</p>",
            "source": "MCA + ICAI",
            "ref": "Section 143(3)(i) + Rule 10A; ICAI GN on IFCFR",
        },
        {
            "q": "How does ISQM 1 differ from SQC 1?",
            "a": "<p>SQC 1 is the existing ICAI firm-level quality control standard, modelled on the older ISQC 1. The new <strong>ISQM 1 (and ISQM 2)</strong> are international Quality Management standards that replace ISQC 1 — a fundamental redesign moving from a process-based approach to a <strong>risk-based quality management system</strong>. ICAI is in the process of issuing an equivalent SQM. Firms in transition should monitor ICAI AASB releases.</p>",
            "source": "ICAI AASB + IAASB",
            "ref": "SQC 1; ISQM 1 + ISQM 2",
        },
        {
            "q": "What is the threshold for tax audit under Section 44AB?",
            "a": "<p>For <strong>business</strong>: turnover > ₹1 crore (raised to ₹10 crore if aggregate cash receipts/payments ≤ 5% of total). For <strong>profession</strong>: gross receipts > ₹50 lakh. The tax audit report (Form 3CA/3CB + Form 3CD) must be filed by the specified due date (typically 30 Sept of AY).</p>",
            "source": "CBDT",
            "ref": "Section 44AB, Income-tax Act",
        },
        {
            "q": "What is the current status of NFRA disciplinary actions?",
            "a": "<p>NFRA has issued ~94 disciplinary orders against CAs and audit firms. The Delhi High Court (Feb 2025) quashed certain show-cause notices on procedural grounds; the Supreme Court (2025) permitted NFRA to continue proceedings but <strong>stayed final orders</strong> and enforcement pending constitutional challenge. Practical effect: cases are progressing but penalties are not currently enforced. Check NFRA's debarment page for current status.</p>",
            "source": "NFRA + Supreme Court of India",
            "ref": "NFRA orders + SC interim orders 2025",
        },
        {
            "q": "Are auditor's responsibilities expanded for ESG / sustainability information?",
            "a": "<p>Currently, mainstream audit (Companies Act) does not extend to ESG/BRSR statements. SEBI requires top 1,000 listed entities to file the <strong>Business Responsibility and Sustainability Report</strong> (BRSR), with <strong>BRSR Core</strong> (a sub-set of indicators) requiring third-party reasonable assurance from FY 2023–24 onwards in a phased manner. ICAI has issued specific guidance on assurance of BRSR Core.</p>",
            "source": "SEBI + ICAI",
            "ref": "SEBI Master Circular on ESG; ICAI Guidance on BRSR Core Assurance",
        },
    ],

    # ------------------------------------------------------------------
    # English (BBC, British Council, Cambridge)
    # ------------------------------------------------------------------
    "english": [
        {
            "q": "Should I learn American English or British English?",
            "a": "<p>For most Indian professional contexts, <strong>British English</strong> is the historical default — Indian legal, financial and academic writing follows British conventions (spelling, punctuation, formal register). American English is acceptable in international tech/startup contexts. The key is <em>consistency within a single document</em>, not which variant you pick.</p>",
            "source": "British Council",
            "ref": "Standard ELT guidance",
        },
        {
            "q": "What's the fastest way to improve spoken English?",
            "a": "<p>Two practices, daily: (1) <strong>Shadowing</strong> — listen to a native speaker (BBC News, BBC Learning English's '6 Minute English') and repeat aloud immediately after, matching their pace, stress and intonation. (2) <strong>Daily 5-minute self-talk</strong> in English on a topic (news, work, hobbies). 8 weeks of 15-minute daily practice produces measurable change.</p>",
            "source": "BBC Learning English",
            "ref": "BBC LE Pronunciation series + ELT research",
        },
        {
            "q": "When do I use 'a' versus 'an'?",
            "a": "<p>Based on the <strong>sound</strong> of the next word, not the letter. 'An hour' (silent h, vowel sound). 'A university' (consonant /j/ sound). 'An MBA' (M starts with vowel sound 'em'). 'A one-time payment' (one starts with /w/ sound).</p>",
            "source": "Cambridge Dictionary",
            "ref": "Cambridge Grammar of English",
        },
        {
            "q": "What's the difference between 'affect' and 'effect'?",
            "a": "<p>'Affect' is usually a <strong>verb</strong> meaning 'to influence': <em>The merger will affect employees</em>. 'Effect' is usually a <strong>noun</strong> meaning 'the result': <em>The effect of the merger was significant</em>. 'Effect' can rarely be a verb meaning 'to bring about': <em>The committee effected a change</em>. Trick: A = Action verb, E = End result noun.</p>",
            "source": "Cambridge Dictionary",
            "ref": "Cambridge English Dictionary; Practical English Usage (Swan)",
        },
        {
            "q": "Why do many Indian speakers confuse /v/ and /w/?",
            "a": "<p>Most Indian languages (Hindi, Tamil, Telugu, Bengali) have <em>one</em> bilabial fricative that's a mid-point between English /v/ and /w/. English distinguishes: <strong>/v/</strong> — top teeth touch bottom lip ('vine', 'very', 'evidence'); <strong>/w/</strong> — lips rounded, no teeth contact ('wine', 'water', 'work'). Practice minimal pairs: vine/wine, vet/wet, vary/wary.</p>",
            "source": "Phonetics / ELT methodology",
            "ref": "IPA; Cambridge English Pronouncing Dictionary",
        },
        {
            "q": "Is 'prepone' a real English word?",
            "a": "<p>It is recognised as an Indianism — coined in Indian English to mean 'bring forward in time'. It's now listed in <a href='https://dictionary.cambridge.org/' target='_blank' rel='noopener'>Cambridge Dictionary</a> as an Indian English usage. However, in international contexts the standard expressions are <strong>'bring forward', 'move up', or 'reschedule earlier'</strong>. Stick to these for documents and conversations with non-Indian audiences.</p>",
            "source": "Cambridge Dictionary",
            "ref": "Cambridge English (Indian English entries)",
        },
        {
            "q": "How many new words should I learn per day?",
            "a": "<p>Quality beats quantity. Target <strong>5–10 new words per day, learned in context</strong> (not from a bare list). Use spaced repetition — review at 1, 3, 7, 30 days. 5 words × daily × 8 weeks ≈ 280 new words actively retained. The Norman Lewis approach of learning by Latin/Greek roots multiplies vocabulary because one root unlocks many words.</p>",
            "source": "Cambridge Vocabulary in Use methodology",
            "ref": "Cambridge English Vocabulary in Use series",
        },
        {
            "q": "Are phrasal verbs really important?",
            "a": "<p>Critical for natural-sounding spoken English. Native speakers use phrasal verbs constantly ('get up', 'give up', 'look into', 'come across'). Replacing them with formal single-word equivalents ('rise', 'abandon', 'investigate', 'encounter') sounds stilted in conversation. For writing, mix both — formal documents lean towards single-word verbs, emails and meetings use more phrasal verbs.</p>",
            "source": "British Council / Cambridge",
            "ref": "English Vocabulary in Use (Advanced) — phrasal verb chapters",
        },
        {
            "q": "Should I try to lose my Indian accent?",
            "a": "<p>No — accent neutrality is not the goal; <strong>mutual intelligibility</strong> is. Focus on three high-leverage items: (1) clear pronunciation of distinctive sounds (th, v vs w, schwa /ə/), (2) correct word stress (pho-TO-gra-pher, not PHO-to-GRA-pher), and (3) appropriate sentence intonation. These are improvable in 2 months. A 'native accent' is a 10-year project; intelligibility is a 2-month project.</p>",
            "source": "ELT methodology",
            "ref": "British Council; David Crystal — English as a Global Language",
        },
        {
            "q": "What are the most useful free resources for self-study?",
            "a": "<p>(1) <a href='https://www.bbc.co.uk/learningenglish' target='_blank' rel='noopener'>BBC Learning English</a> — '6 Minute English', 'English at Work', pronunciation videos. (2) <a href='https://learningenglish.voanews.com/' target='_blank' rel='noopener'>VOA Learning English</a> — slow-paced news. (3) <a href='https://dictionary.cambridge.org/' target='_blank' rel='noopener'>Cambridge Dictionary</a> — pronunciation audio + collocations. (4) <a href='https://www.britishcouncil.in/english' target='_blank' rel='noopener'>British Council LearnEnglish app</a> — grammar exercises. 30 minutes daily on these four beats any paid course at this proficiency level.</p>",
            "source": "BBC, VOA, Cambridge, British Council",
            "ref": "Free public resources",
        },
    ],
}
