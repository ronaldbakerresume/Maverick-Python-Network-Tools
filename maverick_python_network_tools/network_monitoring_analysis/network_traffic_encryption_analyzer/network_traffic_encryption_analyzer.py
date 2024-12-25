"""
Network Traffic Encryption Analyzer
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

This script analyzes network traffic to detect encrypted and unencrypted packets.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet capture).
2. Specify the network interface to monitor.
3. The script will analyze and display details of encrypted and unencrypted packets.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 network_traffic_encryption_analyzer.py
"""

from scapy.all import sniff, IP, TCP, Raw
import re

def is_encrypted(packet):
    """
    Determines if a packet contains encrypted data by checking for plaintext patterns.

    :param packet: The captured packet.
    :return: True if the packet is encrypted; False otherwise.
    """
    if packet.haslayer(Raw):
        payload = packet[Raw].load.decode('utf-8', errors='ignore')
        # Check for unencrypted indicators like HTTP headers
        if re.search(r"(GET|POST|HTTP|User-Agent|Host)", payload, re.IGNORECASE):
            return False
    return True

def packet_handler(packet):
    """
    Handles captured packets and identifies encrypted vs. unencrypted traffic.

    :param packet: The captured network packet.
    """
    if packet.haslayer(IP) and packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        encrypted = is_encrypted(packet)

        encryption_status = "Encrypted" if encrypted else "Unencrypted"
        print(f"{encryption_status} packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

if __name__ == "__main__":
    print("Welcome to the Network Traffic Encryption Analyzer.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface
    interface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ").strip()

    try:
        print(f"Monitoring traffic on interface {interface}. Press Ctrl+C to stop.")
        sniff(iface=interface, prn=packet_handler, store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping encryption analyzer.")
    except Exception as e:
        print(f"An error occurred: {e}")

