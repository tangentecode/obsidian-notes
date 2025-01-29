This is the basic structure of memory:

![](globals-heap-stack-structure.png)

Heres what is stored at each region:

- **Machine Code (Text Segment)**:
		
		- Contains the compiled code of the program, which is executed by the CPU.
		- This area is typically read-only to prevent accidental modification of instructions.
- **Globals (Data Segment)**:
		
		- Stores global and static variables initialized at the start of the program.
		- Variables in this section persist for the lifetime of the program.
		- May be further divided into:
				- **.data**: For initialized global/static variables.
				- **.bss**: For uninitialized global/static variables (default-initialized to zero).
- **Heap**:
		
		- Used for dynamic memory allocation (e.g., with `malloc` in C or `new` in C++).
		- Grows downward (towards higher memory addresses).
		- Memory here must be explicitly managed (allocated and freed by the programmer).
- **Stack**:
		
		- Stores function call frames (local variables, return addresses, function parameters).
		- Grows upward (towards lower memory addresses).
		- Automatically managed (memory is allocated when a function is called and freed when it returns).

## Overflows

- A **_heap overflow_** is when you overflow the heap, touching areas of memory you are not supposed to.
- A **_stack overflow_** is when too many functions are called, overflowing the amount of memory available.
- **Both** of these are considered **_buffer overflows_**.
