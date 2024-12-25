# DNS Query Logger

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

## Description

This script monitors DNS queries in real time and logs details such as:
- Timestamp
- Source IP
- Destination IP
- Queried domain
- Query type

Use it to analyze DNS traffic on your network, detecting which domains are being resolved and by whom.

## Requirements

- Python 3  
- **scapy** (install with `pip install scapy`)
- **Superuser privileges** (required for packet capture)

## Usage

1. Run with `sudo`:  
   ```bash
   sudo python3 dns_query_logger.py
   ```
2. Provide:
   - **Network interface** (e.g., `eth0` or `wlan0`)
   - **Log file path** (e.g., `dns_log.txt`)

Example:
```
Welcome to the DNS Query Logger.
Developer: Ronald Baker
Company: Mavericks Umbrella LLC

Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): eth0
Enter the path to save the log file (e.g., 'dns_log.txt'): dns_log.txt
Monitoring DNS queries on interface eth0. Logging to dns_log.txt. Press Ctrl+C to stop.
2024-12-25 12:34:56 | DNS Query | 192.168.1.10 -> 8.8.8.8 | Domain: example.com. | Type: 1
```

Each DNS query is printed to the console and appended to the specified log file.

## Author

Ronald Baker  
Mavericks Umbrella LLC

## License & Warranty

See the **Disclaimer** above. This script is provided without warranties of any kind. Use at your own risk.
```