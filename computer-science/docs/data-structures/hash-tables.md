- Like [dictionaries](computer-science/docs/python/dictionaries.md) in [python](contents-python.md) but with a [hash-algorithm](hash-functions.md) 

- A hash table could be imagined as follows:  

![](hash-table-basic.png)


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


- Explanation video: [Hash Tables](https://cs50.harvard.edu/x/2025/shorts/hash_tables/)