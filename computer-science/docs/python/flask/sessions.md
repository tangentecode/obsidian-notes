- Requires new library `flask_session`
- Import like this:
```python
from flask_session import Session

# Configure app
app = Flask(__name__)

# Configure session
Session(app)
```

- A session is **user specific data** stored locally 
- For example items stored in their shopping cart so that when their browser restart the items are still there without pulling the data from a [database](contents-sql.md)

- Any type of data can be appended to the session
- Be sure to check whether the data already exist before accidently overwriting it

```python


```