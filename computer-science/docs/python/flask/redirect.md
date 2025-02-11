# Redirect

- Use `redirect()` with and a [app route](routes.md) to send the client to another web page
```python
from flask import Flask, redirect

@app.route("/")
def index():
	return redirect("/greet")

@app.route("/greet")
def gree
```

> `redirect()` needs to be imported