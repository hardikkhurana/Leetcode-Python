# Write your MySQL query statement below
#SELECT FirstName, LastName, City, State
#FROM Person
#NATURAL LEFT JOIN Address;

SELECT FirstName, LastName, City, State
FROM Person
LEFT JOIN Address
ON Person.personid=address.personid;