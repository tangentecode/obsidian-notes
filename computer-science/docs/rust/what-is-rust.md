# What-is-rust

- Rust is statically typed
- Similar to C++/C: compiled
- `rustc` uses LLVM as its backend
- Supports many architectures (also WebAssembly)

## Benefits

- _Compile time [memory](contents-memory.md) safety_ - whole classes of memory bugs are prevented at compile time
		
		- No uninitialized [variables](computer-science/docs/c/variables.md).
		- No double-frees.
		- No use-after-free.
		- No `NULL` [pointers](computer-science/docs/c/pointers.md).
		- No forgotten locked mutexes.
		- No data races between threads.
		- No iterator invalidation.
