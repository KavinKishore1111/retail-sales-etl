-- Top Selling Products
SELECT product_id, SUM(sale_amount) AS total_sales
FROM sales
GROUP BY product_id
ORDER BY total_sales DESC;

-- Weekly Sales Trends
SELECT DATE_TRUNC('week', sale_date) AS week, SUM(sale_amount) AS weekly_sales
FROM sales
GROUP BY week
ORDER BY week;

-- Customer Lifetime Value
SELECT customer_id, SUM(sale_amount) AS CLV
FROM sales
GROUP BY customer_id
ORDER BY CLV DESC;

