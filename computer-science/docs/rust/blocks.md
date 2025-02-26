# Blocks

## Explanation

- A block in rust contains a sequence of expressions, enclosed by braces `{}`
- **Value and [[computer-science/docs/rust/types|type]]** **are those of the last expression** in the block
- The last expression doesn't have a semicolon `;` at the end like returning a value from a [[computer-science/docs/rust/functions|function]]
- A [[computer-science/docs/rust/variables|variable]]'s scope is limited to the enclosing block.

## Example

```rust
fn main() {
    let z = 13;
    let x = {
        let y = 10;
        dbg!(y);
        z - y
    };
    println!(x);
    // println]!(y); Would cause a compilation error because variable is out of scope
}
```
