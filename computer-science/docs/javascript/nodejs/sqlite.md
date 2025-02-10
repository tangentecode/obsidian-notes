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


## With error checking

```javascript
const sqlite3 = require('sqlite3').verbose();

// Open a database connection (creates a file if it doesn’t exist)
const db = new sqlite3.Database('database.db', (err) => {
    if (err) {
        console.error('Error opening database:', err.message);
    } else {
        console.log('Connected to SQLite database.');
    }
});

// Create a table
db.run(`CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)`);

// Insert data
db.run(`INSERT INTO users (name, age) VALUES (?, ?)`, ['Alice', 25], function (err) {
    if (err) {
        return console.error('Error inserting data:', err.message);
    }
    console.log('Inserted row with ID:', this.lastID);
});

// Query data
db.all(`SELECT * FROM users`, [], (err, rows) => {
    if (err) {
        throw err;
    }
    console.log(rows);
});

// Close the database
db.close();

```