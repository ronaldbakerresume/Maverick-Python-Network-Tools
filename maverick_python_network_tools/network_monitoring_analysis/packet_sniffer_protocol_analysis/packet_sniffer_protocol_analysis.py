"""
Packet Sniffer with Protocol Analysis
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

This script captures network packets and analyzes traffic by protocol.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet capture).
2. Specify the network interface to monitor.
3. The script will display real-time traffic statistics categorized by protocol.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 packet_sniffer_protocol_analysis.py
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP
from collections import defaultdict
import time
import threading

# Dictionary to track traffic statistics
traffic_stats = defaultdict(int)

def analyze_packet(packet):
    """
    Analyzes and categorizes packets by protocol.

    :param packet: The captured packet.
    """
    if packet.haslayer(IP):
        proto = packet[IP].proto
        protocol = {6: "TCP", 17: "UDP", 1: "ICMP"}.get(proto, "Other")
        traffic_stats[protocol] += 1

def display_statistics():
    """
    Displays traffic statistics in real-time.
    """
    while True:
        time.sleep(5)  # Update every 5 seconds
        print("\nTraffic Statistics:")
        print(f"{'Protocol':<10}{'Packets':<10}")
        print("-" * 20)
        for protocol, count in traffic_stats.items():
            print(f"{protocol:<10}{count:<10}")
        print("-" * 20)

if __name__ == "__main__":
    print("Welcome to the Packet Sniffer with Protocol Analysis.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface
    interface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ").strip()

    # Start statistics display in a separate thread
    stats_thread = threading.Thread(target=display_statistics, daemon=True)
    stats_thread.start()

    try:
        print(f"Monitoring traffic on interface {interface}. Press Ctrl+C to stop.")
        sniff(iface=interface, prn=analyze_packet, store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping packet sniffer.")
    except Exception as e:
        print(f"An error occurred: {e}")

