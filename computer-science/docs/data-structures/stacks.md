- **_LIFO_** or "last in first out"


 >Just like stacking trays in a dining hall, a tray that is placed in a stack last is the first that may be picked up.

- Specific actions:
	1. _push_: item can join the queue
	2. _pop_: item leaves the queue


- [C](contents-c.md) code:

```c
const int CAPACITY = 50;

typedef struct
{
    person people[CAPACITY];
    int size;
}
queue;
```