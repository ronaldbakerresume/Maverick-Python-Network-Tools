"""
DNS Query Logger
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

This script monitors DNS queries and logs details including domains, source IPs, and query types.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet capture).
2. Specify the network interface and log file path.
3. The script will capture and log DNS query details.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 dns_query_logger.py
"""

from scapy.all import sniff, DNS, DNSQR, IP
import datetime

def log_dns_query(packet, log_file):
    """
    Logs DNS query details to a file.

    :param packet: The captured DNS query packet.
    :param log_file: The path to the log file.
    """
    if packet.haslayer(DNS) and packet[DNS].opcode == 0:  # Standard query
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        queried_domain = packet[DNSQR].qname.decode("utf-8")
        query_type = packet[DNSQR].qtype
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_entry = f"{timestamp} | DNS Query | {src_ip} -> {dst_ip} | Domain: {queried_domain} | Type: {query_type}\n"
        print(log_entry.strip())  # Print to console
        with open(log_file, "a") as f:
            f.write(log_entry)

if __name__ == "__main__":
    print("Welcome to the DNS Query Logger.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface and log file path
    interface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ").strip()
    log_file = input("Enter the path to save the log file (e.g., 'dns_log.txt'): ").strip()

    try:
        print(f"Monitoring DNS queries on interface {interface}. Logging to {log_file}. Press Ctrl+C to stop.")
        sniff(iface=interface, filter="udp port 53", prn=lambda pkt: log_dns_query(pkt, log_file), store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping DNS query logger.")
    except Exception as e:
        print(f"An error occurred: {e}")

