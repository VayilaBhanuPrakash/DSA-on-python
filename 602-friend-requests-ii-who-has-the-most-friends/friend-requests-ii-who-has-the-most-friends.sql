# Write your MySQL query statement below
with count as
(select requester_id as id,count(*) as num from RequestAccepted group by requester_id
union all
select accepter_id as id,count(*) as num from RequestAccepted group by accepter_id),
max_count as
(select id,sum(num) as num from count group by id)
select id,num from max_count where num = (select max(num) from max_count);


