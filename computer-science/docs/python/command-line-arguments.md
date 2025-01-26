- To use command line argument import the `sys` module
- From there you can access the Argument Vector (`argv`) like a list (or [array](lecture-2-arrays.md))

- Example:
```python
import sys
 
print(sys.argv)

# Only prints the first argument provided
print(sys.argv[1])
```

- `sys.argv[0]` will always be the filename
- 