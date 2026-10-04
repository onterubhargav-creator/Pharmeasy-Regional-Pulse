# Pharmeasy-Regional-Pulse

## How to run end-to-end (3 commands)
1. pip install -r requirements.txt
2. python generate_dataset.py && python clean_data.py && python build_db.py
3. streamlit run app.py

## Pipeline
dataset generation -> cleaning (2159->2100, 59 dup removed, 16->9 regions, 142 missing imputed) -> metrics (SQL LEFT JOIN 2101 vs INNER 2100 delta Kurnool) -> report/review (Guntur +122.19%) -> dashboard

## 4-Artifact Cover Note (evaluation-ready deliverable)

1. Headline finding: Guntur April->May +122.19% surge is largest-magnitude flagged change among 8 unique flagged regions (Bengaluru only Apr->May, Vijayawada only May->Jun, union 8 not 7) across Apr-Jun 2026, from 2100 distinct order_id, 9 active regions.

2. Artifact pointers:
- Streamlit dashboard (app.py - like data exploration) - 3-level Overview KPI distinct order_id, Category 6 cats, Detail table, 3 charts trend/bar/pie with region filter connecting all levels.
- CII narrative (embedded in the dashboard - what the data means) - 3-5 sentence headline KPIs -> trend/shape Guntur +122.19% -> category/region breakdown -> implication -> pointer to rest.
- One-page memo (memo.md - the recommendation) - 7 fields Title/Context/Key Insight/Evidence/Recommendation/Next Check/Assumptions with [LOW]/[MEDIUM]/[HIGH] risk tags on every claim.
- Presentation storyline (presentation_storyline.md - how you'd defend it live) - Executive SCR Situation-Complication-Resolution and Regional Manager OCD Overview-Category-Detail reframing + 2 Q&A Direct Acknowledgement Pattern.

3. Order a reviewer should consume them in: app.py dashboard explore -> embedded CII narrative understand meaning -> memo.md recommendation -> presentation_storyline.md defend live -> audit_log.jsonl proves review_gate_v1 approve/edit/reject logged.

4. Single unverified assumption flagged upfront: Hypothesis - Guntur May surge could be due to bulk high-value orders causing order-mix skew, not verified, labeled explicitly as hypothesis in memo.md Assumptions field, needs verification by pulling Guntur May order_id distribution by EOD tomorrow - pulled directly from memo.md Assumptions field.

## Acceptance Criteria
- April->May flags: Hyderabad, Warangal, Visakhapatnam, Guntur, Tirupati, Karimnagar, Bengaluru (7 regions)
- May->June flags: Hyderabad, Warangal, Vijayawada, Visakhapatnam, Guntur, Tirupati, Karimnagar (7 regions)
- Union 8 unique, Nellore never flagged stable
- Guntur April->May +122.19% largest
- LEFT JOIN 2101 vs INNER 2100 delta Kurnool documented
- COUNT DISTINCT order_id not raw row count for KPI
