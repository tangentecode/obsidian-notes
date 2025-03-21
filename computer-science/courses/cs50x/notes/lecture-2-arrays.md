# lecture-2-arrays

## Contents

1. [Compiling](#compiling)
2. [Assembly](#assembly)
3. [Machine Code](#machine-code)
4. [Arrays](#arrays)
5. [Strings](#strings)
6. [Misc](#misc)
7. [Command Line Arguments](#command-line-arguments)
8. [Cryptography](#cryptography)

## Compiling

- File gets compiled to `Machine Code` in these steps
	1. **Preprocessing**: every line that starts with a `#` Symbol (e.g. `#define`, [include](computer-science/docs/c/libraries.md)) gets compiled
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

- Machine lowest abstraction layer
- Binary
- Nearly impossible to read by an human
- Example:

```c
01111111010001010100110001000110
00000010000000010000000100000000
00000000000000000000000000000000
00000000000000000000000000000000
00000001000000000011111000000000
00000001000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
10100000000000100000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
01000000000000000000000000000000
00000000000000000100000000000000
00001010000000000000000100000000
01010101010010001000100111100101
01001000100000111110110000010000
00110001110000001000100111000111
01001000101111100000000000000000
00000000000000000000000000000000
00000000000000001011000000000000
11101000000000000000000000000000
00000000010010001011111100000000
00000000000000000000000000000000
00000000000000000000000001001000
...
```

## Arrays

- Used to chain multiple values of the same [type](computer-science/docs/c/types.md) together
- The values live at an index on the `Array` that start with 0 directly after each other in memory
- Declare `Arrays` like in [variables](computer-science/docs/c/variables.md)

## Strings

- A `string` is an [data types](computer-science/docs/c/types.md) that consist of an `Array` of [chars](computer-science/docs/c/types.md)
- after the last character of `string` there's always an Escape Character (`\0`) stored at the last index of the array in Memory to indicate the end of the `string`
	![](string.png)
- Regarding the explanation in [lecture-0-scratch](lecture-0-scratch.md) about `ASCII` it would look like this in decimal notation
	![](string-decimal.png)

## Strlen

- To simplify the process of counting the length of an string there is the `strlen` Function in the `string.h` library

## Misc

- In `ASCII` you can subtract 32 from a uppercase [char](computer-science/docs/c/types.md) to get its lowercase variant:

```c
char a = 'A' - 32;
```

- Use [ctype.h](computer-science/docs/c/libraries.md) to simplify this action

## Command Line Arguments

- The [main](lecture-1-c.md) function takes two special parameters:
	1. **argc**: `int` number of arguments provided in the command line
	2. **argv**: Command Line Arguments as an array of [strings](computer-science/docs/c/types.md) starting with the file name at index 0

- Example:

```c
int main(int argc, string argv[]) {
	return 0;
}
```

## Cryptography

- Cryptography is the art of ciphering and deciphering a message.
- `plaintext` and a `key` are provided to a `cipher`, resulting in ciphered text.
	![](ciphertext.png)
