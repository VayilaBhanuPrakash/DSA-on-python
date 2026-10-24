# Write your MySQL query statement below
with max_date as
(select product_id,max(change_date) as last_date 
from Products 
where change_date <= '2019-08-16' group by product_id)

select p.product_id,p.new_price as price 
from Products p left join max_date m 
on p.product_id = m.product_id 
where p.change_date = m.last_date

union

select product_id,10 as price 
from Products
group by product_id 
having min(change_date) > '2019-08-16';

