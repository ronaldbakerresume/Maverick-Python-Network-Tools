# Secure Shell Traffic Logger

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

This script logs **SSH traffic** by capturing TCP packets on port 22. It records important details such as source/destination IP, ports, and timestamps.

## Requirements

- Python 3  
- **scapy** (install with `pip install scapy`)
- **Superuser privileges** (needed for packet capture)

## Usage

1. **Run** with superuser privileges:
   ```bash
   sudo python3 secure_shell_traffic_logger.py
   ```
2. Provide:
   - **Network interface** to monitor (e.g., `eth0` or `wlan0`)
   - **Log file path** (e.g., `ssh_log.txt`)

Example:
```
Welcome to the Secure Shell Traffic Logger.
Developer: Ronald Baker
Company: Mavericks Umbrella LLC

Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): eth0
Enter the path to save the log file (e.g., 'ssh_log.txt'): ssh_log.txt
Monitoring SSH traffic on interface eth0. Logging to ssh_log.txt. Press Ctrl+C to stop.
2024-12-25 12:34:56 | SSH Traffic | 192.168.1.15:54321 -> 192.168.1.10:22
```

The script prints each SSH connection to the console and appends it to the specified log file.

## Author

Ronald Baker  
Mavericks Umbrella LLC

## License & Warranty

See the **Disclaimer** above. This script is provided without warranties of any kind. Use at your own risk.
```