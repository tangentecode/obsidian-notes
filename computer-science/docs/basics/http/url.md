# Url

### Basic Guide to URLs

A **URL (Uniform Resource Locator)** is the address used to access resources on the internet. It consists of multiple parts that define where and how to retrieve a resource.

#### **1. Structure of a URL**

A standard URL follows this format:

```c
protocol://domain:port/path?query#fragment
```

Example:

```c
https://www.example.com:8080/docs/page.html?search=hello#section2
```

#### **2. Components of a URL**

- **Protocol (Scheme):** Defines how the browser communicates with the server.
		
	- Examples: `http://`, `https://`, `ftp://`
	- `https://` is the secure version of HTTP (encrypted with SSL/TLS).

- **Domain (Host):** The name of the website or server.
		
	- Example: `www.example.com`
	- Can also be an IP address like `192.168.1.1`.

- **Port (Optional):** Specifies which port the server listens to.
		
	- Default ports: `80` for HTTP, `443` for HTTPS
	- Example: `:8080`

- **Path:** Specifies the location of a resource on the server.
		
	- Example: `/docs/page.html`

- **Query String (Optional):** Contains parameters for dynamic content, separated by `?`.
		
	- Example: `?search=hello&page=2`
	- Multiple parameters are separated with `&`.

- **Fragment (Optional):** Points to a specific section within a page, using `#`.		
	- Example: `#section2`

#### **3. Special Types of URLs**

- **Relative URLs:** Paths relative to the current domain (e.g., `/about.html`).
- **Absolute URLs:** Full URLs including the protocol and domain (e.g., `https://example.com/about.html`).
- **Data URLs:** Used to embed small files (e.g., `data:image/png;base64,…`).

#### **4. Common URL Encoding Rules**

- Spaces are replaced with `%20` or `+`.
- Special characters are encoded (e.g., `?` → `%3F`, `&` → `%26`).
