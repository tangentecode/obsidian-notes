**Read from and write to dynamic memory:**

```c
// Allocate memory  
int *ptr;  
ptr = calloc(4, sizeof(*ptr));  
  
// Write to the memory  
*ptr = 2;   // Equals to: ptr[0] = 2;  
ptr[1] = 4;  
ptr[2] = 6;
```