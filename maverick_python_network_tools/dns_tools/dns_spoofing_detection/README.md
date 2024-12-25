# DNS Spoofing Detection Tool

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

This script detects DNS spoofing by monitoring DNS responses on a given network interface and comparing the returned IPs against a **trusted DNS server**. If a discrepancy is found, an alert is triggered indicating possible DNS spoofing.

## Requirements

- Python 3  
- **scapy** (install with `pip install scapy`)  
- **Superuser privileges** (for packet capture on port 53)

## Usage

1. **Run** with superuser privileges:
   ```bash
   sudo python3 dns_spoofing_detection.py
   ```
2. **Provide**:
   - Network interface (e.g., `eth0`, `wlan0`)
   - Trusted DNS server IP (e.g., `8.8.8.8`)
3. **Monitor** for alerts when the script detects a mismatch between the response IP and the IP returned by the trusted DNS server.

Example:
```
Welcome to the DNS Spoofing Detection Tool.
Developer: Ronald Baker
Company: Mavericks Umbrella LLC

Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): eth0
Enter the trusted DNS server (e.g., 8.8.8.8): 8.8.8.8
Monitoring DNS responses on interface eth0. Press Ctrl+C to stop.
ALERT: DNS Spoofing Detected!
  Domain: example.com
  Spoofed IP: 1.2.3.4
  Trusted IP: 93.184.216.34
```

## Author

Ronald Baker  
Mavericks Umbrella LLC

## License & Warranty

See the **Disclaimer** above. This script is provided without warranties of any kind. Use at your own risk.
```