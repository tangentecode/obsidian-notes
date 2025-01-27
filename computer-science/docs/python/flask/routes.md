@app.route('/about')
def about():
    return "This is the About page."

@app.route('/user/<name>')  # Dynamic route
def user(name):
    return f"Hello, {name}!"
