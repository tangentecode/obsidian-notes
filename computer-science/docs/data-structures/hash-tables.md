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

- to avoid **collision** if the hash function returned the same hash for another value store multiple values in a [singly-linked-list](singly-linked-list.md) at that index:

![](hash-algorithms-collisions.png)


- [C](contents-c.md) code:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 10

// Node structure for separate chaining
typedef struct Node {
    char *key;
    int value;
    struct Node *next;
} Node;

// Hash table array
Node *hashTable[TABLE_SIZE];

// Hash function
unsigned int hash(const char *key) {
    unsigned int hash = 0;
    while (*key) {
        hash = (hash * 31) + *key++;
    }
    return hash % TABLE_SIZE;
}

// Insert function
void insert(const char *key, int value) {
    unsigned int index = hash(key);
    Node *newNode = malloc(sizeof(Node));
    newNode->key = strdup(key);
    newNode->value = value;
    newNode->next = hashTable[index];
    hashTable[index] = newNode;
}

// Search function
int search(const char *key) {
    unsigned int index = hash(key);
    Node *current = hashTable[index];
    while (current) {
        if (strcmp(current->key, key) == 0) {
            return current->value;
        }
        current = current->next;
    }
    return -1; // Key not found
}

// Delete function
void delete(const char *key) {
    unsigned int index = hash(key);
    Node *current = hashTable[index];
    Node *prev = NULL;

    while (current) {
        if (strcmp(current->key, key) == 0) {
            if (prev) {
                prev->next = current->next;
            } else {
                hashTable[index] = current->next;
            }
            free(current->key);
            free(current);
            return;
        }
        prev = current;
        current = current->next;
    }
    printf("Key not found!\n");
}

// Display function
void display() {
    for (int i = 0; i < TABLE_SIZE; i++) {
        printf("[%d]: ", i);
        Node *current = hashTable[i];
        while (current) {
            printf("-> (%s, %d) ", current->key, current->value);
            current = current->next;
        }
        printf("\n");
    }
}

int main() {
    // Example usage
    insert("apple", 10);
    insert("banana", 20);
    insert("grape", 30);
    insert("orange", 40);

    printf("Value for 'apple': %d\n", search("apple"));
    printf("Value for 'banana': %d\n", search("banana"));

    delete("banana");
    printf("After deleting 'banana':\n");
    display();

    return 0;
}

```


- Explanation video: [Hash Tables](https://cs50.harvard.edu/x/2025/shorts/hash_tables/)