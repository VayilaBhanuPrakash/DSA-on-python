# Write your MySQL query statement below
with activities as (select machine_id, process_id, max(timestamp)-min(timestamp) as time_taken from Activity group by machine_id,process_id)
select machine_id, round(avg(time_taken),3) as processing_time from activities group by machine_id;
