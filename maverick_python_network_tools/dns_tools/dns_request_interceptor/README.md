# DNS Request Interceptor

**Developer**: Ronald Baker  

## Description

This script acts as a simple DNS server that intercepts DNS queries and logs queried domains in real time.  
It can also optionally **redirect** specific domains to a user-defined IP address for testing or analysis.

## Requirements

- **Python 3**
- **dnslib** (install with `pip install dnslib`)
- **Superuser privileges** (needed to bind to port 53)

## Usage

1. **Install** dependencies:
   ```bash
   pip install dnslib
   ```
2. **Run** as superuser:
   ```bash
   sudo python3 dns_request_interceptor.py
   ```
3. **Configure** your device or router to use the server’s IP address as its DNS server (or forward DNS traffic to this script on port 53).
4. **Observe** the console output for captured DNS queries.  
   - Requests for a specific domain (e.g., `example.com`) can be redirected to a configured IP address (`REDIRECT_IP`).
   - By default, other requests receive an **NXDOMAIN** response (no answers).

Example session:
```
Welcome to the DNS Request Interceptor.
Developer: Ronald Baker

DNS server running on 0.0.0.0:53
Intercepting DNS queries. Press Ctrl+C to stop.

Received DNS Query: example.com. (A)
Redirecting example.com. to 192.168.1.100
Received DNS Query: google.com. (A)
```

## Notes

- **REDIRECT_IP** in the script is set to `192.168.1.100` by default.  
- You can modify the code to handle additional domains or provide different responses as needed.  

## Disclaimer

This software is provided by the developer "as-is" and without any warranties or conditions,  
express or implied, including but not limited to the implied warranties of merchantability  
and fitness for a particular purpose. In no event shall the developer or its contributors  
be liable for any direct, indirect, incidental, special, exemplary, or consequential damages  
arising from the use of this software.

## Author

Ronald Baker  

## License & Warranty

This script is intended for **educational** and **testing** purposes. Use at your own risk.