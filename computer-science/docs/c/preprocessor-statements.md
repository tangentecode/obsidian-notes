In C, preprocessor directives are commands that are processed **before** compilation. Here’s a complete list of all possible preprocessor directives in C:

### **1. Conditional Compilation Directives**

These allow conditional compilation of code based on defined macros.

- `#if` – Starts a conditional block.
- `#ifdef` – Checks if a macro is defined.
- `#ifndef` – Checks if a macro is **not** defined.
- `#else` – Provides an alternative block if the condition in `#if`, `#ifdef`, or `#ifndef` fails.
- `#elif` – Else-if for `#if` conditions.
- `#endif` – Ends a conditional block.

✅ **Example:**

```c
#ifdef _WIN32
    #include <windows.h>
#else
    #include <unistd.h>
#endif
```

---

### **2. Macro Definition and Undefinition**

These define and remove macros.

- `#define` – Defines a macro.
- `#undef` – Undefines a macro.

✅ **Example:**

```c
#define PI 3.14159
#undef PI  // PI is now undefined
```

---

### **3. File Inclusion Directives**

These allow including external files.

- `#include <filename>` – Includes a system header file.
- `#include "filename"` – Includes a user-defined file.

✅ **Example:**

```c
#include <stdio.h>   // Standard library
#include "myheader.h"  // Custom header
```

---

### **4. Pragma Directives (Compiler-Specific)**

`#pragma` is used for compiler-specific settings.

- `#pragma once` – Ensures a file is included only once.
- `#pragma pack(n)` – Controls memory alignment.
- `#pragma warning` – Controls compiler warnings.
- `#pragma comment` – Adds linker options (MSVC-specific).

✅ **Example:**

```c
#pragma once  // Prevents multiple inclusions of a file
#pragma pack(1)  // Sets 1-byte structure alignment
#pragma comment(lib, "user32.lib")  // Links a Windows library
```

---

### **5. Line Control**

Used to manipulate line numbers and file names in error messages.

- `#line number "filename"`

✅ **Example:**

```c
#line 100 "custom_file.c"
```

If an error occurs after this line, it will be reported as if it happened in `custom_file.c` at line 100.

---

### **6. Error and Warning Directives**

Used to trigger compile-time errors or warnings.

- `#error "Message"` – Stops compilation with a custom error message.
- `#warning "Message"` – Shows a warning but continues compilation (not in standard C, but supported by GCC and Clang).

✅ **Example:**

```c
#ifndef CONFIG_DEFINED
    #error "CONFIG_DEFINED is required!"
#endif
```

---

### **7. Null Directive**

- `#` – A single `#` at the start of a line does nothing; it’s sometimes used for readability.

✅ **Example:**

```c
#
#include <stdio.h>
```

---

### **8. Miscellaneous**

- `##` (Token pasting) – Joins two tokens together.
- `#` (Stringizing) – Converts a macro argument into a string.

✅ **Example:**

```c
#define CONCAT(a, b) a##b
int CONCAT(my, var) = 10;  // Expands to int myvar = 10;

#define STRINGIFY(x) #x
printf("%s", STRINGIFY(Hello World));  // Prints "Hello World"
```

---

## **Summary Table**

|Directive|Description|
|---|---|
|`#define`|Defines a macro|
|`#undef`|Undefines a macro|
|`#include`|Includes a file|
|`#if` / `#elif` / `#else` / `#endif`|Conditional compilation|
|`#ifdef` / `#ifndef`|Checks if a macro is (not) defined|
|`#error` / `#warning`|Produces a compile-time error or warning|
|`#pragma`|Compiler-specific settings|
|`#line`|Changes line number information|
|`##` / `#`|Token pasting and stringizing|

Would you like a deeper explanation of any specific directive? 🚀