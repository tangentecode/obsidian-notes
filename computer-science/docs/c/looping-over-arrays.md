
- Use following line to calculate the [array](lecture-2-arrays.md) size:

```c
#include <stdlib.h>

int size = sizeof(arr) / sizeof(arr[0]);
```

- Then use `size` in the [`for` loop](computer-science/docs/c/loops.md):

```c
#include <stdio.h>

int main() {
    int arr[] = {10, 20, 30, 40, 50}; // Example array
    int size = sizeof(arr) / sizeof(arr[0]); // Calculate the size of the array

    // Loop through every index
    for (int i = 0; i < size; i++) {
        printf("Element at index %d is %d\n", i, arr[i]);
    }

    return 0;
}

```
