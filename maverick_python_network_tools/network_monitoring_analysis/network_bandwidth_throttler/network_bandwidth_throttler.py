"""
Network Bandwidth Throttler
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

This script throttles bandwidth usage for specified targets.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet manipulation).
2. Specify the target IP, port, and bandwidth limit.
3. The script will enforce bandwidth limits in real-time.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 network_bandwidth_throttler.py
"""

from scapy.all import sniff, sendp, IP, TCP, Raw
import time

def throttle_packet(packet, bandwidth_limit):
    """
    Throttles packets by introducing delays based on bandwidth limit.

    :param packet: The captured network packet.
    :param bandwidth_limit: The bandwidth limit in kbps.
    """
    try:
        packet_size_kb = len(packet) / 1024  # Convert bytes to KB
        delay = packet_size_kb / (bandwidth_limit / 8)  # Calculate delay in seconds
        time.sleep(delay)
        sendp(packet, verbose=0)
        print(f"Throttled packet: {packet.summary()}")
    except Exception as e:
        print(f"Error throttling packet: {e}")

def start_throttling(interface, target_ip, target_port, bandwidth_limit):
    """
    Starts the bandwidth throttling process.

    :param interface: The network interface to monitor.
    :param target_ip: The target IP address.
    :param target_port: The target port.
    :param bandwidth_limit: The bandwidth limit in kbps.
    """
    print(f"Throttling traffic to {target_ip}:{target_port} at {bandwidth_limit} kbps.")

    def packet_handler(packet):
        if packet.haslayer(IP) and packet.haslayer(TCP):
            if packet[IP].dst == target_ip and packet[TCP].dport == target_port:
                throttle_packet(packet, bandwidth_limit)

    sniff(iface=interface, filter=f"ip host {target_ip} and tcp port {target_port}", prn=packet_handler, store=0)

if __name__ == "__main__":
    print("Welcome to the Network Bandwidth Throttler.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface, target, and bandwidth limit
    interface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ").strip()
    target_ip = input("Enter the target IP address (e.g., '192.168.1.100'): ").strip()
    target_port = int(input("Enter the target port (e.g., 80): ").strip())
    bandwidth_limit = float(input("Enter the bandwidth limit in kbps (e.g., 512): ").strip())

    try:
        start_throttling(interface, target_ip, target_port, bandwidth_limit)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping bandwidth throttler.")
    except Exception as e:
        print(f"An error occurred: {e}")

