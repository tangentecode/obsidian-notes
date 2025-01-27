- **Purpose:** Searches for patterns in string data using wildcard characters.
		- `%` matches zero or more characters.
		- `_` matches exactly one character.
- **Use:** Commonly used in `WHERE` clauses.

- **Example:**

```sql
SELECT * FROM customers WHERE name LIKE 'A%';
```

_Finds customers whose names start with 'A'._
