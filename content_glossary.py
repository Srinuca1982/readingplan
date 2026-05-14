"""Glossary — every term with a precise legal/professional meaning.

Each entry has: term, definition (one or two sentences), source (the section/standard
that defines it), and tags (which subject areas it relates to).
"""

GLOSSARY = [
    # --- Restructuring / Companies Act / Tax core ---
    {
        "term": "Amalgamation",
        "definition": "Combination of two or more companies into one, where the property and liabilities of the amalgamating company transfer to the amalgamated company and at least 3/4 (by value) of the amalgamating company's shareholders become shareholders of the amalgamated company.",
        "source": "Sec 2(1B), Income-tax Act",
        "tags": ["Restructuring", "Tax"],
    },
    {
        "term": "Demerger",
        "definition": "Transfer of one or more undertakings of a company to a resulting company on a going-concern basis, with proportionate share issue to the demerged company's shareholders and ≥ 3/4 shareholder continuity.",
        "source": "Sec 2(19AA), Income-tax Act",
        "tags": ["Restructuring", "Tax"],
    },
    {
        "term": "Undertaking",
        "definition": "A part of a business that is capable of being carried on independently — includes all assets, liabilities, employees and contracts attributable to it. Self-contained, transferable business unit.",
        "source": "Explanation to Sec 2(19AA), Income-tax Act; Sec 180(1)(a), Companies Act",
        "tags": ["Restructuring", "Tax"],
    },
    {
        "term": "Going concern",
        "definition": "A business that is functional and capable of being carried on by the buyer from the date of transfer, without re-procuring anything material. The unifying test across Sec 2(19AA) demerger, Sec 2(42C) slump sale and GST Notification 12/2017.",
        "source": "Sec 2(19AA)(iv); Notification 12/2017 GST Entry 2",
        "tags": ["Restructuring", "Tax", "Ind AS"],
    },
    {
        "term": "Slump sale",
        "definition": "Transfer of an undertaking as a result of a sale for a lump-sum consideration, without values being assigned to individual assets and liabilities. Taxed under Sec 50B; gain = consideration minus net worth.",
        "source": "Sec 2(42C) read with Sec 50B, Income-tax Act",
        "tags": ["Restructuring", "Tax"],
    },
    {
        "term": "Net worth (for slump sale)",
        "definition": "Aggregate value of total assets minus value of liabilities of the undertaking, computed at book value. Self-generated goodwill is explicitly excluded (post-FY 2020-21); depreciable assets at WDV.",
        "source": "Explanation 2 to Sec 50B; Rule 11UAE",
        "tags": ["Restructuring", "Tax"],
    },
    {
        "term": "Appointed date",
        "definition": "The date specified in a scheme of arrangement from which the transaction is deemed to take effect for accounting, tax and ownership purposes. The fictional 'transfer date'. May be a calendar date or contingent date but generally not more than 12 months before scheme filing (MCA circular Aug 2019).",
        "source": "Sec 232(6), Companies Act 2013",
        "tags": ["Restructuring"],
    },
    {
        "term": "Effective date",
        "definition": "The actual date the NCLT order is filed with the ROC and the scheme operates in real time. Distinct from appointed date (which is usually earlier).",
        "source": "Practice; Marshall Sons doctrine",
        "tags": ["Restructuring"],
    },
    {
        "term": "Fast-track merger",
        "definition": "A merger that bypasses NCLT entirely and goes to the Regional Director via the ROC. Available for small companies, holding-WOS, two start-ups, start-up + small company, and certain unlisted public companies (post Sept 2024 MCA notification).",
        "source": "Sec 233 + Rule 25, CAA Rules 2016",
        "tags": ["Restructuring"],
    },
    {
        "term": "Cross-border merger",
        "definition": "Merger between an Indian company and a foreign company incorporated in a notified jurisdiction. Carries an automatic FEMA deemed-approval if compliant with the Cross Border Merger Regulations 2018.",
        "source": "Sec 234 + Rule 25A, Companies Act; FEMA Cross Border Merger Regulations 2018",
        "tags": ["Restructuring", "FEMA"],
    },
    {
        "term": "Capital reduction",
        "definition": "Tribunal-approved reduction of paid-up share capital. Distribution to shareholders is deemed dividend to the extent of accumulated profits (Anarkali Sarabhai principle).",
        "source": "Sec 66, Companies Act 2013; Sec 2(22)(d), Income-tax Act",
        "tags": ["Restructuring", "Tax"],
    },
    {
        "term": "Buyback",
        "definition": "Company purchase of its own shares from existing shareholders, financed from free reserves / securities premium / proceeds of fresh issue of different securities. Post 1 Oct 2024, taxed in the shareholder's hands as deemed dividend.",
        "source": "Sec 68–70, Companies Act 2013; Sec 115QA (regime change Oct 2024)",
        "tags": ["Restructuring", "Tax"],
    },
    {
        "term": "Scheme of arrangement",
        "definition": "Any compromise or arrangement between a company and its creditors or members — the umbrella vehicle for mergers, demergers, capital reductions and similar transactions. Sanctioned by NCLT.",
        "source": "Sec 230–232, Companies Act 2013",
        "tags": ["Restructuring"],
    },
    {
        "term": "Resolution plan",
        "definition": "A binding restructuring plan submitted under the IBC by a resolution applicant for a corporate debtor under CIRP. Approved by 66% of CoC and sanctioned by NCLT. Carries 'clean slate' effect — all undisclosed past liabilities extinguished (Essar Steel SC).",
        "source": "Sec 30–31, IBC 2016",
        "tags": ["Restructuring", "IBC"],
    },
    {
        "term": "Notified jurisdiction",
        "definition": "A country prescribed under Rule 25A for cross-border mergers — generally FATF / IOSCO MMoU compliant with a bilateral arrangement with India. Examples: USA, UK, Singapore, Mauritius, Netherlands.",
        "source": "Rule 25A, CAA Rules 2016",
        "tags": ["Restructuring", "FEMA"],
    },
    {
        "term": "POEM (Place of Effective Management)",
        "definition": "The place where key management and commercial decisions necessary for the conduct of the business as a whole are made. Test for determining the tax residence of a foreign company.",
        "source": "Sec 6(3)(ii), Income-tax Act; CBDT Circular 6/2017",
        "tags": ["Tax", "FEMA"],
    },
    {
        "term": "GAAR",
        "definition": "General Anti-Avoidance Rule. An 'impermissible avoidance arrangement' — main purpose to obtain tax benefit + one of: not at arm's length / misuse of law / lacks commercial substance / non-bona-fide — can be recharacterised. Threshold: tax benefit > ₹3 cr.",
        "source": "Chapter X-A, Income-tax Act (Sec 95–102)",
        "tags": ["Tax", "Restructuring"],
    },
    {
        "term": "Indirect transfer",
        "definition": "Transfer of shares of a foreign company that derive substantial value (≥ 50% and > ₹10 cr in absolute Indian-asset value) from Indian assets. Taxable in India under Sec 9(1)(i) Explanations 5–7.",
        "source": "Sec 9(1)(i), Explanations 5–7, Income-tax Act",
        "tags": ["Tax", "Restructuring", "FEMA"],
    },
    {
        "term": "FMV (Fair Market Value)",
        "definition": "The price an asset would fetch in the open market between independent willing parties. Specific computation rules in Rules 11UA / 11UAE / 11UAB depending on asset class.",
        "source": "Sec 56(2)(x); Rules 11UA, 11UAE, 11UAB, Income-tax Rules",
        "tags": ["Tax", "Ind AS"],
    },
    {
        "term": "Stamp duty",
        "definition": "State-level transaction tax on instruments of conveyance, including NCLT-sanctioned schemes. Rate and basis vary by State. The court order itself is the chargeable instrument in most States.",
        "source": "State-specific Stamp Acts; Indian Stamp Act 1899 (residual)",
        "tags": ["Restructuring"],
    },
    {
        "term": "Open offer",
        "definition": "Mandatory tender offer by an acquirer to public shareholders, triggered when crossing 25% holding (Reg 3) or acquiring change of control (Reg 4) under SAST.",
        "source": "Regulations 3 & 4, SEBI SAST Regulations 2011",
        "tags": ["Restructuring", "SEBI"],
    },
    {
        "term": "Deal Value Threshold (DVT)",
        "definition": "CCI combination notification trigger — deal value > ₹2,000 cr AND target has substantial business operations in India, regardless of asset/turnover tests. In force from 10 Sept 2024.",
        "source": "Sec 5, Competition Act + Notification S.O. 988(E) dt 7 Mar 2024",
        "tags": ["Restructuring", "Competition"],
    },
    {
        "term": "Reverse flip",
        "definition": "Migration of a foreign-domiciled startup's holding structure back to India — typically by merging the foreign HoldCo into the Indian OpCo. Pursued ahead of a domestic IPO.",
        "source": "Practice; Sec 234 inbound merger; FEMA CBM Regulations 2018",
        "tags": ["Restructuring", "FEMA"],
    },

    # --- Ind AS / Accounting ---
    {
        "term": "Control (consolidation)",
        "definition": "Power over an investee + exposure to variable returns + ability to use power to affect those returns. All three elements required to consolidate.",
        "source": "Ind AS 110, paragraphs 6–18",
        "tags": ["Ind AS"],
    },
    {
        "term": "Significant influence",
        "definition": "Power to participate in the financial and operating policy decisions of an investee but not control. Presumed at 20–50% voting rights.",
        "source": "Ind AS 28, paragraph 5",
        "tags": ["Ind AS"],
    },
    {
        "term": "Joint control",
        "definition": "Contractually agreed sharing of control, requiring unanimous consent of the parties sharing control. Triggers joint operation or joint venture accounting.",
        "source": "Ind AS 111",
        "tags": ["Ind AS"],
    },
    {
        "term": "Performance obligation",
        "definition": "A promise in a contract to transfer a distinct good or service (or series of distinct goods/services that are substantially the same) to the customer.",
        "source": "Ind AS 115, paragraphs 22–30",
        "tags": ["Ind AS"],
    },
    {
        "term": "Transaction price",
        "definition": "The amount of consideration to which an entity expects to be entitled in exchange for transferring promised goods/services. Includes variable consideration constrained for reversal risk.",
        "source": "Ind AS 115, paragraphs 47–72",
        "tags": ["Ind AS"],
    },
    {
        "term": "Stand-alone selling price",
        "definition": "The price at which an entity would sell a promised good or service separately to a customer. Used to allocate transaction price across performance obligations.",
        "source": "Ind AS 115, paragraphs 76–80",
        "tags": ["Ind AS"],
    },
    {
        "term": "Right-of-use (ROU) asset",
        "definition": "Lessee's asset representing the right to use the underlying leased asset for the lease term. Initially measured at the lease liability + initial direct costs + prepayments − incentives.",
        "source": "Ind AS 116, paragraphs 22–25",
        "tags": ["Ind AS"],
    },
    {
        "term": "Lease liability",
        "definition": "Lessee's obligation for lease payments not yet paid, measured at the present value using the rate implicit in the lease or the lessee's incremental borrowing rate.",
        "source": "Ind AS 116, paragraphs 26–28",
        "tags": ["Ind AS"],
    },
    {
        "term": "Expected Credit Loss (ECL)",
        "definition": "Present value of cash shortfalls weighted by the probability of default. Recognised in three stages: 12-month ECL (Stage 1), lifetime ECL (Stages 2 & 3).",
        "source": "Ind AS 109, paragraphs 5.5",
        "tags": ["Ind AS"],
    },
    {
        "term": "SPPI test (Solely Payments of Principal and Interest)",
        "definition": "Contractual cash-flow characteristic test for classification of financial assets at amortised cost or FVTOCI under Ind AS 109. Cash flows must be solely principal and interest on the principal outstanding.",
        "source": "Ind AS 109, paragraph 4.1.2",
        "tags": ["Ind AS"],
    },
    {
        "term": "Functional currency",
        "definition": "The currency of the primary economic environment in which the entity operates — typically the currency that influences sales prices and labour/material costs.",
        "source": "Ind AS 21, paragraphs 9–14",
        "tags": ["Ind AS"],
    },
    {
        "term": "Cash-Generating Unit (CGU)",
        "definition": "The smallest identifiable group of assets that generates cash inflows largely independent of other assets/groups. Impairment is tested at CGU level for goodwill and indefinite-life intangibles.",
        "source": "Ind AS 36, paragraphs 68–73",
        "tags": ["Ind AS"],
    },
    {
        "term": "Recoverable amount",
        "definition": "The higher of fair value less costs of disposal AND value in use. Impairment loss = carrying amount minus recoverable amount.",
        "source": "Ind AS 36, paragraph 6",
        "tags": ["Ind AS"],
    },
    {
        "term": "Defined benefit obligation (DBO)",
        "definition": "Present value of expected future payments required to settle the obligation arising from employee service in the current and prior periods. Measured using the projected unit credit method.",
        "source": "Ind AS 19, paragraphs 65–67",
        "tags": ["Ind AS"],
    },
    {
        "term": "Deferred tax",
        "definition": "Tax effects of temporary differences (difference between carrying amount and tax base of an asset/liability). DTA recognition is limited to the extent it is probable that future taxable profit will be available.",
        "source": "Ind AS 12, paragraphs 15–43",
        "tags": ["Ind AS", "Tax"],
    },
    {
        "term": "Business combination",
        "definition": "A transaction in which an acquirer obtains control of one or more businesses. Recognised using the acquisition method; goodwill = consideration + NCI + previously held interest − fair value of identifiable net assets.",
        "source": "Ind AS 103",
        "tags": ["Ind AS", "Restructuring"],
    },
    {
        "term": "Bargain purchase",
        "definition": "A business combination where the fair value of identifiable net assets exceeds the consideration transferred — recognised as gain in P&L (after reassessment).",
        "source": "Ind AS 103, paragraphs 34–36",
        "tags": ["Ind AS"],
    },
    {
        "term": "Compound financial instrument",
        "definition": "A financial instrument that contains both a liability component and an equity component (e.g., convertible debenture). Split at initial recognition between the two components.",
        "source": "Ind AS 32, paragraphs 28–32",
        "tags": ["Ind AS"],
    },

    # --- IT Act 2025 / Tax ---
    {
        "term": "Previous year",
        "definition": "The financial year (1 April to 31 March) immediately preceding the assessment year. Income earned in the previous year is taxable in the assessment year.",
        "source": "Sec 3, Income-tax Act 2025",
        "tags": ["Tax"],
    },
    {
        "term": "Resident and Ordinarily Resident (R&OR)",
        "definition": "An individual who is resident in India AND has been resident in India for at least 2 out of the preceding 10 years AND was in India for at least 730 days in the preceding 7 years. Subject to tax on world income.",
        "source": "Sec 6, Income-tax Act 2025",
        "tags": ["Tax"],
    },
    {
        "term": "Deemed resident",
        "definition": "An Indian citizen having total income (other than foreign-source income) > ₹15 lakh and not liable to tax in any other country by reason of domicile/residence — deemed to be resident.",
        "source": "Sec 6(1A), Income-tax Act 2025",
        "tags": ["Tax"],
    },
    {
        "term": "Significant Economic Presence (SEP)",
        "definition": "Non-resident's business connection in India through (a) transaction in goods/services/property of ≥ ₹2 cr OR (b) systematic and continuous solicitation/interaction with ≥ 3 lakh users in India.",
        "source": "Sec 9(1)(i) Explanation 2A, Income-tax Act",
        "tags": ["Tax"],
    },
    {
        "term": "Updated return",
        "definition": "Return that can be furnished within 48 months of the end of the relevant assessment year to disclose additional income, on payment of additional tax (25–60% based on timing).",
        "source": "Sec 139(8A), Income-tax Act",
        "tags": ["Tax"],
    },
    {
        "term": "Faceless assessment",
        "definition": "Tax assessment conducted via the National Faceless Assessment Centre (NaFAC) without face-to-face interaction. Team-based, geographically agnostic, automated allocation.",
        "source": "Sec 144B, Income-tax Act",
        "tags": ["Tax"],
    },
    {
        "term": "Set-off and carry-forward",
        "definition": "Set-off: utilising current-year losses against current-year incomes within and across heads. Carry-forward: losses unutilised may be carried to subsequent years (8 years for business loss, etc.).",
        "source": "Chapter VI, Income-tax Act 2025",
        "tags": ["Tax"],
    },
    {
        "term": "Section 79 restriction",
        "definition": "Loss carry-forward in a closely-held company is denied if ≥ 51% of voting power changed beneficial ownership. Relaxed for IBC-resolution-plan cases (Sec 79(2)(c)).",
        "source": "Sec 79, Income-tax Act 2025",
        "tags": ["Tax", "IBC"],
    },
    {
        "term": "Section 56(2)(x)",
        "definition": "Anti-abuse rule taxing receipt of money or property without/inadequate consideration in excess of ₹50,000 as income from other sources, valued at FMV under Rule 11UA.",
        "source": "Sec 56(2)(x), Income-tax Act 2025",
        "tags": ["Tax", "Restructuring"],
    },
    {
        "term": "MAT (Minimum Alternate Tax)",
        "definition": "Alternative tax of 15% on book profits payable when normal tax computation yields a lower liability. Not applicable to companies opting for Sec 115BAA / 115BAB.",
        "source": "Sec 115JB, Income-tax Act 2025",
        "tags": ["Tax", "Ind AS"],
    },
    {
        "term": "PPT (Principal Purpose Test)",
        "definition": "Treaty anti-abuse test under MLI — a treaty benefit is denied if obtaining that benefit was one of the principal purposes of any arrangement, unless granting the benefit is in accordance with the treaty's object.",
        "source": "Multilateral Instrument; Sec 90, Income-tax Act",
        "tags": ["Tax"],
    },

    # --- Audit / Internal Audit ---
    {
        "term": "Reasonable assurance",
        "definition": "High (not absolute) level of assurance — the level an external auditor expresses in an audit opinion. Acknowledges inherent limitations of audit procedures (estimates, sampling, fraud risk).",
        "source": "SA 200, paragraph 5",
        "tags": ["Audit"],
    },
    {
        "term": "Limited assurance",
        "definition": "Lower than reasonable but still meaningful — the level expressed in a review engagement (e.g., quarterly results review). Conclusion is 'negative' ('not aware of any modifications…').",
        "source": "SRE 2400",
        "tags": ["Audit"],
    },
    {
        "term": "Key Audit Matters (KAM)",
        "definition": "Matters that were of most significance in the audit of the current period's financial statements. Mandatory for listed-entity audit reports. Each KAM has description + why-significant + how-addressed.",
        "source": "SA 701",
        "tags": ["Audit"],
    },
    {
        "term": "Material misstatement",
        "definition": "An error or fraud that could individually or in aggregate influence the economic decisions of users of the financial statements. Materiality assessed quantitatively and qualitatively.",
        "source": "SA 320; SA 450",
        "tags": ["Audit"],
    },
    {
        "term": "Significant risk",
        "definition": "An identified and assessed risk of material misstatement that, in the auditor's judgment, requires special audit consideration. Always includes management override of controls and (presumed) revenue recognition.",
        "source": "SA 315 (Revised), paragraph 4(e)",
        "tags": ["Audit"],
    },
    {
        "term": "ICFR (Internal Financial Controls over Financial Reporting)",
        "definition": "Controls designed to provide reasonable assurance regarding the reliability of financial reporting and the preparation of FS for external purposes. Auditor opinion required for listed/prescribed companies under Sec 143(3)(i).",
        "source": "Sec 143(3)(i), Companies Act 2013; ICAI Guidance Note on Audit of IFCFR",
        "tags": ["Audit", "Internal Audit"],
    },
    {
        "term": "CARO 2020",
        "definition": "Companies (Auditor's Report) Order 2020 — 21 specific reporting clauses the auditor must include in addition to the main audit opinion, under Sec 143(11).",
        "source": "Sec 143(11), Companies Act 2013 + CARO 2020 notification",
        "tags": ["Audit"],
    },
    {
        "term": "NOCLAR (Non-compliance with Laws and Regulations)",
        "definition": "Non-compliance by management with laws/regulations relevant to the determination of material amounts/disclosures in the FS. Auditor must understand, document and consider effect on the audit and report.",
        "source": "SA 250",
        "tags": ["Audit"],
    },
    {
        "term": "Three Lines Model",
        "definition": "IIA's 2020 framework: 1st line = management owning and managing risks; 2nd line = risk/compliance/controllership monitoring; 3rd line = internal audit providing independent assurance to the board.",
        "source": "IIA Three Lines Model 2020",
        "tags": ["Internal Audit"],
    },
    {
        "term": "Test of Operating Effectiveness (ToOE)",
        "definition": "Audit procedure to determine whether a control is operating as designed throughout the period of intended reliance. Typically sample-based.",
        "source": "SA 330, paragraphs 8–11; ICAI ICFR Guidance Note",
        "tags": ["Audit", "Internal Audit"],
    },
    {
        "term": "Walkthrough",
        "definition": "Tracing 1–2 transactions through a process to confirm understanding of the process flow and the design of the controls. Establishes whether the control could operate effectively if applied as designed.",
        "source": "SA 315 (Revised); ICAI ICFR Guidance Note",
        "tags": ["Audit", "Internal Audit"],
    },
    {
        "term": "Material weakness",
        "definition": "A deficiency, or combination of deficiencies, in ICFR such that there is a reasonable possibility that a material misstatement will not be prevented or detected on a timely basis.",
        "source": "ICAI ICFR Guidance Note; PCAOB AS 2201",
        "tags": ["Audit"],
    },
    {
        "term": "Risk and Control Matrix (RCM)",
        "definition": "Per-process documentation table: process step → risk → control → control type → frequency → tester → test result. Core internal audit deliverable.",
        "source": "Practice; ICAI IA Practical Guide",
        "tags": ["Internal Audit"],
    },

    # --- Labour Codes ---
    {
        "term": "Wages (under Code on Wages 2019)",
        "definition": "Basic + DA + retaining allowance + such other allowances as specified, subject to a 50% floor — if excluded allowances exceed 50% of total remuneration, the excess is added back into wages for PF/gratuity/leave-encashment computation.",
        "source": "Sec 2(y), Code on Wages 2019",
        "tags": ["Labour"],
    },
    {
        "term": "Gig worker",
        "definition": "A person who performs work or participates in a work arrangement and earns from such activities outside of traditional employer-employee relationship. First statutorily recognised under the Code on Social Security 2020.",
        "source": "Sec 2(35), Code on Social Security 2020",
        "tags": ["Labour"],
    },
    {
        "term": "Platform worker",
        "definition": "A gig worker engaged via an online platform / digital intermediary that connects buyers and sellers of services.",
        "source": "Sec 2(60), Code on Social Security 2020",
        "tags": ["Labour"],
    },
    {
        "term": "Aggregator",
        "definition": "A digital intermediary that connects a buyer with a seller of services (e.g., ride-hailing, food delivery, e-commerce platforms). Required to contribute 1–2% of turnover to the gig worker social security fund.",
        "source": "Sec 2(2), Code on Social Security 2020",
        "tags": ["Labour"],
    },
    {
        "term": "Negotiating union / Negotiating council",
        "definition": "A single union with ≥ 51% support of workers is the sole negotiating union; otherwise a negotiating council with proportionate representation from registered unions. Replaces the older 'sole bargaining agent' concept.",
        "source": "Sec 14, Industrial Relations Code 2020",
        "tags": ["Labour"],
    },
    {
        "term": "Standing Orders",
        "definition": "Conditions of service (hours, leave, holidays, payment, suspension, termination) drawn up by the employer and certified by the certifying officer. Mandatory for establishments with 300+ workers.",
        "source": "Sec 28, Industrial Relations Code 2020",
        "tags": ["Labour"],
    },
    {
        "term": "Fixed-term employment",
        "definition": "Employment for a specified period under a written contract. Worker is entitled to same statutory benefits proportionate to period, gratuity after 1 year (vs 5 for permanent), no notice/compensation on natural expiry of term.",
        "source": "IR Code 2020; OSH Code 2020",
        "tags": ["Labour"],
    },
    {
        "term": "Retrenchment",
        "definition": "Permanent termination of a worker's service for reasons other than disciplinary action. Requires 1 month's notice/pay + 15 days × completed years compensation. Closure of an establishment with 300+ workers requires government permission.",
        "source": "Sec 70 (retrenchment), Sec 75 (closure), Industrial Relations Code 2020",
        "tags": ["Labour"],
    },

    # --- FEMA / SEBI ---
    {
        "term": "NDI Rules 2019",
        "definition": "Foreign Exchange Management (Non-Debt Instruments) Rules 2019 — consolidated framework for foreign investment in Indian companies. Replaced earlier scattered FDI notifications.",
        "source": "FEMA NDI Rules 2019 (notified by Central Government)",
        "tags": ["FEMA", "Restructuring"],
    },
    {
        "term": "ODI Rules 2022",
        "definition": "Foreign Exchange Management (Overseas Investment) Rules 2022 — framework for overseas direct investment by Indian residents. Permits round-tripping up to two layers with conditions.",
        "source": "FEMA OI Rules 2022 + OI Regulations 2022 (RBI Notif. 400)",
        "tags": ["FEMA", "Restructuring"],
    },
    {
        "term": "FC-GPR",
        "definition": "Foreign Currency-Gross Provisional Return — FEMA reporting form filed within 30 days of share allotment to a non-resident.",
        "source": "RBI Master Direction on Foreign Investment",
        "tags": ["FEMA"],
    },
    {
        "term": "FC-TRS",
        "definition": "FEMA reporting form for transfer of equity instruments between resident and non-resident. Filed within 60 days of transfer.",
        "source": "RBI Master Direction on Foreign Investment",
        "tags": ["FEMA"],
    },
    {
        "term": "PN3 / Press Note 3 of 2020",
        "definition": "Government route mandatory for any foreign investment in India by an entity of a country sharing a land border with India, or where the beneficial owner is located in such a country.",
        "source": "Press Note 3 (2020 Series) dated 17 April 2020",
        "tags": ["FEMA"],
    },
    {
        "term": "LODR Regulation 37",
        "definition": "SEBI requirement: listed company must obtain prior in-principle approval of stock exchanges (and through them, SEBI) before filing any scheme of arrangement with NCLT.",
        "source": "Regulation 37, SEBI LODR Regulations 2015",
        "tags": ["SEBI", "Restructuring"],
    },
    {
        "term": "Majority of minority",
        "definition": "Approval threshold under SEBI Master Circular for schemes where the promoter has a related-party interest — public (non-promoter) shareholders must vote and a majority must approve. Promoters cannot vote.",
        "source": "SEBI Master Circular on Schemes of Arrangement",
        "tags": ["SEBI", "Restructuring"],
    },
    {
        "term": "Fairness opinion",
        "definition": "An opinion from an independent SEBI-registered merchant banker on whether the share exchange ratio in a scheme is fair to the shareholders. Mandatory for listed-company schemes.",
        "source": "SEBI Master Circular on Schemes of Arrangement",
        "tags": ["SEBI", "Restructuring"],
    },

    # --- English / general ---
    {
        "term": "Going-concern (English usage)",
        "definition": "Hyphenated when used as a compound modifier before a noun ('a going-concern basis'); unhyphenated as a noun phrase ('the going concern assumption').",
        "source": "Standard English style",
        "tags": ["English"],
    },
    {
        "term": "Schwa /ə/",
        "definition": "The most common English vowel sound — short, neutral, unstressed (the 'a' in 'about', the 'er' in 'butter', the 'o' in 'support'). Indian-English speakers often replace it with the spelled letter.",
        "source": "International Phonetic Alphabet",
        "tags": ["English"],
    },
    {
        "term": "Stress-timed language",
        "definition": "A language where stressed syllables occur at roughly equal intervals (English, German). Contrasts with syllable-timed languages (Hindi, French) where each syllable takes equal time.",
        "source": "Linguistics; David Crystal",
        "tags": ["English"],
    },
]
