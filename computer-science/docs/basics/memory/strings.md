# Strings

- `string s = "HI!"` can be represented as follows:

![](strings-in-memory-1.png)

- the name of the variable (`s`) points to the first letter of the [string](computer-science/docs/python/types.md)
- after that each character is ordered next to this `head` character
- the last character is always the **Null Terminator** (`\0`) which tells the computer: **this string ends here** 

- the [pointer](computer-science/docs/basics/memory/pointers.md) can more accurately be visualized with this image:

![](pointer-in-memory-2.png)

### Addresses of a String

```c
// Prints a string's address as well the addresses of its chars

#include <stdio.h>

int main(void)
{
	char *s = "HI!";
    printf("%p\n", s);
    printf("%p\n", &s[0]);
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);
    printf("%p\n", &s[3]);
}

```

- Implement strings in [C](computer-science/docs/c/strings.md) or in [Python](computer-science/docs/python/variables.md) 
