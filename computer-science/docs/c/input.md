- Most common to get **CLI Input** is `scanf` from [stdio.h](computer-science/docs/c/libraries.md):

```c
#include <stdio.h>

int age;

printf("Age");
scanf("&d", &age) // Need to pass in ADDRESS to predeclared variable
```

| Conversion Specification | Type     |
| ------------------------ | -------- |
| `%c`                     | `char`   |
| `%f`                     | `double` |
| `%f`                     | `float`  |
| `%i`                     | `int`    |
| `%li`                    | `long`   |
| `%s`                     | `string` |