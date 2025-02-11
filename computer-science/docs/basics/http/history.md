# History

## 📜 History of HTTP

- **HTTP/1.0**: It was the original HTTP. It **opened a new TCP connection for each HTTP** **[request-response](process.md)** exchange, this approach is less efficient when multiple requests are sent in succession, hence the need to address this flaw in later versions

- **HTTP/1.1**: To mitigate the flaws of HTTP/1.0, pipelining was implemented which allowed **multiple HTTP request-response exchanges over a single TCP connection**

- **HTTP/2** goes a step further by multiplexing messages within frames over a single open TCP connection
		- **HTTP/2 messages a not human-readable** and are embedded into frames which allows optimizations like compressions of HTTP headers and multiplexing.

> Part of [this Arcticle](https://hackernoon.com/the-essential-guide-to-http)
