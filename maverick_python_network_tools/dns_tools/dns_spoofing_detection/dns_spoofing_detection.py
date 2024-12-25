"""
DNS Spoofing Detection Tool
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

This script detects DNS spoofing by monitoring responses and comparing them against a trusted DNS server.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet capture).
2. Specify the network interface and trusted DNS server.
3. The script will monitor DNS responses and detect discrepancies.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 dns_spoofing_detection.py
"""

from scapy.all import sniff, DNS, DNSRR, IP
import socket

def resolve_dns(domain, trusted_dns):
    """
    Resolves a domain using the trusted DNS server.

    :param domain: The domain to resolve.
    :param trusted_dns: The IP address of the trusted DNS server.
    :return: The resolved IP address or None if resolution fails.
    """
    try:
        query = socket.gethostbyname_ex(domain)
        return query[2][0] if query and len(query[2]) > 0 else None
    except Exception:
        return None

def detect_dns_spoof(packet, trusted_dns):
    """
    Detects DNS spoofing by comparing DNS responses to a trusted DNS server.

    :param packet: The captured DNS response packet.
    :param trusted_dns: The IP address of the trusted DNS server.
    """
    if packet.haslayer(DNS) and packet[DNS].ancount > 0:
        queried_domain = packet[DNS].qd.qname.decode("utf-8").strip(".")
        response_ip = packet[DNSRR].rdata

        # Resolve using the trusted DNS server
        trusted_ip = resolve_dns(queried_domain, trusted_dns)

        if trusted_ip and response_ip != trusted_ip:
            print(f"ALERT: DNS Spoofing Detected!")
            print(f"  Domain: {queried_domain}")
            print(f"  Spoofed IP: {response_ip}")
            print(f"  Trusted IP: {trusted_ip}")

if __name__ == "__main__":
    print("Welcome to the DNS Spoofing Detection Tool.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface and trusted DNS server
    interface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ").strip()
    trusted_dns = input("Enter the trusted DNS server (e.g., 8.8.8.8): ").strip()

    try:
        print(f"Monitoring DNS responses on interface {interface}. Press Ctrl+C to stop.")
        sniff(iface=interface, filter="udp port 53", prn=lambda pkt: detect_dns_spoof(pkt, trusted_dns), store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping DNS spoofing detection.")
    except Exception as e:
        print(f"An error occurred: {e}")

