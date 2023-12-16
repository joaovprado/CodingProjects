SELECT *
FROM sakila.film
WHERE film_id > 10;

SELECT * 
FROM sakila.film
WHERE film_id IN (SELECT film_id FROM sakila.film WHERE film_id > 10); # Nested query aplicada no WHERE
    
SELECT * 
FROM (SELECT * FROM sakila.film WHERE film_ID > 10) AS film_data; # Nested query aplicada no FROM, cria uma tabela "temporária" e precisamos aplicar um ALIAS a essa tabelatemporária

SELECT *
FROM sakila.film
WHERE film_id <= 10
UNION ALL
SELECT *
FROM sakila.film
WHERE film_id >= 10; # União com repetição dos itens presentes nas duas pesquisas

SELECT *
FROM sakila.film
WHERE film_id <= 10
UNION
SELECT *
FROM sakila.film
WHERE film_id >= 10; # União sem repetição dos itens presentes nas duas pesquisas


SELECT title, actor_id 
FROM sakila.film a
LEFT JOIN sakila.film_actor b # Traz todos os atores de cada um dos filmes da tabela A, se tiver algum ator, se não retorna filme com ator NULO
ON a.film_id = b.film_id;


SELECT title, actor_id 
FROM sakila.film a
INNER JOIN sakila.film_actor b # Traz todos os atores de cada um dos filmes da tabela A, apenas se tiver algum ator
ON a.film_id = b.film_id;


SELECT first_name, amount
FROM sakila.payment B
LEFT JOIN
(
	SELECT * FROM sakila.customer
) A
ON B.customer_id = A.customer_id;


SELECT first_name, amount
FROM 
(
	SELECT * FROM sakila.payment
) B
INNER JOIN
(
	SELECT * FROM sakila.customer
) A
ON B.customer_id = A.customer_id;

SELECT * FROM sakila.actor_info; # Isso é uma VIEW, que é uma query pronta, para facilidar o  uso