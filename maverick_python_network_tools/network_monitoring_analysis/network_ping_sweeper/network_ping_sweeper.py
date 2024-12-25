"""
Network Ping Sweeper
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

This script performs a ping sweep over a range of IP addresses to identify active hosts.

Instructions:
1. Run the script from the terminal.
2. Specify the target IP range (e.g., 192.168.1.1-192.168.1.254).
3. The script will display active hosts and log results.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
python3 network_ping_sweeper.py
"""

from scapy.all import IP, ICMP, sr1
import ipaddress

def ping_sweep(start_ip, end_ip, timeout, log_file):
    """
    Performs a ping sweep over a range of IP addresses.

    :param start_ip: The starting IP address.
    :param end_ip: The ending IP address.
    :param timeout: The timeout for each ping request.
    :param log_file: The path to the log file.
    """
    print(f"Starting ping sweep from {start_ip} to {end_ip}...")

    active_hosts = []
    for ip in ipaddress.IPv4Network(f"{start_ip}/{end_ip}", strict=False):
        pkt = IP(dst=str(ip)) / ICMP()
        reply = sr1(pkt, timeout=timeout, verbose=0)

        if reply is not None:
            print(f"Active host detected: {ip}")
            active_hosts.append(str(ip))

            # Log the result
            with open(log_file, "a") as f:
                f.write(f"Active host: {ip}\n")

    print("\nPing Sweep Complete!")
    print(f"Active hosts: {', '.join(active_hosts) if active_hosts else 'None found.'}")

if __name__ == "__main__":
    print("Welcome to the Network Ping Sweeper.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input IP range and timeout
    start_ip = input("Enter the starting IP address (e.g., 192.168.1.1): ").strip()
    end_ip = input("Enter the ending IP address (e.g., 192.168.1.254): ").strip()
    timeout = float(input("Enter the timeout for each ping (seconds, e.g., 1): ").strip())
    log_file = input("Enter the path to save the log file (e.g., 'ping_sweep_log.txt'): ").strip()

    try:
        ping_sweep(start_ip, end_ip, timeout, log_file)
    except ValueError:
        print("Error: Invalid IP address or range.")
    except Exception as e:
        print(f"An error occurred: {e}")

