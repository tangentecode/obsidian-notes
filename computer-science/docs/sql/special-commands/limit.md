- **Purpose:** Restricts the number of rows returned by the query.
- **Use:** Typically paired with `ORDER BY` to fetch a specific subset of rows (e.g., top results).

- **Example:**

```sql
SELECT * FROM orders ORDER BY order_date DESC LIMIT 10;
```

Returns the 10 most recent orders.
