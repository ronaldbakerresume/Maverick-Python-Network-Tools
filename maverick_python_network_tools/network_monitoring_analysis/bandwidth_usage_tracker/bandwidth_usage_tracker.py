"""
Bandwidth Usage Tracker
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

This script tracks and logs bandwidth usage for devices on a local network by monitoring packet sizes in real-time.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet capture).
2. Enter the network interface to monitor (e.g., 'eth0', 'wlan0').
3. The script will capture packets and calculate bandwidth usage.
4. Modify this script to extend functionality as needed.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 bandwidth_usage_tracker.py
"""

from scapy.all import sniff, IP
from collections import defaultdict
import time

# Initialize data counters
bandwidth_data = defaultdict(lambda: {"sent": 0, "received": 0})

def packet_handler(packet):
    """
    Handles incoming packets and calculates bandwidth usage.

    :param packet: The captured packet object.
    """
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        packet_size = len(packet)

        # Update sent and received data
        bandwidth_data[src_ip]["sent"] += packet_size
        bandwidth_data[dst_ip]["received"] += packet_size

def display_bandwidth():
    """
    Displays bandwidth usage statistics in real-time.
    """
    print("\nReal-Time Bandwidth Usage (in bytes):")
    print(f"{'IP Address':<20}{'Sent':<15}{'Received':<15}")
    print("-" * 50)
    for ip, data in bandwidth_data.items():
        print(f"{ip:<20}{data['sent']:<15}{data['received']:<15}")
    print("-" * 50)

if __name__ == "__main__":
    print("Welcome to the Bandwidth Usage Tracker.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface
    iface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ")

    try:
        # Start sniffing packets
        print(f"Monitoring bandwidth on interface: {iface}")
        print("Press Ctrl+C to stop.\n")
        sniff(iface=iface, prn=packet_handler, store=0)

        # Display bandwidth usage periodically
        while True:
            display_bandwidth()
            time.sleep(5)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping bandwidth tracker.")
        display_bandwidth()
    except Exception as e:
        print(f"An error occurred: {e}")

