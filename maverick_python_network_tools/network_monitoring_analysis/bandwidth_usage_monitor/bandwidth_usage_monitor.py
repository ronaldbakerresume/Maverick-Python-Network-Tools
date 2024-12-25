"""
Bandwidth Usage Monitor
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

This script monitors real-time bandwidth usage on a specified network interface.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet capture).
2. Specify the network interface to monitor.
3. The script will display bandwidth usage in real-time.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 bandwidth_usage_monitor.py
"""

from scapy.all import sniff
import time
import threading

# Data tracking for bandwidth usage
traffic_data = {"bytes_in": 0, "bytes_out": 0}

def process_packet(packet):
    """
    Tracks the size of incoming and outgoing packets.

    :param packet: The captured packet.
    """
    if packet.haslayer("IP"):
        if packet["IP"].src:  # Outgoing traffic
            traffic_data["bytes_out"] += len(packet)
        if packet["IP"].dst:  # Incoming traffic
            traffic_data["bytes_in"] += len(packet)

def display_bandwidth():
    """
    Displays real-time bandwidth usage in KB/s and cumulative stats.
    """
    previous_data = traffic_data.copy()

    while True:
        time.sleep(1)
        bytes_in_rate = (traffic_data["bytes_in"] - previous_data["bytes_in"]) / 1024
        bytes_out_rate = (traffic_data["bytes_out"] - previous_data["bytes_out"]) / 1024
        previous_data = traffic_data.copy()

        print(f"\nReal-Time Bandwidth Usage:")
        print(f"Incoming: {bytes_in_rate:.2f} KB/s")
        print(f"Outgoing: {bytes_out_rate:.2f} KB/s")
        print(f"Cumulative:")
        print(f"  Total Incoming: {traffic_data['bytes_in'] / 1024:.2f} KB")
        print(f"  Total Outgoing: {traffic_data['bytes_out'] / 1024:.2f} KB")

if __name__ == "__main__":
    print("Welcome to the Bandwidth Usage Monitor.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface
    interface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ").strip()

    # Start bandwidth display in a separate thread
    display_thread = threading.Thread(target=display_bandwidth, daemon=True)
    display_thread.start()

    try:
        print(f"Monitoring bandwidth on interface {interface}. Press Ctrl+C to stop.")
        sniff(iface=interface, prn=process_packet, store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping bandwidth monitor.")
    except Exception as e:
        print(f"An error occurred: {e}")

