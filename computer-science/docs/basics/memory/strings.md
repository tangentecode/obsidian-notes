- `string s = "HI!"` can be represented as follows:

![](strings-in-memory-1.png)

- the name of the variable (`s`) points to the first letter of the [string](computer-science/docs/python/types.md)
- after that each character is ordered next to this `head` character
- the last character is always the **Null Terminator** (`\0`) which tells the computer: **this string ends here** 


- the [pointer](computer-science/docs/basics/memory/pointers.md) can more accurately be visualized with this image:

![](pointer-in-memory-2.png)



- Implement strings in [C](computer-science/docs/c/strings.md) or in [Python](computer-science/docs/python/variables.md) 