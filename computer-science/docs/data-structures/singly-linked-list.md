- Imagine three values stored in [[memory]]


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