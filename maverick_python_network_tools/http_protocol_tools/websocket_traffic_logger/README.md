```markdown
# WebSocket Traffic Logger

**Developer**: Ronald Baker  

## Description

This script acts as a **WebSocket proxy/server** that intercepts and logs messages in real-time. It shows:

- **WebSocket handshake** when a new client connects  
- **Messages** sent by the client  
- **Messages** sent back or echoed by the server  

## Requirements

- **Python 3**
- **websocket-server** (`pip install websocket-server`)

## Usage

1. **Run** the script:
   ```bash
   python3 websocket_traffic_logger.py
   ```
2. The server listens on **`0.0.0.0:8081`** by default:
   ```
   WebSocket server running on ws://0.0.0.0:8081
   Waiting for connections...
   ```
3. **Configure** your WebSocket client to connect to `ws://<server-ip>:8081`.

**Example session**:
```
Welcome to the WebSocket Traffic Logger.
Developer: Ronald Baker

WebSocket server running on ws://0.0.0.0:8081
Waiting for connections...

New client connected: ('192.168.1.101', 50514)
Message from ('192.168.1.101', 50514): Hello, server!
```

The server **echoes** messages it receives back to the client for testing.

## Author

Ronald Baker  

## License & Disclaimer

This script is provided "as-is" for educational and diagnostic purposes. Use it responsibly.