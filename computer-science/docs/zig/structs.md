# Structs

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

### Accessing Values

#### Dot Notation

- Use this notation if you want to access regular `struct`:

```c
// Declare a struct variable 
struct Person person1;

person1.age = 18;
strcpy(person1.name, "Bob");
```

#### -> Operator

- `->` operator if your working with a [pointer](computer-science/docs/c/pointers.md):

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

- Why use `->`:

```c
ptr->age = 25;   // Shorthand
(*ptr).age = 25; // Equivalent, but more verbose
```

### `typedef`

> `typedef` = Type Definition

- If you want to handle the struct like an data type (`int`, `char`,…) use the `typedef` keyword:

```c
typedef struct
{
        int x;
        int y;
} point;

point variable_name = {10, 25};
// Without typedef: struct point variable_name = {10, 25}
```

- You can also use both ways;

```c
typedef struct point
{
        int x;
        int y;
} point;
```
