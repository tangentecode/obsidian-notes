## What is SQLite?

SQLite is a lightweight, self-contained database engine.
It is serverless, meaning there’s no need for a separate database server process.
Ideal for embedded systems, small-scale applications, and local data storage.
Data is stored in a single .sqlite or .db file.

Key Features of SQLite:

File-based: Entire database stored in a file.
    Zero-configuration: No setup or installation required.
    Cross-platform: Works on almost any operating system.
    ACID-compliant: Guarantees reliable transactions.
    SQL Support: Full SQL standard syntax support.

Basic SQLite Commands:

    Create a Database:

sqlite3 example.db

This creates a new database file named example.db (if it doesn’t already exist)