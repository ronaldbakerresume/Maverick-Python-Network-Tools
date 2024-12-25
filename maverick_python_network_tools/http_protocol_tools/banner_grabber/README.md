# Service Banner Grabbing Tool

**Developer**: Ronald Baker  

## Description

This script connects to a specified IP address and port to retrieve the **service banner**. It can help identify which service is running on an open port.

## Requirements

- **Python 3**
- **socket** (standard library, included with Python)

## Usage

1. **Run**:
   ```bash
   python3 banner_grabber.py
   ```
2. **Provide**:
   - Target IP address (e.g., `192.168.1.1`)
   - Target port (e.g., `80`)

Example session:
```
Welcome to the Service Banner Grabbing Tool.
Developer: Ronald Baker

Enter the target IP address (e.g., '192.168.1.1'): 192.168.1.1
Enter the target port (e.g., 80): 80
Connecting to 192.168.1.1:80...

Banner retrieved from 192.168.1.1:80:
HTTP/1.1 200 OK
Server: ExampleServer/1.0
...
```

If the port is closed or filtered, you may see a timeout or connection refusal message.

## Author

Ronald Baker  

## License & Disclaimer

This script is provided "as-is" for educational and informational purposes. Use at your own risk.