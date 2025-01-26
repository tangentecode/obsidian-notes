- SQL is **Relational databases** which means **stores data in rows and columns** in structures called _tables_.
- Google, X, and Meta all use relational databases to store their information at scale.

- SQL is supports `CRUD` operations:
	1. **C**reate
	2. **R**ead
	3. **U**pdate
	4. **D**elete

- Or in SQL specifically **C**reate is called `INSERT`

- **SELECT**: Retrieves data from a database. It's the most commonly used operation for querying and displaying data.
    
    - Example: `SELECT * FROM employees;`
- **INSERT**: Adds new records to a table.
    
    - Example: `INSERT INTO employees (name, position) VALUES ('John Doe', 'Manager');`
- **UPDATE**: Modifies existing records in a table.
    
    - Example: `UPDATE employees SET position = 'Senior Manager' WHERE name = 'John Doe';`
- **DELETE**: Removes records from a table.
    
    - Example: `DELETE FROM employees WHERE name = 'John Doe';`