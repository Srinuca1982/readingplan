"""Six additional mastery areas — 2-month parallel study programme.

Goal: master all six in 8 weeks alongside (or instead of) the restructuring
curriculum. Each area has an 8-week roadmap, key topics, recommended books,
and authoritative online sources. A detailed study note for each area lives
in content_mastery_notes.py and renders into the materials/ folder.
"""

AREAS = [
    # ------------------------------------------------------------------
    # 1) Ind AS
    # ------------------------------------------------------------------
    {
        "slug": "ind-as",
        "title": "Ind AS — Indian Accounting Standards",
        "subtitle": "Convergence of Indian GAAP with IFRS — the financial reporting framework for Ind AS companies.",
        "summary": (
            "Ind AS is mandatory for listed and large unlisted companies under MCA Rule 4 of the "
            "Companies (Indian Accounting Standards) Rules 2015. The standards cover recognition, "
            "measurement, presentation and disclosure across every category of transaction. "
            "Master the framework and the high-impact standards first; the rest follow naturally."
        ),
        "weeks": [
            {
                "week": "1",
                "title": "Framework & General Presentation",
                "focus": "The conceptual framework, accounting policies, and the format of financial statements.",
                "tasks": [
                    "Conceptual Framework for Financial Reporting under Ind AS — read end-to-end",
                    "Ind AS 1 — Presentation of Financial Statements; Schedule III Division II/III compatibility",
                    "Ind AS 8 — Accounting Policies, Changes in Accounting Estimates and Errors",
                    "Ind AS 10 — Events After the Reporting Period",
                    "Ind AS 7 — Statement of Cash Flows (direct vs indirect)",
                ],
            },
            {
                "week": "2",
                "title": "Tangibles, Intangibles, Investment Property",
                "focus": "How long-term assets are recognised, measured and depreciated.",
                "tasks": [
                    "Ind AS 16 — PPE; component accounting; major spares; cost model vs revaluation model",
                    "Ind AS 38 — Intangible Assets; research vs development; useful life test",
                    "Ind AS 40 — Investment Property; fair value disclosure even when cost model used",
                    "Ind AS 36 — Impairment of Assets; CGU identification; goodwill impairment annual test",
                    "Ind AS 23 — Borrowing Costs; qualifying assets; commencement and cessation",
                ],
            },
            {
                "week": "3",
                "title": "Revenue — Ind AS 115",
                "focus": "The 5-step model. Single most-tested standard for any client-facing company.",
                "tasks": [
                    "Step 1 — Identify the contract; collectibility; combining contracts",
                    "Step 2 — Identify performance obligations; distinct goods/services; series concept",
                    "Step 3 — Determine transaction price; variable consideration; significant financing",
                    "Step 4 — Allocate price; stand-alone selling prices; residual approach",
                    "Step 5 — Recognise revenue; point-in-time vs over-time; output vs input methods",
                    "Practical industries — real estate (POCM vs completion), software licences, telecom bundles, construction",
                ],
            },
            {
                "week": "4",
                "title": "Leases — Ind AS 116",
                "focus": "The single-model lessee approach. Major change vs erstwhile AS 19.",
                "tasks": [
                    "Definition of a lease — identified asset; right to direct use; substantive substitution rights",
                    "Lessee accounting — right-of-use asset and lease liability recognition at commencement",
                    "Short-term leases (≤12 months) and low-value asset exemptions",
                    "Lessor accounting — operating vs finance lease classification (largely unchanged)",
                    "Lease modifications — separate lease vs not; remeasurement of liability",
                    "Sale-and-leaseback transactions; transition (modified retrospective vs full retrospective)",
                ],
            },
            {
                "week": "5",
                "title": "Financial Instruments — Ind AS 109, 32, 107",
                "focus": "Classification, measurement, impairment and hedge accounting.",
                "tasks": [
                    "Ind AS 32 — Liability vs equity classification; compound instruments; preference shares",
                    "Ind AS 109 classification — SPPI test; business model assessment; FVTPL/FVTOCI/Amortised cost",
                    "Ind AS 109 measurement — effective interest method; embedded derivatives",
                    "Expected Credit Loss (ECL) model — 3 stages; simplified approach for trade receivables",
                    "Hedge accounting — fair value hedge, cash flow hedge, net investment hedge",
                    "Ind AS 107 — Disclosures; sensitivity analysis; credit risk concentrations",
                ],
            },
            {
                "week": "6",
                "title": "Consolidation & Business Combinations",
                "focus": "Group structures and the acquisition method.",
                "tasks": [
                    "Ind AS 110 — Control; the three elements; de facto control; structured entities",
                    "Ind AS 111 — Joint Arrangements; joint operation vs joint venture; equity method",
                    "Ind AS 28 — Investments in Associates; significant influence; impairment of associate",
                    "Ind AS 112 — Disclosure of Interests in Other Entities; structured entity disclosures",
                    "Ind AS 103 — Business Combinations; acquisition method; identifying the acquirer",
                    "Ind AS 103 — Recognition of goodwill / bargain purchase; reverse acquisitions; common control transactions (Appendix C)",
                ],
            },
            {
                "week": "7",
                "title": "Income Taxes, Employee Benefits, Provisions",
                "focus": "The complex measurement standards.",
                "tasks": [
                    "Ind AS 12 — Income Taxes; deferred tax on temporary differences; recognition limit on DTA",
                    "Ind AS 19 — Employee Benefits; defined benefit obligations; actuarial valuations; OCI re-measurements",
                    "Ind AS 37 — Provisions, Contingent Liabilities, Contingent Assets",
                    "Ind AS 102 — Share-Based Payment; equity-settled vs cash-settled; vesting conditions",
                    "Ind AS 21 — The Effects of Changes in Foreign Exchange Rates; functional currency determination",
                ],
            },
            {
                "week": "8",
                "title": "Sector Standards, Disclosures & Practical Application",
                "focus": "Tie it all together with disclosures, segment reporting and presentation tests.",
                "tasks": [
                    "Ind AS 108 — Operating Segments; chief operating decision maker (CODM) approach",
                    "Ind AS 24 — Related Party Disclosures; identification; transactions in normal course",
                    "Ind AS 33 — Earnings per Share; basic and diluted; treasury stock method",
                    "Ind AS 105 — Non-current Assets Held for Sale and Discontinued Operations",
                    "ICAI Compendium and Educational Materials — pick three standards and read the ICAI illustrative examples",
                    "Solve at least 10 ICAI practice questions across standards",
                ],
            },
        ],
        "topics": [
            "Conceptual framework & Schedule III (Div II/III)",
            "Ind AS 1, 8, 10, 7 — presentation, policies, events, cash flows",
            "Ind AS 16, 23, 36, 38, 40 — long-term assets and impairment",
            "Ind AS 115 — 5-step revenue model",
            "Ind AS 116 — leases (single-model lessee)",
            "Ind AS 109, 32, 107 — financial instruments",
            "Ind AS 103, 110, 111, 112, 28 — combinations and consolidation",
            "Ind AS 12 — income taxes (deferred tax)",
            "Ind AS 19 — employee benefits (actuarial)",
            "Ind AS 37 — provisions and contingencies",
            "Ind AS 21 — foreign currency",
            "Ind AS 102 — share-based payments",
            "Ind AS 108 — segments",
            "Ind AS 24 — related parties",
            "Ind AS 33 — EPS; Ind AS 105 — discontinued operations",
        ],
        "books": [
            {
                "title": "Indian Accounting Standards (Ind AS) — Interpretation and Application",
                "author": "CA Kamal Garg",
                "publisher": "Bharat Law House · latest edition",
                "why": "The single most cited Ind AS practitioner reference. Standard-by-standard with worked examples, Q&A, and recent ITFG clarifications.",
            },
            {
                "title": "Ind AS — A Comprehensive Guide",
                "author": "Dolphy D'Souza",
                "publisher": "Snow White · multi-volume",
                "why": "Deeper analytical treatment by a Big-4 partner. Best for complex topics — consolidation, financial instruments, business combinations.",
            },
            {
                "title": "Compendium of Indian Accounting Standards",
                "author": "ICAI",
                "publisher": "ICAI Publication · annual edition",
                "why": "The bare-text compendium. Indispensable as the authoritative source. Always cite from the latest published version.",
            },
            {
                "title": "Educational Material on Ind AS (one per standard)",
                "author": "ICAI Accounting Standards Board",
                "publisher": "ICAI · free PDFs",
                "why": "The ICAI ASB publishes a separate Educational Material per standard with FAQs, illustrative examples and decision trees. Free downloads — the best free Ind AS resource in India.",
            },
            {
                "title": "Wiley IFRS Practical Implementation Guide",
                "author": "Mackenzie, Coetsee, Njikizana et al.",
                "publisher": "Wiley · annual edition",
                "why": "Since Ind AS is converged with IFRS, the Wiley IFRS guide is the global counterpart. Useful for cross-checking the underlying IFRS view when Ind AS analysis is ambiguous.",
            },
        ],
        "sources": [
            {
                "name": "MCA — Notifications & Circulars",
                "url": "https://www.mca.gov.in/content/mca/global/en/acts-rules/ebooks/notifications-circulars.html",
                "description": "Companies (Indian Accounting Standards) Rules 2015 and every amendment notification. Source of truth for the legally-effective text of each standard.",
            },
            {
                "name": "ICAI Accounting Standards Board",
                "url": "https://asb.icai.org/",
                "description": "Ind AS educational material, guidance notes and announcements from the ASB. Each Educational Material is a 60–120 page PDF with worked examples.",
            },
            {
                "name": "ICAI Ind AS Transition Facilitation Group (ITFG)",
                "url": "https://www.icai.org/post/12745",
                "description": "ITFG Clarification Bulletins — the closest thing India has to interpretive guidance. Each bulletin addresses 5–15 implementation queries.",
            },
            {
                "name": "ICAI Board of Studies — Knowledge Portal",
                "url": "https://www.icai.org/post/bos-knowledge-portal",
                "description": "ICAI's BoS knowledge portal with study material, mock-test papers and revision videos covering Ind AS in detail.",
            },
            {
                "name": "IFRS Foundation",
                "url": "https://www.ifrs.org/",
                "description": "Underlying global standards (IFRS). Since Ind AS is converged, IFRS Foundation interpretations (IFRIC, IFRS Practice Statements) inform Ind AS application.",
            },
            {
                "name": "EY India — Ind AS Resources",
                "url": "https://www.ey.com/en_in/services/ey-faas-learning-solutions/certificate-program-in-ind-as",
                "description": "EY India's Ind AS hub — pocket books, certificate programmes, sector-specific guides. KPMG, PwC and Deloitte India publish similar annual references.",
            },
            {
                "name": "NFRA — Audit Quality Reports",
                "url": "https://nfra.gov.in/",
                "description": "NFRA's inspection reports highlight Ind AS application issues from real audits. Excellent for learning common pitfalls.",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 2) Income Tax Act 2025
    # ------------------------------------------------------------------
    {
        "slug": "it-act-2025",
        "title": "Income-tax Act 2025",
        "subtitle": "In force from 1 April 2026 — the Act that replaces the Income-tax Act 1961.",
        "summary": (
            "The Income-tax Act 2025 came into force on 1 April 2026, replacing the Income-tax "
            "Act 1961 (which now applies only to transactions and assessments up to 31 March 2026). "
            "Six decades of patchwork legislation have been reorganised into a cleaner, fewer-section "
            "code; substantive tax law is largely retained but renumbered and rewritten in plain "
            "language. Master the mapping from 1961 sections to 2025 sections, and the substantive "
            "changes that have been introduced."
        ),
        "weeks": [
            {
                "week": "1",
                "title": "Structure of the 2025 Act & Transition",
                "focus": "How the new Act is organised; the transitional rules and effective date.",
                "tasks": [
                    "Read the preamble, chapter structure, and overview of the 2025 Act",
                    "Compare the chapter-wise structure of 1961 Act vs 2025 Act",
                    "Effective date and transitional provisions — assessments under old Act, completed cases",
                    "Section-mapping exercise: create your own 1961→2025 cross-reference sheet for the top 30 sections you use daily",
                    "Read at least two Taxmann / Taxsutra / Bloomberg Quint articles on what's new in IT Act 2025",
                ],
            },
            {
                "week": "2",
                "title": "Basic Concepts & Residential Status",
                "focus": "Person, assessment year, previous year; residency rules.",
                "tasks": [
                    "Definition of person, assessee, total income, gross total income under 2025 Act",
                    "Residential status for individuals — 182-day test; deemed residency rules for HNI Indian citizens (≥₹15 lakh income, no tax in any country)",
                    "Residential status for companies, HUFs, firms — place of effective management (POEM)",
                    "Scope of total income — Indian source, deemed accrued, world income for residents",
                    "Income deemed to accrue in India — Sec 9 equivalents under 2025 Act",
                ],
            },
            {
                "week": "3",
                "title": "Heads of Income — Salaries, House Property, Business",
                "focus": "The first three heads of income.",
                "tasks": [
                    "Salaries — perquisites (Rule 3 equivalent); employer-provided benefits; ESOP taxation",
                    "Income from House Property — annual value; standard deduction; loss set-off limits",
                    "Profits and gains of business or profession — admissible deductions; depreciation under block of assets",
                    "Presumptive taxation — Sec 44AD, 44ADA, 44AE equivalents; eligibility thresholds",
                    "Section 43B equivalent — actual payment basis for statutory dues",
                ],
            },
            {
                "week": "4",
                "title": "Capital Gains",
                "focus": "Computation, exemptions and rates under the 2025 regime.",
                "tasks": [
                    "Capital asset definition; transfer; short-term vs long-term classification",
                    "Cost of acquisition rules; cost with indexation (where retained); fair-market-value rules",
                    "Special rates — LTCG on listed equity (12.5% post Budget 2024); STCG (20% post Budget 2024)",
                    "Exemptions — reinvestment exemptions (Sec 54, 54F, 54EC equivalents); transfer between specified relatives",
                    "Slump sale; demerger; amalgamation — tax-neutral provisions retained in 2025 Act",
                    "Indirect transfer of Indian assets — Sec 9(1)(i) equivalent; substantial-value test",
                ],
            },
            {
                "week": "5",
                "title": "Other Sources, Clubbing, Set-off & Carry Forward",
                "focus": "The cleanup heads and loss-utilisation rules.",
                "tasks": [
                    "Income from other sources — dividends post-DDT abolition; gifts under Sec 56(2)(x) equivalent",
                    "Clubbing — spouse income, minor child income, asset transfer to spouse",
                    "Set-off — intra-head and inter-head set-off limits",
                    "Carry forward — periods for business loss, capital loss, speculation loss",
                    "Section 79 equivalent — closely-held company shareholding-change loss restriction; IBC carve-out",
                ],
            },
            {
                "week": "6",
                "title": "Deductions & Computation",
                "focus": "Chapter VI-A deductions and tax computation under the new and old regime.",
                "tasks": [
                    "Old regime vs new regime — current default and tax slabs",
                    "Deductions — Sec 80C, 80D, 80E, 80G, 80TTA, 80TTB, 80EE equivalents (mostly only under old regime now)",
                    "Section 80M equivalent — inter-corporate dividends",
                    "Computation of tax liability; rebate under Sec 87A; surcharge and cess",
                    "Marginal relief computation",
                ],
            },
            {
                "week": "7",
                "title": "TDS, TCS, Advance Tax, Returns",
                "focus": "Compliance machinery and procedural provisions.",
                "tasks": [
                    "TDS sections — salary, contract payments, professional fees, rent, interest, dividend",
                    "TDS on transfer of immovable property; TDS on cash withdrawals; Sec 194Q (purchase of goods)",
                    "TCS — Sec 206C; LRS remittances; sale of goods",
                    "Advance tax — instalments, computation, interest under Sec 234B/234C",
                    "Return filing — due dates; revised return; updated return (Sec 139(8A) equivalent)",
                    "Faceless assessment and faceless appeals — the procedural reform",
                ],
            },
            {
                "week": "8",
                "title": "Penalties, Appeals, GAAR, Search",
                "focus": "Enforcement and dispute-resolution machinery.",
                "tasks": [
                    "Penalty regime — Sec 270A (under-reporting / mis-reporting) equivalent; Sec 271AAB equivalent",
                    "Appeal hierarchy — CIT(A) / Faceless Appeal → ITAT → High Court → Supreme Court",
                    "Vivad se Vishwas-style settlement; Dispute Resolution Committee",
                    "GAAR — Chapter X-A equivalent; the four tainted elements; impermissible avoidance arrangement",
                    "Search and seizure — Sec 132 equivalent; survey under Sec 133A equivalent",
                    "Final wrap-up: complete your personal IT Act 1961 → 2025 mapping sheet for all chapters",
                ],
            },
        ],
        "topics": [
            "Structure of the 2025 Act and 1961→2025 mapping",
            "Residency rules — individuals, companies, HUFs (POEM)",
            "Heads of income — salaries, house property, business, capital gains, other sources",
            "Capital gains — STCG/LTCG; indirect transfers; restructuring carve-outs",
            "Deductions Chapter VI-A — old regime vs new regime",
            "Tax rates — slabs, surcharge, MAT and AMT",
            "TDS / TCS — all sections; thresholds; reporting (Form 26Q, 27Q)",
            "Advance tax and interest provisions",
            "Faceless assessment and faceless appeals",
            "GAAR — substance over form; impermissible avoidance arrangement",
            "Penalties — under-reporting, mis-reporting, search-related",
            "Appeals — CIT(A), ITAT, HC, SC; statutory time limits",
            "Search, seizure, survey",
            "Special provisions — startups, IBC cases, NRI tax",
            "Tax treaties and MLI — Principal Purpose Test (PPT)",
        ],
        "books": [
            {
                "title": "Income-tax Act 2025 — Bare Act with Section Navigator",
                "author": "Taxmann",
                "publisher": "Taxmann · annual edition",
                "why": "The bare act with side-by-side mapping to the 1961 Act. Essential as the primary source. Taxmann's edition includes amendment history per section.",
            },
            {
                "title": "Direct Taxes — Law and Practice",
                "author": "Vinod K Singhania & Kapil Singhania",
                "publisher": "Taxmann · annual edition",
                "why": "The most widely used direct-tax reference for practitioners. Detailed commentary on each chapter with worked examples and recent case law.",
            },
            {
                "title": "Direct Tax Laws & International Taxation",
                "author": "TN Manoharan & GR Hari",
                "publisher": "Snow White · annual edition",
                "why": "Examination-oriented but practitioner-grade. Strong on computation problems and procedural law. Used by CA Final students nationally.",
            },
            {
                "title": "Master Guide to Income Tax",
                "author": "Taxmann editorial",
                "publisher": "Taxmann · annual edition",
                "why": "Topic-wise summary with the most up-to-date Finance Act amendments. Quick reference when you need a current view on a specific question.",
            },
            {
                "title": "Income Tax Bill 2025 — Section-wise Analysis",
                "author": "CA Girish Ahuja & CA Ravi Gupta",
                "publisher": "Wolters Kluwer / Commercial Law Publishers",
                "why": "Section-by-section commentary specifically on the 2025 Act with mapping to the 1961 Act and worked examples. The bridge book for practitioners transitioning.",
            },
        ],
        "sources": [
            {
                "name": "Income-tax Department — Income-tax Act 2025",
                "url": "https://www.incometaxindia.gov.in/income-tax-act-2025",
                "description": "Official text of the Income-tax Act 2025 (in force 1 April 2026), with section navigator. Always verify the latest amendments here.",
            },
            {
                "name": "Income-tax Department — Notifications",
                "url": "https://www.incometaxindia.gov.in/notifications",
                "description": "Every CBDT notification, circular, instruction. Subscribe to email alerts for daily updates.",
            },
            {
                "name": "Taxmann — Research & Daily Digest",
                "url": "https://www.taxmann.com",
                "description": "The most comprehensive subscription source — case digests, daily news, expert commentary. Free headlines; paid for full case law.",
            },
            {
                "name": "Taxsutra",
                "url": "https://www.taxsutra.com",
                "description": "Subscription tax news and analysis platform. Free trial available. Strong international taxation coverage.",
            },
            {
                "name": "ICAI — Direct Taxes Committee",
                "url": "https://www.icai.org/post/direct-taxes-committee",
                "description": "ICAI's publications, technical guides, post-budget memoranda. CA Final direct-tax background materials are extremely thorough.",
            },
            {
                "name": "ITAT Online",
                "url": "https://www.itatonline.org/",
                "description": "Free aggregator of ITAT, High Court and Supreme Court tax judgments. Search by section and topic.",
            },
            {
                "name": "LiveMint Money — Personal Finance",
                "url": "https://www.livemintmoney.com/personal-finance",
                "description": "Mainstream tax-news commentary; useful to track ministerial signals and budget proposals.",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 3) Internal Audit
    # ------------------------------------------------------------------
    {
        "slug": "internal-audit",
        "title": "Internal Audit",
        "subtitle": "Risk-based, value-adding assurance — the IIA/ICAI framework.",
        "summary": (
            "Internal audit is mandated for prescribed companies under Section 138 of the Companies "
            "Act 2013 read with Rule 13. The discipline has shifted from compliance-checking to "
            "risk-based, value-adding assurance. Master the IIA's International Professional "
            "Practices Framework (IPPF) and ICAI's Standards on Internal Audit (SIAs)."
        ),
        "weeks": [
            {
                "week": "1",
                "title": "Internal Audit Framework",
                "focus": "Definitions, mandates, and the global IPPF.",
                "tasks": [
                    "Sec 138 of Companies Act 2013 + Rule 13 — applicability thresholds; turnover/loan triggers",
                    "IIA IPPF — Mission, Core Principles, Code of Ethics, Standards (Attribute + Performance)",
                    "ICAI Standards on Internal Audit (SIAs) — overview of all 18 SIAs",
                    "Three Lines Model (formerly Three Lines of Defence) — management controls, risk/compliance, internal audit",
                    "Internal audit charter — typical contents; board-approval requirement",
                ],
            },
            {
                "week": "2",
                "title": "Risk-Based Internal Auditing",
                "focus": "The shift from transaction-testing to risk-based assurance.",
                "tasks": [
                    "COSO Enterprise Risk Management (ERM) framework — 5 components, 20 principles",
                    "ISO 31000 risk management — principles and processes",
                    "Risk assessment matrix — likelihood × impact; heat maps",
                    "Annual internal audit plan — risk-based prioritisation",
                    "Risk appetite and tolerance — how the board sets these and how internal audit aligns",
                ],
            },
            {
                "week": "3",
                "title": "Internal Controls — COSO 2013",
                "focus": "The internal-control framework underlying ICFR reporting.",
                "tasks": [
                    "COSO 2013 Internal Control Framework — 5 components, 17 principles",
                    "Entity-level controls vs process-level controls",
                    "Key controls vs compensating controls",
                    "Segregation of duties — the four-eyes principle; ARP-PAR (Authorisation, Recording, Custody, Reconciliation)",
                    "IT general controls (ITGC) vs application controls",
                ],
            },
            {
                "week": "4",
                "title": "Audit Planning, Engagement & Sampling",
                "focus": "How an internal audit is conducted in practice.",
                "tasks": [
                    "Engagement planning — objectives, scope, criteria, resources",
                    "Walk-through and process flowcharting",
                    "Risk and Control Matrix (RCM) — building one for a process",
                    "Audit programme — sample working papers",
                    "Sampling methods — statistical (MUS), non-statistical, judgmental; ICAI SA 530 (applies by analogy)",
                ],
            },
            {
                "week": "5",
                "title": "Testing — Controls and Substantive",
                "focus": "Designing tests that produce reliable evidence.",
                "tasks": [
                    "Test of design (ToD) vs test of operating effectiveness (ToOE)",
                    "Sample selection — random, systematic, haphazard",
                    "Substantive analytical procedures",
                    "Documentation requirements — working papers; trail",
                    "Data analytics in internal audit — CAATs, Excel/Python/Power BI use",
                ],
            },
            {
                "week": "6",
                "title": "Process Audits — The Key Cycles",
                "focus": "Master one cycle per day for a week — the practical core.",
                "tasks": [
                    "Order-to-Cash (O2C) cycle — credit limits, pricing master, dispute management, revenue recognition controls",
                    "Procure-to-Pay (P2P) cycle — vendor master, three-way match, GRN, payment controls",
                    "Payroll cycle — employee master, attendance, PF/ESI/TDS compliance, full-and-final settlement",
                    "Treasury / cash and bank — bank reconciliation, forex hedging, investment policy compliance",
                    "Fixed assets / inventory — physical verification protocols; capitalisation policy",
                    "IT general controls — change management, access controls, backups, BCP/DR",
                ],
            },
            {
                "week": "7",
                "title": "ICFR & SOX Compliance",
                "focus": "Internal control over financial reporting under Companies Act 2013.",
                "tasks": [
                    "Sec 134(5)(e) — director's responsibility statement on IFC",
                    "Sec 143(3)(i) — auditor's responsibility on IFCFR for listed and prescribed companies",
                    "ICAI Guidance Note on Audit of Internal Financial Controls — read at least Chapters 1–4",
                    "SOX 404 (US) — comparison with Indian ICFR; PCAOB AS 2201",
                    "Documentation requirements — process flow, RCM, design and operating effectiveness testing",
                ],
            },
            {
                "week": "8",
                "title": "Reporting, Quality & Emerging Trends",
                "focus": "Communicating findings and adapting to digital audit.",
                "tasks": [
                    "Audit report structure — observations, root cause, risk implication, recommendation, management response",
                    "Rating systems — Critical, High, Medium, Low; ICAI's SIA 17 on internal audit reports",
                    "Follow-up audit — closure verification",
                    "Quality Assessment Review (QAR) — external every 5 years per IIA Standards",
                    "Emerging areas — ESG audit, cybersecurity audit, AI/ML model audit, third-party risk",
                ],
            },
        ],
        "topics": [
            "IPPF — Mission, Principles, Ethics, Standards",
            "ICAI Standards on Internal Audit (SIAs)",
            "Sec 138 + Rule 13 — applicability and scope",
            "Three Lines Model",
            "COSO Internal Control Framework 2013",
            "COSO ERM framework",
            "ISO 31000 risk management",
            "Risk-based internal audit planning",
            "Risk and Control Matrix (RCM)",
            "Walkthroughs and process flowcharting",
            "Controls testing — design vs operating effectiveness",
            "Substantive testing and analytics",
            "Sampling — statistical and non-statistical",
            "Key business cycles — O2C, P2P, payroll, treasury, fixed assets, inventory",
            "IT general controls and application controls",
            "ICFR — Companies Act ICAI Guidance Note",
            "SOX 404 and PCAOB framework",
            "Internal audit reporting; rating; follow-up",
            "Data analytics — CAATs, Excel, Python, Power BI",
            "Emerging — ESG audit, cyber, AI model audit",
        ],
        "books": [
            {
                "title": "Sawyer's Internal Auditing — The Practice of Modern Internal Auditing",
                "author": "Lawrence B. Sawyer / IIA Editorial",
                "publisher": "Institute of Internal Auditors · 7th Edition",
                "why": "The global reference. Comprehensive treatment of every aspect of internal audit. 1,500+ pages — use as a desk reference rather than cover-to-cover.",
            },
            {
                "title": "Standards on Internal Audit — Bare + Background Materials",
                "author": "ICAI",
                "publisher": "ICAI Publication · latest edition",
                "why": "The 18 SIAs with explanatory text. Mandatory reading for any internal audit engagement in India.",
            },
            {
                "title": "Internal Auditing — Assurance & Advisory Services",
                "author": "Anderson, Head, Ramamoorti (Common Body of Knowledge)",
                "publisher": "IIA Research Foundation · 4th Edition",
                "why": "The CIA exam textbook. Excellent on risk-based approach, IT audit, and emerging topics. Strong on theoretical foundations.",
            },
            {
                "title": "Practical Guide to Internal Audit",
                "author": "ICAI Internal Audit Standards Board",
                "publisher": "ICAI",
                "why": "India-specific. Detailed RCMs and audit programmes for common cycles — O2C, P2P, payroll, treasury, IT. Practitioner-oriented.",
            },
            {
                "title": "Guidance Note on Audit of Internal Financial Controls Over Financial Reporting",
                "author": "ICAI",
                "publisher": "ICAI Publication",
                "why": "The ICFR bible. Covers Section 143(3)(i) auditor responsibilities, top-down risk-based approach, and documentation standards. Read in parallel with the SAs.",
            },
            {
                "title": "COSO Internal Control — Integrated Framework",
                "author": "COSO",
                "publisher": "AICPA / COSO · free executive summary, paid full text",
                "why": "The underlying global framework. Read at least the Executive Summary (free) and the 5-components / 17-principles structure.",
            },
        ],
        "sources": [
            {
                "name": "Institute of Internal Auditors (IIA) — Global",
                "url": "https://www.theiia.org/",
                "description": "IPPF, position papers, GTAGs (Global Technology Audit Guides). The Code of Ethics and Standards are mandatory references.",
            },
            {
                "name": "Institute of Internal Auditors — India",
                "url": "https://iiaindia.co/",
                "description": "Indian chapter; local events, CIA examination resources, member forums. (Domain moved from iiaindia.co.in.)",
            },
            {
                "name": "ICAI Internal Audit Standards Board",
                "url": "https://www.icai.org/post/internal-audit-standards-board",
                "description": "Standards on Internal Audit (SIAs), Technical Guides on industries, FAQs.",
            },
            {
                "name": "COSO",
                "url": "https://www.coso.org/",
                "description": "Internal Control — Integrated Framework (2013) and ERM Framework (2017). Executive summaries are free.",
            },
            {
                "name": "ISO 31000 — Risk Management",
                "url": "https://www.iso.org/iso-31000-risk-management.html",
                "description": "The international risk management standard. Principles, framework and process.",
            },
            {
                "name": "PCAOB Auditing Standards",
                "url": "https://pcaobus.org/oversight/standards/auditing-standards",
                "description": "AS 2201 on audit of ICFR is the US counterpart of ICAI's ICFR Guidance Note. Useful comparator.",
            },
            {
                "name": "MCA — Acts & Rules",
                "url": "https://www.mca.gov.in/content/mca/global/en/acts-rules/ebooks.html",
                "description": "Section 138 + Rule 13 of Companies (Accounts) Rules 2014. Mandatory applicability check for every internal audit engagement.",
            },
            {
                "name": "NFRA — Audit Inspection Reports",
                "url": "https://nfra.gov.in/",
                "description": "Real-world examples of internal control deficiencies in published companies. Excellent learning resource.",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 4) New Labor Codes
    # ------------------------------------------------------------------
    {
        "slug": "labor-codes",
        "title": "The Four Labour Codes",
        "subtitle": "29 central labour laws consolidated into 4 codes — the biggest labour reform since independence.",
        "summary": (
            "Parliament has enacted four codes — the Code on Wages 2019, the Industrial Relations "
            "Code 2020, the Code on Social Security 2020, and the Occupational Safety, Health and "
            "Working Conditions Code 2020 — to replace 29 central labour laws. The codes are "
            "notified but their substantive provisions are operationalised state-by-state via "
            "State Rules. Master the codes' text, the State Rules, and the practical compliance "
            "changes for HR and payroll."
        ),
        "weeks": [
            {
                "week": "1",
                "title": "Overview of the Four Codes",
                "focus": "What each code covers, status of notification, and the consolidated structure.",
                "tasks": [
                    "Code on Wages 2019 — subsumes 4 acts (Payment of Wages, Minimum Wages, Payment of Bonus, Equal Remuneration)",
                    "Industrial Relations Code 2020 — subsumes 3 acts (ID Act, Trade Unions Act, Standing Orders Act)",
                    "Code on Social Security 2020 — subsumes 9 acts (EPF, ESIC, Maternity, Gratuity, Employee Compensation, etc.)",
                    "OSH Code 2020 — subsumes 13 acts (Factories, Contract Labour, Inter-State Migrant, Mines, etc.)",
                    "Constitutional position — labour is in Concurrent List; both Centre and States can legislate; status of notification by State",
                ],
            },
            {
                "week": "2",
                "title": "Code on Wages 2019",
                "focus": "The wage and bonus regime applicable to all employees in all establishments.",
                "tasks": [
                    "Definition of 'wages' under Sec 2(y) — the inclusive and exclusive parts; capping of allowances at 50%",
                    "Minimum wages — Sec 6–8; the National Floor Wage; State-fixed minimum wages",
                    "Payment of wages — periodicity, mode (digital), wage period, deductions allowed",
                    "Bonus — Sec 26; eligibility (employees earning up to specified ceiling); minimum 8.33%, maximum 20%; available surplus",
                    "Equal remuneration — Sec 3; gender-based discrimination prohibition",
                    "Compliance — single registration, simplified records, simplified return",
                ],
            },
            {
                "week": "3",
                "title": "Industrial Relations Code 2020",
                "focus": "Union recognition, employment terms, and the layoff/retrenchment/closure regime.",
                "tasks": [
                    "Negotiating union and council — Sec 14; recognition by at least 51% support; otherwise negotiating council",
                    "Standing orders — Sec 28; mandatory for establishments with 300+ workers; model standing orders",
                    "Definition of worker; supervisor; manager — exclusion threshold (₹18,000/month for supervisors)",
                    "Layoff — Sec 67; conditions; compensation @ 50% of wages",
                    "Retrenchment — Sec 70; one-month notice or pay; compensation @ 15 days × completed years",
                    "Closure — Sec 75; 60-day notice; government permission for 300+ worker establishments",
                    "Industrial Tribunal procedures — Sec 44; reference; awards; enforcement",
                    "Strikes and lockouts — Sec 62; notice requirements; public utility services",
                ],
            },
            {
                "week": "4",
                "title": "Code on Social Security 2020 — Part 1",
                "focus": "EPF, ESIC and Gratuity under the new code.",
                "tasks": [
                    "EPF — Sec 15; applicability to 20+ employee establishments; voluntary coverage; international workers",
                    "EPF contribution — 12% employer, 12% employee; on basic wages (revised wage definition)",
                    "EPS contribution — 8.33% out of employer's 12%; pension calculation",
                    "ESI — Sec 28; applicability to 10+ employee establishments; wage threshold ₹21,000/month",
                    "Gratuity — Sec 53; 5 years' continuous service (or as prescribed); 15 days × completed years × last drawn wage; cap ₹20 lakh (subject to revision)",
                    "Working journalist gratuity — special provision",
                ],
            },
            {
                "week": "5",
                "title": "Code on Social Security 2020 — Part 2",
                "focus": "Maternity, employee compensation, unorganised workers, gig and platform workers.",
                "tasks": [
                    "Maternity benefit — Sec 59; 26 weeks paid leave; conditions and exclusions; creche facility for 50+ employees",
                    "Employee Compensation — Sec 76; coverage for unorganised workers; schedule of injuries; computation",
                    "Unorganised workers — Sec 109; social security board; welfare schemes",
                    "Gig and platform workers — Sec 113; landmark inclusion; contribution by aggregators (1–2% of turnover)",
                    "Building and other construction workers — Sec 100; cess; welfare schemes",
                ],
            },
            {
                "week": "6",
                "title": "OSH Code 2020",
                "focus": "Working conditions across all sectors and the unified factory licence.",
                "tasks": [
                    "OSH Code applicability — Sec 1; establishments with 10+ workers (with electricity) or 20+ (without)",
                    "Working hours — Sec 25; max 48 hours/week; overtime double rate; weekly off",
                    "Annual leave with wages — Sec 32; 1 day per 20 days worked; 12 days minimum encashable",
                    "Contract labour — Chapter XI; deemed direct-employment if not registered contractor; 50-worker threshold for registration",
                    "Inter-state migrant workers — Chapter X; reduction of threshold to 10 workers; portable benefits",
                    "Women — Sec 43; allowed in all establishments and shifts with safety provisions",
                    "Safety committees and safety officers — Sec 22; mandatory for hazardous establishments",
                ],
            },
            {
                "week": "7",
                "title": "Compliance Changes for HR & Payroll",
                "focus": "The practical operational impact.",
                "tasks": [
                    "Wage definition change — basic + DA must be at least 50% of CTC; impact on PF, gratuity, leave encashment",
                    "Restructuring CTC — model new compensation structures that comply with the 50% rule",
                    "EPF/ESIC implications — higher contributions on a higher base",
                    "Working hours flexibility — daily limit raised to 12 hours in some states (subject to weekly 48-hour cap)",
                    "Fixed-term employment — formalised; same benefits as permanent workers proportionate; gratuity after 1 year",
                    "Single registration and single return — but verify State Rules notification status",
                    "Audit trail — digital records mandated under the codes",
                ],
            },
            {
                "week": "8",
                "title": "State Rules, Transitions & Litigation",
                "focus": "How the codes operate in practice and the ongoing transition.",
                "tasks": [
                    "State Rules under each code — status check (Karnataka, Maharashtra, Telangana, etc.)",
                    "Transitions from old laws — when do old EPF Act provisions stop applying?",
                    "Pending litigation under old acts — continuance; saving clauses",
                    "Penalties under the codes — compoundable offences; first-offence-warning concept",
                    "Inspector-cum-Facilitator regime — replacing adversarial inspections",
                    "Practical compliance calendar — build one for a typical 200-employee manufacturing unit",
                ],
            },
        ],
        "topics": [
            "Code on Wages 2019 — minimum wage, payment, bonus, equal remuneration",
            "Wage definition — Sec 2(y); the 50% cap on allowances",
            "Industrial Relations Code — negotiating union, standing orders, layoff/retrenchment/closure",
            "Standing orders — applicability threshold (300+ workers)",
            "Code on Social Security — EPF, ESIC, gratuity, maternity, employee compensation",
            "Gig and platform workers — first-ever statutory recognition",
            "Aggregator contribution — 1–2% of turnover for gig worker fund",
            "OSH Code — working hours, leave, contract labour, inter-state migrants",
            "Women in workplace — all shifts permissible with conditions",
            "Fixed-term employment — formalised under IR Code",
            "Single registration, single return, single inspection (cum-facilitator)",
            "State Rules — status across major industrial states",
            "Saving clauses — pending litigation under old acts",
            "Penalties — compoundable, first-offence warning",
            "Digital records and audit trail",
        ],
        "books": [
            {
                "title": "Labour Laws",
                "author": "Avtar Singh",
                "publisher": "Universal Law Publishing / LexisNexis · latest edition",
                "why": "The standard university and practitioner reference. Excellent for the underlying jurisprudence on which the codes build.",
            },
            {
                "title": "The New Labour Codes — A Complete Guide",
                "author": "Taxmann editorial",
                "publisher": "Taxmann · latest edition",
                "why": "All four codes with bare text, section-wise commentary, comparative table with old acts, and State Rules tracker.",
            },
            {
                "title": "Practical Guide to the Four Labour Codes",
                "author": "CA Vikrant Suryavanshi / industry practitioners",
                "publisher": "Bharat Law House · latest edition",
                "why": "HR/payroll-focused commentary with compliance calendar, format checklists, model documents.",
            },
            {
                "title": "Industrial and Labour Laws",
                "author": "SN Misra",
                "publisher": "Central Law Publications · latest edition",
                "why": "Comprehensive treatment of each labour law with case law. Useful for understanding the regulatory logic before mapping to the new codes.",
            },
            {
                "title": "Handbook on Compliance Calendar — Labour Codes",
                "author": "ICSI / NIRC",
                "publisher": "ICSI / Wadhwa & Co.",
                "why": "Compliance-focused reference. Month-by-month checklist for an HR professional.",
            },
        ],
        "sources": [
            {
                "name": "Ministry of Labour & Employment",
                "url": "https://labour.gov.in/",
                "description": "Central ministry website with all four codes, draft rules, FAQs and notification status. The authoritative source.",
            },
            {
                "name": "EPFO — Employees' Provident Fund Organisation",
                "url": "https://www.epfindia.gov.in/",
                "description": "EPF circulars, contribution rates, FAQ on Code on Social Security provisions.",
            },
            {
                "name": "ESIC — Employees' State Insurance Corporation",
                "url": "https://www.esic.gov.in/",
                "description": "ESI registration, contribution, benefits, and the Code on Social Security mapping.",
            },
            {
                "name": "DGFASLI — Factory Advice Service",
                "url": "https://dgfasli.gov.in/introduction",
                "description": "Occupational safety, factory inspections, safety committees under the OSH Code.",
            },
            {
                "name": "Shram Suvidha Portal",
                "url": "https://shramsuvidha.gov.in/",
                "description": "Unified compliance portal — single registration, returns, inspection management.",
            },
            {
                "name": "ICSI — Labour Law Updates",
                "url": "https://www.icsi.edu/",
                "description": "ICSI's Compendium on Labour Codes and webinar archive. Strong on company-secretarial compliance angle.",
            },
            {
                "name": "Nishith Desai — HR Law (Employment & Labour)",
                "url": "https://www.nishithdesai.com/SectionArticleList/32/Areas-of-Service/167/HumanResourcesLawEmploymentandLabour.html",
                "description": "Industry-leading practitioner papers on the labour codes — implementation impact, sector-specific issues.",
            },
            {
                "name": "Bar & Bench",
                "url": "https://www.barandbench.com/",
                "description": "Latest judgments on labour disputes; case-law tracking by sector.",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 5) Auditing (ICAI latest updates)
    # ------------------------------------------------------------------
    {
        "slug": "auditing",
        "title": "Auditing — ICAI Latest Updates",
        "subtitle": "Standards on Auditing (SAs), CARO 2020, ICFR and the NFRA framework.",
        "summary": (
            "Statutory audit is governed by Sections 139–148 of the Companies Act 2013 read with "
            "the Standards on Auditing (SAs) issued by ICAI. The SA framework is harmonised with "
            "the International Standards on Auditing (ISAs) of the IAASB. ICAI revises specific "
            "SAs periodically — most recently SA 600 (group audits) and SA 315 (risk assessment). "
            "Master the standards, CARO 2020 reporting, and the ICFR framework."
        ),
        "weeks": [
            {
                "week": "1",
                "title": "Audit Framework",
                "focus": "The legal mandate and the standard-setting architecture.",
                "tasks": [
                    "Sec 139–148 of Companies Act 2013 — appointment, term, rotation, removal of auditor",
                    "Sec 139(2) and Rule 5 — auditor rotation thresholds (individual 5 years, firm 10 years)",
                    "Sec 144 — prohibited services (the negative list)",
                    "Sec 141 — eligibility, qualifications, disqualifications",
                    "ICAI Auditing and Assurance Standards Board (AASB) — role; SAs vs SREs vs SAEs",
                    "NFRA — jurisdiction (over Big-listed companies and other prescribed); disciplinary actions",
                ],
            },
            {
                "week": "2",
                "title": "Audit Reporting — SA 700 series",
                "focus": "The auditor's report and the Key Audit Matters (KAM) regime.",
                "tasks": [
                    "SA 700 (revised) — Forming an Opinion and Reporting on Financial Statements",
                    "SA 701 — Communicating Key Audit Matters (KAM) — applicable to listed entities",
                    "SA 705 — Modifications to the Opinion (qualified, adverse, disclaimer)",
                    "SA 706 — Emphasis of Matter and Other Matter paragraphs",
                    "SA 710 — Comparative Information; corresponding figures vs comparative financial statements",
                    "Practical reading — pull 3 recent audit reports from listed-company annual reports; identify KAMs, EOM, OM",
                ],
            },
            {
                "week": "3",
                "title": "Risk Assessment — SA 315 (Revised)",
                "focus": "The new risk-assessment standard, effective FY 2022-23.",
                "tasks": [
                    "SA 315 (revised) — five elements of system of internal control; understanding the entity",
                    "Inherent risk factors — the new spectrum-of-risk concept (subjectivity, complexity, uncertainty, etc.)",
                    "Significant risks vs other risks",
                    "Stand-back review — overall assessment of risk identification completeness",
                    "Linkage with SA 330 — responses to assessed risks",
                ],
            },
            {
                "week": "4",
                "title": "Fraud, Laws, Communication — SA 240, 250, 260, 265",
                "focus": "The auditor's responsibilities beyond ordinary risk.",
                "tasks": [
                    "SA 240 — Auditor's Responsibilities Relating to Fraud; the fraud triangle (incentive, opportunity, rationalisation)",
                    "SA 240 — presumed significant risk of management override of controls; journal entry testing",
                    "SA 250 — Consideration of Laws and Regulations (NOCLAR — Non-compliance with Laws and Regulations)",
                    "SA 260 — Communication with Those Charged with Governance; required vs other communications",
                    "SA 265 — Communicating Deficiencies in Internal Control",
                ],
            },
            {
                "week": "5",
                "title": "Audit Evidence — SA 500 series",
                "focus": "How auditors gather, evaluate and use evidence.",
                "tasks": [
                    "SA 500 — Audit Evidence; sufficient and appropriate; reliability hierarchy",
                    "SA 501 — Specific considerations for inventory, litigation, segment information",
                    "SA 505 — External Confirmations; positive vs negative; bank confirmations",
                    "SA 520 — Analytical Procedures; substantive analytical procedures",
                    "SA 530 — Audit Sampling; statistical vs non-statistical; sample size determination",
                    "SA 540 (revised) — Auditing Accounting Estimates; the new risk-based approach",
                    "SA 550 — Related Parties; identification; transactions in normal course of business",
                ],
            },
            {
                "week": "6",
                "title": "Group Audits — SA 600 (Revised)",
                "focus": "Group audit responsibilities — major revision effective from FY 2026-27 (verify current effective date).",
                "tasks": [
                    "SA 600 — Using the Work of Another Auditor (original)",
                    "SA 600 (revised) — Special Considerations — Audits of Group Financial Statements",
                    "Component identification; component materiality; component audits",
                    "Direction, supervision, review of component auditor's work",
                    "ICAI's recent guidance on group audits — Big-listed group challenges",
                ],
            },
            {
                "week": "7",
                "title": "CARO 2020 — The Reporting Companion",
                "focus": "The 21 reporting clauses every audit report on a non-exempt company carries.",
                "tasks": [
                    "Applicability — Sec 143(11); exemptions (small companies, OPC, certain charitable companies)",
                    "Clause-by-clause — property, plant and equipment; inventory; loans given; statutory compliance; income tax disputes; etc.",
                    "Clause 3(xi) — fraud reporting; relationship with SA 240; whistleblower mechanism",
                    "Clause 3(xvi) — NBFC/RBI registration; CIC; recent additions",
                    "Documentation requirements per clause — typical evidence file structure",
                ],
            },
            {
                "week": "8",
                "title": "ICFR, Quality Control, Specialised Audits",
                "focus": "Beyond financial statement audit — the broader assurance toolkit.",
                "tasks": [
                    "Sec 143(3)(i) — ICFR audit; Companies (Audit and Auditors) Rules 2014 Rule 10A",
                    "ICAI Guidance Note on Audit of Internal Financial Controls Over Financial Reporting",
                    "SQC 1 — Quality Control for Firms; current; new ISQM 1 / ISQM 2 (international move to quality management)",
                    "Tax audit u/s 44AB — Form 3CA/3CB and 3CD; recent CBDT amendments",
                    "Transfer pricing audit — Form 3CEB",
                    "Statutory branch audit, concurrent audit (banks), revenue audit (banks)",
                    "Final wrap-up — review SAs 200–810 once over via the ICAI Compendium index",
                ],
            },
        ],
        "topics": [
            "Sec 139–148 Companies Act — auditor appointment, rotation, prohibited services",
            "ICAI AASB and NFRA jurisdictions",
            "SAs framework — SA 100–999 numbering; ISA convergence",
            "SA 200 — Overall Objectives",
            "SA 220 — Quality Control; SQC 1; ISQM 1",
            "SA 240 — Fraud; journal entry testing; management override",
            "SA 250 — Laws and regulations; NOCLAR",
            "SA 260 — Communication with TCWG; SA 265 — deficiencies",
            "SA 300, 315 (revised), 320, 330 — Audit planning and risk",
            "SA 500–580 — Audit evidence",
            "SA 540 (revised) — Accounting estimates",
            "SA 600 (revised) — Group audits",
            "SA 700–710 — Reporting; KAM",
            "SA 720 — Other Information",
            "CARO 2020 — 21 clauses",
            "ICFR — Sec 143(3)(i); Guidance Note",
            "Tax audit — Form 3CD; Schedules",
            "Specialised audits — bank concurrent, transfer pricing, GST audit",
            "NFRA disciplinary orders — learning from real cases",
        ],
        "books": [
            {
                "title": "Auditing and Assurance Standards — Compendium",
                "author": "ICAI",
                "publisher": "ICAI Publication · annual edition",
                "why": "The bare SAs with explanatory text. Mandatory primary source for every audit. Always cite from the latest published version.",
            },
            {
                "title": "Students' Guide to Auditing Standards",
                "author": "CA Surbhi Bansal",
                "publisher": "Bestword / VSI · latest edition",
                "why": "The most widely-used student/practitioner companion to the SAs. Each SA explained in plain language with chart summaries and exam-style questions.",
            },
            {
                "title": "Auditing and Assurance — Padhuka's Students' Guide",
                "author": "GS Saxena & Ravi Kapoor",
                "publisher": "Padhuka / Commercial Law Publishers · latest edition",
                "why": "Comprehensive treatment of auditing concepts, SAs, CARO, and Companies Act audit provisions. Strong on practical examples.",
            },
            {
                "title": "Practical Auditing",
                "author": "BN Tandon, Sudharsanam, Sundharabahu",
                "publisher": "S Chand · latest edition",
                "why": "The classic Indian auditing reference. Excellent for understanding the audit process from planning to reporting.",
            },
            {
                "title": "Guidance Note on Audit of Internal Financial Controls Over Financial Reporting",
                "author": "ICAI",
                "publisher": "ICAI Publication",
                "why": "Essential for the Sec 143(3)(i) ICFR opinion. Read alongside the SAs for any listed-company audit.",
            },
            {
                "title": "CARO 2020 — Practical Guide",
                "author": "ICAI / Taxmann editorial",
                "publisher": "Taxmann · annual edition",
                "why": "Clause-wise commentary on CARO 2020 with sample working papers and reporting language. Indispensable for every audit closure.",
            },
        ],
        "sources": [
            {
                "name": "ICAI Auditing & Assurance Standards Board",
                "url": "https://www.icai.org/post/auditing-assurance-standards-board",
                "description": "All SAs, Guidance Notes, Implementation Guides. The starting point for any audit query.",
            },
            {
                "name": "ICAI Board of Studies — Knowledge Portal",
                "url": "https://www.icai.org/post/bos-knowledge-portal",
                "description": "Searchable repository of ICAI publications, study material and revision videos. Cross-references between SAs and Companies Act provisions.",
            },
            {
                "name": "MCA — Acts & Rules",
                "url": "https://www.mca.gov.in/content/mca/global/en/acts-rules/ebooks.html",
                "description": "Section 139–148, Audit Rules, CARO 2020 notification. Authoritative source for the statutory mandate.",
            },
            {
                "name": "NFRA — Inspection Reports & Disciplinary Orders",
                "url": "https://nfra.gov.in/",
                "description": "Real-world quality-control findings and disciplinary orders against audit firms. The best source for learning about common audit failures.",
            },
            {
                "name": "IAASB — International Standards on Auditing",
                "url": "https://www.iaasb.org/",
                "description": "The underlying global standards on which Indian SAs are based. New ISA developments (e.g., ISA 600 revision, ISQM 1/2) signal upcoming SA revisions.",
            },
            {
                "name": "PwC India — Audit & Assurance",
                "url": "https://www.pwc.in/audit-services.html",
                "description": "Thought leadership on SA implementation, ICFR, ESG and IT audit. KPMG, EY and Deloitte India publish similar series.",
            },
            {
                "name": "Comptroller & Auditor General of India (CAG)",
                "url": "https://cag.gov.in/en",
                "description": "India's Supreme Audit Institution. Performance audits, compliance audits and reports tabled in Parliament — useful reference for public-sector auditors.",
            },
            {
                "name": "Income-tax Department — Notifications",
                "url": "https://www.incometaxindia.gov.in/notifications",
                "description": "Annual Form 3CD updates, tax-audit threshold notifications, due-date extensions.",
            },
        ],
    },

    # ------------------------------------------------------------------
    # 6) English — Spoken & Grammar
    # ------------------------------------------------------------------
    {
        "slug": "english",
        "title": "Spoken English & Grammar",
        "subtitle": "From foundational grammar to professional fluency — the language layer that compounds every other skill.",
        "summary": (
            "Strong English compounds with every other skill on this plan — your audit reports "
            "are clearer, your client emails are more persuasive, and your professional confidence "
            "grows. The plan combines daily grammar drills, vocabulary building, listening, and "
            "spoken practice. Consistency over intensity — 30 minutes a day for 8 weeks beats "
            "binge-studying."
        ),
        "weeks": [
            {
                "week": "1",
                "title": "Sentence Structure & Parts of Speech",
                "focus": "Foundation. The building blocks of grammar.",
                "tasks": [
                    "Parts of speech — noun, pronoun, verb, adjective, adverb, preposition, conjunction, interjection",
                    "Sentence types — declarative, interrogative, imperative, exclamatory",
                    "Subject and predicate; finite vs non-finite verbs",
                    "Phrases (noun, verb, adjective, adverb, prepositional) and clauses (independent, dependent)",
                    "Wren & Martin Chapter 1–5; do 20 sentences in writing daily",
                ],
            },
            {
                "week": "2",
                "title": "The 12 Tenses",
                "focus": "The single most common source of error for Indian speakers.",
                "tasks": [
                    "Simple present, present continuous, present perfect, present perfect continuous",
                    "Simple past, past continuous, past perfect, past perfect continuous",
                    "Simple future, future continuous, future perfect, future perfect continuous",
                    "Tense usage in narration; sequence of tenses",
                    "Daily writing — 5 sentences per tense; record yourself saying them aloud",
                ],
            },
            {
                "week": "3",
                "title": "Articles, Prepositions, Conjunctions",
                "focus": "The small words that trip up non-native speakers.",
                "tasks": [
                    "Articles — a, an, the; zero article; common errors with Indian English",
                    "Prepositions of time, place, direction, manner; collocations (interested IN, depend ON, suffer FROM)",
                    "Coordinating conjunctions (FANBOYS — for, and, nor, but, or, yet, so)",
                    "Subordinating conjunctions — when, while, because, although, if, unless",
                    "Correlative conjunctions — either…or, neither…nor, not only…but also, both…and",
                    "Practical Usage by Michael Swan — pick 10 problem prepositions and master them",
                ],
            },
            {
                "week": "4",
                "title": "Active/Passive, Direct/Indirect, Modals",
                "focus": "Transformations and modal verbs.",
                "tasks": [
                    "Active to passive — rules across tenses; when to use passive (formal writing, unknown agent)",
                    "Direct to indirect speech — tense back-shift; reporting verbs",
                    "Modals — can, could, may, might, must, shall, should, will, would; meanings and contexts",
                    "Modal perfects — must have, should have, could have; subjunctive mood",
                    "Conditional sentences — zero, first, second, third, mixed",
                ],
            },
            {
                "week": "5",
                "title": "Vocabulary Building",
                "focus": "Word roots, prefixes, suffixes — the engine of English vocabulary.",
                "tasks": [
                    "Norman Lewis Word Power Made Easy — 1 chapter daily; flashcard review",
                    "Common Latin and Greek roots — bene, mal, mort, vit, hydro, geo, phon, vid",
                    "Common prefixes — un-, re-, dis-, mis-, in-, im-, pre-, post-, sub-, super-",
                    "Common suffixes — -tion, -ment, -ness, -ity, -able, -ous, -ly",
                    "Phrasal verbs — 20 most common; one verb (e.g., 'get') across all its phrasal forms",
                    "Idioms — 5 idioms per day; use in writing same day",
                ],
            },
            {
                "week": "6",
                "title": "Pronunciation & Common Errors",
                "focus": "The Indian English specifics.",
                "tasks": [
                    "IPA — the 44 sounds of English; vowels (12) + consonants (24) + diphthongs (8)",
                    "Indian English specifics — TH sounds (think, this), V vs W, schwa /ə/, syllable stress",
                    "Word stress patterns — re-CORD (verb) vs RE-cord (noun); two-syllable rule",
                    "Sentence stress and intonation — content words vs function words; rising vs falling intonation",
                    "BBC Learning English Pronunciation series — 1 video daily; shadow the speaker",
                    "Record yourself reading a 200-word passage daily; compare with native speaker reference",
                ],
            },
            {
                "week": "7",
                "title": "Spoken English — Fluency Building",
                "focus": "From hesitant to fluent — the practice-based week.",
                "tasks": [
                    "Daily 5-minute self-talk on a topic in English (news, work, hobbies)",
                    "Shadowing — listen to BBC News and repeat aloud, matching pace and intonation",
                    "Conversation partners — find one on iTalki, Cambly, or a local English-speaking colleague",
                    "Topic-based monologues — describe a process from your work in 2 minutes",
                    "Common spoken constructions — fillers (well, you know, like), polite forms, opinion phrases (in my view, I'd argue, the way I see it)",
                    "Role plays — meet a client, present an audit finding, decline a request politely",
                ],
            },
            {
                "week": "8",
                "title": "Business English — Writing & Speaking",
                "focus": "The professional register of English.",
                "tasks": [
                    "Business emails — subject lines, opening, body, closing; passive vs active voice in formal writing",
                    "Audit reports — concise, factual, observation-based language; avoiding hedging",
                    "Meeting language — chairing, contributing, summarising, disagreeing politely",
                    "Presentations — structure (signposting), engagement (questions, examples), closing",
                    "Common Indian English vs Standard English — kindly (overused), revert (often misused), prepone (Indianism), do the needful (avoid)",
                    "Final wrap-up — write a 500-word professional summary of your 2-month journey; record a 2-minute spoken version",
                ],
            },
        ],
        "topics": [
            "Parts of speech and sentence structure",
            "The 12 tenses — formation and usage",
            "Articles and zero article",
            "Prepositions — time, place, direction; collocations",
            "Conjunctions — coordinating, subordinating, correlative",
            "Active and passive voice",
            "Direct and indirect speech",
            "Modal verbs and modal perfects",
            "Conditional sentences — all four types",
            "Subjunctive mood",
            "Vocabulary — roots, prefixes, suffixes",
            "Phrasal verbs and idioms",
            "Pronunciation — IPA, word stress, sentence stress",
            "Indian English vs Standard English",
            "Business email writing",
            "Audit-report language",
            "Meeting and presentation skills",
            "Listening — BBC, VOA, podcasts",
            "Speaking — shadowing, monologues, role plays",
            "Vocabulary in context — read a quality newspaper daily",
        ],
        "books": [
            {
                "title": "High School English Grammar and Composition",
                "author": "Wren & Martin (revised by N.D.V. Prasada Rao)",
                "publisher": "S. Chand · latest edition",
                "why": "The foundational Indian English-grammar textbook for 100 years. Comprehensive coverage with thousands of exercises. Best place to start.",
            },
            {
                "title": "Practical English Usage",
                "author": "Michael Swan",
                "publisher": "Oxford University Press · 4th Edition",
                "why": "The world's leading reference on English usage. Alphabetical entries on every common difficulty — articles, prepositions, tenses, common errors. Indispensable.",
            },
            {
                "title": "Word Power Made Easy",
                "author": "Norman Lewis",
                "publisher": "Goyal Publishers / Anchor",
                "why": "The single best book for vocabulary building in English. Etymology-based; teaches you to deconstruct unknown words. Indian classic.",
            },
            {
                "title": "English Vocabulary in Use (Pre-Intermediate, Intermediate, Advanced)",
                "author": "Stuart Redman / Felicity O'Dell",
                "publisher": "Cambridge University Press · latest editions",
                "why": "Topic-organised vocabulary with exercises. Three levels; pick your starting point honestly and progress.",
            },
            {
                "title": "Spoken English — A Self-Learning Guide to Conversation Practice",
                "author": "V. Sasikumar & P.V. Dhamija",
                "publisher": "Tata McGraw-Hill · latest edition",
                "why": "Designed for the Indian learner. Functional units (greetings, agreeing/disagreeing, requesting, complaining) with sample dialogues.",
            },
            {
                "title": "The Elements of Style",
                "author": "William Strunk Jr. and E.B. White",
                "publisher": "Pearson · 4th Edition",
                "why": "A short, classic style guide. The 'omit needless words' philosophy will transform your professional writing. Read it in one sitting; re-read annually.",
            },
        ],
        "sources": [
            {
                "name": "BBC Learning English",
                "url": "https://www.bbc.co.uk/learningenglish",
                "description": "The single best free resource for spoken English. 6 Minute English (vocabulary), English at Work (business), Pronunciation in the News (IPA-based).",
            },
            {
                "name": "British Council India",
                "url": "https://www.britishcouncil.in/english",
                "description": "Free LearnEnglish app and online courses. Strong on grammar exercises and IELTS preparation.",
            },
            {
                "name": "Cambridge Dictionary",
                "url": "https://dictionary.cambridge.org/",
                "description": "Free dictionary with pronunciation audio (British and American), example sentences, collocations. Better than Google Translate for nuance.",
            },
            {
                "name": "VOA Learning English",
                "url": "https://learningenglish.voanews.com/",
                "description": "News stories at three levels of speed. Best for slow-paced listening practice that builds up to native speed.",
            },
            {
                "name": "Grammarly Blog",
                "url": "https://www.grammarly.com/blog",
                "description": "Bite-sized articles on grammar, usage, and writing style. Browser extension catches common errors in real time.",
            },
            {
                "name": "engVid",
                "url": "https://www.engvid.com/",
                "description": "Free video lessons by native-speaker teachers. Particularly strong on pronunciation and accent.",
            },
            {
                "name": "Coursera / edX — English Courses",
                "url": "https://www.coursera.org/browse/language-learning/learning-english",
                "description": "University-level English courses. The Georgia Tech 'Business Writing' course is excellent for professional writing.",
            },
            {
                "name": "TED Talks (with English subtitles)",
                "url": "https://www.ted.com/",
                "description": "10–18 minute talks on a wide range of topics. Best for practising listening to varied accents and absorbing rhetorical structure.",
            },
        ],
    },
]
