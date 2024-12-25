```markdown
# Network Traffic Shaper

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

This script shapes network traffic by introducing **delays**, **packet drops**, or **bandwidth limits** on a specified interface.  
It leverages **scapy** to capture packets and then manipulates them according to the user’s chosen mode:

- **delay**: Introduce a fixed delay (in seconds) before sending each packet.  
- **drop**: Randomly drop packets with a specified probability (0 to 1).  
- **limit**: Limit bandwidth by calculating a delay based on packet size and the given kbps limit.

## Requirements

- **Python 3**
- **scapy** (`pip install scapy`)
- **Superuser privileges** (to intercept and send packets)

## Usage

1. **Run** with superuser privileges:
   ```bash
   sudo python3 network_traffic_shaper.py
   ```
2. **Select** the network interface (e.g., `eth0`, `wlan0`) to monitor.
3. **Choose** the traffic shaping mode:
   - `delay`
   - `drop`
   - `limit`
4. **Enter** the parameter for that mode:
   - Delay time (seconds)
   - Drop probability (`0` to `1`, e.g., `0.3`)
   - Bandwidth limit (kbps, e.g., `512`)

**Example session**:
```
Welcome to the Network Traffic Shaper.
Developer: Ronald Baker
Company: Mavericks Umbrella LLC

Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): eth0
Enter traffic shaping mode ('delay', 'drop', 'limit'): drop
Enter drop probability (0 to 1, e.g., 0.3): 0.3
Applying traffic shaping mode 'drop' with parameter 0.3 on interface eth0.
```

Each packet passing through `eth0` has a 30% chance of being dropped.

Press **Ctrl + C** to stop.

## Author

Ronald Baker  
Mavericks Umbrella LLC

## License & Warranty

See the **Disclaimer** above. This script is provided without warranties of any kind. Use at your own risk.