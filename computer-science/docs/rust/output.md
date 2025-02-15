`println!` is a macro used to print text to the console with a newline at the end.

It works similarly to `printf` in [C](contents-c.md) or `print` in [python](contents-python.md).

## Basic Usage

```rust
println!("Hello, world!");
```

## Avoid new line

- Use `print!` instead of `println!`:
```rust
print!("Hello, "); 
print!("world!");
```

## Passing variables 

- Use `{}` to define a placeholder for a formatted values:
```rust

```
