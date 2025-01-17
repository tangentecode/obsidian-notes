## What is a pointer?


- Create variable:
```c
int x = 4;
```


- **Pointer to variable**
```c
int * pX = &x;
```

- English: integer pointer named `pX` is set to the address of `x`
- If `*` is used next to a [type](computer-science/docs/c/types.md): **pointer to that type** 
- No type nearby: **pointer get dereferenced** which means it takes the value at that 
### Memory:

| Adress | Value       |
| ------ | ----------- |
| 0x1000 | Ox4 (x)     |
| 0x1004 | 0x1000 (pX) |
| 0x1008 |             |
| 0x100C |             |
| ...    |             |






- Good vid by [Low Level Learning](https://www.youtube.com/watch?v=2ybLD6_2gKM&t=438s)
- 