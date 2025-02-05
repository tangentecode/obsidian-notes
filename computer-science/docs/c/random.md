- To generate a random [integer](computer-science/docs/c/types.md) use `rand()` from [`stdlib.h`](computer-science/docs/c/libraries.md)
- Its common practice to use is with the [modulo operator](computer-science/docs/c/operators.md) to specify a range of numbers:

```c
// Random int between 0 and 19
int r = rand() % 20;
```

- Advanced example:

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int getRandomNumber(int lower, int upper) {
    return (rand() % (upper - lower + 1)) + lower;
}

int main() {
    // Seed the random number generator
    srand(time(0));

    int lower = 10, upper = 50;
    int randomNum = getRandomNumber(lower, upper);

    printf("Random Number between %d and %d: %d\n", lower, upper, randomNum);

    return 0;
}
```
