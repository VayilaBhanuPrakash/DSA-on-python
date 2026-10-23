# Write your MySQL query statement below
(select u.name as results from MovieRating m left join Users u on m.user_id = u.user_id group by u.user_id,u.name order by count(*) desc,u.name asc limit 1)
union all
(select mo.title as results from MovieRating m left join Movies mo on m.movie_id = mo.movie_id where m.created_at >= '2020-02-01' and m.created_at < '2020-03-01' group by mo.movie_id,mo.title order by avg(m.rating) desc,mo.title asc limit 1);