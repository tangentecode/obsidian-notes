```python
button = QPushButton("Button Text")
button.clicked.connect(someFunction())
# or
button.clicked.connect(lambda: print("example"))
```

# Import:
```python
from PyQt6.Widgets import QPushButton
```