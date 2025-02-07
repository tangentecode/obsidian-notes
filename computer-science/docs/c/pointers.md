# Pointers

## What is a Pointer?

### Explanation

- Create variable:

```c
int x = 4;
```

- **Pointer to variable**

```c
int * pX = &x;
```

- English: integer pointer named `pX` is set to the address of `x`
- If `*` is used next to a [type](computer-science/docs/c/types.md): **pointer to that type** 
- No type nearby: **pointer get dereferenced** which means it takes the value at that location
- The `&` sign just means **the address of the following variable**
- [Naming conventions](computer-science/docs/c/style.md) for pointers: take the **variable name** the pointer points to and set a lowercase **p in front**

### Memory:

| Address | Value       |
| ------ | ----------- |
| 0x1000 | Ox4 (x)     |
| 0x1004 | 0x1000 (pX) |
| 0x1008 |             |
| 0x100C |             |
| …    |             |

### & And *

- & Provides the address of something stored in memory.

- Instructs the compiler to go to a location in memory.

> Good vid by [Low Level Learning](https://www.youtube.com/watch?v=2ybLD6_2gKM&t=438s)

## Why Use Pointers?

Example: you want to to make a function to swap to values

```c
#include <stdio.h>

void swap(int a, int b);

int main(void)
{
    int x = 1;
    int y = 2;

    swap(x, y);
}

void swap(int a, int b)
{
    int tmp = a;
    a = b;
    b = tmp;
}
```

- this code would fail because `x` and `y` is only in the `local scope` of the `main` function.

 - this happens to be because function are allocated at different parts in memory

![](two-function-in-memory.png)

- Corrected code:

```c
// Swaps two integers using pointers

#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x is %i, y is %i\n", x, y);
    swap(&x, &y);
    printf("x is %i, y is %i\n", x, y);
}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
```

- Notice that variables are not passed by **_value_** but by **_reference_** in memory.
- You can visualize this as follows:

![](two-function-pointer-in-memory.png)

> look at [globals-heap-stack](globals-heap-stack.md) for further explanation
