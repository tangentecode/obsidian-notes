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

// Create a table 
db.run(`CREATE TABLE IF NOT EXISTS users ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER )`);

// Insert data
db.run(`INSERT INTO users (name, age) VALUES (?, ?)`, ['Alice', 25], function () { console.log('Inserted row with ID:', this.lastID); }); 

// Query data 
db.all(`SELECT * FROM users`, [], (_, rows) => { console.log(rows); }); 

// Close the database 
db.close()
```
