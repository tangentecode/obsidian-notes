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