# Variables

## Structure

| Data type     | [types](computer-science/docs/c/types.md) (e.g. int, char)                              |
| ------------- | --------------------------------------------------------------- |
| Variable name | Anything apart from [[computer-science/docs/c/functions]] names (recommended [[computer-science/docs/c/style]]) |
| Value         | Needs to be from the data [types](computer-science/docs/c/types.md) declared before     |

## Declaration

- Only variable name and type:

```c
int age;
```

## Definition

- Gives a predeclared variable a value:

```c
age = 18;
```

## Initialization

- Combines `Declaration` and `Definition` in one step:

```c
int age = 18;
```

## Incrementation

- Increment/decrement a variable by one with this syntax:

```c
age++;
// or
age --;
```

## Arrays

- Declare `int scores[3];` with the size that needs to be [allocated](allocate-memory.md) in square brackets

- Define each index individually

```c
scores[0] = 72;
scores[1] = 73;
scores[2] = 33;
```

or use this syntax

```c
scores = {72, 73, 33};
```
