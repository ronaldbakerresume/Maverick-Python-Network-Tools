"""
Network Intrusion Detection Tool
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

This script monitors network traffic and detects potential intrusions.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet capture).
2. Specify the network interface to monitor.
3. The script will monitor traffic and provide real-time alerts for suspicious activity.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 network_intrusion_detection.py
"""

from scapy.all import sniff, IP, TCP, UDP
from collections import defaultdict
import time

# Data storage for detection
traffic_stats = defaultdict(int)
attack_threshold = 50  # Number of packets in a short duration to trigger an alert
check_interval = 5  # Check interval in seconds

def detect_intrusions(packet):
    """
    Analyzes packets for potential intrusion patterns.

    :param packet: The captured packet.
    """
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        traffic_stats[src_ip] += 1

def monitor_traffic():
    """
    Monitors traffic statistics and alerts for suspicious activity.
    """
    while True:
        time.sleep(check_interval)
        print("\nTraffic Statistics:")
        for ip, count in traffic_stats.items():
            print(f"Source IP: {ip}, Packets: {count}")

            # Alert for suspicious activity
            if count > attack_threshold:
                print(f"ALERT: Potential intrusion detected from IP {ip} with {count} packets!")
        
        # Reset stats for the next interval
        traffic_stats.clear()

if __name__ == "__main__":
    print("Welcome to the Network Intrusion Detection Tool.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface
    interface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ").strip()

    try:
        # Start monitoring thread
        import threading
        monitor_thread = threading.Thread(target=monitor_traffic, daemon=True)
        monitor_thread.start()

        print(f"Monitoring traffic on interface {interface}. Press Ctrl+C to stop.")
        sniff(iface=interface, prn=detect_intrusions, store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping intrusion detection tool.")
    except Exception as e:
        print(f"An error occurred: {e}")

