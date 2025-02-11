# Redirect

- Use `redirect()` with and a [app route](routes.md) to send the client to another web page
```python
from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
	return redirect("/greet")

@app.route("/greet")
def greet():
	return "You have been redirected"
```

> `redirect()` needs to be imported