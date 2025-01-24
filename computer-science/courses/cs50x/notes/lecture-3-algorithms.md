## Linear Search


- a linear search look on every index of an array one by one an the return a [boolean](computer-science/docs/c/types.md) or [binary](binary.md) if the desired value can be found at that index 

![](linear_search.png)


- Pseudocode:
```
For each door from left to right
    If 50 is behind door
        Return true
Return false
```


## Binary search

- Assuming that the values in an [array](lecture-2-arrays.md) have been ordered from left to right the array can be always split up into two parts:
	1. The value is larger than the current index value
	2. The value is smaller than the current index value

- Pseuduocode:
```
If no doors left
    Return false
If 50 is behind middle door
    Return true
Else if 50 < middle door
    Search left half
Else if 50 > middle door
    Search right half
```


## Running time

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi mathvariant="normal">&#x3A9;</mi>
</math> represents the **best-case**
<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi mathvariant="normal">&#x398;</mi>
</math> represents the **worst-case**

... that an algorithm 