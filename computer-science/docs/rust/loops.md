Rust provides several types of loops for different use cases: `loop`, `while`, and `for`. Let’s go over each one with examples.

---

## **1. `loop` (Infinite Loop)**
The `loop` keyword creates an infinite loop that runs until explicitly broken with `break`.

```rust
fn main() {
    let mut counter = 0;

    loop {
        println!("Counter: {}", counter);
        counter += 1;

        if counter == 5 {
            break; // Exit the loop
        }
    }
}
```

- Use `continue` to skip to the next iteration:
  ```rust
  fn main() {
      let mut num = 0;

      loop {
          num += 1;

          if num == 3 {
              continue; // Skips printing 3
          }

          println!("Number: {}", num);

          if num == 5 {
              break;
          }
      }
  }
  ```

---

## **2. `while` Loop**
Runs as long as the condition is `true`.

```rust
fn main() {
    let mut number = 3;

    while number > 0 {
        println!("Number: {}", number);
        number -= 1;
    }

    println!("Done!");
}
```

---

## **3. `for` Loop (Iterating Over Ranges and Collections)**
### **Iterating Over a Range**
Rust provides `for` loops for iterating over a range of numbers:

```rust
fn main() {
    for i in 1..5 { // Exclusive range (1 to 4)
        println!("i: {}", i);
    }
}
```

To include the upper bound, use `1..=5`:

```rust
fn main() {
    for i in 1..=5 { // Inclusive range (1 to 5)
        println!("i: {}", i);
    }
}
```

### **Iterating Over a Collection**
```rust
fn main() {
    let numbers = [10, 20, 30, 40, 50];

    for num in numbers.iter() {
        println!("Number: {}", num);
    }
}
```

---

## **4. Loop Labels (Nesting Loops)**
Rust allows you to label loops and control them using `break` and `continue`.

```rust
fn main() {
    'outer: for i in 1..=3 {
        for j in 1..=3 {
            if i == 2 && j == 2 {
                break 'outer; // Breaks out of the outer loop
            }
            println!("i: {}, j: {}", i, j);
        }
    }
}
```

---

## **5. Using `loop` as an Expression**
You can return a value from a `loop`:

```rust
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2; // Returns 20
        }
    };

    println!("Result: {}", result);
}
```

---

### **Summary**
- **`loop`** → Infinite loop, needs `break` to stop.
- **`while`** → Runs while a condition is true.
- **`for`** → Iterates over ranges and collections.
- **Loop Labels** → Control nested loops with `'label`.
- **Returning from a `loop`** → Use `break value`.

Would you like some advanced examples, like iterators or concurrency loops? 🚀