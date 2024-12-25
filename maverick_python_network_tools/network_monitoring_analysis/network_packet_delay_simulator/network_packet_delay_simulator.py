"""
Network Packet Delay Simulation Tool
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

This script simulates network delays by intercepting and replaying packets with an artificial time delay.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet interception).
2. Specify the network interface to monitor.
3. Define the artificial delay time in seconds.
4. Modify this script to extend functionality as needed.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 network_packet_delay_simulator.py
"""

from scapy.all import sniff, sendp, Ether
import time

def delay_packet(packet, delay):
    """
    Introduces a delay before sending the packet.

    :param packet: The captured packet to delay.
    :param delay: The artificial delay in seconds.
    """
    print(f"Delaying packet: {packet.summary()} by {delay} seconds...")
    time.sleep(delay)
    sendp(packet, verbose=0)
    print("Packet sent.")

def packet_handler(packet, delay):
    """
    Handles captured packets and applies the delay.

    :param packet: The captured packet.
    :param delay: The artificial delay in seconds.
    """
    delay_packet(packet, delay)

if __name__ == "__main__":
    print("Welcome to the Network Packet Delay Simulation Tool.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface
    interface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ")

    # Input delay time
    try:
        delay_time = float(input("Enter the artificial delay time in seconds (e.g., 1.5): "))
    except ValueError:
        print("Invalid delay time. Defaulting to 1 second.")
        delay_time = 1.0

    try:
        print(f"Monitoring packets on interface {interface} with {delay_time} seconds delay.")
        print("Press Ctrl+C to stop.")
        sniff(iface=interface, prn=lambda pkt: packet_handler(pkt, delay_time), store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping packet delay simulation.")
    except Exception as e:
        print(f"An error occurred: {e}")

