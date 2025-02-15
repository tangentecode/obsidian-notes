# Executing-code

## Basics

- go to your previously [created project](creating-project.md) and use `cargo run` to build and run your binary:

```shell
$ cd exercise
$ cargo run
   Compiling exercise v0.1.0 (/home/mgeisler/tmp/exercise)
    Finished dev [unoptimized + debuginfo] target(s) in 0.75s
     Running `target/debug/exercise`
Hello, world!
```

## Advanced

- `cargo check`: to quickly check your project for errors 

- `cargo build` to compile it without running it. Output: `target/debug/`  

- `cargo build --release` to produce an optimized release build in `target/release/`.
