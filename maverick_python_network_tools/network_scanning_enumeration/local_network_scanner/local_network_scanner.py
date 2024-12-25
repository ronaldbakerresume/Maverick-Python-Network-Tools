"""
Local Network Scanner
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

This script scans the local network and lists connected devices.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for ARP scanning).
2. Specify the IP range to scan.
3. The script will list active devices with their IP and MAC addresses.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 local_network_scanner.py
"""

from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    """
    Scans the specified IP range using ARP requests.

    :param ip_range: The IP range to scan (e.g., 192.168.1.0/24).
    :return: List of dictionaries containing IP and MAC addresses.
    """
    print(f"Scanning network range: {ip_range}")
    devices = []

    # Create ARP request
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request

    # Send the request and receive responses
    answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    for sent, received in answered_list:
        devices.append({"ip": received.psrc, "mac": received.hwsrc})

    return devices

if __name__ == "__main__":
    print("Welcome to the Local Network Scanner.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input IP range
    ip_range = input("Enter the IP range to scan (e.g., 192.168.1.0/24): ").strip()

    try:
        devices = scan_network(ip_range)

        print("\nDevices Found:")
        print(f"{'IP Address':<20}{'MAC Address':<20}")
        print("=" * 40)
        for device in devices:
            print(f"{device['ip']:<20}{device['mac']:<20}")
    except Exception as e:
        print(f"An error occurred: {e}")

