> CSV is a standard table format which stands for **Comma Separated Values** 

- Python has built-in support for `CSV` files just need to import the csv library

### Open

- Common modes:

| mode | description                        |
| ---- | ---------------------------------- |
| "r"  | read the file                      |
| "w"  | write file from scratch            |
| "a"  | append to already existing content |

- Open with a standard local scope variable in your desired mode:
```python
file = open("file-name.csv", "a")
```

- The **Pythonic** would be:
```python
with open("file-name.csv", "a") as file:
	# do something
```

### Writing

- Write a row to prevously 