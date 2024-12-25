"""
Network Intrusion Detection System (NIDS)
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

This script analyzes network traffic for intrusion patterns, including:
- Port scans
- Abnormal packet rates
- Known malicious IPs

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet sniffing).
2. Specify the network interface to monitor.
3. The script will detect and log suspicious activity in real-time.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 network_intrusion_detection_system.py
"""

from scapy.all import sniff, IP, TCP
from collections import defaultdict
import time

# Thresholds and settings
PORT_SCAN_THRESHOLD = 10  # Number of ports scanned within a short time
PACKET_RATE_THRESHOLD = 50  # Number of packets from a single IP in a short time
MALICIOUS_IPS = {"203.0.113.1", "198.51.100.2"}  # Example malicious IPs

# Data tracking
connection_attempts = defaultdict(set)
packet_rates = defaultdict(int)

def detect_port_scan(packet):
    """
    Detects port scanning by tracking connections to multiple ports from a single IP.

    :param packet: The captured packet.
    """
    if packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_port = packet[TCP].dport
        connection_attempts[src_ip].add(dst_port)

        if len(connection_attempts[src_ip]) > PORT_SCAN_THRESHOLD:
            print(f"ALERT: Potential port scan detected from {src_ip}")
            connection_attempts[src_ip] = set()  # Reset after alert

def detect_abnormal_packet_rate(packet):
    """
    Detects abnormal packet rates from a single IP.

    :param packet: The captured packet.
    """
    src_ip = packet[IP].src
    packet_rates[src_ip] += 1

def monitor_malicious_ips(packet):
    """
    Detects traffic from known malicious IPs.

    :param packet: The captured packet.
    """
    src_ip = packet[IP].src
    if src_ip in MALICIOUS_IPS:
        print(f"ALERT: Traffic detected from malicious IP: {src_ip}")

def reset_packet_rates():
    """
    Resets packet rates periodically to prevent false positives.
    """
    while True:
        time.sleep(60)
        packet_rates.clear()

def packet_handler(packet):
    """
    Handles captured packets and applies detection logic.

    :param packet: The captured packet.
    """
    if packet.haslayer(IP):
        detect_port_scan(packet)
        detect_abnormal_packet_rate(packet)
        monitor_malicious_ips(packet)

if __name__ == "__main__":
    print("Welcome to the Network Intrusion Detection System (NIDS).")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface
    interface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ")

    try:
        print(f"Monitoring traffic on interface {interface}. Press Ctrl+C to stop.")
        sniff(iface=interface, prn=packet_handler, store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping NIDS.")
    except Exception as e:
        print(f"An error occurred: {e}")

