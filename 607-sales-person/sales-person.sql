# Write your MySQL query statement below

SELECT name
FROM SalesPerson S
WHERE sales_id NOT IN (
    SELECT sales_id id
    FROM Orders O
    JOIN Company C ON C.com_id = O.com_id
    WHERE C.name = 'RED'
)
