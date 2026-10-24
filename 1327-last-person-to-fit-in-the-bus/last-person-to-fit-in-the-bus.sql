# Write your MySQL query statement below
with Bus as
(select person_id,person_name,weight,turn,(select sum(weight) from Queue q1 where q1.turn <= q2.turn) as cumulative_weight from Queue q2)

select person_name from Bus where cumulative_weight <= 1000 order by cumulative_weight desc limit 1;