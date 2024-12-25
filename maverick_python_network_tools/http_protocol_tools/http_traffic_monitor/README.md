```markdown
# HTTP Traffic Monitor

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

This script monitors **HTTP traffic** on port 80. It logs details such as HTTP methods (e.g., GET, POST), detected URLs, source and destination IP addresses, and ports.

## Requirements

- Python 3  
- **scapy** (`pip install scapy`)  
- **Superuser privileges** (to capture packets)

## Usage

1. **Run** with superuser privileges:
   ```bash
   sudo python3 http_traffic_monitor.py
   ```
2. Provide:
   - **Network interface** (e.g., `eth0`, `wlan0`)
   - **Log file path** (e.g., `http_log.txt`)

Example session:
```
Welcome to the HTTP Traffic Monitor.
Developer: Ronald Baker
Company: Mavericks Umbrella LLC

Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): eth0
Enter the path to save the log file (e.g., 'http_log.txt'): http_log.txt
Monitoring HTTP traffic on interface eth0. Logging to http_log.txt. Press Ctrl+C to stop.
2024-12-25 12:34:56 | HTTP GET | http://example.com | 192.168.1.15:54123 -> 93.184.216.34:80
```

Each HTTP request is printed to the console and appended to the specified log file.

## Author

Ronald Baker  
Mavericks Umbrella LLC

## License & Warranty

See the **Disclaimer** above. This script is provided without warranties of any kind. Use at your own risk.
```