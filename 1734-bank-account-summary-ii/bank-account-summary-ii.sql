# Write your MySQL query statement below
select sum(t.amount) as balance,u.name as NAME 
from Transactions t join Users u on t.account = u.account
group by t.account having sum(t.amount) > 10000;
