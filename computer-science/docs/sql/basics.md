- SQL is **Relational databases** which means **stores data in rows and columns** in structures called _tables_.
- Google, X, and Meta all use relational databases to store their information at scale.

- SQL is supports `CRUD` operations:
	1. **C**reate
	2. **R**ead
	3. **U**pdate
	4. **D**elete

	- Or in SQL specifically **C**reate is called INSERT









## [SELECT](https://cs50.harvard.edu/x/2025/notes/7/#select)

- For example, we can execute `SELECT COUNT(*) FROM favorites WHERE language = 'C';`. A count is presented.
- Further, we could type `SELECT COUNT(*) FROM favorites WHERE language = 'C' AND problem = 'Hello, World;`. Notice how the `AND` is utilized to narrow our results.
- Similarly, we could execute `SELECT language, COUNT(*) FROM favorites GROUP BY language;`. This would offer a temporary table that would show the language and count.
- We could improve this by typing `SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*);`. This will order the resulting table by the `count`.
- Likewise, we could execute `SELECT COUNT(*) FROM favorites WHERE language = 'C' AND (problem = 'Hello, World' OR problem = 'Hello, It''s Me');`. Do notice that there are two `''` marks as to allow the use of single quotes in a way that does not confuse SQL.
- Further, we could execute `SELECT COUNT(*) FROM favorites WHERE language = 'C' AND problem LIKE 'Hello, %';` to find any problems that start with `Hello,` (including a space).
- We can also group the values of each language by executing `SELECT language, COUNT(*) FROM favorites GROUP BY language;`.
- We can order the output as follows: `SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*) DESC;`.
- We can even create aliases, like variables in our queries: `SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC;`.
- Finally, we can limit our output to 1 or more values: `SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC LIMIT 1;`.

## [INSERT](https://cs50.harvard.edu/x/2025/notes/7/#insert)

- We can also `INSERT` into a SQL database utilizing the form `INSERT INTO table (column…) VALUES(value, …);`.
- We can execute `INSERT INTO favorites (language, problem) VALUES ('SQL', 'Fiftyville');`.
- You can verify the addition of this favorite by executing `SELECT * FROM favorites;`.

## [DELETE](https://cs50.harvard.edu/x/2025/notes/7/#delete)

- `DELETE` allows you to delete parts of your data. For example, you could `DELETE FROM favorites WHERE Timestamp IS NULL;`. This deletes any record where the `Timestamp` is `NULL`.

## [UPDATE](https://cs50.harvard.edu/x/2025/notes/7/#update)

- We can also utilize the `UPDATE` command to update your data.
- For example, you can execute `UPDATE favorites SET language = 'SQL', problem = 'Fiftyville';`. This will result in overwriting all previous statements where C and Scratch were the favorite programming language.
- Notice that these queries have immense power. Accordingly, in the real-world setting, you should consider who has permissions to execute certain commands and if you have backups available!
