## Linear Search


- a linear search look on every index of an array one by one an the return a [boolean](computer-science/docs/c/types.md) or [binary](binary.md) if the desired value can be found at that index 

![](linear-search.png)


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

**big O Notation:**

![](big-o-notation.png)

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi mathvariant="normal">&#x3A9;</mi>
</math> represents the **best-case**
<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi mathvariant="normal">&#x398;</mi>
</math> represents the **worst-case**

... that an algorithm takes to run

Examples:
	1. <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>O</mi>
  <mo stretchy="false">(</mo>
  <mn>1</mn>
  <mo stretchy="false">)</mo>
</math> is always the fastest because it has an constant time
	2. Linear search was of order <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>O</mi>
  <mo stretchy="false">(</mo>
  <mi>n</mi>
  <mo stretchy="false">)</mo>
</math> because it could take _n_ steps in the worst-case to run.
	3. Binary search was of order <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>O</mi>
  <mo stretchy="false">(</mo>
  <mi>log</mi>
  <mo data-mjx-texclass="NONE">&#x2061;</mo>
  <mi>n</mi>
  <mo stretchy="false">)</mo>
</math> because it would take fewer and fewer steps to run, even in the worst-case.


> _Asymptotic notation_ is the measure of how well algorithms perform as the input gets larger.

## Structs in c

 - refer to [structs](structs.md) c guide


## [Sorting](contents-sorting.md)

## [Recursion in C](computer-science/docs/c/loops.md)

## Summing Up

- Algorithms.
- Big _O_ notation.
- Binary search and linear search.
- Various sort algorithms, including bubble sort, selection sort, and merge sort.
- Recursion.