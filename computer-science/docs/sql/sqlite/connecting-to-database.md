```python
conn = sqlite3.connect('example.db') # Creates or connects to the database 
cursor = conn.cursor() # Establishing  a cursor 

conn.commit()  # Save changes
conn.close()  # Closing connection
```
