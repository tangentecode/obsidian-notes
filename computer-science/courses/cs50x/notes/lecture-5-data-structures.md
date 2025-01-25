## Data Structures

- **_Data structures_** essentially are forms of organization in memory.

- Individual Guides:
	1. [singly-linked-list](singly-linked-list.md)
	2. [doubly-linked-list](doubly-linked-list.md)
	3. [stacks](stacks.md)
	4. [queues](queues.md)
	5. [dictionaries](computer-science/docs/data-structures/dictionaries.md)
	6. [hash-tables](hash-tables.md)


- Videos:
	- [Singly-Linked Lists](https://cs50.harvard.edu/x/2025/shorts/singly_linked_lists/)
	- [Doubly-Linked Lists](https://cs50.harvard.edu/x/2025/shorts/doubly_linked_lists/)
	- [Stacks](https://cs50.harvard.edu/x/2025/shorts/stacks/)
	- [Queues](https://cs50.harvard.edu/x/2025/shorts/queues/)
	- [Hash Tables](https://cs50.harvard.edu/x/2025/shorts/hash_tables/)



## Stacks

- **_LIFO_** or "last in first out"


 >Just like stacking trays in a dining hall, a tray that is placed in a stack last is the first that may be picked up.

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


- Explanation video: [Stacks](https://cs50.harvard.edu/x/2025/shorts/stacks/)****

## Queues
