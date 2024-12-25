"""
Network Packet Loss Monitor
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

This script monitors network packet loss by sending ICMP echo requests.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for ICMP requests).
2. Specify the target host to monitor.
3. The script will calculate and display packet loss in real-time.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 network_packet_loss_monitor.py
"""

from scapy.all import IP, ICMP, sr1
import time

def monitor_packet_loss(target, interval, max_packets):
    """
    Monitors packet loss by sending ICMP requests.

    :param target: The target IP or hostname to ping.
    :param interval: Time between pings in seconds.
    :param max_packets: Number of packets to send.
    """
    sent_packets = 0
    received_packets = 0

    print(f"Monitoring packet loss to {target}...")
    print("Press Ctrl+C to stop.\n")

    try:
        for _ in range(max_packets):
            sent_packets += 1
            packet = IP(dst=target) / ICMP()
            reply = sr1(packet, timeout=1, verbose=0)

            if reply:
                received_packets += 1
                print(f"Packet {sent_packets}: Reply from {target}")
            else:
                print(f"Packet {sent_packets}: No response")

            time.sleep(interval)

        loss_percentage = ((sent_packets - received_packets) / sent_packets) * 100
        print(f"\nTotal Packets Sent: {sent_packets}")
        print(f"Total Packets Received: {received_packets}")
        print(f"Packet Loss: {loss_percentage:.2f}%")

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
        loss_percentage = ((sent_packets - received_packets) / sent_packets) * 100
        print(f"Total Packets Sent: {sent_packets}")
        print(f"Total Packets Received: {received_packets}")
        print(f"Packet Loss: {loss_percentage:.2f}%")

if __name__ == "__main__":
    print("Welcome to the Network Packet Loss Monitor.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input target and monitoring parameters
    target = input("Enter the target IP or hostname (e.g., 8.8.8.8 or google.com): ").strip()
    interval = float(input("Enter the interval between pings (seconds, e.g., 1): ").strip())
    max_packets = int(input("Enter the number of packets to send (e.g., 10): ").strip())

    try:
        monitor_packet_loss(target, interval, max_packets)
    except Exception as e:
        print(f"An error occurred: {e}")

