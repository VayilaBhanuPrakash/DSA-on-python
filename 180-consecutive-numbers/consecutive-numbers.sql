# Write your MySQL query statement below
with Consecutive as
(select num, lag(num) over(order by id) as Prev, lead(num) over(order by id) as Next from Logs)
select distinct num as ConsecutiveNums from Consecutive where num = Prev and num = Next;