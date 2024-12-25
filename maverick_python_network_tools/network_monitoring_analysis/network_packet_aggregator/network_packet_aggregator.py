"""
Network Packet Aggregator and Analyzer
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

This script captures and aggregates network traffic, providing real-time summaries by protocol and IP.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet capture).
2. Specify the network interface to monitor.
3. The script will display live traffic statistics.
4. Modify this script to extend functionality as needed.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 network_packet_aggregator.py
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP
from collections import defaultdict
import time
import threading

# Data structure for traffic aggregation
traffic_data = defaultdict(lambda: {"count": 0, "bytes": 0})

def packet_handler(packet):
    """
    Handles captured packets and aggregates traffic data.

    :param packet: The captured network packet.
    """
    if packet.haslayer(IP):
        proto = packet[IP].proto
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        packet_size = len(packet)

        # Update traffic data
        protocol = {6: "TCP", 17: "UDP", 1: "ICMP"}.get(proto, "Other")
        traffic_data[protocol]["count"] += 1
        traffic_data[protocol]["bytes"] += packet_size
        traffic_data[src_ip]["count"] += 1
        traffic_data[src_ip]["bytes"] += packet_size

def display_traffic_summary():
    """
    Periodically displays aggregated traffic data.
    """
    while True:
        time.sleep(5)  # Update every 5 seconds
        print("\nTraffic Summary:")
        print(f"{'Protocol':<10}{'Packets':<10}{'Bytes':<15}")
        print("-" * 35)
        for protocol, data in traffic_data.items():
            if isinstance(data, dict):
                print(f"{protocol:<10}{data['count']:<10}{data['bytes']:<15}")
        print("-" * 35)
        print(f"{'Source IP':<20}{'Packets':<10}{'Bytes':<15}")
        print("-" * 45)
        for ip, data in traffic_data.items():
            if not isinstance(data, dict):
                print(f"{ip:<20}{data['count']:<10}{data['bytes']:<15}")

if __name__ == "__main__":
    print("Welcome to the Network Packet Aggregator and Analyzer.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface
    interface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ")

    # Start traffic summary display in a separate thread
    threading.Thread(target=display_traffic_summary, daemon=True).start()

    try:
        print(f"Monitoring traffic on interface {interface}. Press Ctrl+C to stop.")
        sniff(iface=interface, prn=packet_handler, store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping packet aggregator.")
    except Exception as e:
        print(f"An error occurred: {e}")

