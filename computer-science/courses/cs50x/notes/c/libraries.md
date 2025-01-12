## Include

- Use `#include` to import third party and built in library's
- Common built in libraries are:

	- **stdio.h**: Provides input and output functions like `printf`, `scanf`, file operations (`fopen`, `fclose`, etc.), and error handling (`perror`).
    
	- **stdlib.h**: Contains general utilities such as memory management (`malloc`, `free`, `realloc`), process control (`exit`, `system`), and other miscellaneous functions (`atoi`, `rand`, `abs`).
    
	- **math.h**: Includes mathematical functions like `sin`, `cos`, `sqrt`, `pow`, and constants like `M_PI`.
	    
	- **string.h**: Offers string manipulation functions such as `strcpy`, `strcat`, `strlen`, `strcmp`, and memory functions like `memset`, `memcpy`, `memmove`.
	    
	- **ctype.h**: Provides functions for character handling such as `isalpha`, `isdigit`, `tolower`, `toupper`.
	    
	- **time.h**: Includes functions for date and time operations, such as `time`, `ctime`, `gmtime`, `strftime`.
	    
	- **stdbool.h**: Defines the boolean data type and constants `true` and `false` (if C99 or later).
	    
	- **assert.h**: Defines the `assert` macro for debugging purposes, to check assumptions in the program.
	    
	- **errno.h**: Provides error numbers set by system calls and functions, with macros like `errno`, `perror`, `strerror`.
## Example

```
#include <stdio.h>
```

Imports Stdio for varios functions like ``