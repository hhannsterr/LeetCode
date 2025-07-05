# Write your MySQL query statement below

WITH cte AS (
    SELECT product_id, SUM(unit) unit
    FROM Orders
    WHERE order_date >= '2020-02-01' AND order_date <= '2020-02-29'
    GROUP BY product_id
)

SELECT p.product_name, c.unit
FROM Products p
INNER JOIN cte c ON p.product_id = c.product_id
WHERE c.unit >= 100
