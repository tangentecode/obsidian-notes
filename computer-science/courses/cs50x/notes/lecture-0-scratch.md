# lecture-0-scratch

## Content

1. [Computer Science](#computer-science)  
2. [Binary](#binary)  
3. [ASCII](#ascii)  
4. [UNICODE](#unicode)  
5. [RGB](#rgb)  
6. [Algorithm](#algorithm)  
7. [Pseudocode](#pseudocode)  
8. [Scratch](#scratch)  

## Computer Science

> Computer science is solving problems and
> creating output from by modifying user input

![](input-output.png)

## Binary

- Computer count in binary
- If you imagine a light bulb: 1 means light bulb one, 2 means light bulb off
- Representing numbers in Binary:

Example:

```c
4 2 1 
1 1 1
```

would equal **seven**

- Generally you use 8 Bits so one Byte

| 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |

- with one byte you can count up to 255 (in binary: 11111111)

## ASCII

> ASCII = **American Standard Code for Information Interchange**

- ASCII is a standard to represent letters and some special characters in binary
- Heres an very basic ASCII table:
<table>
	<thead>
		<tr>
			<th>Letter</th>
			<th>Binary</th>
			<th>Decimal</th>
		</tr>
	</thead>
	<tbody>
		<tr><td>A</td><td>01000001</td><td>65</td></tr>
		<tr><td>B</td><td>01000010</td><td>66</td></tr>
		<tr><td>C</td><td>01000011</td><td>67</td></tr>
		<tr><td>D</td><td>01000100</td><td>68</td></tr>
		<tr><td>E</td><td>01000101</td><td>69</td></tr>
		<tr><td>F</td><td>01000110</td><td>70</td></tr>
		<tr><td>G</td><td>01000111</td><td>71</td></tr>
		<tr><td>H</td><td>01001000</td><td>72</td></tr>
		<tr><td>I</td><td>01001001</td><td>73</td></tr>
		<tr><td>J</td><td>01001010</td><td>74</td></tr>
		<tr><td>K</td><td>01001011</td><td>75</td></tr>
		<tr><td>L</td><td>01001100</td><td>76</td></tr>
		<tr><td>M</td><td>01001101</td><td>77</td></tr>
		<tr><td>N</td><td>01001110</td><td>78</td></tr>
		<tr><td>O</td><td>01001111</td><td>79</td></tr>
		<tr><td>P</td><td>01010000</td><td>80</td></tr>
		<tr><td>Q</td><td>01010001</td><td>81</td></tr>
		<tr><td>R</td><td>01010010</td><td>82</td></tr>
		<tr><td>S</td><td>01010011</td><td>83</td></tr>
		<tr><td>T</td><td>01010100</td><td>84</td></tr>
		<tr><td>U</td><td>01010101</td><td>85</td></tr>
		<tr><td>V</td><td>01010110</td><td>86</td></tr>
		<tr><td>W</td><td>01010111</td><td>87</td></tr>
		<tr><td>X</td><td>01011000</td><td>88</td></tr>
		<tr><td>Y</td><td>01011001</td><td>89</td></tr>
		<tr><td>Z</td><td>01011010</td><td>90</td></tr>
	</tbody>
</table>

- [More information](https://en.wikipedia.org/wiki/ASCII)

## UNICODE

- Unicode is similar to ASCII but with an extended range characters
- for example emojis
- ![😀](https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f600.png)  
- [More information](https://en.wikipedia.org/wiki/Unicode)

## RGB

> RGB = Red, Green, Blue

- Zeros and ones can be used to represent color
 ![](rgb.png)  
- equals
	![](yellow-rgb.png)

- one RGB stored pixel needs 3 bytes of memory

## Algorithm

- An _algorithm_ is a step-by-step set of instructions to solve a problem

![](algorithm-time.png)

- More about in [[lecture-3-algorithms]]

## Pseudocode

- Is an way of representing code that is more readable by humans but doesn't compile or run
- Example:

```c
1  Pick up phone book
2  Open to middle of phone book
3  Look at page
4  If person is on page
5      Call person
6  Else if person is earlier in book
7      Open to middle of left half of book
8      Go back to line 3
9  Else if person is later in book
10     Open to middle of right half of book
11     Go back to line 3
12 Else
13     Quit
```

## Scratch

### Scratch Basics: [Havard](https://cs50.harvard.edu/x/2025/notes/0/#scratch)

### Use Scratch: [Scratch](https://scratch.mit.edu/)
