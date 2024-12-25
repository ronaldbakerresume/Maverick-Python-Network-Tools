"""
Network Traffic Shaper
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

This script shapes network traffic by introducing delays, bandwidth limits, or packet drops.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet manipulation).
2. Specify the network interface, traffic manipulation mode, and related parameters.
3. The script will shape network traffic based on user inputs.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 network_traffic_shaper.py
"""

from scapy.all import sniff, sendp
import time
import random

def delay_packet(packet, delay):
    """
    Introduces a delay before sending the packet.

    :param packet: The captured packet to delay.
    :param delay: The artificial delay in seconds.
    """
    time.sleep(delay)
    sendp(packet, verbose=0)
    print(f"Packet delayed by {delay} seconds and sent: {packet.summary()}")

def drop_packet(packet, drop_probability):
    """
    Randomly drops a packet based on the specified probability.

    :param packet: The captured packet to evaluate.
    :param drop_probability: The probability (0 to 1) of dropping the packet.
    :return: True if the packet is dropped; False otherwise.
    """
    if random.random() < drop_probability:
        print(f"Packet dropped: {packet.summary()}")
        return True
    return False

def limit_bandwidth(packet, bandwidth_limit):
    """
    Limits bandwidth by introducing delays proportional to packet size.

    :param packet: The captured packet to limit.
    :param bandwidth_limit: The bandwidth limit in kbps.
    """
    packet_size_kb = len(packet) / 1024.0  # Convert bytes to KB
    delay = packet_size_kb / (bandwidth_limit / 8)  # Calculate delay based on bandwidth
    delay_packet(packet, delay)

def packet_handler(packet, mode, param):
    """
    Handles captured packets and applies the specified traffic shaping mode.

    :param packet: The captured packet.
    :param mode: The traffic shaping mode (delay, drop, limit).
    :param param: The parameter for the shaping mode (e.g., delay time, drop probability, bandwidth limit).
    """
    if mode == "delay":
        delay_packet(packet, param)
    elif mode == "drop" and drop_packet(packet, param):
        return  # Do not send dropped packets
    elif mode == "limit":
        limit_bandwidth(packet, param)
    else:
        sendp(packet, verbose=0)  # Default: forward packet

if __name__ == "__main__":
    print("Welcome to the Network Traffic Shaper.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface and traffic shaping mode
    interface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ").strip()
    mode = input("Enter traffic shaping mode ('delay', 'drop', 'limit'): ").strip().lower()

    # Input parameters based on mode
    if mode == "delay":
        param = float(input("Enter delay time in seconds (e.g., 1.5): "))
    elif mode == "drop":
        param = float(input("Enter drop probability (0 to 1, e.g., 0.3): "))
    elif mode == "limit":
        param = float(input("Enter bandwidth limit in kbps (e.g., 512): "))
    else:
        print("Invalid mode. Exiting.")
        exit(1)

    try:
        print(f"Applying traffic shaping mode '{mode}' with parameter {param} on interface {interface}.")
        sniff(iface=interface, prn=lambda pkt: packet_handler(pkt, mode, param), store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping traffic shaper.")
    except Exception as e:
        print(f"An error occurred: {e}")

