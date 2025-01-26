- The `string` [type](computer-science/docs/c/types.md) is not natively supported by [c](contents-c.md) instead initialize a string with an [arrays](lecture-2-arrays.md) of [chars](computer-science/docs/c/types.md):

```c
char s[] = "HI!"; 
```

### Explanation:

- `char` is the type used to represent a single character in C.
- `char s[]` creates an array of characters to hold the string, including the null terminator `\0` that marks the end of the string.
- The `"HI!"` initializes the array with the string.


> Look at [this](computer-science/docs/basics/memory/strings.md) to see how strings are represented in [memory](lecture-4-memory.md)