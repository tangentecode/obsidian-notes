# Html-templates

- The [HTML](contents-html.md) file needs to be as described in [file-structure](computer-science/docs/python/flask/file-structure.md) in the **templates** directory:

```python
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

```
