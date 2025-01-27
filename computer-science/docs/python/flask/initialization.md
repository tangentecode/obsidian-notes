

```python
from flask import Flask

app = Flask(__name__)  # Initialize Flask app

@app.route('/')  # Define the home route
def home():
    return "Welcome to Flask!"

if __name__ == '__main__':
    app.run(debug=True)  # Start the development server

```

- When `debug=True` if  the code changes the browser page gets automatically reloaded