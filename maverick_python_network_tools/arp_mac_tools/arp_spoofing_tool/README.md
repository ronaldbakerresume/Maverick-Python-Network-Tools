# ARP Spoofing and Interception Tool

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

This script performs ARP spoofing to redirect network traffic for interception and analysis.

## Requirements

- Python 3  
- scapy (Install with `pip install scapy`)

## Usage

1. Run with superuser privileges:  
   ```bash
   sudo python3 arp_spoofing_tool.py
   ```
2. Enter the target device’s IP address and the gateway’s IP address when prompted.  
3. Enter the network interface (e.g., `eth0` or `wlan0`).  
4. The script sends ARP spoofing packets continuously and starts intercepting traffic.  
5. Press `Ctrl + C` to stop and restore ARP tables.

Example:
```
Welcome to the ARP Spoofing and Interception Tool.
Developer: Ronald Baker
Company: Mavericks Umbrella LLC

Enter the target device's IP address: 192.168.1.100
Enter the gateway's IP address: 192.168.1.1
Enter the network interface to use (e.g., 'eth0', 'wlan0'): eth0
Sending ARP spoofing packets. Press Ctrl+C to stop.
Sniffing packets on interface eth0. Press Ctrl+C to stop.
```

## Author

Ronald Baker  
Mavericks Umbrella LLC

## License & Warranty

See the **Disclaimer** above. This script is provided without warranties of any kind. Use at your own risk.
```