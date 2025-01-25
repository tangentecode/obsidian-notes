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