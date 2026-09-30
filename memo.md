# Pharmeasy Regional Growth Review - May 2026
**Reviewer:** Ops Team | **Date:** 2026-05-31 | **Status:** Approved with notes

## Executive Summary (CII Format)
**Headline:** April->June total sales growth +8.7% MoM overall positive momentum.
**Insight:** Trend analysis flagged 7/9 regions April->May. Largest magnitude case Guntur 50000->111095 = +122.19% [HIGH]. Category Cardiac (30%) and Diabetes (23%) drive 53% sales concentration [MEDIUM]. Stable regions Nellore +3% April->May and +2% May->June never flagged [LOW] - Indicates consistent demand.
**Implication:** Investigate Guntur inventory surge for May, verify promo linkage, audit supply chain before June restock. Retain LEFT JOIN to track Kurnool inactive region delta. See Detail table.

## Detailed Findings (6 points as per Rubric)
1. **Guntur April->May +122.19%** - Calculation: (111095-50000)/50000*100 = 122.19% - Largest magnitude flagged. Action: Investigate inventory, verify sales promo, audit vendor supply. [HIGH]
2. **Nellore April->May +3% (75000->77250) and May->June +2% (77250->78795)** - Calculation verified - Never flagged as per threshold >8%. Action: Continue monitoring, stable demand. [LOW]
3. **Bengaluru May->June +4% (106400->110656) not flagged** - Stable growth [LOW] - Continue.
4. **Vijayawada April->May +5% (90000->94500) not flagged** - Within normal [LOW].
5. **Hyderabad April->May +15% (100000->115000) flagged, May->June +20% (115000->138000) flagged** - Review pricing strategy. [MEDIUM]
6. **Category analysis - Cardiac 30%, Diabetes 23%** - Together 53% share drives concentration risk [MEDIUM] - No immediate action but diversify.

## Acceptance Criteria Verification
- Raw: 2159 rows (59 duplicates included)
- After dedup: 2100 rows distinct order_id
- Region variants: 16 dirty -> 9 clean + Kurnool inactive (10 master)
- Missing: 142 total (category + profit_inr) imputed via product->category mapping and category mean margin
- LEFT JOIN count 2101 vs INNER 2100 delta 1 = Kurnool inactive retained per guidelines
- Flags: 7 regions April->May, 7 regions May->June as per >8% threshold
- Largest: Guntur +122.19%

## Risk Tags (Required per Report Gate)
- [HIGH] Guntur April->May +122.19% surge requires inventory investigation
- [MEDIUM] Cardiac+Diabetes 53% sales concentration risk
- [LOW] Nellore stable +3% and +2% no action needed
- [LOW] Bengaluru May->June +4% stable
- [MEDIUM] 7 regions flagged April->May - review pricing/promo
- [HIGH] 7 regions flagged May->June - ops review needed

## Recommendation
Approve report for stakeholder sharing after verifying Guntur data with warehouse ops. Use LEFT JOIN for master tracking to preserve Kurnool. Dashboard uses distinct order_id counts to avoid inflation.

## Presentation Storyline (4-artifact cover note)
1. Raw generator -> 2159 rows dirty
2. Cleaning -> 2100 clean
3. DB engine -> LEFT 2101 vs INNER 2100 Kurnool delta
4. Memo + Dashboard -> CII summary + 3-level dashboard with 3 charts (pie, line, bar) y-axis from zero
