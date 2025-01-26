- To use command line argument import the `sys` module
- From there you can access the Argument Vector (`argv`) like a list (or [array](lecture-2-arrays.md))
- Example:

```python
import sys

# Print 
print(sys.argv)

print(sys.argv[1])
```