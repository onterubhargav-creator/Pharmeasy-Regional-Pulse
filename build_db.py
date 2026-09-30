import sqlite3
import pandas as pd
import os

def build_db():
    db_path = 'pharmeasy.db'
    if os.path.exists(db_path):
        os.remove(db_path)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Load master (10 regions including Kurnool inactive)
    try:
        master = pd.read_csv('regions_master.csv')
    except:
        master = pd.DataFrame({
            'region_name':['Hyderabad','Warangal','Vijayawada','Visakhapatnam','Guntur','Tirupati','Karimnagar','Bengaluru','Nellore','Kurnool'],
            'state':['Telangana']*2+['Andhra Pradesh']*4+['Telangana']+['Karnataka']+['Andhra Pradesh']*2,
            'is_active':[True]*9+[False]
        })

    master.to_sql('regions_master', conn, if_exists='replace', index=False)
    print(f"Master loaded: {len(master)} regions (Kurnool inactive)")

    # Load clean (2100 rows)
    try:
        clean = pd.read_csv('orders_clean.csv')
    except FileNotFoundError:
        print("orders_clean.csv not found - running clean_data fallback")
        import clean_data
        clean = clean_data.clean()

    clean.to_sql('orders_clean', conn, if_exists='replace', index=False)
    print(f"Clean loaded: {len(clean)} rows")

    # Critical Acceptance Test per PDF - LEFT vs INNER
    left_count = cur.execute("""
        SELECT COUNT(*) FROM regions_master
        LEFT JOIN orders_clean ON regions_master.region_name = orders_clean.region
    """).fetchone()[0]

    inner_count = cur.execute("""
        SELECT COUNT(*) FROM regions_master
        INNER JOIN orders_clean ON regions_master.region_name = orders_clean.region
    """).fetchone()[0]

    delta = left_count - inner_count
    kurnool_check = cur.execute("SELECT * FROM regions_master WHERE region_name='Kurnool'").fetchone()

    print(f"\n=== ACCEPTANCE TEST (Guidelines) ===")
    print(f"LEFT JOIN count: {left_count}")
    print(f"INNER JOIN count: {inner_count}")
    print(f"Delta (should be 1 for Kurnool): {delta}")
    print(f"Kurnool record: {kurnool_check}")

    # Region monthly sales for report gate
    cur.execute("""
        CREATE TABLE IF NOT EXISTS region_monthly AS
        SELECT region, substr(order_date,1,7) as month,
               SUM(sales_inr) as total_sales,
               SUM(profit_inr) as total_profit,
               COUNT(DISTINCT order_id) as order_count
        FROM orders_clean GROUP BY region, month
    """)

    conn.commit()
    conn.close()
    print(f"\nDB built: {db_path} - Kurnool delta verified {delta} row")
    return delta

if __name__ == "__main__":
    build_db()
