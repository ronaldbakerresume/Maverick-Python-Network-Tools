# ARP Spoofing Detection Tool

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

This Python script detects ARP spoofing by monitoring ARP traffic and comparing IP–MAC mappings. If any mapping changes unexpectedly, the script alerts you to a potential ARP spoofing attack on the network.

## Requirements

- Python 3  
- scapy (Install with: `pip install scapy`)

## Usage

1. Ensure superuser privileges by running with `sudo`:  
   ```bash
   sudo python3 arp_spoofing_detection.py
   ```
2. When prompted, enter the network interface (e.g., `eth0`, `wlan0`).  
3. Press `Ctrl + C` to stop monitoring at any time.

Example:
```bash
sudo python3 arp_spoofing_detection.py
Welcome to the ARP Spoofing Detection Tool.
Developer: Ronald Baker
Company: Mavericks Umbrella LLC

Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): eth0
Monitoring ARP traffic on interface eth0. Press Ctrl+C to stop.
```

When a mismatch is detected:
```
ALERT: Potential ARP spoofing detected!
  IP: 192.168.1.50
  Previous MAC: 00:11:22:33:44:55
  Current MAC: aa:bb:cc:dd:ee:ff
```

## Author

Ronald Baker  
Mavericks Umbrella LLC

## License & Warranty

See the **Disclaimer** above. This script is provided without warranties of any kind. Use at your own risk.
```