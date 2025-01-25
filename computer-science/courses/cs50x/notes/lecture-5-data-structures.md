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

- Queues are **FIFO** which stands for "first in first out"


 >You can imagine yourself in a line for a ride at an amusement park. The first person in the line gets to go on the ride first. The last person gets to go on the ride last.


- Specific actions:
	1. _enqueued_: item can join the queue
	2. _dequeued_: item leaves the queue


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


- Explanation video: [Queues](https://cs50.harvard.edu/x/2025/shorts/queues/)


## Singly Linked Lists

- Imagine three values stored in [memory](lecture-4-memory.md)
![](3-values-memory.png)



- We could imagine the data pictured above as follows:
![](linkes-list-basic.png)


- Keep track of the next element ([node](structs.md)) by storing a pointer aside from the value like this:
![](linkes-list-advanced.png)
>Last node stores an NULL [pointer](pointers.md ) because there is no next element


- the **head** is the a points to the first node
![](linked-list-head.png)


A _node_ contains both an _item_ and a pointer called _next_. In code, you can imagine a node as follows:

```c
typedef struct node
{
    int number;
    struct node *next;
}
node;
```




- [C](contents-c.md) code:

```c
// Start to build a linked list by prepending nodes


#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
} node;

int main(void)
{
    // Memory for numbers
    node *list = NULL;

    // Build list
    for (int i = 0; i < 3; i++)
    {
        // Allocate node for number
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return 1;
        }
        n->number = i * 2;
        n->next = NULL;

        // Prepend node to list
        n->next = list;
        list = n;
    }
    return 0;
}
```

>First, a `node` is defined as a `struct`. For each element of the list, memory for a `node` is allocated via `malloc` to the size of a node. `n->number` (or `n`’s number field) is assigned an integer. `n->next` (or `n`’s next field) is assigned `null`. Then, the node is placed at the start of the list at memory location `list`.

- Print the list on correct order:
```c
// Print numbers
node *ptr = list;
while (ptr != NULL)
{
    printf("%i\n", ptr->number);
    ptr = ptr->next;
}

```
- Explanation video: - [Singly-Linked Lists](https://cs50.harvard.edu/x/2025/shorts/singly_linked_lists/)


## Doubly Linked Lists

- Basically like [singly-linked-lists](singly-linked-list.md) but they have another pointer with the address of the previous [node](structs.md)


## Dictionarys


- Dictionaries have **_key_** and **_values_**

- The _holy grail_ of algorithmic time complexity is <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>O</mi>
  <mo stretchy="false">(</mo>
  <mn>1</mn>
  <mo stretchy="false">)</mo>
</math> or _constant time_.

![](dicts-running-time.png)

- You can easily implement a [dictionary](dictionaries.md) in [python](contents-python.md) and in [c](contents-c.md) in form of a [hash-table](hash-tables.md) 