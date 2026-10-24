# Write your MySQL query statement below
with minimum_year as
(select product_id, min(year) as first_year from Sales group by product_id)
select s.product_id,m.first_year,s.quantity,s.price from Sales s inner join minimum_year m on s.product_id = m.product_id where s.year = m.first_year;