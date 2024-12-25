"""
Network Traffic Statistics Tool
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

This script monitors and calculates network traffic statistics.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet capture).
2. Specify the network interface to monitor.
3. The script will calculate and display real-time network statistics.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 network_traffic_statistics.py
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP
from collections import defaultdict
import time

# Statistics data
traffic_stats = {
    "total_packets": 0,
    "total_data": 0,
    "protocol_counts": defaultdict(int)
}

def update_statistics(packet):
    """
    Updates network statistics based on the captured packet.

    :param packet: The captured network packet.
    """
    traffic_stats["total_packets"] += 1
    traffic_stats["total_data"] += len(packet)

    if packet.haslayer(TCP):
        traffic_stats["protocol_counts"]["TCP"] += 1
    elif packet.haslayer(UDP):
        traffic_stats["protocol_counts"]["UDP"] += 1
    elif packet.haslayer(ICMP):
        traffic_stats["protocol_counts"]["ICMP"] += 1
    elif packet.haslayer(IP):
        traffic_stats["protocol_counts"]["Other IP"] += 1
    else:
        traffic_stats["protocol_counts"]["Other"] += 1

def display_statistics():
    """
    Displays current network traffic statistics.
    """
    print("\n--- Network Traffic Statistics ---")
    print(f"Total Packets: {traffic_stats['total_packets']}")
    print(f"Total Data Transferred: {traffic_stats['total_data']} bytes")
    print("Protocol Distribution:")
    for proto, count in traffic_stats["protocol_counts"].items():
        print(f"  {proto}: {count}")

if __name__ == "__main__":
    print("Welcome to the Network Traffic Statistics Tool.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface
    interface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ").strip()

    try:
        print(f"Monitoring traffic on interface {interface}. Press Ctrl+C to stop.")
        print("Statistics will update every 5 seconds.\n")

        # Start sniffing in a separate thread
        sniff_thread = sniff(iface=interface, prn=update_statistics, store=0, stop_filter=None)

        # Periodically display statistics
        while True:
            time.sleep(5)
            display_statistics()
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping traffic statistics monitoring.")
        display_statistics()
    except Exception as e:
        print(f"An error occurred: {e}")

