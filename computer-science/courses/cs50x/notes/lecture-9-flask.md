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

## Handling Forms

## Routes

## Advanced
