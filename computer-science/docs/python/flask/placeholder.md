
- Define a **placeholder** in your [HTML](contents-html.md) code:
```html
<!DOCTYPE html>

<html lang="en">

    <head>
        <meta name="viewport" content="initial-scale=1, width=device-width">
        <title>hello</title>
    </head>

    <body>
        hello, {{ name }}
    </body>

</html>
  
```

- Set the value for the placeholder
```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	name1 = "Bob"
	return render_template("index.html", name=name1) # Placeholder 'name' equals the variable 'name1'
```

- Retrieve value
```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	name = request.args.get("name")
	return render_template()
```

> How to use [`.get()`](computer-science/docs/python/dictionaries.md)
