- **No libraries required** unlike [Python](computer-science/docs/python/regex.md) or [C](contents-c.md)
- Use `match()` to match a text with a predefined [pattern](computer-science/docs/basics/regex.md)
- Access the parts where 

```javascript
const text = "There are 123 apples";
const pattern = /\d+/;
const match = text.match(pattern);
console.log(match[0]);  // Output: 123

```