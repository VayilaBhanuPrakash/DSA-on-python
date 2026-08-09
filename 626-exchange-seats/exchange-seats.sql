# Write your MySQL query statement below
select id,
case 
when 
(mod(id,2) = 1  and (select student from Seat ss where ss.id = Seat.id + 1) is not null) 
then 
(select student from Seat s2 where s2.id = Seat.id + 1)
when 
mod(id,2) = 0 
then  
(select student from Seat s2 where s2.id = Seat.id - 1)
else 
(select student from Seat s where s.id = Seat.id)
end as student
from Seat;
