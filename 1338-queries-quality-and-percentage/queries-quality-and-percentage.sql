# Write your MySQL query statement below
with Query as 
(select query_name, rating, (rating / position) as quality
from Queries)
select query_name, round(avg(quality),2) as quality, 
round((sum(case when rating < 3 then 1 else 0 end) * 100) / count(*), 2) as poor_query_percentage from Query group by query_name;

