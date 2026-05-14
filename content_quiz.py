"""Objective-type MCQs per subject — for active recall and self-test.

Each MCQ has:
  q: question text (HTML allowed)
  options: list of 4 strings (HTML allowed)
  correct: index (0-3) of the correct option
  explain: explanation shown after answering
  source: authority for the answer (section / standard / circular)
"""

QUIZ = {
    # ----------------------------------------------------------------------
    # Restructuring
    # ----------------------------------------------------------------------
    "restructuring": [
        {
            "q": "For Section 2(1B) to apply to an amalgamation, what minimum percentage of shareholders (in value) of the amalgamating company must become shareholders of the amalgamated company?",
            "options": ["More than 50%", "Two-thirds", "Three-fourths", "Nine-tenths"],
            "correct": 2,
            "explain": "Section 2(1B)(iii) requires that shareholders holding ≥ 3/4 in value of the shares of the amalgamating company (other than shares already held by the amalgamated company or its nominee) must become shareholders of the amalgamated company.",
            "source": "Sec 2(1B), Income-tax Act",
        },
        {
            "q": "Which of the following is NOT one of the five conditions for a demerger to qualify under Section 2(19AA)?",
            "options": [
                "All property of the undertaking transfers on a going-concern basis",
                "Resulting company issues shares to demerged-company shareholders pro rata",
                "Transfer occurs at fair market value of assets",
                "Shareholders holding ≥ 3/4 in value become shareholders of resulting company",
            ],
            "correct": 2,
            "explain": "Sec 2(19AA)(iii) requires transfer at book value (not FMV). Recognising assets at FMV in a demerger BREAKS the tax neutrality — the standard cited condition is 'at values appearing in the books'.",
            "source": "Sec 2(19AA), Income-tax Act",
        },
        {
            "q": "From 1 October 2024, who is taxed on buyback consideration?",
            "options": [
                "Company at 20%+",
                "Shareholder as deemed dividend",
                "Both — at company level under 115QA AND at shareholder level",
                "Neither (it's a return of capital, exempt)",
            ],
            "correct": 1,
            "explain": "The regime changed on 1 Oct 2024. Sec 115QA was withdrawn; the buyback proceeds are now taxed in the shareholder's hands as deemed dividend under Sec 2(22), subject to TDS u/s 194.",
            "source": "Finance (No. 2) Act 2024",
        },
        {
            "q": "Per the Marshall Sons doctrine, the appointed date in a scheme of arrangement:",
            "options": [
                "Has no legal effect; only the order date matters",
                "Binds the company but not the tax authorities",
                "Is binding on all parties including tax authorities, even when the order comes much later",
                "Must always be the date of the NCLT order",
            ],
            "correct": 2,
            "explain": "Marshall Sons (SC 1997) held that the appointed date is binding on tax authorities. The amalgamating company ceases to exist for tax purposes from the appointed date, regardless of when the NCLT order is passed. MCA's Aug 2019 circular added a 12-month look-back guidance.",
            "source": "Marshall Sons (SC 1997); MCA Circular 09/2019",
        },
        {
            "q": "Section 233 fast-track merger is available for which combination (post Sept 2024 MCA notification)?",
            "options": [
                "Two listed public companies of any size",
                "Two small companies; or holding-WOS; or two start-ups; or start-up + small co; certain unlisted public cos",
                "Only government companies",
                "Only foreign companies merging into Indian companies",
            ],
            "correct": 1,
            "explain": "Sec 233 + Rule 25 enable fast-track merger for small companies, holding-WOS, start-ups, and (post Sept 2024) certain unlisted public companies meeting prescribed thresholds. Listed companies are NOT eligible.",
            "source": "Sec 233 + Rule 25, CAA Rules 2016; MCA Notif. Sept 2024",
        },
        {
            "q": "Under SEBI's Master Circular on Schemes of Arrangement, when is majority-of-minority approval required?",
            "options": [
                "For every scheme involving a listed company",
                "Only when the scheme is between two unrelated parties",
                "When the scheme is between a listed company and a related party (e.g., a promoter group entity)",
                "Only when CCI approval is also required",
            ],
            "correct": 2,
            "explain": "Majority-of-minority — approval by majority of public (non-promoter) shareholders — is required when the scheme involves a related party. Promoters cannot vote on such resolutions.",
            "source": "SEBI Master Circular on Schemes of Arrangement",
        },
        {
            "q": "For an IBC resolution plan involving a combination, when must CCI approval be obtained?",
            "options": [
                "After NCLT sanctions the plan",
                "Before the plan is placed before the CoC for approval",
                "Only after the resolution applicant takes over",
                "CCI approval is never required for IBC plans",
            ],
            "correct": 1,
            "explain": "The Supreme Court in Independent Sugar Corp. v. Girish Sriram Juneja (2025) held that where the resolution plan involves a combination, prior CCI approval is mandatory before the plan goes to the CoC. The order of operations is non-negotiable.",
            "source": "Independent Sugar Corp. v. Girish Sriram Juneja (SC 2025)",
        },
        {
            "q": "Net worth for slump sale (Section 50B) is computed using:",
            "options": [
                "FMV of all assets minus FMV of liabilities",
                "Book value of assets (WDV for depreciable; nil for self-generated goodwill) minus book value of liabilities",
                "Aggregate of FMV of assets minus aggregate of liabilities, excluding revaluation",
                "The same value as the sale consideration",
            ],
            "correct": 1,
            "explain": "Per Sec 50B Explanation, net worth = aggregate value of total assets minus value of liabilities, both at book value. Depreciable assets at WDV per Sec 43(6); self-generated goodwill explicitly excluded (post-FY 2020-21). NOT at FMV.",
            "source": "Sec 50B Explanation",
        },
        {
            "q": "Under Section 47(via), tax-neutral inbound cross-border merger requires:",
            "options": [
                "Foreign company to be incorporated in a country with a tax treaty with India",
                "≥ 25% of the shareholders of the foreign company to continue as shareholders of the Indian company",
                "At least 51% of shareholders of the foreign company to continue (no specific value test)",
                "All the conditions of Sec 2(1B) plus continuity of business in India",
            ],
            "correct": 3,
            "explain": "Sec 47(via) — the inbound foreign-to-Indian merger exemption — requires (1) the conditions of Sec 2(1B) to be met, and (2) the amalgamated Indian company to continue the business of the amalgamating foreign company. The 25% test in option (b) applies to Sec 47(vicc), not 47(via).",
            "source": "Sec 47(via), Income-tax Act",
        },
        {
            "q": "Anarkali Sarabhai (SC 1997) established that capital reduction with payment to shareholders is:",
            "options": [
                "Always a tax-free return of capital",
                "A deemed dividend under Sec 2(22)(d) to the extent of accumulated profits, balance return of capital",
                "Always taxable as capital gains",
                "Tax-free up to the FMV of shares; taxable above",
            ],
            "correct": 1,
            "explain": "Anarkali Sarabhai held that distribution on capital reduction is a deemed dividend under Sec 2(22)(d) to the extent of the company's accumulated profits (capitalised or not); excess is treated as return of capital. Post-Oct 2020 the dividend is taxed at shareholder slab rate.",
            "source": "Anarkali Sarabhai v. CIT (1997) 224 ITR 422 (SC)",
        },
    ],

    # ----------------------------------------------------------------------
    # Ind AS
    # ----------------------------------------------------------------------
    "ind-as": [
        {
            "q": "The threshold for mandatory Ind AS applicability for an unlisted company is net worth of:",
            "options": ["₹100 crore", "₹250 crore", "₹500 crore", "₹1,000 crore"],
            "correct": 1,
            "explain": "Rule 4 of the Companies (Indian Accounting Standards) Rules 2015 — unlisted companies with net worth ≥ ₹250 crore mandatorily apply Ind AS. Their subsidiaries, joint ventures and associates also become Ind AS preparers.",
            "source": "Rule 4, Companies (Ind AS) Rules 2015",
        },
        {
            "q": "Under Ind AS 115, the 5-step model is applied in which order?",
            "options": [
                "Recognise → Identify obligations → Allocate price → Identify contract → Determine price",
                "Identify contract → Identify obligations → Determine price → Allocate price → Recognise revenue",
                "Determine price → Identify contract → Identify obligations → Recognise → Allocate",
                "Identify obligations → Identify contract → Determine price → Recognise → Allocate",
            ],
            "correct": 1,
            "explain": "Ind AS 115's 5-step model: (1) Identify the contract, (2) Identify performance obligations, (3) Determine transaction price, (4) Allocate price to obligations, (5) Recognise revenue when/as obligation is satisfied.",
            "source": "Ind AS 115",
        },
        {
            "q": "Under Ind AS 116, which of the following leases are EXEMPT from on-balance-sheet recognition by the lessee?",
            "options": [
                "All leases up to 24 months",
                "Leases of low-value assets and short-term leases (≤ 12 months)",
                "Only operating leases",
                "Only leases where the asset value < ₹10 lakh",
            ],
            "correct": 1,
            "explain": "Ind AS 116 paragraph 5 allows the lessee to elect not to apply the on-balance-sheet model to (a) short-term leases (≤ 12 months) by class of asset, and (b) low-value asset leases on a lease-by-lease basis. Both are exemptions, not exclusions.",
            "source": "Ind AS 116, paragraph 5",
        },
        {
            "q": "For Ind AS 109 ECL on trade receivables, the simplified approach requires:",
            "options": [
                "12-month ECL always",
                "Lifetime ECL always",
                "12-month ECL for current receivables; lifetime for overdue",
                "Stage 1/2/3 logic same as the general approach",
            ],
            "correct": 1,
            "explain": "Per Ind AS 109 paragraph 5.5.15, the simplified approach for trade receivables (and contract assets without significant financing component) always uses lifetime ECL — no stage migration logic needed.",
            "source": "Ind AS 109, paragraph 5.5.15",
        },
        {
            "q": "Under Ind AS 110, an investor has 'control' over an investee when which of the following exists?",
            "options": [
                "Only power over the investee",
                "Only majority voting rights",
                "Power + exposure to variable returns + ability to use power to affect returns",
                "Power + ability to remove the management",
            ],
            "correct": 2,
            "explain": "Ind AS 110 defines control through 3 cumulative elements: power over the investee, exposure (or rights) to variable returns from its involvement, and the ability to use power to affect those returns. All three must coexist.",
            "source": "Ind AS 110, paragraph 7",
        },
        {
            "q": "Under Ind AS 103, common-control business combinations are:",
            "options": [
                "Accounted for using the acquisition method",
                "Outside the scope of Ind AS 103; accounted at carrying value per Appendix C (pooling)",
                "Treated as a slump sale",
                "Always result in goodwill",
            ],
            "correct": 1,
            "explain": "Ind AS 103 paragraph 2(c) excludes common-control transactions. Appendix C prescribes the pooling-of-interests / carrying-value method — no goodwill is recognised; the difference between consideration and carrying value of net assets goes to capital reserve.",
            "source": "Ind AS 103 paragraph 2(c) + Appendix C",
        },
        {
            "q": "Goodwill under Ind AS is:",
            "options": [
                "Amortised over 10 years",
                "Amortised over its useful life (≤ 20 years)",
                "Not amortised; tested for impairment annually",
                "Written off in the year of acquisition",
            ],
            "correct": 2,
            "explain": "Goodwill recognised under Ind AS 103 is NOT amortised. It is tested for impairment at least annually at the cash-generating-unit level, regardless of impairment indicators (Ind AS 36 paragraph 10).",
            "source": "Ind AS 103 + Ind AS 36 paragraph 10",
        },
        {
            "q": "Under Ind AS 12, a deferred tax asset on tax losses is recognised:",
            "options": [
                "Always, since losses can be carried forward",
                "Only to the extent it is probable that future taxable profit will be available against which the loss can be utilised",
                "Only after the entity becomes profitable",
                "Equal to the tax loss × current tax rate, without further test",
            ],
            "correct": 1,
            "explain": "Ind AS 12 paragraph 24 — DTAs are recognised only to the extent it is probable that future taxable profit will be available against which the deductible temporary difference (or loss) can be utilised. The probability assessment must be reassessed every reporting period.",
            "source": "Ind AS 12, paragraph 24",
        },
        {
            "q": "Under Ind AS 19, actuarial gains and losses on a defined benefit obligation are recognised in:",
            "options": [
                "P&L immediately",
                "P&L over the average remaining service life",
                "Other Comprehensive Income, not subsequently reclassified to P&L",
                "Equity directly, bypassing comprehensive income",
            ],
            "correct": 2,
            "explain": "Ind AS 19 — remeasurements (including actuarial gains/losses) of the net defined benefit liability/asset are recognised in OCI and NOT subsequently reclassified to P&L. They remain in OCI permanently.",
            "source": "Ind AS 19, paragraph 122",
        },
        {
            "q": "Investment property under Ind AS 40 is measured at:",
            "options": [
                "Fair value, with changes in P&L",
                "Cost model only; fair value disclosure in notes is mandatory",
                "Choice of cost model or fair value model (similar to PPE revaluation)",
                "Lower of cost and net realisable value",
            ],
            "correct": 1,
            "explain": "Ind AS 40 permits ONLY the cost model for measurement (unlike IAS 40 which has a fair value option). However, fair value disclosure is mandatory — entities must determine and disclose FV even when carrying at cost.",
            "source": "Ind AS 40, paragraphs 30 + 76",
        },
    ],

    # ----------------------------------------------------------------------
    # IT Act 2025
    # ----------------------------------------------------------------------
    "it-act-2025": [
        {
            "q": "The Income-tax Act 2025 became operative on:",
            "options": ["1 April 2025", "1 January 2026", "1 April 2026", "1 July 2026"],
            "correct": 2,
            "explain": "The Income-tax Act 2025 took effect on 1 April 2026, replacing the Income-tax Act 1961 prospectively. The 1961 Act applies only to assessments and transactions for periods up to 31 March 2026.",
            "source": "Income-tax Act 2025; CBDT",
        },
        {
            "q": "Under Section 6(1A) — 'deemed resident' — the income threshold is:",
            "options": ["₹5 lakh", "₹10 lakh", "₹15 lakh", "₹50 lakh"],
            "correct": 2,
            "explain": "An Indian citizen with total income (other than foreign-source) > ₹15 lakh, not liable to tax in any other country by reason of domicile/residence, is deemed resident in India under Sec 6(1A).",
            "source": "Sec 6(1A), Income-tax Act",
        },
        {
            "q": "LTCG on listed equity, for transfers post-23 July 2024, is taxed at:",
            "options": [
                "10% with ₹1 lakh exemption",
                "12.5% with ₹1.25 lakh exemption",
                "15% with no exemption",
                "20% with indexation",
            ],
            "correct": 1,
            "explain": "Budget 2024 increased the LTCG rate on listed equity from 10% to 12.5%, and increased the basic exemption from ₹1 lakh to ₹1.25 lakh. Indexation is not available.",
            "source": "Sec 112A; Finance Act 2024",
        },
        {
            "q": "STCG on listed equity, post-Budget 2024, is taxed at:",
            "options": ["15%", "20%", "25.168%", "30%"],
            "correct": 1,
            "explain": "STCG on listed equity (held ≤ 12 months) was increased from 15% to 20% by Budget 2024.",
            "source": "Sec 111A; Finance Act 2024",
        },
        {
            "q": "The GAAR threshold (aggregate tax benefit in a financial year) for invoking impermissible avoidance arrangement is:",
            "options": ["₹50 lakh", "₹1 crore", "₹3 crore", "₹10 crore"],
            "correct": 2,
            "explain": "Rule 10U sets the threshold at ₹3 crore — GAAR applies only when the aggregate tax benefit from an arrangement exceeds this amount in a financial year.",
            "source": "Sec 95 + Rule 10U",
        },
        {
            "q": "Updated returns under Section 139(8A) can be filed within:",
            "options": [
                "12 months from end of AY",
                "24 months from end of AY",
                "48 months from end of AY",
                "Anytime, with sufficient cause",
            ],
            "correct": 2,
            "explain": "The window was extended from 24 to 48 months by Finance Act 2025 (or the equivalent provision in IT Act 2025). Additional tax of 25-60% applies based on timing of filing.",
            "source": "Sec 139(8A), Income-tax Act",
        },
        {
            "q": "Sec 43B(h) disallowance for delayed MSME payments applies:",
            "options": [
                "Only to micro enterprises",
                "To micro and small enterprises beyond MSMED Act payment timelines (15/45 days)",
                "To all MSMEs regardless of payment terms",
                "Only to manufacturing MSMEs",
            ],
            "correct": 1,
            "explain": "Sec 43B(h) (effective FY 2023-24) disallows amounts payable to MICRO or SMALL enterprises (not medium) that exceed the MSMED Act timeline — 15 days without agreement, 45 days with written agreement. Unless paid in the year, the amount is disallowed.",
            "source": "Sec 43B(h); MSMED Act 2006",
        },
        {
            "q": "Virtual Digital Assets (VDAs) under Sec 115BBH are taxed at:",
            "options": [
                "Slab rate",
                "20% with indexation",
                "30% with no set-off and no deduction other than cost",
                "15% (similar to STCG on listed equity)",
            ],
            "correct": 2,
            "explain": "Sec 115BBH taxes income from transfer of VDAs at a flat 30%. No deduction is allowed other than cost of acquisition. No set-off of losses from one VDA against gains from another. TDS at 1% under Sec 194S.",
            "source": "Sec 115BBH; Finance Act 2022",
        },
        {
            "q": "POEM (Place of Effective Management) test for foreign-company residency requires:",
            "options": [
                "Majority of directors to be Indian residents",
                "Place where key management and commercial decisions are made",
                "Place of incorporation",
                "Place where books of account are kept",
            ],
            "correct": 1,
            "explain": "POEM is defined as the place where key management and commercial decisions that are necessary for the conduct of the business of the entity as a whole are, in substance, made. Codified in Sec 6(3)(ii); CBDT Circular 6/2017 provides guidelines.",
            "source": "Sec 6(3)(ii); CBDT Circular 6/2017",
        },
        {
            "q": "Faceless assessment is conducted via:",
            "options": [
                "The jurisdictional AO with video-conferencing",
                "The Central Board of Direct Taxes directly",
                "The National Faceless Assessment Centre (NaFAC) with automated team-based allocation",
                "Any AO with a digital signature",
            ],
            "correct": 2,
            "explain": "Sec 144B prescribes the faceless mechanism — case allocation is automated, geographically agnostic, team-based, and conducted through the NaFAC. No face-to-face interaction. Codified in Sec 144B with implementation via CBDT scheme.",
            "source": "Sec 144B; CBDT Scheme & Notifications",
        },
    ],

    # ----------------------------------------------------------------------
    # Internal Audit
    # ----------------------------------------------------------------------
    "internal-audit": [
        {
            "q": "Internal audit is mandatory under Sec 138 + Rule 13 for a private company having:",
            "options": [
                "Paid-up capital ≥ ₹20 crore",
                "Turnover ≥ ₹100 crore or borrowings ≥ ₹50 crore",
                "Turnover ≥ ₹200 crore or borrowings ≥ ₹100 crore",
                "Any private company",
            ],
            "correct": 2,
            "explain": "Per Rule 13(1)(c), a private company must appoint an internal auditor if its turnover ≥ ₹200 crore OR outstanding loans/borrowings from banks/PFIs ≥ ₹100 crore at any point during the immediately preceding financial year.",
            "source": "Sec 138 + Rule 13(1)(c)",
        },
        {
            "q": "Can the statutory auditor also perform internal audit of the same company?",
            "options": [
                "Yes, with audit committee approval",
                "No, prohibited by Sec 144 of Companies Act",
                "Yes, but only for non-listed companies",
                "Yes, if the same partner doesn't sign both",
            ],
            "correct": 1,
            "explain": "Sec 144 prohibits the statutory auditor from providing internal audit services (and other listed services) to the auditee — to maintain auditor independence. The functions must be performed by different persons/firms.",
            "source": "Sec 144, Companies Act 2013",
        },
        {
            "q": "The Three Lines Model was introduced by IIA in:",
            "options": ["2010", "2015", "2020", "2023"],
            "correct": 2,
            "explain": "IIA updated the 'Three Lines of Defence' framework to the 'Three Lines Model' in July 2020, emphasising collaboration and alignment with organisational objectives rather than 'defence' against threats.",
            "source": "IIA Three Lines Model, July 2020",
        },
        {
            "q": "Under COSO 2013 Internal Control framework, how many components are there?",
            "options": ["3", "5", "7", "17"],
            "correct": 1,
            "explain": "COSO 2013 framework has 5 components — Control Environment, Risk Assessment, Control Activities, Information & Communication, Monitoring Activities — and 17 underlying principles supporting the components.",
            "source": "COSO Internal Control — Integrated Framework (2013)",
        },
        {
            "q": "An external quality assessment of the internal audit function (per IIA Standards) must be conducted:",
            "options": [
                "Every year",
                "Every 3 years",
                "Every 5 years",
                "Only when management requires",
            ],
            "correct": 2,
            "explain": "IIA Standard 1312 requires external quality assessments at least once every 5 years by a qualified, independent reviewer. ICAI SIA 530 mirrors this. Internal quality monitoring (Standard 1311) is continuous.",
            "source": "IIA Standard 1312; ICAI SIA 530",
        },
        {
            "q": "For ICFR under Sec 143(3)(i), a 'material weakness' is:",
            "options": [
                "Any control deficiency",
                "A deficiency such that there is a reasonable possibility of a material misstatement going undetected",
                "An error of any magnitude in the financial statements",
                "A control that the auditor cannot test",
            ],
            "correct": 1,
            "explain": "Per the ICAI GN on Audit of IFCFR — material weakness is a deficiency, or combination, in ICFR such that there is a reasonable possibility that a material misstatement will not be prevented or detected on a timely basis. Significant deficiency is less severe.",
            "source": "ICAI Guidance Note on Audit of IFCFR",
        },
        {
            "q": "Walkthrough procedure is performed primarily to:",
            "options": [
                "Test operating effectiveness of controls",
                "Confirm understanding of the process flow and the design of controls",
                "Substantiate account balances",
                "Comply with sample-size requirements",
            ],
            "correct": 1,
            "explain": "Walkthrough = tracing 1-2 transactions end-to-end to confirm the auditor's understanding of the process flow and the design effectiveness of key controls. It is NOT a substantive procedure and provides minimal evidence of operating effectiveness.",
            "source": "SA 315 (Revised); ICAI GN on IFCFR",
        },
        {
            "q": "Segregation of Duties (SOD) primarily addresses risks in:",
            "options": [
                "Cost reduction",
                "Authorisation, recording, custody and reconciliation being concentrated in one person",
                "Compliance with statutory filings",
                "Speed of transaction processing",
            ],
            "correct": 1,
            "explain": "SOD is a preventive control that separates the four functions — Authorisation, Recording, Custody and Reconciliation — across different individuals/roles. Concentration in one person creates fraud / error opportunity. The 'four-eyes principle' is an extension.",
            "source": "Standard internal-control theory; COSO 2013",
        },
        {
            "q": "Which of the following is NOT a 'second line' function under the IIA Three Lines Model?",
            "options": [
                "Risk management",
                "Compliance",
                "Operational management",
                "Controllership",
            ],
            "correct": 2,
            "explain": "Operational management is the FIRST line — managers and process owners who own and manage risks at the source. Second line: risk, compliance, controllership functions that monitor and challenge first-line. Third line: internal audit.",
            "source": "IIA Three Lines Model 2020",
        },
        {
            "q": "The Risk and Control Matrix (RCM) for a process typically does NOT include:",
            "options": [
                "The control activity description",
                "The frequency of the control",
                "The market share of competitors",
                "The risk that the control mitigates",
            ],
            "correct": 2,
            "explain": "An RCM documents per-process: process step, risk, control, control type (preventive/detective; manual/automated; key/compensating), frequency, tester, test result. It does NOT include market or competitive information.",
            "source": "Practice; ICAI IA Practical Guide",
        },
    ],

    # ----------------------------------------------------------------------
    # Labour Codes
    # ----------------------------------------------------------------------
    "labor-codes": [
        {
            "q": "Under the Code on Wages 2019, if excluded allowances exceed what percentage of total remuneration, they get added back to 'wages'?",
            "options": ["33%", "40%", "50%", "60%"],
            "correct": 2,
            "explain": "Section 2(y) — if the aggregate of excluded items (HRA, conveyance, OT etc.) exceeds 50% of total remuneration, the excess is added back into 'wages' for PF, gratuity, leave-encashment computation. This is the 50% floor on basic + DA.",
            "source": "Sec 2(y), Code on Wages 2019",
        },
        {
            "q": "Maternity leave under the Code on Social Security 2020 is:",
            "options": [
                "12 weeks for all children",
                "26 weeks for first two children; 12 weeks for third onwards",
                "26 weeks for all children regardless of order",
                "20 weeks with employer's discretion",
            ],
            "correct": 1,
            "explain": "Sec 59 of the Code on Social Security 2020 retains the Maternity Benefit Amendment 2017 framework — 26 weeks paid leave for first two surviving children; 12 weeks for third and subsequent. Adopting mothers and commissioning mothers: 12 weeks.",
            "source": "Sec 59, Code on Social Security 2020",
        },
        {
            "q": "For aggregators (digital platforms), the social-security contribution to the gig-worker fund is:",
            "options": [
                "0.5% of turnover",
                "1-2% of annual turnover (capped)",
                "5% of amount paid to gig workers, no cap",
                "Fixed ₹1 lakh per year",
            ],
            "correct": 1,
            "explain": "Section 114 of the Code on Social Security 2020 — aggregators must contribute 1-2% of annual turnover (or 5% of amount paid to gig workers, whichever lower, capped at industry-prescribed limit) to a dedicated social-security fund for gig workers.",
            "source": "Sec 114, Code on Social Security 2020",
        },
        {
            "q": "Standing Orders under the Industrial Relations Code 2020 are mandatory for establishments with how many workers?",
            "options": ["100 or more", "200 or more", "300 or more", "500 or more"],
            "correct": 2,
            "explain": "Sec 28 IR Code 2020 raised the threshold to 300 or more workers (from 100 under the old Industrial Employment Standing Orders Act). Smaller establishments may voluntarily adopt model standing orders.",
            "source": "Sec 28, Industrial Relations Code 2020",
        },
        {
            "q": "Government permission for retrenchment or closure under IR Code 2020 is required if the establishment has:",
            "options": ["50 or more workers", "100 or more workers", "300 or more workers", "1,000 or more workers"],
            "correct": 2,
            "explain": "Sec 70 (retrenchment) and Sec 75 (closure) — government permission threshold raised to 300 workers (from 100 under the old ID Act). Below 300, only 60-day notice + 15 days × completed years compensation are required.",
            "source": "Sec 70, 75 — IR Code 2020",
        },
        {
            "q": "Under the Code on Social Security 2020, the minimum service for gratuity for a fixed-term employee is:",
            "options": ["3 months", "1 year", "3 years", "5 years"],
            "correct": 1,
            "explain": "Sec 53 — fixed-term employees become eligible for gratuity after 1 year of continuous service (vs 5 years for permanent employees). Computation: 15 days' wages × completed years.",
            "source": "Sec 53, Code on Social Security 2020",
        },
        {
            "q": "A 'negotiating union' status under IR Code 2020 requires support of:",
            "options": [
                "At least 25% of workers",
                "Simple majority (>50%) of workers",
                "≥ 51% of workers",
                "75% of workers",
            ],
            "correct": 2,
            "explain": "Sec 14 IR Code 2020 — a union must have ≥ 51% support of workers to be the sole negotiating union. Otherwise, a negotiating council with proportionate representation from registered unions is constituted.",
            "source": "Sec 14, IR Code 2020",
        },
        {
            "q": "Women can work in:",
            "options": [
                "Only day shifts in all establishments",
                "Day shifts in factories, but not in night shifts under any circumstance",
                "All establishments and all shifts, subject to safety provisions (transport, lighting, consent)",
                "Only shops & commercial establishments, not factories",
            ],
            "correct": 2,
            "explain": "Sec 43 of the OSH Code 2020 explicitly permits women in all establishments and all shifts. The qualifying conditions are: safe transport, adequate lighting, and the woman worker's consent. This is a major change from the older restrictions.",
            "source": "Sec 43, OSH Code 2020",
        },
        {
            "q": "The Shram Suvidha portal is used for:",
            "options": [
                "Filing income-tax returns",
                "Unified labour-law compliance: single registration, returns and inspection management",
                "Booking factory inspections only",
                "GST returns for labour-supply contracts",
            ],
            "correct": 1,
            "explain": "shramsuvidha.gov.in is the Ministry of Labour's unified online compliance portal covering all 4 codes — single registration of establishments, consolidated returns, online inspection management, grievance redressal.",
            "source": "Ministry of Labour & Employment",
        },
        {
            "q": "Contract-labour licensing under the OSH Code is mandatory when the principal employer engages:",
            "options": [
                "10 or more contract workers",
                "20 or more contract workers",
                "50 or more contract workers",
                "100 or more contract workers",
            ],
            "correct": 2,
            "explain": "Chapter XI of the OSH Code 2020 — contractor licensing required when 50 or more contract workers are engaged (raised from 20 under the old Contract Labour Act). Welfare facilities remain the principal employer's responsibility.",
            "source": "Chapter XI, OSH Code 2020",
        },
    ],

    # ----------------------------------------------------------------------
    # Auditing
    # ----------------------------------------------------------------------
    "auditing": [
        {
            "q": "Statutory auditor rotation for an audit firm under Sec 139(2) is mandatory after:",
            "options": ["5 years", "10 years", "15 years", "Not required for firms"],
            "correct": 1,
            "explain": "Sec 139(2) — an audit FIRM cannot be appointed for more than two consecutive terms of 5 years each (i.e., 10 years total), followed by a 5-year cooling-off period. Individual auditors: 5 years, then 5 cooling-off.",
            "source": "Sec 139(2) + Rule 5, Companies Act 2013",
        },
        {
            "q": "Key Audit Matters (KAM) reporting under SA 701 is mandatory for:",
            "options": [
                "All companies with statutory audit",
                "Listed entities only",
                "Companies with turnover > ₹100 cr",
                "Companies under CARO 2020",
            ],
            "correct": 1,
            "explain": "SA 701 requires KAM communication only for audits of complete sets of general-purpose financial statements of listed entities. For other entities, KAM is voluntary but encouraged.",
            "source": "SA 701",
        },
        {
            "q": "SA 240 presumes which of the following as a significant risk in every audit?",
            "options": [
                "Revenue recognition only",
                "Management override of controls only",
                "Both management override AND (typically) revenue recognition",
                "Bank reconciliations",
            ],
            "correct": 2,
            "explain": "SA 240 paragraph 32 — there is always a presumed risk of management override of controls (mandatory significant risk). Paragraph 26 also presumes revenue recognition risk in most cases, though it may be rebutted in specific circumstances.",
            "source": "SA 240 paragraphs 26 + 32",
        },
        {
            "q": "Which SA covers the auditor's responsibilities relating to laws and regulations?",
            "options": ["SA 200", "SA 240", "SA 250", "SA 260"],
            "correct": 2,
            "explain": "SA 250 — Consideration of Laws and Regulations in an Audit of Financial Statements. Distinguishes (a) laws affecting amounts/disclosures in FS — auditor obtains understanding and considers effect; (b) other laws material to operations — auditor performs specified procedures.",
            "source": "SA 250",
        },
        {
            "q": "CARO 2020 does NOT apply to:",
            "options": [
                "Listed companies",
                "Public companies above thresholds",
                "OPCs, small companies, certain charitable companies, banking/insurance/electricity cos",
                "Any company with turnover > ₹100 cr",
            ],
            "correct": 2,
            "explain": "CARO 2020 paragraph 1(2) exemptions: One-Person Companies, small companies, certain Section 8 (charitable) companies, banking companies, insurance companies, and electricity-sector companies (which have separate sectoral audit frameworks).",
            "source": "CARO 2020 paragraph 1(2)",
        },
        {
            "q": "Under SA 540 (Revised), accounting estimates with significant subjectivity, complexity or uncertainty:",
            "options": [
                "Don't require special audit procedures",
                "Require risk-based audit response calibrated to complexity",
                "Are not auditable",
                "Must always be tested at 100% population",
            ],
            "correct": 1,
            "explain": "SA 540 (Revised) — the new estimates standard — takes a risk-based approach. Audit procedures must be scaled to the complexity, subjectivity and inherent risk of the estimate. Simple estimates (depreciation) → minimal; complex estimates (ECL, fair value of L3 instruments) → significant procedures.",
            "source": "SA 540 (Revised)",
        },
        {
            "q": "The materiality threshold under SA 320 is:",
            "options": [
                "Fixed at 5% of pre-tax profit",
                "Determined by the auditor's professional judgment considering quantitative and qualitative factors",
                "Set by the Companies Act at ₹1 crore",
                "Determined by management",
            ],
            "correct": 1,
            "explain": "SA 320 does NOT prescribe a fixed percentage. Materiality is the auditor's professional judgment. Common benchmarks: 5% of pre-tax profit, 1% of revenue, 1% of total assets — selected based on entity nature and key users. Performance materiality is typically 50-75% of overall.",
            "source": "SA 320",
        },
        {
            "q": "Section 143(3)(i) — audit reporting on ICFR — applies to:",
            "options": [
                "All companies",
                "Only listed companies",
                "Listed + prescribed unlisted/private companies; small co. and OPCs exempt",
                "Companies with turnover > ₹500 cr only",
            ],
            "correct": 2,
            "explain": "ICFR audit reporting under Sec 143(3)(i) — applies to all listed companies, plus unlisted public and private companies meeting thresholds (turnover ≥ ₹50 cr OR borrowings ≥ ₹25 cr OR deposits ≥ ₹25 cr). OPCs, small companies, and certain dormant/charitable cos are exempt under the Companies (Amendment) Act 2017.",
            "source": "Sec 143(3)(i) + Rule 10A",
        },
        {
            "q": "SA 600 (Revised) — Special Considerations: Audits of Group Financial Statements — is effective for periods beginning on or after:",
            "options": ["1 April 2023", "1 April 2024", "1 April 2025", "1 April 2026"],
            "correct": 3,
            "explain": "Per ICAI's notification, SA 600 (Revised) is effective for audits of group financial statements for periods commencing on or after 1 April 2026. The earlier SA 600 continues to apply to prior periods.",
            "source": "ICAI AASB",
        },
        {
            "q": "Under Sec 44AB, the tax audit threshold for business is:",
            "options": [
                "₹50 lakh turnover",
                "₹1 crore turnover; ₹10 crore if cash transactions ≤ 5%",
                "₹2 crore turnover",
                "₹10 crore for all businesses",
            ],
            "correct": 1,
            "explain": "Sec 44AB — businesses with turnover > ₹1 crore require tax audit. Threshold rises to ₹10 crore if aggregate cash receipts AND aggregate cash payments are each ≤ 5% of total receipts/payments. For professionals: receipts > ₹50 lakh.",
            "source": "Sec 44AB, Income-tax Act",
        },
    ],

    # ----------------------------------------------------------------------
    # English
    # ----------------------------------------------------------------------
    "english": [
        {
            "q": "Choose the correct article: 'I am ____ MBA student at ____ university.'",
            "options": [
                "a / a",
                "an / a",
                "an / an",
                "a / an",
            ],
            "correct": 1,
            "explain": "Articles depend on the SOUND, not the letter. 'MBA' begins with /em/ — a vowel sound → 'an'. 'University' begins with /ju:/ — a consonant sound (the y-glide) → 'a'.",
            "source": "Cambridge English usage",
        },
        {
            "q": "Which sentence is grammatically correct?",
            "options": [
                "I have completed my work yesterday.",
                "I completed my work yesterday.",
                "I am completed my work yesterday.",
                "I had completed my work yesterday.",
            ],
            "correct": 1,
            "explain": "Present perfect ('have completed') cannot be used with a specific past time marker ('yesterday'). Use simple past — 'I completed... yesterday'. Option (d) past perfect requires a context of another past action.",
            "source": "Standard English grammar",
        },
        {
            "q": "The correct past participle of 'to lie' (meaning recline) is:",
            "options": ["lay", "lied", "laid", "lain"],
            "correct": 3,
            "explain": "'Lie' (recline): lie / lay / lain. 'Lay' (place down): lay / laid / laid. 'Lie' (tell untruth): lie / lied / lied. The most error-prone English irregular verb set.",
            "source": "Cambridge Dictionary; Practical English Usage",
        },
        {
            "q": "'____ I help you?' is the most polite form when offering help:",
            "options": ["Can", "May", "Will", "Shall"],
            "correct": 1,
            "explain": "'May I help you?' is the most formal/polite. 'Can I help you?' is acceptable but slightly less polite. 'Shall I help you?' (British) is also acceptable. 'Will I help you?' is incorrect — sounds like a question about future intent.",
            "source": "Cambridge English Usage",
        },
        {
            "q": "Change to passive voice: 'Someone has stolen my bag.'",
            "options": [
                "My bag has stolen by someone.",
                "My bag has been stolen.",
                "My bag was stolen.",
                "My bag is stolen by someone.",
            ],
            "correct": 1,
            "explain": "Present perfect active 'has stolen' → present perfect passive 'has been stolen'. Option (c) ('was stolen') is simple past passive, which changes the tense. Option (a) misses 'been'. Option (d) uses simple present passive.",
            "source": "Standard English grammar — voice transformation",
        },
        {
            "q": "Choose the correct preposition: 'She is interested ____ classical music.'",
            "options": ["on", "in", "about", "for"],
            "correct": 1,
            "explain": "'Interested IN' is the fixed collocation. Other common collocations: depend ON, suffer FROM, agree WITH (person), agree TO (proposal), look AT, look FOR, look AFTER.",
            "source": "Cambridge English Vocabulary in Use",
        },
        {
            "q": "Which is the correct third conditional?",
            "options": [
                "If I had known, I would help.",
                "If I knew, I would have helped.",
                "If I had known, I would have helped.",
                "If I knew, I would help.",
            ],
            "correct": 2,
            "explain": "Third conditional (unreal past): If + past perfect, would have + past participle. Option (d) is second conditional (unreal present); option (a) and (b) are mixed/wrong.",
            "source": "Standard English grammar — conditionals",
        },
        {
            "q": "Indirect speech: She said, 'I am leaving tomorrow.' becomes:",
            "options": [
                "She said that she is leaving tomorrow.",
                "She said that she was leaving the next day.",
                "She told me that she leaves tomorrow.",
                "She said that she has been leaving tomorrow.",
            ],
            "correct": 1,
            "explain": "Reporting verb 'said' is past — tense shifts back: present continuous 'am leaving' → past continuous 'was leaving'. Time adverb 'tomorrow' → 'the next day' / 'the following day'.",
            "source": "Standard English grammar — reported speech",
        },
        {
            "q": "Which word is INCORRECTLY used in standard English?",
            "options": [
                "Beneficial",
                "Maleficent",
                "Beneficiary",
                "Maleficiary",
            ],
            "correct": 3,
            "explain": "There is no word 'maleficiary'. The legitimate forms are: beneficial / beneficiary (bene = good); malevolent / malefactor / malice (mal = bad). The 'beneficiary' pattern doesn't have a 'mal' equivalent — 'wrongdoer' or 'malefactor' is used.",
            "source": "Cambridge Dictionary; Norman Lewis Word Power",
        },
        {
            "q": "The phrase 'do the needful' is an example of:",
            "options": [
                "Standard British English",
                "Indian English usage that's considered informal/dated in international contexts",
                "Standard American English",
                "Legal/contractual jargon used worldwide",
            ],
            "correct": 1,
            "explain": "'Do the needful' is a hallmark of Indian English. While understandable to global audiences, it's considered informal/dated and is best replaced with specific requests in international correspondence — 'please process this' or 'please proceed with the requirements'.",
            "source": "Cambridge Dictionary (Indian English entries)",
        },
    ],
}
