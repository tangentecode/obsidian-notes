- If the amount of memory reserved is not enough it can be resized to make it larger
- To achieve that use the `realloc()` function with the parameters:
	1. Pointer to memory being resized
	2. Size of the new memory (in bytes)

- Example:
```c
int *ptr1, *ptr2, size;  
  
// Allocate memory for four integers  
size = 4 * sizeof(*ptr1);  
ptr1 = malloc(size);  
  
printf("%d bytes allocated at address %p \n", size, ptr1);  
  
// Resize the memory to hold six integers  
size = 6 * sizeof(*ptr1);  
ptr2 = realloc(ptr1, size);  

printf("%d bytes reallocated at address %p \n", size, ptr2);
```