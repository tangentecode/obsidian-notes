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

### Basic writer

- Write a row to previously opened file:
```python
# Define data
name = "Bob"
age = "30"

# Specify a writer
writer = csv.writer(file)
writer.writerow([name,age])
```


### Dict Writer

- Similarly, we can write a dictionary as follows within the CSV file:
    
```python
import csv
    
    name = input("Name: ")
    number = input("Number: ")
    
    with open("phonebook.csv", "a") as file:
    
        writer = csv.DictWriter(file, fieldnames=["name", "number"])
        writer.writerow({"name": name, "number": number})
    ```
    
    Notice this code is quite similar to our prior iteration but with `csv.DictWriter` instead.


