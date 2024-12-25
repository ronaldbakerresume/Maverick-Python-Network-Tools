# DNS Spoofing Tool

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

This script intercepts DNS queries on the local network and responds with spoofed DNS answers for a specific domain,  
effectively redirecting clients to a chosen IP address.  

## Requirements

- Python 3  
- **scapy** (install with `pip install scapy`)  
- **Superuser privileges** (to capture and send DNS packets on UDP port 53)

## Usage

1. **Run** with superuser privileges:
   ```bash
   sudo python3 dns_spoofing_tool.py
   ```
2. Provide:
   - **Target domain** to spoof (e.g., `example.com`)
   - **Spoofed IP address** to map the domain to (e.g., `192.168.1.100`)
3. **Configure** your network or devices to use this machine’s IP as their DNS server (or intercept/forward DNS traffic to port 53).
4. When a DNS query for the target domain is intercepted, the script replies with the spoofed IP.

Example session:
```
Welcome to the DNS Spoofing Tool.
Developer: Ronald Baker
Company: Mavericks Umbrella LLC

Enter the target domain to spoof (e.g., example.com): example.com
Enter the spoofed IP address (e.g., 192.168.1.100): 192.168.1.100
Listening for DNS queries for example.com...
Spoofing DNS response for example.com -> 192.168.1.100
```

## Author

Ronald Baker  
Mavericks Umbrella LLC

## License & Warranty

See the **Disclaimer** above. This script is provided without warranties of any kind. Use at your own risk.
```