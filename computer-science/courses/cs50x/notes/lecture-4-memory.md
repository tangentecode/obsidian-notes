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

## What is a pointer?

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

| Adress | Value       |
| ------ | ----------- |
| 0x1000 | Ox4 (x)     |
| 0x1004 | 0x1000 (pX) |
| 0x1008 |             |
| 0x100C |             |
| ...    |             |

### & and *

- & Provides the address of something stored in memory.

- * Instructs the compiler to go to a location in memory.



> Good vid by [Low Level Learning](https://www.youtube.com/watch?v=2ybLD6_2gKM&t=438s)


## Strings

- The `string` [type](computer-science/docs/c/types.md) is not natively supported by [c](contents-c.md) instead initialize a string with an [arrays](lecture-2-arrays.md) of [chars](computer-science/docs/c/types.md):

```c
char s[] = "HI!"; 
```

### Explanation:

- `char` is the type used to represent a single character in C.
- `char s[]` creates an array of characters to hold the string, including the null terminator `\0` that marks the end of the string.
- The `"HI!"` initializes the array with the string.

