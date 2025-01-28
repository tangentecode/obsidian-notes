## Installation

Install **Flask** with [pip](computer-science/docs/python/libraries.md):

```shell
pip install flask

```

Make sure **Python** is installed 

(Version 3.7 or higher is recommended)

## Running

To run a flask application run these commands in preferred shell:

```shell
export FLASK_APP=app.py  # On Windows, use set FLASK_APP=app.py
flask run
```

## Initialization

```python
from flask import Flask

app = Flask(__name__)  # Initialize Flask app

@app.route('/')  # Define the home route
def home():
    return "Welcome to Flask!"

if __name__ == '__main__':
    app.run(debug=True)  # Start the development server

```

- When `debug=True` if the code changes the browser page gets automatically reloaded

## File Structure

The basic file structure looks like this:

```shell
my_flask_app/
│
├── app.py            # Main Flask application
├── templates/        # HTML templates
│   ├── index.html
│   └── form.html
├── static/           # Static files (CSS, JS, images)
│   └── style.css

```

the only required to run a **Flask** web app is the main **Python** file

## HTML Templates

- The [HTML](contents-html.md) file needs to be as described in [file-structure](computer-science/docs/python/flask/file-structure.md) in the **templates** directory:

```python
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

```

## Handling Forms

- Create a [form](forms.md) in an [HTML](contents-html.md) file and [render](html-templates.md) it:

```html
<form method="POST" action="/submit">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name">
    <button type="submit">Submit</button>
</form>
```

## Routes

-  Routes define the [URLs](lecture-8-html-css-javascript.md) in your apps

```python
@app.route('/about')
def about():
    return "This is the About page."

@app.route('/user/<name>')  # Dynamic route
def user(name):
    return f"Hello, {name}!"

```

## Advanced

- **Learn Flask Extensions**:

		- Flask-SQLAlchemy (database integration)
		- Flask-WTF (form handling)
		- Flask-Login (user authentication)

- **Read Flask Documentation**:
		
		- Flask Official Documentation
