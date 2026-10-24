# Write your MySQL query statement below
with first_login as
(select player_id, min(event_date) as first from Activity group by player_id)
select round((sum(case when a.event_date = DATE_ADD(f.first, INTERVAL 1 DAY) then 1 else 0 end)/count(distinct f.player_id)),2) as fraction from Activity a left join first_login f on a.player_id = f.player_id;
