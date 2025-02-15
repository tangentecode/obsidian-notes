# Types

Here are some basic built-in types, and the syntax for literal values of each type.

|                        | Types                                      | Literals                       |
| ---------------------- | ------------------------------------------ | ------------------------------ |
| Signed integers        | `i8`, `i16`, `i32`, `i64`, `i128`, `isize` | `-10`, `0`, `1_000`, `123_i64` |
| Unsigned integers      | `u8`, `u16`, `u32`, `u64`, `u128`, `usize` | `0`, `123`, `10_u16`           |
| Floating point numbers | `f32`, `f64`                               | `3.14`, `-10.0e20`, `2_f32`    |
| Unicode scalar values  | `char`                                     | `'a'`, `'α'`, `'∞'`            |
| Booleans               | `bool`                                     | `true`, `false`                |

The types have widths as follows:

- `iN`, `uN`, and `fN` are _N_ bits wide,
- `isize` and `usize` are the width of a pointer,
- `char` is 32 bits wide,
- `bool` is 8 bits wide.



### **Quick Rules of Thumb**

- **Working with small numbers?** → `u8`, `i8`, `u16`, `i16`
- **General-purpose?** → `i32` (default)
- **Need big numbers?** → `i64`, `u64`, `i128`, `u128`
- **Indexing an array?** → `usize`
- **Optimizing for performance?** → Stick to `i32` or `u32` unless memory constraints require smaller types.