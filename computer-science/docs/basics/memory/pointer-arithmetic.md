
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