- **Purpose:** Groups rows that have the same values in specified columns, often used with aggregate functions like `SUM`, `COUNT`, `AVG`, etc.
- **Use:** Comes after `WHERE` and before `ORDER BY`.

- **Example:**
```sql
SELECT department, COUNT(*) AS employee_count FROM employees GROUP BY department;
```