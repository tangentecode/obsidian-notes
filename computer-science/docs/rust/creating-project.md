# Creating-project

- Use

```shell
cargo new project_name
```

- This will create:
```shell
project_name/
│
├── .gitignore         # Contains the ignored files for git
├── Cargo.toml         # Dependecies
├── src/               
│   └── main.rs        # Main application code
├── .git/              # Data for the Git repo
│   └── ...

```

> `cargo` automatically initializes a git