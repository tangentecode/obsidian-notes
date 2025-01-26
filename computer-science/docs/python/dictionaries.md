### Initialization

- Initialize a [dictionary](computer-science/docs/basics/data-structures/dictionaries.md) like this:
```python

my_dict = {
    "name": "Bob",
    "age": 30,
    "city": "los Angeles",
}

```

- Or using the `dict` constructor
```python
another_dict = dict(name="Bob", age=30, city="Los Angeles")
```

### Accessing Values
```python
# Access value by key
print(my_dict["name"])  # Output: Alice

# Using `.get()` (avoids KeyError if key doesn't exist)
print(my_dict.get("age"))  # Output: 25
print(my_dict.get("country", "Unknown"))  # Output: Unknown

```


### Searching
