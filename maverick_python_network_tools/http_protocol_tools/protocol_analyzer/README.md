```markdown
# Protocol Analyzer

**Developer**: Ronald Baker  

## Description

This script **captures network packets** to analyze specific protocols—**HTTP**, **FTP**, and **SMB**—in real-time. It prints out protocol-specific details such as:

- **HTTP**: Displays request/response lines.  
- **FTP**: Detects commands (e.g., USER, PASS, STOR, RETR).  
- **SMB**: Flags packets on port 445 for SMB traffic.  

## Requirements

- **Python 3**
- **scapy** (install with `pip install scapy`)
- **Superuser privileges** (to capture packets)

## Usage

1. **Run** with superuser privileges:
   ```bash
   sudo python3 protocol_analyzer.py
   ```
2. **Enter** the network interface (e.g., `eth0`, `wlan0`).
3. The script sniffs packets and routes them to the appropriate handler:
   - **HTTP** packets (contains “HTTP” in payload)
   - **FTP** commands (starts with “USER”, “PASS”, “STOR”, or “RETR”)
   - **SMB** traffic (port 445)

**Example:**
```
Welcome to the Protocol Analyzer.
Developer: Ronald Baker

Enter the network interface to sniff on (e.g., 'eth0', 'wlan0'): eth0
Sniffing on interface: eth0
Press Ctrl+C to stop.

[HTTP Packet] Source: 192.168.1.10 -> Destination: 93.184.216.34
GET / HTTP/1.1

[FTP Packet] Source: 192.168.1.15 -> Destination: 192.168.1.100
FTP Command: USER admin

[SMB Packet] Source: 192.168.1.20 -> Destination: 192.168.1.30
SMB Protocol communication detected.
```

Press **Ctrl + C** to stop sniffing.

## Author

Ronald Baker  

## License & Disclaimer

This script is provided "as-is" for educational and diagnostic purposes. Use at your own risk.