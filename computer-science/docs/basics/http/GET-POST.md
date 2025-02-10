

### **Key Characteristics of GET**

✅ **Retrieves Data** from the server  
✅ **Uses URL Parameters** (query strings)  
✅ **Safe and Idempotent** (multiple identical requests have the same effect)  
✅ **Can Be Cached** by browsers and proxies  
✅ **Less Secure** because parameters appear in the URL

### **POST vs. GET**

|Feature|POST|GET|
|---|---|---|
|Purpose|Send data (create/update)|Retrieve data|
|Data Location|Request body|URL|
|Idempotent?|❌ No|✅ Yes|
|Cached?|❌ No|✅ Yes|
|Secure for sensitive data?|✅ Yes|❌ No|