- **Purpose**: Counts the number of rows in a result set or non-NULL values in a column.

- **Example**:

```sql
SELECT COUNT(*) AS total_rows
FROM employees;
```

- **Output**: Returns the total number of rows.

- With a specific column:

```sql
SELECT COUNT(department) AS department_count
FROM employees;
```

- **Output**: Counts only non-NULL values in the `department` column.
