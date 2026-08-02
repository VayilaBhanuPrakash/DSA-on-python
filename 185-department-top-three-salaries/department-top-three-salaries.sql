# Write your MySQL query statement below
select Department.name as Department,
Employee.name as Employee,
Employee.salary as Salary 
from Employee left join Department
on Employee.departmentId = Department.id

where (select count(distinct e.salary) from Employee e where Employee.departmentId = e.departmentId and e.salary > Employee.salary
) < 3;
