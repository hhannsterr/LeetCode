# Write your MySQL query statement below

-- SELECT D.name Department, E.name Employee, E.salary Salary
-- FROM Employee E
-- JOIN Department D ON D.id = E.departmentId
-- GROUP BY D.name
-- ORDER BY MAX(E.salary) DESC

WITH cte AS (
    SELECT departmentId, MAX(salary) max_salary
    FROM Employee
    GROUP BY departmentId
)

SELECT D.name Department, E.name Employee, E.salary Salary
FROM Employee E
JOIN cte C ON C.departmentId = E.departmentId
JOIN Department D ON D.id = E.departmentId
WHERE E.salary = C.max_salary

