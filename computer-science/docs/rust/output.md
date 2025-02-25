# Output

**# Output

`println!` is a macro used to print text to the console with a newline at the end.

It works similarly to `printf` in [C](contents-c.md) or `print` in [python](contents-python.md).

## Basic Usage

```rust
println!("Hello, world!");
```

## Avoid New line

- Use `print!` instead of `println!`:

```rust
print!("Hello, "); 
print!("world!");
```

## Passing Variables

- In you `{}` placeholder type the variable name directly

```rust
println!("My name is {name} and I am {age} years old.");
```

## Passing Variables by order

- Use `{}` to define a placeholder for a formatted values:

```rust
println!("My name is {} and I am {} years old.", name, age);
```

## Named Arguments

- When multiple values get passed it gets messy
- Define a placeholder with a name a define a variable with that name

```rust
println!("{subject} is {adjective}!", subject="Rust", adjective="awesome");
```
