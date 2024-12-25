# Network Traffic Replayer

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

This script replays **network traffic** stored in a **PCAP** file back onto the network.  
It sends each packet in the capture to the specified interface, allowing you to recreate or test specific network conditions,  
debug protocols, or perform demonstrations.

## Requirements

- **Python 3**  
- **scapy** (`pip install scapy`)  
- **Superuser privileges** (to send raw packets)

## Usage

1. **Run** with superuser privileges:
   ```bash
   sudo python3 network_traffic_replayer.py
   ```
2. **Provide**:
   - The **PCAP file** path (e.g., `traffic.pcap`)
   - The **network interface** (e.g., `eth0`, `wlan0`) to replay traffic on

Example:
```
Welcome to the Network Traffic Replayer.
Developer: Ronald Baker
Company: Mavericks Umbrella LLC

Enter the path to the PCAP file (e.g., 'traffic.pcap'): traffic.pcap
Enter the network interface to replay traffic on (e.g., 'eth0', 'wlan0'): eth0
Reading packets from traffic.pcap...
Loaded 42 packets.
Replaying packets on interface eth0...
```

## Author

Ronald Baker  
Mavericks Umbrella LLC

## License & Warranty

See the **Disclaimer** above. This script is provided without warranties of any kind. Use at your own risk.
```