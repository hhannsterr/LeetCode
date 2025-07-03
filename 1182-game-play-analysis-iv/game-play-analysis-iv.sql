# Write your MySQL query statement below

WITH cte AS (
    SELECT player_id, MIN(event_date) first_day
    FROM Activity
    GROUP BY player_id
)

SELECT ROUND((
    SELECT COUNT(*)
    FROM Activity A
    JOIN cte C ON A.player_id = C.player_id
    WHERE event_date = DATE_ADD(C.first_day, INTERVAL 1 DAY)
) / COUNT(DISTINCT player_id), 2) fraction
FROM Activity
