# 📝 HTTP Messages

There are two types of HTTP messages:

- **HTTP Request** messages sent by the client to the server
- **HTTP Response** messages sent from the server to the client each of these messages has a format in which they are generated

### HTTP Request Message
![](Pasted%20image%2020250211082903.png)
The request message consists of the following:


- The HTTP method: these methods are usually a verb like 'GET' or 'POST' that defines the operation applied by the client to the resource, in this case, the HTTP method is GET note HTTP methods are case sensitive.
- The Request-URI: identifies the resource upon which the HTTP method is applied. The exact resource is determined using the Request-URI and the Host header field
- The HTTP protocol version: In this case the version is HTTP/1.1
- Request headers: Conveys additional information about the request and about the client itself to the servers, in this case, we have the following request headers;
    - Host: It specifies the internet port(IP) address and port number of the server where the requested resource is stored, an IP address without a trailing port defaults to port number 80 for HTTP requests and 443 for HTTPS requests. Note without specifying the Host header field, the request will return an error
    - Accept-Language: Specifies which language the client is able to understand, in this case, the language is 'en' for English, other values could be 'fr' for French
- Body: An optional field that contains the information being sent to the server for storage, mainly used when using HTTP methods like POST, PATCH

### HTTP Response Message

The response message consists of the following:

  

- The HTTP protocol version: In this case the version is HTTP/1.1
- Status code: in this case, is 200
- Response headers: Conveys additional information about the response and about the server itself to the client, in this case, we have the following request headers;
    - Accept-Ranges: It is used by the server to show its support for partial requests
    - Server: Describes the software used by the origin by the origin server that handled the request
    - Content-type: This header field indicates the resource content type
    - E-Tag: it identifies the specific resource version
- Body: An optional field that contains fetched information being sent to the client from the server, mainly used when using HTTP methods like GET.