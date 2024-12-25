"""
ARP Spoofing Detection Tool
Developer: Ronald Baker
Company: Mavericks Umbrella LLC

Disclaimer:
This software is provided by Mavericks Umbrella LLC "as-is" and without any warranties or conditions,
express or implied, including but not limited to the implied warranties of merchantability and fitness for a particular purpose.
In no event shall Mavericks Umbrella LLC or its contributors be liable for any direct, indirect, incidental,
special, exemplary, or consequential damages (including but not limited to procurement of substitute goods or services;
loss of use, data, or profits; or business interruption) however caused and on any theory of liability,
whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of
the use of this software, even if advised of the possibility of such damage.

This script detects ARP spoofing by monitoring ARP traffic for inconsistent IP-MAC mappings.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet capture).
2. Specify the network interface to monitor.
3. The script will alert for potential ARP spoofing attacks.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 arp_spoofing_detection.py
"""

from scapy.all import sniff, ARP

# Dictionary to store observed ARP mappings
observed_mappings = {}

def detect_arp_spoof(packet):
    """
    Detects ARP spoofing based on inconsistent IP-MAC mappings.

    :param packet: The captured ARP packet.
    """
    if packet.haslayer(ARP):
        ip = packet[ARP].psrc
        mac = packet[ARP].hwsrc

        if ip in observed_mappings:
            if observed_mappings[ip] != mac:
                print(f"ALERT: Potential ARP spoofing detected!")
                print(f"  IP: {ip}")
                print(f"  Previous MAC: {observed_mappings[ip]}")
                print(f"  Current MAC: {mac}")
        else:
            observed_mappings[ip] = mac

if __name__ == "__main__":
    print("Welcome to the ARP Spoofing Detection Tool.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface
    interface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ").strip()

    try:
        print(f"Monitoring ARP traffic on interface {interface}. Press Ctrl+C to stop.")
        sniff(iface=interface, filter="arp", prn=detect_arp_spoof, store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping ARP spoofing detection.")
    except Exception as e:
        print(f"An error occurred: {e}")

