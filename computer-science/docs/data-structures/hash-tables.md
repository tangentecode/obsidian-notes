- Like [dictionaries](computer-science/docs/python/dictionaries.md) in [python](contents-python.md) but with a [hash-algorithm](hash-functions.md) 

- A hash table could be imagined as follows:  
![](hash-table-basic.png)

- if you want to **store** a value let it go trough an proper [hash-functions](hash-functions.md) and store it at the index the hash function returned
- to **search** and value you need to again run it trough the same hashing process and look at that specific index
- **searching** has a [running-time](running-time.md) of <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>O</mi>
  <mo stretchy="false">(</mo>
  <mi>n</mi>
  <mo stretchy="false">)</mo>
</math>

- to avoid **collision** if the hash function returned the same hash for another value store multiple values in a linked at that index:


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