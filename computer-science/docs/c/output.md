## Explanation

- Part of [stdio.h library](computer-science/docs/c/libraries.md)
- [Manual](https://manual.cs50.io/3/printf)
- Print to the screen

## Print Types

| Conversion Specification | Type     |
| ------------------------ | -------- |
| `%c`                     | `char`   |
| `%f`                     | `double` |
| `%f`                     | `float`  |
| `%i`                     | `int`    |
| `%li`                    | `long`   |
| `%s`                     | `string` |

## Example

```c
#include <stdio.h>

printf("Hello, world!\n")

int age = 18
printf("Age: %i\n", age)
```
