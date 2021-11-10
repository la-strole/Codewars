SELECT film.title
FROM film
INNER JOIN film_actor
ON film.film_id = film_actor.film_id
WHERE film_actor.actor_id=122
AND
film_actor.film_id IN
(SELECT film_actor.film_id
FROM film_actor
WHERE actor_id=105);