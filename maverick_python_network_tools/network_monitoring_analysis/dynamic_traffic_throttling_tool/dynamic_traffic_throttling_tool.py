"""
Dynamic Traffic Throttling Tool
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

This script throttles network traffic dynamically based on a defined bandwidth limit and traffic patterns.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet manipulation).
2. Specify the network interface and bandwidth limit.
3. The script will throttle traffic dynamically.
4. Modify this script to extend functionality as needed.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 dynamic_traffic_throttling_tool.py
"""

from scapy.all import sniff, sendp
import time

def throttle_packet(packet, bandwidth_limit):
    """
    Throttles the packet flow based on the defined bandwidth limit.

    :param packet: The captured packet to throttle.
    :param bandwidth_limit: The bandwidth limit in kbps.
    """
    packet_size_kb = len(packet) / 1024.0  # Convert bytes to KB
    delay = packet_size_kb / (bandwidth_limit / 8)  # Calculate delay based on bandwidth
    print(f"Throttling packet: {packet.summary()} with {delay:.3f} seconds delay...")
    time.sleep(delay)
    sendp(packet, verbose=0)
    print("Packet sent.")

def packet_handler(packet, bandwidth_limit):
    """
    Handles captured packets and applies throttling.

    :param packet: The captured packet.
    :param bandwidth_limit: The bandwidth limit in kbps.
    """
    throttle_packet(packet, bandwidth_limit)

if __name__ == "__main__":
    print("Welcome to the Dynamic Traffic Throttling Tool.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface
    interface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ")

    # Input bandwidth limit
    try:
        bandwidth_limit = float(input("Enter the bandwidth limit in kbps (e.g., 512): "))
    except ValueError:
        print("Invalid bandwidth limit. Defaulting to 512 kbps.")
        bandwidth_limit = 512.0

    try:
        print(f"Monitoring traffic on interface {interface} with bandwidth limit: {bandwidth_limit} kbps.")
        print("Press Ctrl+C to stop.")
        sniff(iface=interface, prn=lambda pkt: packet_handler(pkt, bandwidth_limit), store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping traffic throttling.")
    except Exception as e:
        print(f"An error occurred: {e}")

