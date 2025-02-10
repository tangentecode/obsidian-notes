## E
- Similar to lambda [functions](computer-science/docs/javascript/functions.md) in [python](contents-python.md) you can shorten functions without using the `function` keyword by using the `=>` operator:
- You define a arrow function like you initialize a normal [variable](computer-science/docs/javascript/variables.md)
- Often these are **constants**
- **Parameters** are specified after the `=` sign and before the `=>`
- If there are multiple parameters use parenthesis

```javascript
const add = (a, b) => a + b; 

console.log(add(2, 3));
```