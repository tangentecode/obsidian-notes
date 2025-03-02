In Zig, loops are primarily implemented using `while`, `for`, and `inline while/for` constructs. Here's a breakdown of each:

---

### **1. `while` Loop (Basic Looping)**

The `while` loop executes a block of code as long as a condition is `true`.

```zig
var i: usize = 0;
while (i < 5) : (i += 1) {
    std.debug.print("Iteration: {}\n", .{i});
}
```

- `i < 5` is the condition.
- `: (i += 1)` is the post-expression (executed after each iteration).

Equivalent manual form:

```zig
var i: usize = 0;
while (i < 5) {
    std.debug.print("Iteration: {}\n", .{i});
    i += 1;
}
```

#### **Breaking a `while` Loop**

Use `break` to exit early.

```zig
var i: usize = 0;
while (i < 10) : (i += 1) {
    if (i == 5) break;
    std.debug.print("Iteration: {}\n", .{i});
}
```

#### **Skipping Iterations (`continue`)**

Use `continue` to skip to the next iteration.

```zig
var i: usize = 0;
while (i < 10) : (i += 1) {
    if (i % 2 == 0) continue; // Skip even numbers
    std.debug.print("Odd number: {}\n", .{i});
}
```

---

### **2. `for` Loop (Iterating Over Collections)**

The `for` loop iterates over arrays, slices, tuples, or other iterable objects.

```zig
const list = [_]i32{ 1, 2, 3, 4, 5 };
for (list) |item| {
    std.debug.print("Item: {}\n", .{item});
}
```

- `list` is the iterable.
- `|item|` is the value in each iteration.

#### **Iterating with Index**

To get both the index and value:

```zig
for (list, 0..) |item, index| {
    std.debug.print("Index: {}, Value: {}\n", .{index, item});
}
```

---

### **3. Infinite Loop (`while (true)`)**

A loop that runs indefinitely (useful for event loops).

```zig
while (true) {
    std.debug.print("Running...\n", .{});
}
```

To break out, use `break` when needed.

---

### **4. `inline while` and `inline for` (Compile-Time Execution)**

Used in `comptime` to unroll loops at compile time.

```zig
comptime {
    var i: usize = 0;
    inline while (i < 3) : (i += 1) {
        std.debug.print("Compile-time iteration: {}\n", .{i});
    }
}
```

For iterating over tuples at compile time:

```zig
const tuple = .{ "A", "B", "C" };
inline for (tuple) |char| {
    std.debug.print("Compile-time item: {s}\n", .{char});
}
```

---

### **5. `while` with Optional Value Unwrapping**

Useful when dealing with optional values.

```zig
var optional_value: ?i32 = 42;
while (optional_value) |val| {
    std.debug.print("Got value: {}\n", .{val});
    optional_value = null; // End loop
}
```

- If `optional_value` is `null`, the loop exits.

---

### **Summary**

|Loop Type|Usage|
|---|---|
|`while`|General looping with a condition.|
|`for`|Iterating over collections like arrays or slices.|
|`inline while/for`|Compile-time iteration.|
|`while (true)`|Infinite loops (e.g., event loops).|
|`while` with optionals|Unwrapping and iterating over `?T`.|

Would you like an example for a specific use case? 🚀