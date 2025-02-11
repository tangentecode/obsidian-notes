# Redirect

- Use `redirect()` with and a [app route](routes.md) to send the client to another web page
```python
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def index():

```

> `redirect()` needs to be imported