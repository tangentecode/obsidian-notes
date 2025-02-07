# Command-line-arguments

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

- Use `len(sys.argv)` to check how many arguments the user provided
- Similar to `argc` in [c](contents-c.md) 
