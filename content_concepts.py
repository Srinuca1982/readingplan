"""Conceptual learning: plain-English explanations with worked examples."""

CONCEPTS = [
    {
        "tag": "Foundation",
        "title": "Why companies restructure",
        "summary": "The five economic motives — and how each maps to a different statutory route.",
        "body": (
            "Restructuring is never an end in itself. Every transaction answers some "
            "commercial pressure: <strong>scale</strong> (acquire to grow faster than organically), "
            "<strong>synergy</strong> (combine to extract cost or revenue gains), <strong>focus</strong> "
            "(separate non-core businesses so each can be funded and managed on its own merits), "
            "<strong>tax efficiency</strong> (use loss carry-forwards, reset cost bases, eliminate "
            "double taxation), and <strong>regulatory or family</strong> reasons (succession, "
            "promoter exit, listing, distressed turnaround). Identify the motive first; the legal "
            "route follows from it."
        ),
        "example": (
            "<strong>Example.</strong> A diversified group runs FMCG and pharma under one listed "
            "entity. The pharma business has different margins, capex cycle, and investor profile. "
            "Management <em>demerges</em> pharma under Sec 230–232 read with Sec 2(19AA) into a "
            "separately listed entity, so each unit gets focused capital. The motive — focus — "
            "drives the choice of demerger over slump sale."
        ),
        "hooks": (
            "Companies Act <span class='sec'>Sec 230–232</span> · Income-tax "
            "<span class='sec'>Sec 2(1B)</span>, <span class='sec'>Sec 2(19AA)</span>, "
            "<span class='sec'>Sec 50B</span> · FEMA Cross Border Merger Regulations 2018."
        ),
        "pitfalls": (
            "Letting tax tail wag the commercial dog. A scheme designed only for tax efficiency "
            "without commercial substance attracts <strong>GAAR</strong> and <strong>McDowell</strong> "
            "scrutiny. Always document the business rationale in the explanatory statement."
        ),
    },
    {
        "tag": "Comparison",
        "title": "Merger vs Demerger vs Slump Sale vs Buyback vs Capital Reduction",
        "summary": "When to use each route. The taxonomy every CA needs to know cold.",
        "body": (
            "Five routes, five mental models. <strong>Merger</strong>: company A dissolves into "
            "company B; everything moves; shareholders of A get shares of B. <strong>Demerger</strong>: "
            "one undertaking of company A spins off into a new company R; A continues, R is born; "
            "A's shareholders get shares of R pro rata. <strong>Slump sale</strong>: company A "
            "sells an undertaking to buyer B for cash; no court, no scheme, but tax under Sec 50B. "
            "<strong>Buyback</strong>: company returns cash to shareholders by buying back its own "
            "shares; capital comes down. <strong>Capital reduction</strong>: NCLT-approved write-down "
            "of paid-up capital, often to clean up accumulated losses or return surplus."
        ),
        "example": (
            "<strong>Example.</strong> Promoter wants to exit one division and take cash. "
            "<em>Slump sale</em> works if a buyer wants the whole undertaking — fastest, no court. "
            "<em>Demerger</em> works if the promoter wants to keep ownership but separate listings. "
            "<em>Capital reduction</em> works if the goal is to return cash from accumulated reserves "
            "without divesting the business. Same starting facts, three different routes — pick by "
            "commercial goal."
        ),
        "hooks": (
            "Merger/Demerger: Companies Act <span class='sec'>Sec 230–232</span>. "
            "Slump sale: Income-tax <span class='sec'>Sec 50B</span>, <span class='sec'>Sec 2(42C)</span>. "
            "Buyback: Companies Act <span class='sec'>Sec 68–70</span>, IT <span class='sec'>Sec 115QA</span>. "
            "Capital reduction: Companies Act <span class='sec'>Sec 66</span>, IT <span class='sec'>Sec 2(22)(d)</span>."
        ),
        "pitfalls": (
            "Treating slump sale and itemised sale as interchangeable. If individual asset values "
            "are assigned, Sec 50B will not apply — and you lose the favourable treatment. "
            "<strong>Drafting note:</strong> the BTA must clearly state a lump-sum consideration."
        ),
    },
    {
        "tag": "Tax timing",
        "title": "Appointed date vs effective date",
        "summary": "The single most-tested timing concept in scheme practice.",
        "body": (
            "Every scheme has two dates. The <strong>appointed date</strong> is the date the "
            "transaction is deemed to take effect for accounting, tax and ownership purposes — "
            "the legal fiction. The <strong>effective date</strong> is the date the NCLT order "
            "is filed with the ROC and the scheme actually operates in real time. The gap between "
            "them is usually 6–18 months. All P&L and asset movements between the two dates are "
            "deemed to be on behalf of the transferee — even though, in reality, the transferor "
            "ran the business."
        ),
        "example": (
            "<strong>Example.</strong> A scheme sets appointed date = 1 April 2024. NCLT sanctions "
            "on 15 October 2025. Effective date = 30 October 2025. For FY 2024–25, the transferred "
            "undertaking's income is taxed in the transferee's hands, even though tax was paid by "
            "the transferor during the year. Reconciliation through a <em>combined return</em> or "
            "<em>revised return</em> is then needed. This is the principle in <strong>Marshall Sons "
            "& Co. (India) Ltd. v. ITO (1996) — appointed date binds even when the order comes later</strong>."
        ),
        "hooks": (
            "Companies Act <span class='sec'>Sec 232(6)</span> · MCA circular dated 21 August 2019 "
            "(appointed date may be a specific date or contingent date; generally not more than 12 "
            "months prior to filing) · Marshall Sons principle."
        ),
        "pitfalls": (
            "Setting an appointed date far in the past (>12 months before filing) without strong "
            "commercial justification. The MCA pushes back, and the tax department may treat it as "
            "a colourable device. Document the rationale."
        ),
    },
    {
        "tag": "Tax design",
        "title": "Tax-neutral vs taxable restructuring",
        "summary": "How the Sec 47 exemption regime works — and how it can be lost.",
        "body": (
            "The Income-tax Act treats every transfer of a capital asset as a taxable event, unless "
            "it falls within <strong>Sec 47</strong>. Mergers, demergers, certain cross-border "
            "transactions and intra-group share transfers each have specific exemptions: "
            "<span class='sec'>Sec 47(vi)/(vii)</span> for amalgamation, "
            "<span class='sec'>Sec 47(vib)/(vid)</span> for demerger, "
            "<span class='sec'>Sec 47(via)/(vic)/(vicc)</span> for cross-border. Each exemption "
            "rides on definitions in <span class='sec'>Sec 2(1B)</span> and "
            "<span class='sec'>Sec 2(19AA)</span> being met. If you fail a single condition, the "
            "exemption falls and the entire transaction becomes taxable."
        ),
        "example": (
            "<strong>Example.</strong> Demerger of a logistics undertaking. The scheme transfers "
            "vehicles, contracts, employees and goodwill — but the parent <em>retains</em> the "
            "key customer contract because it's tied to its name. Sec 2(19AA) requires <em>all</em> "
            "properties of the undertaking to transfer. The exemption fails. Capital gains arise on "
            "the entire transfer. <strong>Fix:</strong> assign or novate the contract; or restructure "
            "so the contract was never part of the undertaking definition in the first place."
        ),
        "hooks": (
            "Definitions in <span class='sec'>Sec 2(1B)</span> (amalgamation) and "
            "<span class='sec'>Sec 2(19AA)</span> (demerger); exemption sections in "
            "<span class='sec'>Sec 47</span>; cost rules in <span class='sec'>Sec 49(2)/(2C)/(2D)</span>; "
            "loss carry-forward in <span class='sec'>Sec 72A</span>; withdrawal of exemption in "
            "<span class='sec'>Sec 47A</span>."
        ),
        "pitfalls": (
            "Sec 47A withdrawal is the silent killer. If conditions are breached within 8 years "
            "(e.g., the transferee disposes of the undertaking, fails the 75% asset retention test), "
            "the originally exempt transaction is reassessed as taxable in the year of breach. "
            "<strong>Maintain post-transaction monitoring memos.</strong>"
        ),
    },
    {
        "tag": "Cross-border",
        "title": "Domestic vs cross-border restructuring",
        "summary": "What changes when the transaction crosses India's borders.",
        "body": (
            "A domestic merger touches the Companies Act and the Income-tax Act. A cross-border "
            "merger adds two more regimes: <strong>FEMA</strong> (foreign exchange) and "
            "<strong>regulatory clearance</strong> from sectoral regulators. The Companies Act "
            "permits cross-border mergers only between an Indian company and a foreign company "
            "incorporated in a <em>notified jurisdiction</em> (essentially FATF-compliant, with "
            "a bilateral arrangement). FEMA Cross Border Merger Regulations 2018 grant "
            "<em>deemed RBI approval</em> if the regulations are complied with, including the "
            "two-year window to dispose of non-compliant assets and borrowings."
        ),
        "example": (
            "<strong>Example.</strong> A Mauritius holding company wants to merge into its Indian "
            "operating subsidiary — a classic <em>reverse flip</em>. Steps: (1) Companies Act Sec 234 "
            "+ Rule 25A scheme, (2) NCLT petition with shareholders' approval, (3) FEMA Cross Border "
            "Merger Regulations 2018 compliance certificate, (4) NDI Rules 2019 pricing for any new "
            "shares issued to the Mauritius shareholders, (5) tax under Sec 47(via)/(vic) if "
            "conditions met. Five regulators, one transaction. Sequence and timing matter — get "
            "Companies Act / FEMA simultaneously rather than serially."
        ),
        "hooks": (
            "Companies Act <span class='sec'>Sec 234</span> + Rule 25A · FEMA Cross Border Merger "
            "Regs 2018 · NDI Rules 2019 (inbound) · ODI Rules 2022 (outbound) · IT "
            "<span class='sec'>Sec 47(via)/(vic)/(vicc)</span> · PN3 if neighbouring country."
        ),
        "pitfalls": (
            "Forgetting that PN3 (Press Note 3 of 2020) requires <strong>government route</strong> "
            "for any investment with a beneficial owner in a country sharing a land border with "
            "India. A Mauritius vehicle with Chinese ultimate ownership <em>does not</em> escape PN3."
        ),
    },
    {
        "tag": "Listed companies",
        "title": "Extra hoops for listed companies",
        "summary": "SEBI's overlay on every scheme involving a listed entity.",
        "body": (
            "If any party is listed, SEBI's <strong>LODR Regulation 37</strong> kicks in: the listed "
            "company must obtain stock exchange / SEBI <em>prior approval</em> before filing the "
            "scheme with NCLT. The SEBI <strong>Master Circular on Schemes of Arrangement</strong> "
            "specifies what the application must contain — fairness opinion from an independent "
            "merchant banker, valuation report, no-objection from stock exchanges, "
            "post-scheme listing undertaking, and a positive recommendation from the audit committee "
            "and the committee of independent directors. Separately, <strong>SAST Regulations 2011</strong> "
            "may trigger an open offer if the scheme results in acquisition of 25% or more (Reg. 3) "
            "or change of control (Reg. 4)."
        ),
        "example": (
            "<strong>Example.</strong> A promoter wants to demerge a listed cement business into "
            "a separately listed entity. Sequence: (1) board approval, (2) merchant banker fairness "
            "opinion, (3) audit committee recommendation, (4) BSE/NSE in-principle approval under "
            "Reg. 37, (5) SEBI observation letter, (6) shareholder approval — note: majority of "
            "minority shareholders required if related-party scheme, (7) NCLT petition, (8) post-"
            "sanction listing of new entity. Skipping the SEBI step or filing NCLT first invites "
            "rejection or remand."
        ),
        "hooks": (
            "SEBI LODR <span class='sec'>Reg. 37</span> · SEBI Master Circular on Schemes (latest "
            "version) · SAST 2011 <span class='sec'>Reg. 3, 4, 10(1)(d)</span> · ICDR for any "
            "preferential issue of new shares post-scheme."
        ),
        "pitfalls": (
            "<strong>Related-party schemes</strong> need majority-of-minority approval — promoters "
            "cannot vote on their own scheme. Many schemes have failed at this gate. Plan governance "
            "approvals as carefully as legal ones."
        ),
    },
    {
        "tag": "Procedure",
        "title": "Court route vs out-of-court route",
        "summary": "Trade-off: certainty (NCLT) vs speed (BTA, buyback, simple share transfer).",
        "body": (
            "Two ways to move assets between companies. The <strong>court route</strong> — Sections "
            "230–234, NCLT-sanctioned scheme — gives universal binding effect: all creditors and "
            "shareholders are bound by the order, automatic vesting of property, stamp-duty treatment "
            "as a court order rather than a registered instrument, and a clean record. The "
            "<strong>out-of-court route</strong> — slump sale BTA, buyback under Sec 68, "
            "share transfer — is faster (3–6 months vs 12–18 months) and avoids tribunal exposure, "
            "but requires individual consents (creditor novations, customer assignments, employee "
            "transfers), separate stamping of each instrument, and is more fragile if any third "
            "party refuses to consent."
        ),
        "example": (
            "<strong>Example.</strong> Two group companies want to combine their FMCG businesses. "
            "Option A — Scheme of arrangement: 12 months, NCLT, but clean and tax-neutral if Sec 2(1B) "
            "met. Option B — Slump sale BTA: 4 months, no court, but capital gains tax under Sec 50B "
            "and stamp duty on the conveyance. Choose A if the businesses share employees and "
            "creditors that would be hard to novate individually. Choose B if speed dominates and "
            "the parties can absorb the tax."
        ),
        "hooks": (
            "Court route: Companies Act <span class='sec'>Sec 230–234</span>, CAA Rules 2016. "
            "Out-of-court: <span class='sec'>Sec 50B</span> slump sale, <span class='sec'>Sec 68</span> "
            "buyback, <span class='sec'>Sec 180(1)(a)</span> shareholder approval for substantial "
            "asset disposal."
        ),
        "pitfalls": (
            "Choosing the out-of-court route to save time, then discovering halfway that 30 customers "
            "have anti-assignment clauses. Run a contracts heat-map <em>before</em> committing to "
            "either route."
        ),
    },
    {
        "tag": "Universal principle",
        "title": "The going-concern principle",
        "summary": "The single test that runs across slump sale, demerger and cross-border alike.",
        "body": (
            "Every tax-favoured restructuring depends on transferring the business as a <em>going "
            "concern</em> — i.e., the business is functional, employees are in place, contracts are "
            "live, and the buyer can continue operations from day one. <strong>Sec 2(19AA)(iv)</strong> "
            "requires demerger to be on a going-concern basis. <strong>GST Notification 12/2017</strong> "
            "exempts business transfer as a going concern from GST. <strong>Slump sale</strong> under "
            "Sec 2(42C) implies transfer of an undertaking — which means it must be functional, not "
            "a heap of dismantled assets. The unifying idea: tax law rewards transfers that "
            "<em>preserve economic activity</em>; it penalises transfers that are pure asset-stripping."
        ),
        "example": (
            "<strong>Example.</strong> A factory has been shut for 18 months. The owner sells the "
            "land, building and machinery to a buyer. Is this a slump sale or an itemised sale? "
            "If the business is not <em>capable of being carried on</em>, courts have held it's not "
            "a going concern — therefore not a slump sale under Sec 2(42C), and not GST-exempt. "
            "<strong>Drafting test:</strong> can the buyer start operations on the date of transfer "
            "without re-procuring anything material? If yes, going concern. If no, you have a tax problem."
        ),
        "hooks": (
            "<span class='sec'>Sec 2(19AA)(iv)</span> demerger condition · <span class='sec'>Sec 2(42C)</span> "
            "slump sale undertaking · GST Notification 12/2017 entry 2 · FEMA Cross Border Merger "
            "Regs 2018 compliance certificate referring to going concern."
        ),
        "pitfalls": (
            "Pre-closing reorganisations that dismantle the workforce or terminate the lease "
            "<em>before</em> closing can break the going-concern characterisation. Sequence the "
            "operational reorganisation <em>after</em> the closing date, not before."
        ),
    },
]
