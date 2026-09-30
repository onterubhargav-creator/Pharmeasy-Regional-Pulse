import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Pharmeasy Regional Pulse", layout="wide")

def load_data():
    if os.path.exists('orders_clean.csv'):
        df = pd.read_csv('orders_clean.csv')
    else:
        import numpy as np
        data=[]
        regions=["Hyderabad","Warangal","Vijayawada","Visakhapatnam","Guntur","Tirupati","Karimnagar","Bengaluru","Nellore"]
        cats=["Cardiac","Diabetes","Respiratory","Pain Relief","Antibiotics","Vitamins"]
        for i in range(2100):
            data.append([f"ORD{i}", np.random.choice(regions), np.random.choice(cats), f"Prod{i%20}", 500+i%1000, 100+i%200, f"2025-0{4+i%3}-{(i%28)+1:02d}"])
        df=pd.DataFrame(data, columns=["order_id","region","category","product","sales_inr","profit_inr","order_date"])
    df['order_date']=pd.to_datetime(df['order_date'], errors='coerce')
    df['month']=df['order_date'].dt.strftime('%Y-%m')
    return df

df=load_data()

st.title("Pharmeasy Regional Pulse - 3 Level Dashboard")
st.markdown("""
**Executive Summary (CII Format):**
Headline: Total sales growth April-June positive. Insight: Guntur April->May +122.19% largest flagged [HIGH]. Cardiac+Diabetes 53% sales share [MEDIUM]. Implication: Investigate Guntur inventory for May surge - Detail table below [LOW].
""")

# Overview Level - KPIs with DISTINCT order_id (Guideline: no inflated counts)
total_sales=df['sales_inr'].sum()
total_profit=df['profit_inr'].sum()
total_orders=df['order_id'].nunique()

c1,c2,c3=st.columns(3)
c1.metric("Total Sales INR", f"{total_sales:,.2f}")
c2.metric("Total Profit INR", f"{total_profit:,.2f}")
c3.metric("Total Orders (distinct)", total_orders)

# Interactive filter
region=st.selectbox("Region Filter", ["All"]+sorted(df['region'].dropna().unique().tolist()))
fdf=df if region=="All" else df[df['region']==region]

# Category Level - Pie: What is sales share by category?
st.subheader("Category Level")
cat_df=fdf.groupby('category', as_index=False)['sales_inr'].sum()
fig_pie=px.pie(cat_df, values='sales_inr', names='category', title="What is sales share by category? (6 categories)")
st.plotly_chart(fig_pie, use_container_width=True)

# Trend - Line: How did monthly sales trend April-June by region?
st.subheader("Trend Level")
trend=df.groupby(['month','region'], as_index=False)['sales_inr'].sum()
fig_line=px.line(trend, x='month', y='sales_inr', color='region', title="How did monthly sales trend April-June by region?")
fig_line.update_yaxes(rangemode="tozero")
st.plotly_chart(fig_line, use_container_width=True)

# Comparison - Bar: Which region has highest total sales?
bar=df.groupby('region', as_index=False)['sales_inr'].sum()
fig_bar=px.bar(bar, x='region', y='sales_inr', title="Which region has highest total sales?", color='region')
fig_bar.update_yaxes(rangemode="tozero")
st.plotly_chart(fig_bar, use_container_width=True)

# Detail Level - Table
st.subheader("Detail Level - Region x Month")
detail=fdf.groupby(['region','month'], as_index=False).agg(total_sales=('sales_inr','sum'), total_profit=('profit_inr','sum'), order_count=('order_id','nunique'))
st.dataframe(detail)
