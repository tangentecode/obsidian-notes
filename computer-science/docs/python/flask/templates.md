# Templates

> Place these [HTML](contents-html.md), like in [file-structure](computer-science/docs/python/flask/file-structure.md) in the `templates` folder

- With **templates** you can simplify HTML files by defining a **layout** and then only pasting the regarding block of your site:

### `layout.html`

```html
<!DOCTYPE html>

<html lang="en">

    <head>
        <meta name="viewport" content="initial-scale=1, width=device-width">
        <title>hello</title>
    </head>

    <body>
        {% block body %}{% endblock %}
    </body>

</html>
```

## `form.html`

```html
{% extends "layout.html" %}

{% block body %}

    <form action="/greet" method="get">
        <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
        <button type="submit">Greet</button>
    </form>

{% endblock %}
```
