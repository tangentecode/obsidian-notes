## Structure

1. Define a function `fn` 
2. The function name (Similar to [functions](computer-science/docs/c/functions.md) in [C](contents-c.md))
3. Parameters in parentheses
4. `->` with return type (Similar [functions](computer-science/docs/python/functions.md) in [python](contents-python.md))

# Example

```rust
fn add(a: i32, b: i32) -> i32 {
    a + b // No semicolon = implicit return
    return a + b; // Explicit return statement
}

fn main() {
    let sum = add(5, 7);
    println!("The sum is: {}", sum);
}
1
```

The `main` function like in other languages acts as the entry point for the program
