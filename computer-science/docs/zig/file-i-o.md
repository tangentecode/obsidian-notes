# File-i-o

File I/O (Input/Output) in C is done using the standard library functions provided by `<stdio.h>`. The basic operations include opening, reading, writing, and closing files.

### 1. **Opening A File**

Use `fopen()` to open a file. It returns a `FILE*` pointer.

```c
FILE *file = fopen("example.txt", "r");
if (file == NULL) {
    printf("Error opening file!\n");
    return 1;
}
```

Common file opening modes:

- `"r"` – Read (file must exist)
- `"w"` – Write (creates new or overwrites existing file)
- `"a"` – Append (adds to existing file or creates new)
- `"r+"` – Read/Write (file must exist)
- `"w+"` – Read/Write (creates new or overwrites existing)
- `"a+"` – Read/Append (preserves existing content)

---

### 2. **Writing To a File**

Use `fprintf()` or `fwrite()` to write data.

```c
FILE *file = fopen("example.txt", "w");
if (file) {
    fprintf(file, "Hello, World!\n");
    fclose(file);
}
```

Using `fwrite()` for binary data:

```c
int numbers[] = {1, 2, 3, 4, 5};
FILE *file = fopen("data.bin", "wb");
fwrite(numbers, sizeof(int), 5, file);
fclose(file);
```

---

### 3. **Reading From a File**

Use `fscanf()` for formatted input or `fgets()` for line-by-line reading.

```c
FILE *file = fopen("example.txt", "r");
char buffer[100];
if (file) {
    while (fgets(buffer, sizeof(buffer), file)) {
        printf("%s", buffer);
    }
    fclose(file);
}
```

Using `fread()` for binary data:

```c
int numbers[5];
FILE *file = fopen("data.bin", "rb");
fread(numbers, sizeof(int), 5, file);
fclose(file);
```

---

### 4. **Closing A File**

Always close files using `fclose()` to free system resources.

```c
fclose(file);
```

---

### 5. **Checking For End of File (EOF)**

```c
if (feof(file)) {
    printf("End of file reached.\n");
}
```

---

### 6. **Error Handling**

```c
if (file == NULL) {
    perror("Error opening file");
    return 1;
}
```

This covers the basics of file I/O in C. Let me know if you need more details! 🚀
