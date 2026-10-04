# Data Quality Report - 7 Dimensions

Uniqueness: Found 59 duplicate order_id, removed via drop_duplicates -> 2159 to 2100 rows.
Consistency: Region had 16 messy variants like 'Guntur-',' guntur ', normalized to 9 canonical via strip().rstrip('-').title().
Completeness+Validity: 48 missing category imputed via product->category deterministic lookup.
Accuracy+Completeness: 94 missing profit_inr imputed via category_mean_margin = mean(profit/sales), profit=round(sales*margin,2).
Timeliness: Apr-Jun 2026 data, cleaned immediately same pipeline.
Relevance: Kept only 8 required cols order_id,order_date,region,product,category,sales_inr,profit_inr,quantity.

At least 4 dimensions mapped as required.
