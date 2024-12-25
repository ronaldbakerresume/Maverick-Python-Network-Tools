# HTTP Proxy Server

**Developer**: Ronald Baker  
**Company**: Mavericks Umbrella LLC  

## Disclaimer

This software is provided by Mavericks Umbrella LLC "as-is" and without any warranties or conditions,  
express or implied, including but not limited to the implied warranties of merchantability and fitness for a particular purpose.  
In no event shall Mavericks Umbrella LLC or its contributors be liable for any direct, indirect, incidental,  
special, exemplary, or consequential damages (including but not limited to procurement of substitute goods or services;  
loss of use, data, or profits; or business interruption) however caused and on any theory of liability,  
whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of  
the use of this software, even if advised of the possibility of such damage.

---

## Description

This script creates a simple **HTTP proxy server** which listens for incoming HTTP requests and relays them to the target host. It logs both the **request** and the **response** for analysis or troubleshooting.

## Requirements

- Python 3
- **No extra libraries** needed (uses only standard libraries: `socket`, `threading`)

## Usage

1. **Run** the script:
   ```bash
   python3 http_proxy_server.py
   ```
2. **Enter** the listening port (e.g., `8080`).
3. **Configure** your browser or application to use `127.0.0.1:<port>` as the HTTP proxy.

**Example session**:
```
Welcome to the HTTP Proxy Server.
Developer: Ronald Baker
Company: Mavericks Umbrella LLC

Enter the port for the proxy server (e.g., 8080): 8080
HTTP Proxy Server running on port 8080
Accepted connection from ('127.0.0.1', 52310)

[Request]
GET http://example.com/ HTTP/1.1
Host: example.com
...

[Response]
HTTP/1.1 200 OK
Date: ...
Server: ...
...
```

## Notes

- By default, **port 80** is used if none is specified in the HTTP request line.
- For HTTPS traffic or advanced features (e.g., SSL interception), additional configurations or a more advanced proxy framework would be required.

## Author

Ronald Baker  
Mavericks Umbrella LLC

## License & Warranty

Use at your own risk. See **Disclaimer** above for full details.