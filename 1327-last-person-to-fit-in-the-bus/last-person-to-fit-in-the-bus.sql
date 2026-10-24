# Write your MySQL query statement below
with Bus as
(select person_name, sum(weight) over(order by turn) as cumulative_weight from Queue)

select person_name from Bus where cumulative_weight <= 1000 order by cumulative_weight desc limit 1;