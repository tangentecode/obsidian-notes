## What is SQLite?

- SQLite is a **lightweight**, self-contained **database engine**.
- It is `serverless`, meaning there's no need for a separate database server process.
-  Ideal for embedded systems, small-scale applications, and local data storage.
- Data is stored in a single `.sqlite` or `.db` file.

## Key Features of SQLite

1. File-based: Entire database stored in a file.
2. Zero-configuration: No setup or installation required.
3. Cross-platform: Works on almost any operating system.
4. ACID-compliant: Guarantees reliable transactions.
5. SQL Support: Full SQL standard syntax support.

## Create a Database:

```shell
sqlite3 example.db
```

This creates a **new database** file named `example.db` (if it doesn't already exist)
