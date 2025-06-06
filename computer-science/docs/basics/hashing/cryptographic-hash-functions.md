# Cryptographic-hash-functions

- Basics are the same like common [hash functions](hash-functions.md) but they follow a certain set of rules:

	1. **One-way process**: You can create a hash from the data, but you can't reverse the hash to get the original data.
	2.  **Unique output**: Even a tiny change in the input produces a completely different hash
		(this is called the **avalanche effect**).
	3.  **Fixed size**: The output hash is always the same length, no matter how large or small the input is.
	4.  **Secure**: It's extremely difficult to find two different inputs that produce the same hash (called a **collision**).

### Common Uses:

1. **Password storage**: Instead of storing passwords, websites store their hashes for security.

2. **Data integrity**: To ensure files haven't been tampered with, their hashes are checked.

3. **Digital signatures**: Hashes help verify the authenticity of digital communications.

> Most well known cryptographic hash algorithm is **SHA-256** which is used for **Bitcoin**
> Here is an [visualization](https://sha256algorithm.com/)
