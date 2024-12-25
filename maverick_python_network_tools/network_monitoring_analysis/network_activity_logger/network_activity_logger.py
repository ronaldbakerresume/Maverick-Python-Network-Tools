"""
Network Activity Logger
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

This script captures network traffic and logs details to a file.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet capture).
2. Specify the network interface to monitor and the log file path.
3. The script will capture packets and log details to the specified file.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 network_activity_logger.py
"""

from scapy.all import sniff, IP, TCP, UDP
import datetime

def log_packet(packet, log_file):
    """
    Logs packet details to a file.

    :param packet: The captured packet.
    :param log_file: The path to the log file.
    """
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "TCP" if packet.haslayer(TCP) else "UDP" if packet.haslayer(UDP) else "Other"
        src_port = packet[TCP].sport if packet.haslayer(TCP) else packet[UDP].sport if packet.haslayer(UDP) else "-"
        dst_port = packet[TCP].dport if packet.haslayer(TCP) else packet[UDP].dport if packet.haslayer(UDP) else "-"
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_entry = f"{timestamp} | {src_ip}:{src_port} -> {dst_ip}:{dst_port} | Protocol: {protocol}\n"
        print(log_entry.strip())  # Print to console
        with open(log_file, "a") as f:
            f.write(log_entry)

if __name__ == "__main__":
    print("Welcome to the Network Activity Logger.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface and log file path
    interface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ").strip()
    log_file = input("Enter the path to save the log file (e.g., 'network_log.txt'): ").strip()

    try:
        print(f"Monitoring traffic on interface {interface}. Logging to {log_file}. Press Ctrl+C to stop.")
        sniff(iface=interface, prn=lambda pkt: log_packet(pkt, log_file), store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping network activity logger.")
    except Exception as e:
        print(f"An error occurred: {e}")

