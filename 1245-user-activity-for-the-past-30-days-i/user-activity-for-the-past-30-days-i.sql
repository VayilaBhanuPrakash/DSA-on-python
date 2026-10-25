# Write your MySQL query statement below
with activities as
(select distinct activity_date,user_id from Activity)

select activity_date as day,count(*) as active_users 
from activities 
group by activity_date 
having activity_date between date_sub('2019-07-27',interval 29 day) and  '2019-07-27';
