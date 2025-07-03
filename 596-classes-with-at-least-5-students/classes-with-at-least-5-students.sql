# Write your MySQL query statement below

WITH cte AS (
    SELECT class, COUNT(student) cnt
    FROM Courses
    GROUP BY class
)

SELECT class
FROM cte
WHERE cnt >= 5
