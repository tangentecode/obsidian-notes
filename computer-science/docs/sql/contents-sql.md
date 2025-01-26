1. [basics](computer-science/docs/sql/basics.md)
2. [select](select.md)
3. [update](update.md)
4. [insert](insert.md)
5. [delete](delete.md)


- **Purpose**: Filters out duplicate values and returns unique values in a column.
- **Example**:
		
		```sql

		SELECT DISTINCT department

		FROM employees;

		```c
		

- **Output**: Returns a list of unique departments.

### 4. **LOWER**

- **Purpose**: Converts a string to lowercase.
- **Example**:
		
		```sql

		SELECT LOWER(name) AS lowercase_name

		FROM employees;

		```c
		

- **Output**: Returns all names in lowercase.

### 5. **MAX**

- **Purpose**: Finds the maximum (largest) value in a column.
- **Example**:
		
		```sql

		SELECT MAX(salary) AS highest_salary

		FROM employees;

		```c
		

- **Output**: Returns the highest salary in the `salary` column.

### 6. **MIN**

- **Purpose**: Finds the minimum (smallest) value in a column.
- **Example**:
		
		```sql

		SELECT MIN(salary) AS lowest_salary

		FROM employees;

		```c
		

- **Output**: Returns the lowest salary in the `salary` column.

### 7. **UPPER**

- **Purpose**: Converts a string to uppercase.
- **Example**:
		
		```sql

		SELECT UPPER(name) AS uppercase_name

		FROM employees;

		```c
		

- **Output**: Returns all names in uppercase.

These keywords are widely used in SQL for data analysis and transformation tasks.
