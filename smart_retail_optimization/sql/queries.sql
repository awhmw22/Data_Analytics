--Top 10 Products by Profit
SELECT
  p.product_id,
  p.name,
  p.category,
  SUM((p.price - p.cost) * s.quantity) AS total_profit
FROM "Clean_Sales" s
JOIN "Clean_Products" p ON s.product_id = p.product_id
GROUP BY p.product_id, p.name, p.category
ORDER BY total_profit DESC
LIMIT 10;

--Monthly Sales Trend
SELECT
  DATE_TRUNC('month', s.date::timestamp) AS month,
  SUM(s.quantity * p.price)    AS revenue,
  SUM((p.price - p.cost) * s.quantity) AS profit
FROM "Clean_Sales" s
JOIN "Clean_Products" p ON s.product_id = p.product_id
GROUP BY 1
ORDER BY 1;

--Customer Lifetime Value (Total Spend per Customer)
SELECT
  c.customer_id,
  c.name,
  COUNT(*)            AS orders_count,
  SUM(s.quantity * p.price) AS total_spent
FROM "Clean_Sales" s
JOIN "Clean_Customers" c  ON s.customer_id = c.customer_id
JOIN "Clean_Products" p   ON s.product_id  = p.product_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC
LIMIT 20;

--Orders per Customer Distribution
SELECT
  orders_count,
  COUNT(*) AS customer_count
FROM (
  SELECT
    customer_id,
    COUNT(*) AS orders_count
  FROM "Clean_Sales"
  GROUP BY customer_id
) AS t
GROUP BY orders_count
ORDER BY orders_count;

--Inventory Turnover Ratio by Category
WITH category_sales AS (
  SELECT
    p.category,
    SUM(s.quantity * p.cost) AS cost_of_goods_sold
  FROM "Clean_Sales" s
  JOIN "Clean_Products" p ON s.product_id = p.product_id
  GROUP BY p.category
),
category_inventory AS (
  SELECT
    p.category,
    SUM(i.stock_level * p.cost) AS avg_inventory_value
  FROM "Clean_Inventory" i
  JOIN "Clean_Products" p ON i.product_id = p.product_id
  GROUP BY p.category
)
SELECT
  cs.category,
  cs.cost_of_goods_sold / ci.avg_inventory_value AS inventory_turnover_ratio
FROM category_sales cs
JOIN category_inventory ci USING (category)
ORDER BY inventory_turnover_ratio DESC;

--Products Near Reorder Point
WITH recent_sales AS (
  SELECT
    product_id,
    SUM(quantity) AS sold_last_3m
  FROM "Clean_Sales"
  WHERE date::date >= (CURRENT_DATE - INTERVAL '3 months')
  GROUP BY product_id
)
SELECT
  p.product_id,
  p.name,
  i.stock_level,
  (sold_last_3m / 3.0)   AS avg_monthly_sales,
  i.stock_level <= (sold_last_3m / 3.0) AS needs_reorder
FROM "Clean_Inventory" i
JOIN recent_sales rs  ON i.product_id = rs.product_id
JOIN "Clean_Products" p       ON i.product_id = p.product_id
ORDER BY needs_reorder DESC, avg_monthly_sales DESC;