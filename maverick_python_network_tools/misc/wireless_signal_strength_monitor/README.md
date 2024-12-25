```markdown
# Wireless Signal Strength Monitor

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

This script monitors the **signal strength** of nearby wireless networks in real-time using **scapy**.  
It captures 802.11 beacon and probe response frames, extracting details like:

- **SSID** (network name)  
- **BSSID** (access point MAC address)  
- **Signal Strength** (in dBm)  
- **Channel**

## Requirements

- **Python 3**
- **scapy** (`pip install scapy`)
- **Superuser privileges** (to capture wireless traffic)

## Usage

1. **Put** your wireless interface into **monitor mode** (e.g., `airmon-ng start wlan0` → `wlan0mon`).
2. **Run** the script with `sudo`:
   ```bash
   sudo python3 wireless_signal_strength_monitor.py
   ```
3. **Provide** the wireless interface in monitor mode (e.g., `wlan0mon`) when prompted.
4. Press **Ctrl + C** to stop monitoring.

Example session:
```
Welcome to the Wireless Signal Strength Monitor.
Developer: Ronald Baker
Company: Mavericks Umbrella LLC

Enter the wireless interface to monitor (e.g., 'wlan0mon'): wlan0mon
Monitoring wireless signals on interface wlan0mon. Press Ctrl+C to stop.
Detected Network: SSID=HomeNetwork, BSSID=00:11:22:33:44:55, Signal=-42 dBm, Channel=6
Detected Network: SSID=GuestNetwork, BSSID=66:77:88:99:AA:BB, Signal=-50 dBm, Channel=11
```

## Author

Ronald Baker  
Mavericks Umbrella LLC

## License & Warranty

See the **Disclaimer** above. This script is provided without warranties of any kind. Use at your own risk.
```