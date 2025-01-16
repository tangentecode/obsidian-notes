> Run the same code multiple times

## `for` loop

- Iterates the code in the code as long the condition (the second parameter) is no longer met:
- Conditions need to have an [operators](operators.md) in most cases

```c
for (int i = 0; i < 3; i++) {
	// do something three times
}
```


## `while` loop

- Do something as long as the condition after the `while` keyword is true
- You cannot define the [variable](computer-science/docs/c/variables.md) in the `while` loop like in a `for` loop

```c
int i = 0
while (i < 3) {
	// do something three times
	i++;
}
```

- If you want to create an infinite loop:

```c
while (true) {
	// cancel with control+c
}
```
