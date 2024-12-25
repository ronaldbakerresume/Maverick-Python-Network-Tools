"""
HTTP Traffic Monitor
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

This script monitors HTTP traffic and logs details including methods, URLs, and headers.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet capture).
2. Specify the network interface and log file path.
3. The script will capture and log HTTP traffic details.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 http_traffic_monitor.py
"""

from scapy.all import sniff, IP, TCP, Raw
import re
import datetime

def log_http_traffic(packet, log_file):
    """
    Logs HTTP traffic details to a file.

    :param packet: The captured HTTP packet.
    :param log_file: The path to the log file.
    """
    if packet.haslayer(Raw):
        payload = packet[Raw].load.decode('utf-8', errors='ignore')
        http_method = re.search(r"(GET|POST|PUT|DELETE|HEAD|OPTIONS|PATCH)", payload)
        if http_method:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            url = re.search(r"Host: (.*?)\r\n", payload)
            full_url = f"http://{url.group(1)}" if url else "Unknown"
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            log_entry = f"{timestamp} | HTTP {http_method.group(0)} | {full_url} | {src_ip}:{src_port} -> {dst_ip}:{dst_port}\n"
            print(log_entry.strip())  # Print to console
            with open(log_file, "a") as f:
                f.write(log_entry)

if __name__ == "__main__":
    print("Welcome to the HTTP Traffic Monitor.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface and log file path
    interface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ").strip()
    log_file = input("Enter the path to save the log file (e.g., 'http_log.txt'): ").strip()

    try:
        print(f"Monitoring HTTP traffic on interface {interface}. Logging to {log_file}. Press Ctrl+C to stop.")
        sniff(iface=interface, filter="tcp port 80", prn=lambda pkt: log_http_traffic(pkt, log_file), store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping HTTP traffic monitor.")
    except Exception as e:
        print(f"An error occurred: {e}")

