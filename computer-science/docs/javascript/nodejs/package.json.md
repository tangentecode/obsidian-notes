# package.json

The `package.json` file is a core component of any Node.js project using NPM (Node Package Manager). It stores important project metadata, dependencies, scripts, and configurations.

---

### **1. Creating a `package.json`**

To generate a `package.json` file, run:

```sh
npm init
```

or use the automatic mode with:

```sh
npm init -y
```

This creates a default `package.json` file without prompts.

---

### **2. Key Sections in `package.json`**

A typical `package.json` looks like this:

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "description": "A simple project",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "test": "echo \"No tests specified\" && exit 1"
  },
  "dependencies": {
    "express": "^4.18.2"
  },
  "devDependencies": {
    "nodemon": "^2.0.22"
  },
  "engines": {
    "node": ">=14"
  },
  "license": "MIT"
}
```

---

### **Basic Information**

- **`name`** – Project name (must be lowercase and URL-friendly).
- **`version`** – Version number following [semantic versioning (semver)](https://semver.org/).
- **`description`** – Short summary of the project.
- **`main`** – Entry point file (default: `index.js`).
- **`license`** – Specifies the license type (e.g., `"MIT"`).