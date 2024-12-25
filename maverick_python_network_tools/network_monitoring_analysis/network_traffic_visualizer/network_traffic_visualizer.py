"""
Network Traffic Visualizer
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

This script captures and visualizes network traffic in real-time, categorizing packets by protocol.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet capture).
2. Enter the network interface to monitor (e.g., 'eth0', 'wlan0').
3. The script will display traffic statistics and update them in real-time.
4. Modify this script to extend functionality as needed.

Required Libraries:
- scapy (Install with `pip install scapy`)
- matplotlib (Install with `pip install matplotlib`)

Usage:
sudo python3 network_traffic_visualizer.py
"""

from scapy.all import sniff, IP
from collections import defaultdict
import matplotlib.pyplot as plt
import threading
import time

# Initialize counters for traffic statistics
traffic_stats = defaultdict(int)

def packet_handler(packet):
    """
    Handles incoming packets and categorizes traffic by protocol.

    :param packet: The captured packet object.
    """
    if packet.haslayer(IP):
        protocol = packet[IP].proto
        if protocol == 6:
            traffic_stats["TCP"] += 1
        elif protocol == 17:
            traffic_stats["UDP"] += 1
        elif protocol == 1:
            traffic_stats["ICMP"] += 1
        else:
            traffic_stats["Other"] += 1

def visualize_traffic():
    """
    Visualizes traffic statistics in real-time using a bar chart.
    """
    plt.ion()
    fig, ax = plt.subplots()

    while True:
        try:
            protocols = list(traffic_stats.keys())
            counts = list(traffic_stats.values())

            ax.clear()
            ax.bar(protocols, counts)
            ax.set_title("Network Traffic by Protocol")
            ax.set_xlabel("Protocol")
            ax.set_ylabel("Packet Count")
            plt.pause(1)
        except KeyboardInterrupt:
            print("\nStopping visualization.")
            break

if __name__ == "__main__":
    print("Welcome to the Network Traffic Visualizer.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface
    iface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ")

    try:
        # Start packet sniffing in a separate thread
        sniff_thread = threading.Thread(target=sniff, kwargs={"iface": iface, "prn": packet_handler, "store": 0})
        sniff_thread.daemon = True
        sniff_thread.start()

        # Start visualization
        visualize_traffic()
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping network traffic visualizer.")
    except Exception as e:
        print(f"An error occurred: {e}")

