# Guntur +122.19% Presentation Storyline

## 1. For an executive (Situation-Complication-Resolution)
Situation: PharmEasy 9 active regions total sales from 2100 distinct orders Apr-Jun 2026 stable.
Complication: Guntur +122.19% Apr->May surge largest among 8 unique flagged regions >8% threshold, at-risk of over-interpretation.
Resolution: Recommend review May order-mix, verify no duplication, monitor next month via save_state_v1.

## 2. For a regional manager (Overview-Category-Detail)
Overview: Guntur Apr->May +122.19% computed (May-Apr)/Apr*100 from pharmeasy.db.
Category: 6 medicine categories drive sales, Guntur surge driven by specific categories visible in bar/pie (pie capped 6 slices).
Detail: Evidence from orders_clean 2100 rows, per-region per-month table, methodology LEFT JOIN regions_master 10 rows, COUNT DISTINCT order_id, trend line chart monthly with axis starts at zero no 3D labeled axes INR.

## Q&A Direct Acknowledgement Pattern
Q1 Why should I believe +122.19%? Acknowledge valid concern large swing. Verified via Part2 SQL SUM GROUP BY traceable, Not verified whether bulk orders cause. Resolve by pulling order_id distribution by EOD tomorrow.
Q2 What if alternative explanation? Acknowledge order-mix variation can cause 8%+ with few dozen orders. Verified flag is operational-alert not statistical test fixed 8%. Not verified external market. Resolve compare category share vs other regions and rerun load_previous_state_v1 by EOD tomorrow.
