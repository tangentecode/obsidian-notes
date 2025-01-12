## Compiling

- File gets compiled to `Machine Code` in these steps
	1. **Preprocessing**: every line that starts with a `#` Symbol (e.g. `#define`, [#include](libraries.md)) gets compiled
	2. **Compiling**: gets converted to `Assembly Code`
	3. Assembling: runs `Assembly Code`
	4. **linking**

## Assembly
- Low level language
- Based on processor architecture
- Directly moves data in memory and performs other operation
- Example:
```asm
...
main:
    .cfi_startproc
# BB#0:
    pushq    %rbp
.Ltmp0:
    .cfi_def_cfa_offset 16
.Ltmp1:
    .cfi_offset %rbp, -16
    movq    %rsp, %rbp
.Ltmp2:
    .cfi_def_cfa_register %rbp
    subq    $16, %rsp
    xorl    %eax, %eax
    movl    %eax, %edi
    movabsq    $.L.str, %rsi
    movb    $0, %al
    callq    get_string
    movabsq    $.L.str.1, %rdi
    movq    %rax, -8(%rbp)
    movq    -8(%rbp), %rsi
    movb    $0, %al
    callq    printf
    ...
```

## Machine Code

-