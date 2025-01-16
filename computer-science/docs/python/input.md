
## Basics

- To create a typable input field use the `input()` function:
```python
input("Name: ")
```

- Assign to [variables](computer-science/docs/python/variables.md) to use in later operations
```python
name = input("Name: ")
```

- Use different [types](computer-science/docs/python/types.md) to specify what can be inputted by the user
```python
age = int(input("Age: "))
```

## Tricks
- You have three options:
```python
print("1. Option")
print("2. Option")
print("3. Option")
```
- Often you end up creating a pattern like this:
```python
user_input = int(input("Choose 1,2 or 3: "))
if user_input == 1:
    # do something
elif user_input == 2:
    # do something
elif user_input == 3:
    # do something
```

- A much cleaner [style](computer-science/docs/python/style.md) of handling this is with an input match case scenario:
```python
match input("Ente)
```