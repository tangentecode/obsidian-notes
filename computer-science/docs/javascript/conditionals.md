# Conditionals

- Conditionals in JavaScript are syntactically the same to conditionals in [C](contents-c.md)

## Compare Two Values

with multiple conditions

```c
if (x > y) {
	// do something
}
else if (x < y) {
	// do something else
}
else {
	// previous conditions not met
}
```

## Chain Conditions

### 1. And

```c
if ((x > y) && (x == y)) {
	// both conditions are met
}
```

### 2. Or

```c
if ((x > y) || (x == y)) {
	// one or more of the conditions are met
}
```
