# Loops

> Run the same code multiple times

## `for` Loop

- Iterates the code in the code as long the condition (the second parameter) is no longer met:
- Conditions need to have an [operator](computer-science/docs/python/operators.md) in most cases

```python
for i in range(3):
	# do something three times
```

## `while` Loop

- Do something as long as the condition after the `while` keyword is true
- You cannot define the [variables](computer-science/docs/python/variables.md) in the `while` loop like in a `for` loop

```python
i = 0
while i < 3:
	# do something three times

```

- If you want to create an infinite loop:

```python
while True:
	# cancel with control+c
```
