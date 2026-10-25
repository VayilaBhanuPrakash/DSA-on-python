# Write your MySQL query statement below
with AmountPerWeek as
(select distinct c1.visited_on, 
(select sum(c2.amount) from Customer c2 
where c2.visited_on <= c1.visited_on 
and c2.visited_on >= date_sub(c1.visited_on, interval 6 day)) 
as amount
from Customer c1)

select visited_on, amount, round((amount / 7), 2) as average_amount 
from AmountPerWeek 
where visited_on >= (select date_add(min(visited_on), interval 6 day)
from Customer);
