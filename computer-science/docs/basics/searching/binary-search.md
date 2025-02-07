# Binary-search

- Assuming that the values in an [array](lecture-2-arrays.md) have been ordered from left to right the array can be always split up into two parts:
	1. The value is larger than the current index value
	2. The value is smaller than the current index value

- Pseuduocode:

```c
If no doors left
    Return false
If 50 is behind middle door
    Return true
Else if 50 < middle door
    Search left half
Else if 50 > middle door
    Search right half
```
