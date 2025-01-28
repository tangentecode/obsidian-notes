- **_LIFO_** or "last in first out"

 > Just like stacking trays in a dining hall, a tray that is placed in a stack last is the first that may be picked up.

- Specific actions:
	1. _push_: places something on top of the stack
	2. _pop_: removes something from the top of the stack

- [C](contents-c.md) code:

```c
const int CAPACITY = 50;

typedef struct
{
    person people[CAPACITY];
    int size;
}
stack;
```

- Explanation video: [Stacks](https://cs50.harvard.edu/x/2025/shorts/stacks/)
