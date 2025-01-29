### Basic structs

- `structs` are user defined data [types](computer-science/docs/c/types.md)
- unlike [arrays](lecture-2-arrays.md) they can store values of multiple types
- Define a simple struct like this:
```c
struct Person
{
		char name[50];
		int age;
		float height;
}
```