# Redirect

- Use `redirect()` with and a [app route](routes.md) to send the client to another web page
```python

@app.route("/")
def index():
	return redirect	
```

> `redirect()` needs to be imported