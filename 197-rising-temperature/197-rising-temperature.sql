# Write your MySQL query statement below
SELECT a.id
FROM Weather AS a, Weather AS b
WHERE DATEDIFF(a.recordDate,b.recordDate)=1
AND a.temperature>b.temperature;
