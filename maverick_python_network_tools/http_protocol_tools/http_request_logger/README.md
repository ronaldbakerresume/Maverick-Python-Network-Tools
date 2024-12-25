# HTTP/HTTPS Request Logger

**Developer**: Ronald Baker  

## Description

This script uses **mitmproxy** to set up a proxy that captures and logs HTTP/HTTPS requests. It displays:

- Request URL  
- HTTP Method (e.g., GET, POST)  
- Request Headers  
- Request Body (if present)  

It operates as an **addon** for mitmproxy, printing out each request’s details to the console.

## Requirements

- Python 3  
- **mitmproxy** (`pip install mitmproxy`)

## Usage

1. **Save** the script as `http_request_logger.py`.  
2. **Run** it via mitmproxy:
   ```bash
   mitmproxy -s http_request_logger.py
   ```
   or use `mitmweb`:
   ```bash
   mitmweb -s http_request_logger.py
   ```
3. **Configure** your device or browser to use `localhost:8080` (or the mitmproxy default port) as the HTTP/HTTPS proxy.  
4. The script will log request details to the console.

Example session:
```
HTTP/HTTPS Request Logger initialized. Listening on port 8080.
Request URL: http://example.com/
HTTP Method: GET
Headers:
  Host: example.com
  User-Agent: Mozilla/5.0
Body:
--------------------------------------------------
```

## Notes

- **HTTPS Decryption**: For HTTPS traffic, you may need to install the **mitmproxy CA certificate** on your device, allowing mitmproxy to decrypt traffic.  
- For more details on **mitmproxy** usage and configuration, see the [mitmproxy documentation](https://docs.mitmproxy.org/stable/).

## Author

Ronald Baker  

## License & Disclaimer

This script is provided "as-is" for educational and debugging purposes. Use it responsibly on networks and systems you have permission to test.  