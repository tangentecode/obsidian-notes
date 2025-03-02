# Functions

## Structure

| Return type    | `int`, `char`,… (No return value: `void`)                                     |
| -------------- | ------------------------------------------------------------------------------- |
| Functions name | Anything apart from variable names (Recommended [style](computer-science/docs/c/style.md))               |
| Parameters     | Data passed in to the local scope of the function (use `void` for no parameters) |

## Example

```c
void example(int age) {
	// do something
}
```

## `main` Function

- Every C Program needs to have a `main` function.
- It acts like an entry point for the program
- The `main` functions always returns an `int`
- If the `int` is not zero there was an error in the programm

```c
int main(void) {
	// do something
}
```
