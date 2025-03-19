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

### 3. First Combining

- Start by combining the frequency of the 2 least frequent characters and connect those with a node
- In this case:
```plaintext
 |--(2)--|
 |       |
D(1)    C(1)    B(2)    A(3)
```

### 4. Build Tree

 - Repeat the step above but combine the least frequent character that is not connected to a node with the previously created node
 - This step must be repeated as often as there are no **Leaf Nodes**
- Complete Tree:

```plaintext

				 |--(7)--| 
                 |	     |
		 |--(4)--|      A(3)
         |       |	
 |--(2)--|      B(2)    
 |       |
D(1)    C(1)    

```

### 5. Decode with Tree

- The left connection of a node as a **0** while the right connection is a **1**
- Now look up the path to your current char beginning from the **Root** and write down the 1/0 
- Path to **C** would be  `001`

> Step-by-Step Example [here](https://www.youtube.com/watch?v=iEm1NRyEe5c)
