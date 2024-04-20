# Write your MySQL query statement below
SELECT prod.product_name, sales.year, sales.price
FROM Sales sales
JOIN Product prod ON sales.product_id = prod.product_id;