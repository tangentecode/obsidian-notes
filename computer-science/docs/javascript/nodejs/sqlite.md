# Sqlite

## Installation

- Install via [npm](managing-dependencies.md):

```shell
npm install sqlite3
```

## Usage

- Similar to [sqlite in python](contents-sqlite.md)

```javascript
// Import sqlite3
const sqlite3 = require('sqlite3').verbose();

// Open a database connection (creates a file if it doesn’t exist)
const db = new sqlite3.Database('database.db');
```
