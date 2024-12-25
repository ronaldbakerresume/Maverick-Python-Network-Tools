# Packet Replay Tool

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

This script captures **network packets** for a specified duration and saves them to a file,  
then allows you to **replay** the captured packets back onto a target network interface.

It has two main modes:
1. **Capture Packets**: Sniffs traffic on a specified interface and writes it to a `.pcap` file.  
2. **Replay Packets**: Reads packets from a `.pcap` file and sends them out on a given interface.

## Requirements

- **Python 3**
- **scapy** (`pip install scapy`)
- **Superuser privileges** (to capture and transmit raw packets)

## Usage

1. **Run** with superuser privileges:
   ```bash
   sudo python3 packet_replay_tool.py
   ```
2. **Select** an operation:
   1. Capture Packets
   2. Replay Packets
3. **Specify**:
   - **Network interface** (e.g., `eth0`, `wlan0`)  
   - **File name** (e.g., `capture.pcap`) for storing or reading packets

Example session:
```
Welcome to the Packet Replay Tool.
Developer: Ronald Baker
Company: Mavericks Umbrella LLC

Choose an operation:
1. Capture Packets
2. Replay Packets
Enter your choice (1/2): 1
Enter the network interface to use (e.g., 'eth0', 'wlan0'): eth0
Enter the output file name for captured packets (e.g., 'capture.pcap'): capture.pcap
Capturing packets on interface eth0. Press Ctrl+C to stop.

Packets saved to capture.pcap.

Choose an operation:
1. Capture Packets
2. Replay Packets
Enter your choice (1/2): 2
Enter the network interface to use (e.g., 'eth0', 'wlan0'): eth0
Enter the input file name for replaying packets (e.g., 'capture.pcap'): capture.pcap
Replaying packets from capture.pcap on interface eth0...

Packet replay complete.
```

## Author

Ronald Baker  
Mavericks Umbrella LLC

## License & Warranty

See the **Disclaimer** above. This script is provided without warranties of any kind.  
Use at your own risk.
```