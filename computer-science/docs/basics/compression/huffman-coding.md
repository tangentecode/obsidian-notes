# Huffman-coding

Compresses and decodes any string to bits

## Example

**Input string:** "AABCBAD"

### 1. [[rle]] (Frequency Table)

- Count each appearances of each character in the string

| **char** | **frequency** |
| -------- | ------------- |
| A        | 3             |
| B        | 2             |
| C        | 1             |
| D        | 1             |

### 2. Create Leaf Nodes

- Create a node for each character in your frequency table and sort the from least frequent to most frequent
- A Node could look like something like this:
```plaintext
Leaf Nodes:
D(1)    C(1)    B(2)    A(3)
```

### 3. Build tree

- Start by combining the frequency of the 2 


> Step-by-Step Example [here](https://www.youtube.com/watch?v=iEm1NRyEe5c)
