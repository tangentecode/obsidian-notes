# Methods

- Flask can utilize different [http](contents-http.md) [methods](computer-science/docs/basics/http/methods.md)
- For example use `POST` to hide data in the the [url](url.md):

```python
@app.route("/greet", methods=["POST"])
def greet():
    return render_template("greet.html", name=request.form.get("name", "world"))
```

- Define one [route](routes.md) with multiple methods by changing the accordingly in the HTML code
- For example set the method of [form](forms.md) to POST:
- `index.html`

```html
{% extends "layout.html" %}

{% block body %}

    <form action="/" method="post">
        <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
        <button type="submit">Greet</button>
    </form>

{% endblock %}
```

- `app.py`

```python
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("greet.html", name=request.form.get("name"))
    return render_template("index.html")
```
