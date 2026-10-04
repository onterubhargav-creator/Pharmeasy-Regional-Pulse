import sqlite3
conn = sqlite3.connect("pharmeasy.db")
print("Task 2.2 JOIN Validation")
print(conn.execute("SELECT COUNT(*) FROM regions_master").fetchone()) # 10
print(conn.execute("SELECT COUNT(*) FROM orders_clean").fetchone()) # 2100
print("LEFT JOIN count:", conn.execute("SELECT COUNT(*) FROM regions_master r LEFT JOIN orders_clean o ON r.region=o.region").fetchone())
print("INNER JOIN count:", conn.execute("SELECT COUNT(*) FROM regions_master r INNER JOIN orders_clean o ON r.region=o.region").fetchone())
print("Duplicate order_id check:", conn.execute("SELECT order_id, COUNT(*) c FROM orders_clean GROUP BY order_id HAVING c>1").fetchall())
print("COUNT(*) vs COUNT(o.order_id) for Kurnool pitfall:")
print(conn.execute("SELECT r.region, COUNT(*) as cnt_star, COUNT(o.order_id) as cnt_order FROM regions_master r LEFT JOIN orders_clean o ON r.region=o.region GROUP BY r.region").fetchall())
print("Task 2.3 Metrics SQL:")
for row in conn.execute("SELECT region, strftime('%Y-%m',order_date) as month, SUM(sales_inr) as total FROM orders_clean GROUP BY region, month ORDER BY region, month"):
    print(row)
