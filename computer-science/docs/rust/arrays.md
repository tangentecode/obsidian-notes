# Arrays

## Structure

- Type declaration for an array looks different to normal [[computer-science/docs/rust/variables|variables]]:

```rust
let a: [T; N] = [value1, value2, …]
```

Where:

**T** is the type of the elements.
**N** is the fixed length of the array.Where:

## Examples:

Explicit Type and Length:

```rust
let numbers: [i32; 3] = [1, 2, 3];
```

Implicit Type and Length Inferred:

```rust
let numbers = [1, 2, 3]; // Compiler infers [i32; 3]
```

Repeating Elements:

```rust
let zeros: [i32; 5] = [0; 5]; // Equivalent to [0, 0, 0, 0, 0]
```

Accessing Elements

```rust
let first = numbers[0]; // Access first element
```

## Iterating

- Similar to [[contents-python]] rust uses the `IntoIterator` for looping through arrays:

```rust
fn main() {
    let primes = [2, 3, 5, 7, 11, 13, 17, 19];
    for prime in primes {
        println!(“Current Prime: {prime}“, prime);
    }
}
```
