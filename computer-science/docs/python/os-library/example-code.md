# Example-code

```python
import os

# Get current working directory
current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")

# List files and directories in a path
files = os.listdir(current_dir)
print(f"Files and directories: {files}")

# Create a new directory
new_dir = "test_directory"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Created directory: {new_dir}")

# Rename the directory
os.rename(new_dir, "new_test_directory")
print(f"Renamed directory to: new_test_directory")

# Remove the directory
os.rmdir("new_test_directory")
print("Removed directory: new_test_directory")

```
