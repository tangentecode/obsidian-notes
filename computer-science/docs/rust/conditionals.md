# Conditionals

> Basic **conditionals** in rust are very similar to [javascript](computer-science/docs/javascript/contents-javascript.md) an [c](contents-c.md) 

### 1. **Basic `if` Statement**

```rust
fn main() {
    let number = 10;

    if number > 5 {
        println!("Number is greater than 5");
    }
}
```

### 2. **`if`-`else` Statement**

```rust
fn main() {
    let number = 3;

    if number > 5 {
        println!("Greater than 5");
    } else {
        println!("5 or less");
    }
}
```

### 3. **`if`-`else if`-`else` Statement**

```rust
fn main() {
    let number = 10;

    if number < 0 {
        println!("Negative number");
    } else if number == 0 {
        println!("Zero");
    } else {
        println!("Positive number");
    }
}
```

### 4. **Using `if` As an Expression**

Since Rust is an expression-based language, `if` can return a value:

```rust
fn main() {
    let condition = true;
    let number = if condition { 10 } else { 5 }; // Must return the same type

    println!("The number is: {}", number);
}
```

### 5. **`match` Statement (Alternative to `if`-`else`)**

`match` is a powerful control-flow operator that acts like a `switch` statement:

```rust
fn main() {
    let number = 2;

    match number {
        1 => println!("One"),
        2 => println!("Two"),
        3 => println!("Three"),
        _ => println!("Something else"), // Catch-all case
    }
}
```

### 6. **`if let` For Matching a Single Pattern**

`if let` is useful for checking a single pattern inside an `Option` or `Result` type:

```rust
fn main() {
    let some_value = Some(42);

    if let Some(x) = some_value {
        println!("The value is: {}", x);
    } else {
        println!("No value");
    }
}
```
