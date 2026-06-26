# Write your MySQL query statement below

select Department.name as Department,
Employee.name as Employee,
salary as Salary 
from Employee left join Department
on Employee.departmentId = Department.id
where Employee.salary = (
    select max(salary) from Employee where Employee.departmentId = Department.id
);