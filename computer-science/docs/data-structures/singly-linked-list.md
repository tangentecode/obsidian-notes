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
const int CAPACITY = 50;

typedef struct
{
    person people[CAPACITY];
    int size;
}
queue;
```


- Explanation video: - [Singly-Linked Lists](https://cs50.harvard.edu/x/2025/shorts/singly_linked_lists/)