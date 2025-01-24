- _Bubble sort_ is another sorting algorithm that works by repeatedly swapping elements to “bubble” larger elements to the end.

- The pseudocode for Bubble sort is:
    
```
Repeat n-1 times
    For i from 0 to n–2
        If numbers[i] and numbers[i+1] out of order
            Swap them
    If no swaps
        Quit
```

- [running time](running-time.md) is:
	1. worst-case: <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>O</mi>
  <mo stretchy="false">(</mo>
  <msup>
    <mi>n</mi>
    <mn>2</mn>
  </msup>
  <mo stretchy="false">)</mo>
</math>
	2. best-case: <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi mathvariant="normal">&#x3A9;</mi>
  <mo stretchy="false">(</mo>
  <mi>n</mi>
  <mo stretchy="false">)</mo>
</math>


- [Visualize](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html) this algorithm