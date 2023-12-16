SELECT count(DISTRICT) as n_district, district
FROM sakila.address sak
GROUP BY District
order by n_district DESC;

#############################################################################################################

SELECT * 
FROM sakila.actor 
ORDER BY first_name, last_name DESC;

#############################################################################################################

SELECT * FROM sakila.actor WHERE first_name = 'ADAM';

#############################################################################################################

SELECT * FROM sakila.actor WHERE (first_name = 'ADAM' and last_name <> 'Grant') or last_name = "JOHANSSON";

#############################################################################################################

SELECT distinct last_name FROM sakila.actor;

#############################################################################################################

SELECT distinct first_name, last_name FROM sakila.actor;

#############################################################################################################

SELECT * FROM sakila.payment
WHERE amount > 1.00
AND amount < 6;

#############################################################################################################

SELECT max(amount), min(amount), avg(amount) as media, count(amount), sum(amount) as total
FROM sakila.payment
;

#############################################################################################################

SELECT customer_id, avg(amount) as media
FROM sakila.payment
GROUP BY customer_id
ORDER BY media DESC;

#############################################################################################################

SELECT COUNT(DISTINCT category_id)
FROM sakila.film_category;

#############################################################################################################

SELECT COUNT(DISTINCT category_id)
FROM sakila.film_category
WHERE category_id <> 1;

#############################################################################################################

CREATE TABLE sakila.ENDERECO(
	ID_estudante INTEGER,
    ENDERECO varchar(50)
);

#############################################################################################################

INSERT INTO sakila.ENDERECO (ID_estudante, ENDERECO)
VALUES (2, 'RUA EDGAR');

#############################################################################################################

SELECT * FROM sakila.endereco;