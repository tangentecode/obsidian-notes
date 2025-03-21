# Merge-sort

- leveraging recursion in our quest for a more efficient sort algorithm and implement what is called **_merge sort_**, a very efficient sort algorithm

- The pseudocode for Merge sort is:

```c
If only one number
    Quit
Else
    Sort left half of number
    Sort right half of number
    Merge sorted halves
```

- [running time](running-time.md) is:
	1. worst-case: <math xmlns="http://www.w3.org/1998/Math/MathML">
	<mi>O</mi>
	<mo stretchy="false">(</mo>
	<mi>n</mi>
	<mi>log</mi>
	<mo data-mjx-texclass="NONE">&#x2061;</mo>
	<mi>n</mi>
	<mo stretchy="false">)</mo>
</math>
	2. best-case: <math xmlns="http://www.w3.org/1998/Math/MathML">
	<mi mathvariant="normal">&#x3A9;</mi>
	<mo stretchy="false">(</mo>
	<mi>n</mi>
	<mi>log</mi>
	<mo data-mjx-texclass="NONE">&#x2061;</mo>
	<mi>n</mi>
	<mo stretchy="false">)</mo>
</math> 

- bestand worst-case still have the same running time because the algorithm still needs to [iterate](computer-science/docs/c/loops.md) over each index

- [Visualize](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html) this algorithm
