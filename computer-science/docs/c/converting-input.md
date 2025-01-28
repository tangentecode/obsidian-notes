- Converts a string array into multiple [ints](computer-science/docs/c/types.md)
- Requires: `stdio.h`, `stdlib.h`, `string.h`

```c
char str_nums[100]; // Buffer to store input 
int numbers[10]; // Array to store parsed integers
int count = 0; // Counter for the number of integers
printf("Input multiple numbers separated by spaces: \n"); fgets(str_nums, sizeof(str_nums), stdin);  // Read the whole line of input 
// Split the string and convert each part to an integer
char *token = strtok(str_nums, " ");
// Use space as a delimiter 
while (token != NULL)
{ 
	numbers[count++] = atoi(token); // Convert to integer and store in array 
	token = strtok(NULL, " "); // Get the next token
}
```