- To generate a random [integer](computer-science/docs/c/types.md) use `rand()` from [`stdlib.h`](computer-science/docs/c/libraries.md)
- Its common practice to use is with the [modulo operator](computer-science/docs/c/operators.md) to specify a range of numbers:

```c
// Random int between 0 and 19
int r = rand() % 20;
```