# GET-POST

### **Key Characteristics of GET**

✅ **Retrieves Data** from the server  
✅ **Uses URL Parameters** (query strings)  
✅ **Safe and Idempotent** (multiple identical requests have the same effect)  
✅ **Can Be Cached** by browsers and proxies  
✅ **Less Secure** because parameters appear in the URL

### **Key Characteristics of POST**

✅ **Sends Data in the Request Body** (not in the URL)  
✅ **Creates or Updates Resources** on the server  
✅ **Non-Idempotent** (multiple identical requests create multiple entries)  
✅ **More Secure than GET** (data isn't logged in URLs or browser history)

### **POST Vs. GET**

|Feature|POST|GET|
|---|---|---|
|Purpose|Send data (create/update)|Retrieve data|
|Data Location|Request body|URL|
|Idempotent?|❌ No|✅ Yes|
|Cached?|❌ No|✅ Yes|
|Secure for sensitive data?|✅ Yes|❌ No|
