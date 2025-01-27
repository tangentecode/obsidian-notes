-  Routes define the [URLs](lecture-8-html-css-javascript.md) in your apps

```python
@app.route('/about')
def about():
    return "This is the About page."

@app.route('/user/<name>')  # Dynamic route
def user(name):
    return f"Hello, {name}!"

```