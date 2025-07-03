# Write your MySQL query statement below

WITH cte AS (
    SELECT managerId, COUNT(managerId) cnt
    FROM Employee
    GROUP BY managerId
)

SELECT E.name
FROM Employee E
JOIN cte C ON C.managerId = E.id
WHERE C.cnt >= 5
