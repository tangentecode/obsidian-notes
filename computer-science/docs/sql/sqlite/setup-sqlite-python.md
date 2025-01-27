
1. **Install SQLite Module**: Built into Python (`sqlite3` module), so no installation required.
2. **Connecting to a Database**:
```python
import sqlite3

conn = sqlite3.connect('example.db') # Creates or connects to the database 
cursor = conn.cursor()

```