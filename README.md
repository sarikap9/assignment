# Assignments

The repository contains 3 folders for 3 different tasks of this assignment:
1. CORS (Cross Origin Resource Sharing)
2. API_Throughput_Middleware
3. Monitoring using Prometheus and Grafana
---
## Cross Origin Resource Sharing (CORS)

## Overview
This project focuses on enabling **CORS (Cross-Origin Resource Sharing)** for an API built using python. The primary requirement was to **allow CORS only for GET requests**, ensuring secure cross-origin access while preventing unintended exposure of other HTTP methods.

## CORS Implementation
While implementing CORS, i have explored different strategies and applied based on use-case requirements:

### 1️⃣ Single-Origin CORS
- Restricts access to requests coming from a specific origin.
- This is the most secure and suitable for **internal applications** where only one frontend interacts with the backend.

### 2️⃣ Multiple-Origin CORS
- Extends CORS access to a predefined set of allowed origins.
- Useful when multiple frontend clients (e.g., web and mobile applications) need to interact with the API securely.

### 3️⃣ Preflight Request Handling
- Handles **OPTIONS** requests, which are sent by browsers before executing **non-simple requests** (like POST, PUT, DELETE with custom headers).
- Ensures that the browser can verify which methods are allowed before making the actual request.

## Additional CORS Strategies
During research, i have identified additional CORS strategies that are useful for various scenarios:

### 4️⃣ Dynamic Origin CORS
- Instead of hardcoding allowed origins, the server dynamically verifies and permits origins based on a **database or configuration file**.
- Recommended for **SaaS or multi-tenant systems** where allowed origins may change over time.

### 5️⃣ Credentialed Requests CORS
- Required when dealing with **authenticated requests** (e.g., APIs using cookies or authorization headers).
- Ensures that credentials (such as session cookies) can be securely transmitted while maintaining strict origin controls.

### 6️⃣ Wildcard CORS
- Allows requests from **any origin (`*`)**.
- Typically used for **open/public APIs** where unrestricted cross-origin access is necessary.

### 7️⃣ Custom Header Handling in CORS
- Required when APIs send and receive **custom headers** (e.g., `X-Auth-Token`, `X-Request-ID`).
- Helps maintain security while allowing custom request-response handling.

## Best Practices Based on Use Cases
🔹 **For internal apps:** Single-origin or multiple-origin CORS is fine.  
🔹 **For SaaS/multi-tenant systems:** Dynamic Origin CORS is recommended.  
🔹 **For APIs using authentication:** Credentialed Requests CORS is needed.  
🔹 **For open APIs:** Wildcard CORS works best.  
🔹 **For APIs with custom headers:** Custom Header Handling CORS is essential.  

## Conclusion
Since the **current requirement** was to enable CORS **only for GET requests**, the **most practical implementations** i've applied. However, if the API evolves to support authentication, dynamic clients, or public access, additional CORS strategies may need to be implemented to maintain security and usability.

