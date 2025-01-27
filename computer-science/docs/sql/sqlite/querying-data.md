- To print out the result of your [executed query](executing-queries.md) you need to use the `.fetchall()` method
- Optionally you can print it row by row

```python
# Querying data
cursor.execute('SELECT * FROM users')
results = cursor.fetchall()  # Fetch all rows
for row in results:
    print(row)
```
