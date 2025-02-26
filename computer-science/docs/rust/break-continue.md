
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