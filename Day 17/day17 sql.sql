-- select c.categoryname, avg(price), sum(price)from categories as c join 
use RetailProductDB;
 select * from categories;
 select * from products;
 
select c.categoryname, c.categoryid, avg(p.price) 
from categories c
join products p
on c.categoryid = p.categoryid
group by c.categoryname, c.categoryid
having avg(p.price) > 10000
order by avg(p.price);

select brand ,count(productId) from products group by brand order by count(productId) desc;
 
-- Display brands whose total inventory value exceeds ₹2,00,000.
select brand, sum(price) from products group by brand having sum(price) > 20000;

-- Display categories having more than three products and an average price greater than ₹5,000.
select c.categoryname, count(p.productId), avg(p.price) 
from categories c
join products p
on c.categoryid = p.categoryid
group by categoryname 
having count(p.productid) > 3 and avg(p.price) > 5000;

-- Find brands where the total sold quantity is greater than the total stock quantity.
select * from products;
select brand, sum(soldquantity), sum(stockquantity) 
from products 
group by brand
having sum(soldquantity) > sum(stockquantity);

-- Display categories where the difference between maximum and minimum product prices exceeds ₹20,000.
select * from categories;
select * from products;
select c.categoryname, max(p.price), min(p.price)
from categories c
join products p
on c.categoryid = p.categoryid
group by c.categoryname
having (max(p.price) - min(p.price) > 20000);

-- Display each category and brand combination with total products, average price and total revenue.
select 
	c.categoryname, count(p.productname), 
    avg(p.price),
    sum(p.soldquantity) as sold_quantity,
    sum(p.price) as total_price, 
    sum(p.soldquantity)* sum(p.price) as Revenue
from  categories c
join products p
on c.categoryid = p.categoryid
group by c.categoryname;

select * from products;
select * from categories;

-- Find categories having total stock greater than 100 and total sales revenue greater than ₹3,00,000.
select 
	c.categoryname,
    sum(p.stockquantity) as total_stock,
    sum(p.soldquantity)* sum(p.price) as Revenue
from  categories c
join products p
on c.categoryid = p.categoryid
group by c.categoryname
having sum(p.stockquantity) > 100 and sum(p.soldquantity)* sum(p.price) > 300000;

select * from products; 


-- Display brands having a minimum product price greater than ₹1,000 and a maximum product price greater than ₹20,000.
select * from products where brand = 'Dell';
select brand, min(price) as min_price, max(price) as max_price
from products 
group by brand
having min(price) > 1000 and max(price) > 20000;