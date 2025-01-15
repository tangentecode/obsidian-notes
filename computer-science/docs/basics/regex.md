## General

1. **Literals**
    - Match exact text.  
        Example: `cat` matches "cat" in "The cat sat on the mat."

2. **Metacharacters**
    
    - Special characters with unique meanings:
        - `.`: Matches any single character except newline.
        - `^`: Matches the start of a string.
        - `$`: Matches the end of a string.
        - `*`: Matches 0 or more of the preceding element.
        - `+`: Matches 1 or more of the preceding element.
        - `?`: Matches 0 or 1 of the preceding element.
        - `[]`: Matches any one character inside the brackets.
        - `|`: Acts as an OR operator.
        - `\`: Escapes a metacharacter to treat it as a literal.

3. **Character Classes**
    
    - Predefined shorthand for common groups of characters:
        - `\d`: Matches any digit (0–9).
        - `\D`: Matches any non-digit.
        - `\w`: Matches any word character (alphanumeric or underscore).
        - `\W`: Matches any non-word character.
        - `\s`: Matches any whitespace (space, tab, newline).
        - `\S`: Matches any non-whitespace character.

4. **Quantifiers**

    - Specify the number of times an element must appear:
        - `{n}`: Exactly n times.
        - `{n,}`: At least n times.
        - `{n,m}`: Between n and m times.

5.  **Groups and Capturing**
    
    - Parentheses `()` define groups.  
        Example: `(cat)` captures "cat".
    - Use `\1`, `\2`, etc., to reference groups.

5. **Special Sequences**
    
    - `\b`: Matches a word boundary.
    - `\B`: Matches a non-word boundary.

## How to use when programming

- Python [Re library](computer-science/docs/python/regex.md)
- In [C](contents-c.md) include `regex.h`
- JavaScript: 

> **Tip:** Test regex patterns interactively using tools like [regex101](https://regex101.com/)
