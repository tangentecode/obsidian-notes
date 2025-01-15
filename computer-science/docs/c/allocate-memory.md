> C has two types of [memory](lecture-4-memory.md): **Static memory** and **Dynamic Memory**

## Malloc

- To use **Dynamic Memory** include `stdlib.h`
- For allocating memory use the `malloc()` function
- The `malloc()` function has one parameter, _size_, which specifies how much memory to allocate, measured in bytes.
- `sizeof()` is a common use case for that

```c
#include <stdlib.h>

int *ptr;
ptr = malloc(sizeof(*ptr))
```


>**Be careful:** `sizeof(*ptr1)` tells C to measure the size of the data at the address. If you forget the `*` and write `sizeof(ptr1)` instead, it will measure the size of the pointer itself, which is the (usually) 8 bytes that are needed to store a memory address.


## Calloc

 `calloc()` behaves pretty much the same like `malloc()`:
 
- Takes another parameter ([int](computer-science/docs/c/types.md)) which defines how often the allocation process should be completed
- Instead writing unpredictable data to 