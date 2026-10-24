# Write your MySQL query statement below
with deliveries as (select customer_id,min(order_date) as order_date,min(customer_pref_delivery_date) as delivery_date from Delivery group by customer_id)
select round((sum(case when order_date = delivery_date then 1 else 0 end)/count(*)) * 100,2) as immediate_percentage from deliveries;
