"""
Network Ping Sweep Tool
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

This script performs a ping sweep to identify active devices in an IP range.

Instructions:
1. Run the script with Python.
2. Specify the IP range to scan.
3. The script will identify active devices in the range.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
python3 network_ping_sweep.py
"""

from scapy.all import sr1, IP, ICMP
import ipaddress

def ping_host(ip):
    """
    Sends a single ICMP echo request to the target IP.

    :param ip: The IP address to ping.
    :return: True if the host responds, False otherwise.
    """
    packet = IP(dst=str(ip)) / ICMP()
    response = sr1(packet, timeout=1, verbose=0)
    return response is not None

def ping_sweep(network_range):
    """
    Performs a ping sweep across a specified IP range.

    :param network_range: The IP range to scan (e.g., 192.168.1.0/24).
    """
    active_hosts = []

    print(f"Performing ping sweep on network range: {network_range}")
    for ip in ipaddress.IPv4Network(network_range, strict=False):
        if ping_host(ip):
            print(f"Host {ip} is active.")
            active_hosts.append(ip)
        else:
            print(f"Host {ip} is not responding.")

    print("\nPing Sweep Complete.")
    print(f"Active Hosts ({len(active_hosts)}):")
    for host in active_hosts:
        print(f"  - {host}")

if __name__ == "__main__":
    print("Welcome to the Network Ping Sweep Tool.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input IP range
    network_range = input("Enter the IP range to scan (e.g., '192.168.1.0/24'): ").strip()

    try:
        ping_sweep(network_range)
    except Exception as e:
        print(f"An error occurred: {e}")

