
- A **_hash function_** is an algorithm that reduces a larger value to something small and predictable. Generally, this function takes in an item you wish to add to your hash table, and returns an integer representing the array index in which the item should be placed. 
- As example for an **hash function** you can look at this [python](contents-python.md) code:

```python
for char in input_string: 
	hash_value += ord(char) 
hash_value % 256
```

### Explanation:

1. **Input**: A string (e.g., "hello").
2. **Process**:
    - Sum up the ASCII values of each character in the string using `ord()`.
    - Use modulo (`% 256`) to ensure the hash value stays within a range (0–255).
3. **Output**: A small hash value.



- A basic hash functions in [c](contents-c.md) could look like this:
```c
#include <ctype.h>

unsigned int hash(const char *word)
{
    return toupper(word[0]) - 'A';
}

```
