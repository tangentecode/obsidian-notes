# Input

- Most common to get **CLI Input** is `scanf` from [stdio.h](computer-science/docs/c/libraries.md):

```c
#include <stdio.h>

int age;

printf("Age");
scanf("%d", &age);

char name[100];

printf("Name: ");
scanf("%99s", &name); 
```

- `99` to avoid [buffer overflow](globals-heap-stack.md)
 - Need to pass in [address](computer-science/docs/c/pointers.md) to predeclared variable

| Conversion Specification | Type     |
| ------------------------ | -------- |
| `%c`                     | `char`   |
| `%f`                     | `double` |
| `%f`                     | `float`  |
| `%i`                     | `int`    |
| `%li`                    | `long`   |
| `%s`                     | `string` |
