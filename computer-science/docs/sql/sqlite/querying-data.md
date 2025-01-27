- To print out the result of your [executed query](executing-queries.md) you need to use the `.fetchall()` method
- Optionally you can print it row by row

```python

conn = sqlite3.connect("example.db") # Connecting to a database
cursor = conn.cursor() # Establishing a cursor
conn.commit()  # Save changes
conn.close()  # Closing connection
```
