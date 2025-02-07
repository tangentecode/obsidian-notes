# Connecting-to-database

- There are a few basic functions for managing the database:

```python
conn = sqlite3.connect("example.db") # Creates or connects to the database 

cursor = conn.cursor() # Establishing a cursor 

# Execute querys here:

# e.g. cursor.execute("SELECT * FROM users")

conn.commit()  # Save changes
conn.close()  # Closing connection
```
