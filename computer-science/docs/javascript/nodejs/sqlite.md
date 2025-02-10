# Sqlite

## Installation

- Install via [npm](managing-dependencies.md):

```shell
npm install sqlite3
```

## Usage

- Similar to [contents-sqlite](contents-sqlite.md)

```javascript
// Import sqlite3
const sqlite3 = require('sqlite3').verbose();


const db = new sqlite3.Database('database.db');
```
