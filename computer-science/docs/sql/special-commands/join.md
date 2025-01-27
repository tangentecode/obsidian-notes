- We are pulling data from `shows` and `ratings`. Notice how both `shows` and `ratings` have an `id` in common.
- How could we combine tables temporarily? Tables could be joined together using the `JOIN` command.
- Execute the following command:

```c
SELECT * FROM shows
JOIN ratings on shows.id = ratings.show_id
WHERE rating >= 6.0
LIMIT 10;
```

Notice this results in a wider table than we have previously seen.

- Where the previous queries have illustrated the _one-to-one_ relationship between these keys, let's examine some _one-to-many_ relationships. Focusing on the `genres` table, execute the following:

```sql
SELECT * FROM genres
LIMIT 10;
```

Notice how this provides us a sense of the raw data. You might notice that one show has three values. This is a one-to-many relationship.

- We can learn more about the `genres` table by typing `.schema genres`.
- Execute the following command to learn more about the various comedies in the database:

```sql
SELECT title FROM shows
WHERE id IN (
	SELECT show_id FROM genres
	WHERE genre = 'Comedy'
	LIMIT 10
);
```

Notice how this produces a list of comedies, including _Catweazle_.

- To learn more about Catweazle, by joining various tables through a join:

```sql
SELECT * FROM shows
JOIN genres
ON shows.id = genres.show_id
WHERE id = 63881;
```

Notice that this results in a temporary table. It is fine to have a duplicate table.

- In contrast to one-to-one and one-to-many relationships, there may be _many-to-many_ relationships.
- We can learn more about the show _The Office_ and the actors in that show by executing the following command:

```sql
SELECT name FROM people WHERE id IN 
	(SELECT person_id FROM stars WHERE show_id = 
		(SELECT id FROM shows WHERE title = 'The Office' AND year = 2005));
```

Notice that this results in a table that includes the names of various stars through nested queries.

- We find all the shows in which Steve Carell starred:

```sql
SELECT title FROM shows WHERE id IN 
	(SELECT show_id FROM stars WHERE person_id = 
		(SELECT id FROM people WHERE name = 'Steve Carell'));
```

This results in a list of titles of shows wherein Steve Carell starred.

- This could also be expressed in this way:

```sql
SELECT title FROM shows, stars, people 
WHERE shows.id = stars.show_id
AND people.id = stars.person_id
AND name = 'Steve Carell';
```

- The wildcard `%` operator can be used to find all people whose names start with `Steve C` one could employ the syntax `SELECT * FROM people WHERE name LIKE 'Steve C%';`.

> Explanation from [Havard CS50](https://cs50.harvard.edu/x/2025/notes/7/#joins)
