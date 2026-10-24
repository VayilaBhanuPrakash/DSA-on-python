# Write your MySQL query statement below
with cumulative_weights as
(select person_id,person_name,weight,turn,(select sum(weight) from Queue q1 where q1.turn <= q2.turn) as cumulative from Queue q2 order by q2.turn)

select person_name from cumulative_weights where cumulative <= 1000 order by cumulative desc limit 1;