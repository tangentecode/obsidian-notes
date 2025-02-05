> Run the same code multiple times

## `for` Loop

- Iterates the code in the code as long the condition (the second parameter) is no longer met:
- Conditions need to have an [operators](computer-science/docs/c/operators.md) in most cases

```javascript
for (let i = 0; i < 3; i++) {
	// do something three times
}
```

## `while` Loop

- Do something as long as the condition after the `while` keyword is true
- You cannot define the [variable](computer-science/docs/javascript/variables.md) in the `while` loop like in a `for` loop

```javascript
let i = 0
while (i < 3) {
	// do something three times
	i++;
}
```

- If you want to create an infinite loop:

```javascript
while (true) {
	// cancel with control+c
}
```
