# Break-continue

## Break

### Explanation

- Use the `break` keyword to exit a loop early
- For example if a certain [[computer-science/docs/rust/conditionals|condition]] is met

### Example

```rust
fn main() {
	let mut i = 0;
	loop {
		i+=1;
		if i > 5 {
			break
		}
	}
}
```

## Continue

### Explanation

- To immediately start the next iteration use [`continue`](https://doc.rust-lang.org/reference/expressions/loop-expr.html#continue-expressions).

### Example

```rust
fn main() {
	let mut i = 0;
	loop {
		i+=1;
		if i % 2 == 0 {
			continue
		}
	}
}
```
