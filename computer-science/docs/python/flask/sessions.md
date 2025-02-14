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
- For example items stored in their shopping cart so that when their browser reastarts the items are s