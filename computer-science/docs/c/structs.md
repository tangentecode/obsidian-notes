### Initializing

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

### Accessing values

#### Dot notation

- Use this notation if you want to access regular `struct`:
```c
// Declare a struct variable 
struct Person person1;

person1.age = 18;
strcpy(person1.name, "Bob");
```

- `->` operator if your working with a pointer:
```c
struct Point
{
        int x;
        int y;
}

struct Point p = {10, 5};
struct Point *ptr = &p;

ptr->x = 20;
ptr->y = 10;
```
