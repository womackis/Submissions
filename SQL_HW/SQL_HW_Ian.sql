USE sakila;

-- 1A: Display first and last names of actors in table 'actor'
SELECT first_name, last_name FROM actor;

-- 1B: Display first and last name of each actor in single column
SELECT CONCAT(first_name, ' ', last_name) AS 'Actor Name'
FROM actor;

-- 2A: Find ID, first name, last name with first name "Joe"
SELECT actor_id, first_name, last_name FROM actor
WHERE first_name = 'Joe'; 

-- 2B: Find actors whoe last name contains 'GEN'
SELECT * FROM actor
WHERE last_name LIKE '%GEN%';

-- 2C: Find actors whose last names contain 'LI', order by last name, first name
SELECT * FROM actor
WHERE last_name LIKE '%LI%'
ORDER BY last_name, first_name;

-- 2D: Display 'country id' and 'country' from Afghanistan, Bangladesh, and Chine
SELECT country_id, country FROM country
WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

-- 3A: Add 'middle_name' column to table actor after 'first_name'
ALTER TABLE actor
ADD middle_name VARCHAR(30) 
AFTER first_name;

SELECT * FROM actor;

-- 3B: Change Datatype of middle_name to to 'blobs'
ALTER TABLE actor
MODIFY middle_name BLOB;

-- 3C: Delete middle_name column
ALTER TABLE actor

DROP middle_name;

SELECT * FROM actor;

-- 4A: List actors and count by last name
SELECT last_name, count(last_name) as 'count' FROM actor
GROUP BY last_name;

-- 4B: List actors and count by lsast name but only if shared by at least 2 actors
SELECT last_name, count(last_name) as 'count' FROM actor
GROUP BY last_name
HAVING count >= 2;

-- 4C: Fix name of actor Groucho Williams to Harpo Williams
SET SQL_SAFE_UPDATES=0;

UPDATE actor
SET first_name = 'HARPO'
WHERE first_name = 'GROUCHO'AND last_name='WILLIAMS';

SELECT * from actor
WHERE first_name = 'HARPO' AND last_name = 'WILLIAMS';

-- 4D: Change name back to Groucho AND 
SET SQL_SAFE_UPDATES=0;

UPDATE actor
SET first_name = 'GROUCHO'
WHERE actor_id = 172 AND first_name = 'HARPO';

SELECT * FROM actor
WHERE last_name = 'WILLIAMS';

UPDATE actor
SET first_name = 'MUCHO GROUCHO'
WHERE actor_id = 172 AND first_name != 'HARPO';

SELECT * FROM actor
WHERE last_name = 'WILLIAMS';

-- 5A: Recreate schema of address table
CREATE schema address;


-- 6A: Use 'JOIN' to display first and last names, address of each staff member
SELECT first_name, last_name, address
FROM staff s
INNER JOIN address a
ON s.address_id = a.address_id;

-- 6B: Use 'JOIN' to display total amount rung up by each staff member in Aug 2005
SELECT first_name,last_name,SUM(amount) as total
FROM payment p
INNER JOIN staff s
ON s.staff_id = p.staff_id
WHERE payment_date LIKE '2005-08%'
GROUP BY first_name,last_name;


-- 6C: List each film and # of actors listed for film
SELECT title, COUNT(actor_id) AS 'actor count'
FROM film f
INNER JOIN film_actor fa
ON f.film_id = fa.film_id
GROUP BY title;


-- 6D: How many copies of "Hunchback Impossible" exist in inventory?
SELECT title, count(i.film_id) as 'inventory count'
FROM inventory i
INNER JOIN film_text ft
ON i.film_id = ft.film_id
WHERE title = 'Hunchback Impossible'
group by title;

-- 6E: List total paid by each customer, ordered alphabetically by last name
SELECT first_name, last_name, sum(amount)
FROM customer c
INNER JOIN payment p
ON c.customer_id = p.customer_id
group by first_name, last_name
order by last_name;

-- 7a: Use subqueries to diplay titles of English movies starting with letters 'K' and 'Q'
SELECT * FROM film;
SELECT * FROM language;


SELECT title
FROM film
WHERE title like 'K%' OR title like'Q%'
AND language_id IN (
	SELECT language_id FROM language
    WHERE name = 'English'
    );
    
    
-- 7b: Use subqueries to display all actors who appear in 'Alone Trip'
SELECT first_name, last_name
FROM actor
WHERE actor_id IN (
	SELECT actor_id FROM film_actor
	WHERE film_id IN (
		SELECT film_id FROM film 
		WHERE title ='Alone Trip'
		)
	);
    

-- 7c: Retrieve names and emails of all Canadians customers
SELECT first_name, last_name, email from customer
where address_id IN(
	SELECT address_id
    FROM address
    WHERE city_id IN(
		SELECT city_id
        FROM city
        WHERE country_id IN(
			SELECT country_id
            FROM country
            WHERE country = 'Canada'
            )
		)
	);


-- 7d: Identify all movies categorized as family films
SELECT title from film
WHERE film_id IN (
	SELECT film_id
	FROM film_category
	WHERE category_id IN (
		SELECT category_id
        FROM category
        WHERE name = 'Family'
        )
	);
    
-- 7e: Display most frequently rented movies in descending order
SELECT title, count(title) as count
FROM film f
INNER JOIN inventory i
ON f.film_id = i.film_id
INNER JOIN rental r
ON i.inventory_id = r.inventory_id
GROUP BY title
ORDER BY count desc;
 

-- 7f: Display business per store
SELECT store_id,sum(amount) as amount
FROM payment p
INNER JOIN staff s
ON p.staff_id = s.staff_id
group by store_id;

-- 7g: Display each store ID, city, and country
SELECT store_id, city, country
FROM store s
INNER JOIN address a
ON s.address_id = a.address_id
INNER JOIN city
ON a.city_id = city.city_id
INNER JOIN country
ON city.country_id = country.country_id;

-- 7h: List top 5 genres in gross revenue in descending order
SELECT name as 'genres', sum(amount) as 'gross revenue'
FROM category c
INNER JOIN film_category fc
ON c.category_id = fc.category_id
INNER JOIN inventory i
ON fc.film_id = i.film_id
INNER JOIN rental r
ON i.inventory_id = r.inventory_id
INNER JOIN payment p
ON r.rental_id = p.rental_id
group by name
ORDER BY name desc
limit 5;

-- 8a: Create view from 7h
CREATE VIEW top_5_genres AS

SELECT name as 'genres', sum(amount) as 'gross revenue'
FROM category c
INNER JOIN film_category fc
ON c.category_id = fc.category_id
INNER JOIN inventory i
ON fc.film_id = i.film_id
INNER JOIN rental r
ON i.inventory_id = r.inventory_id
INNER JOIN payment p
ON r.rental_id = p.rental_id
group by name
ORDER BY name desc
limit 5;

-- 8b: Display view from 8a
SELECT * FROM top_5_genres;

-- 8c: Drop view 'top_five_genres'
DROP VIEW to_5_genres;