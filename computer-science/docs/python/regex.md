- Import `re` to use **Regular Expressions** in Python
- Use `re.search` to search for pattern in a string [pattern](computer-science/docs/basics/regex.md) 
- Use `re.match` to see if the string exactly matches the [pattern](computer-science/docs/basics/regex.md)
- The `group()` method returns the part which matched the pattern  

```python
import re

match = re.search(r'\d+', 'There are 123 apples')

if match:
	print(match.group()) # Output: 123
```

> **Tip:** use rawstrings (`r" "`) to avoid errors  