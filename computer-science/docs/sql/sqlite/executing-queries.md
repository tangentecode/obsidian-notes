- Use `.execute()` on an open cursor with an SQL Query as parameter:

```python
cursor.execute('SELECT * FROM users')
```

- To pass in data if your [inserting](insert.md) use this syntax:
```python
cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', ('Alice', 'alice@example.com'))
```

- The **?** represent placeholders for the data in the second parameter of the `.exe`
