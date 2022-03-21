SELECT D.name as Department,E.name as Employee,E.Salary
From Employee as E
INNER JOIN Department as D
ON E.departmentid=D.id
Where E.salary=(SELECT max(salary) FROM Employee WHERE Employee.DepartmentId=D.Id);
