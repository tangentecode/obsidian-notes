> CLI = Command Line Interface

## Commands

- `cd`: Change the current directory (folder).
    
    - Example: `cd /path/to/folder`
- `cp`: Copy files and directories.
    
    - Example: `cp file.txt /destination/folder/`
- `ls`: List files in a directory.
    
    - Example: `ls -la` (includes hidden files and detailed info).
- `mkdir`: Make a new directory.
    
    - Example: `mkdir new_folder`
- `mv`: Move or rename files and directories.
    
    - Example: `mv old_name.txt new_name.txt`
- `rm`: Remove (delete) files.
    
    - Example: `rm file.txt`
- `rmdir`: Remove (delete) empty directories.
    
    - Example: `rmdir empty_folder`
- `touch`: Create an empty file or update the timestamp of a file.
    
    - Example: `touch new_file.txt`
- `echo`: Display a message or value of a variable.
    
    - Example: `echo "Hello, World!"`
- `cat`: View the contents of a file.
    
    - Example: `cat file.txt`
- `pwd`: Print the current working directory.
    
    - Example: `pwd`
- `find`: Search for files or directories.
    
    - Example: `find /path -name "*.txt"`
- `grep`: Search for patterns within files.
    
    - Example: `grep "search_term" file.txt`
- `chmod`: Change file permissions.
    
    - Example: `chmod 755 script.sh`
- `chown`: Change file ownership.
    
    - Example: `chown user:group file.txt`
- `man`: Display the manual for a command.
    
    - Example: `man ls`

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

---

## Examples

### Combine commands with `|`