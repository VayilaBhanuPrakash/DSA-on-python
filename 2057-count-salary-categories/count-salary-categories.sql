# Write your MySQL query statement below
with Salary_Category as
(select (case when income < 20000 then 'Low Salary' when income <= 50000 then 'Average Salary' else 'High Salary' end) as category from Accounts)
select 'High Salary' as category, sum(category = 'High Salary') as accounts_count from Salary_Category
union all
select 'Low Salary', sum(category = 'Low Salary') from Salary_Category
union all
select 'Average Salary', sum(category = 'Average Salary') from Salary_Category;
