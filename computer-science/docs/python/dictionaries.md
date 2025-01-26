### Initialization

- Initialize a [dictionary](computer-science/docs/basics/data-structures/dictionaries.md) like this:
```python

my_dict = {
    "name": "Bob",
    "age": 30,
    "city": "Los Angeles",
}

```

- Or using the `dict` constructor
```python
another_dict = dict(name="Bob", age=30, city="Los Angeles")
```

### Accessing Values

- Using `.get()` function:

```python

print(my_dict.get("age"))  # Returns the associated value: 25

```


- The second parameter is the value that gets [returned](computer-science/docs/python/functions.md) if the key doesn't exist:

```python
print(my_dict.get("country", "Unknown"))  # Output: Unknown
```

### Adding or updating entries

- Use square brackets to access individual `keys`

- Create new key value pair:
```python
my_dict["country"] = "USA"
```

- Update existing value
```python
my_dict["age"] = 40
```

### Removing

- Removing a specific key:
```python
my_dict.pop("city")  # Removes "city"
```

- Removing the last inserted key-value pair: 
```python
my_dict.popitem()
```

-  Clear all entries
```python
my_dict.clear()
```

### Iterating

- Iterating over keys
```python
for key in my_dict:
	print(key)
```

- Iterating over values
```python
for value in my_dict.valu
```

- Looping trough key-value pairs:
```python

```

### Searching



### Why dictionaries?

- Good for representing `JSON` like objects
- Or more general just multiple values associated with multiple keys
- Accessing or [searching](contents-searching.md) has a constant [running time](running-time.md)
 