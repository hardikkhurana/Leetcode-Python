# Write your MySQL query statement below
SELECT class
FROM courses
GROUP BY class
HAVING Count(Student)>4;