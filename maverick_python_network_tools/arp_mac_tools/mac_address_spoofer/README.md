# MAC Address Spoofer

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

This script changes the MAC address of a specified network interface temporarily. It can either accept a user-specified MAC address or generate a random one.

## Requirements

- Python 3
- Superuser privileges (via `sudo`)
- No additional Python libraries are required—standard libraries only.

## Usage

1. Run with `sudo`:
   ```bash
   sudo python3 mac_address_spoofer.py
   ```
2. When prompted, specify:
   - The network interface (e.g., `eth0`, `wlan0`).
   - Whether to generate a random MAC address or provide one manually.
3. Confirm the MAC address has changed:
   - The script attempts to bring the interface down, apply the new MAC, then bring it up again.

Example session:
```
Welcome to the MAC Address Spoofer.
Developer: Ronald Baker
Company: Mavericks Umbrella LLC

Enter the network interface (e.g., 'eth0', 'wlan0'): eth0
Current MAC address of eth0: 00:11:22:33:44:55
Do you want to generate a random MAC address? (yes/no): yes
Changing MAC address of eth0 to 00:16:3e:23:a8:b2...
MAC address changed successfully to 00:16:3e:23:a8:b2.
```

## Author

Ronald Baker  
Mavericks Umbrella LLC

## License & Warranty

See the **Disclaimer** above. This script is provided without warranties of any kind. Use at your own risk.
```