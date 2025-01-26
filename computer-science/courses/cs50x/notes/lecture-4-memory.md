## [Pixel Art](pixel-art.md)

> **Bitmap images:** map of [bits](binary.md) 

 0 represent **black**
 1 represent **white**

![](pixel_art.png)


## [Hexadecimal](hexadecimal.md)

- **16** counting values:
```
0 1 2 3 4 5 6 7 8 9 A B C D E F
```

- Notice that `F` would represent `15` in decimal
- Hexadecimal is also known as `base-16`
- Examples:

| Decimal | Hexadecimal |
| ------- | ----------- |
| 0       | 00          |
| 1       | 01          |
| 9       | 09          |
| 10      | 0A          |
| 15      | 0F          |
| 16      | 10          |
| 255     | FF          |

- The highest you can count with two-digit Hexadecimal is `FF` (Decimal: `255`)
- Hexadecimal is useful because you can represent higher numbers with fewer digits

## Memory Addresses

- start with the `0x` prefix
- count up in [hexadecimal](hexadecimal.md)

![](memory-addresses.png)

## [Pointers](computer-science/docs/c/pointers.md)

### How to use a pointer?

#### Explanation

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

#### Memory:

| Adress | Value       |
| ------ | ----------- |
| 0x1000 | Ox4 (x)     |
| 0x1004 | 0x1000 (pX) |
| 0x1008 |             |
| 0x100C |             |
| ...    |             |

#### & and *

- & Provides the address of something stored in memory.

- * Instructs the compiler to go to a location in memory.



> Good vid by [Low Level Learning](https://www.youtube.com/watch?v=2ybLD6_2gKM&t=438s)

### How is a pointer represented in memory?

- the **pointer** has the address of an [integer](computer-science/docs/c/types.md) 50 as value:

![](pointer-in-memory-1.png)

- You can more accurately visualize a pointer as one address that points to another:
![](pointer-in-memory-2.png)

- Implement pointers in [C](computer-science/docs/c/pointers.md)
## Strings

- The `string` [type](computer-science/docs/c/types.md) is not natively supported by [c](contents-c.md) instead initialize a string with an [arrays](lecture-2-arrays.md) of [chars](computer-science/docs/c/types.md):

```c
char s[] = "HI!"; 
```

### Explanation:

- `char` is the type used to represent a single character in C.
- `char s[]` creates an array of characters to hold the string, including the null terminator `\0` that marks the end of the string.
- The `"HI!"` initializes the array with the string.


### Strings in Memory

- `string s = "HI!"` can be represented as follows:

![](strings-in-memory-1.png)

- the name of the variable (`s`) points to the first letter of the [string](computer-science/docs/python/types.md)
- after that each character is ordered next to this `head` character
- the last character is always the **Null Terminator** (`\0`) which tells the computer: **this string ends here** 


- the [pointer](computer-science/docs/basics/memory/pointers.md) can more accurately be visualized with this image:

![](pointer-in-memory-2.png)



- Implement strings in [C](computer-science/docs/c/strings.md) or in [Python](computer-science/docs/python/variables.md) 

### Practical Tip:

- Use `char s[]` if you need a **modifiable string**.
- Use `char *s` if you want a **constant string** and don't need to modify it. Use `const char *s = "HI!";` to make your intention explicit.

### Addresses of a string

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


## Pointer Arithmetic

- because [memory addresses](addresses.md) are just ([hexadecimal](hexadecimal.md)) numbers you can do math with them
- you can use Pointer Arithmetic instead of accessing indexes of an array with square brackets because the compiler converts these brackets to Pointer Arithmetic
- Example:

```c
// Prints substrings via pointer arithmetic

#include <stdio.h>

int main(void)
{
    char *s = "HI!";
    printf("%s\n", s);
    printf("%s\n", s + 1);
    printf("%s\n", s + 2);
}
```


## Copying and `malloc`

**Look at:**
	1. [allocate-memory](allocate-memory.md)
	2. [reallocate-memory](reallocate-memory.md)
	3. [access-memory](access-memory.md)


## Globals, Heap, Stack...

This is the basic structure of memory:

![](globals-heap-stack-structure.png)


Heres what is stored at each region:

- **Machine Code (Text Segment)**:
    
    - Contains the compiled code of the program, which is executed by the CPU.
    - This area is typically read-only to prevent accidental modification of instructions.
- **Globals (Data Segment)**:
    
    - Stores global and static variables initialized at the start of the program.
    - Variables in this section persist for the lifetime of the program.
    - May be further divided into:
        - **.data**: For initialized global/static variables.
        - **.bss**: For uninitialized global/static variables (default-initialized to zero).
- **Heap**:
    
    - Used for dynamic memory allocation (e.g., with `malloc` in C or `new` in C++).
    - Grows downward (towards higher memory addresses).
    - Memory here must be explicitly managed (allocated and freed by the programmer).
- **Stack**:
    
    - Stores function call frames (local variables, return addresses, function parameters).
    - Grows upward (towards lower memory addresses).
    - Automatically managed (memory is allocated when a function is called and freed when it returns).
## Why use pointers?

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


