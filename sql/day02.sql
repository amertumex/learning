-- SELECT DISTINCT rating
-- FROM film;

-- select film.title
-- from film
-- where rating = 'PG' and length < 90;

-- select film.title
-- from film
-- where title LIKE 'A%';

-- select rating, count(*)
-- from film
-- group by rating;

-- select AVG(length) as "Avg film time"
-- from film;

-- select customer.customer_id, first_name, last_name,
--        SUM(amount) as "Total purchase",
--        count(payment_id) as "Count payment"
-- from payment
-- join customer on payment.customer_id = customer.customer_id
-- group by customer.customer_id, first_name, last_name
-- order by "Total purchase" desc
-- limit 5;

-- select rating,
--        count(film_id),
--        avg(length) as "Average film length"
-- from film
-- group by rating
-- having (avg(length)) > (select avg(length)
--     from film)

-- select name, count(film_category.film_id) as "Count films"
-- from category
-- join film_category on category.category_id = film_category.category_id
-- group by name
-- order by "Count films" desc
-- limit 5;