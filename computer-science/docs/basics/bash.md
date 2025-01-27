> CLI = Command Line Interface

## Commands

| Command | Description                                 | Example                            |
| ------- | ------------------------------------------- | ---------------------------------- |
| `cd`    | Change the current directory (folder).      | `cd /path/to/folder`               |
| `cp`    | Copy files and directories.                 | `cp file.txt /destination/folder/` |
| `ls`    | List files in a directory.                  | `ls -la`                           |
| `mkdir` | Make a new directory.                       | `mkdir new_folder`                 |
| `mv`    | Move or rename files and directories.       | `mv old_name.txt new_name.txt`     |
| `rm`    | Remove (delete) files.                      | `rm file.txt`                      |
| `rmdir` | Remove (delete) empty directories.          | `rmdir empty_folder`               |
| `touch` | Create an empty file or update a timestamp. | `touch new_file.txt`               |
| `echo`  | Display a message or value of a variable.   | `echo "Hello, World!"`             |
| `cat`   | View the contents of a file.                | `cat file.txt`                     |
| `pwd`   | Print the current working directory.        | `pwd`                              |
| `find`  | Search for files or directories.            | `find /path -name "*.txt"`         |
| `grep`  | Search for patterns within files.           | `grep "search_term" file.txt`      |
| `man`   | Display the manual for a command.           | `man ls`                           |

---

## Operators
### `pipe` operator (`|`)

- Pass the output of one command as input to another command.
  - Example: `ls | grep "pattern"`

### `redirect` operator (`>` and `>>`)

- `>`: Redirect output to a file (overwrites existing content).
  - Example: `echo "Hello" > file.txt`
  
- `>>`: Append output to a file.
  - Example: `echo "World" >> file.txt`

### `logical` operators (`&&` and `||`)

- `&&`: Run the next command only if the previous one succeeds.
  - Example: `mkdir new_folder && cd new_folder`
  
- `||`: Run the next command only if the previous one fails.
  - Example: `mkdir existing_folder || echo "Folder already exists"`

### `background` operator (`&`)

- Run a command in the background.
  - Example: `sleep 10 &`
