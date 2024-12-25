"""
Network Device Enumerator
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

This script scans the network to enumerate connected devices.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for ARP scanning).
2. Specify the IP range to scan.
3. The script will display information about each discovered device.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 network_device_enumerator.py
"""

from scapy.all import ARP, Ether, srp

def enumerate_devices(ip_range):
    """
    Scans the network and enumerates connected devices.

    :param ip_range: The range of IPs to scan (e.g., 192.168.1.0/24).
    :return: A list of dictionaries containing device information.
    """
    print(f"Scanning network range: {ip_range}")
    devices = []

    # Create ARP request
    arp_request = ARP(pdst=ip_range)
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    request = ether_frame / arp_request

    # Send the request and capture responses
    answered, _ = srp(request, timeout=2, verbose=0)

    for sent, received in answered:
        devices.append({"ip": received.psrc, "mac": received.hwsrc})

    return devices

if __name__ == "__main__":
    print("Welcome to the Network Device Enumerator.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input IP range
    ip_range = input("Enter the IP range to scan (e.g., 192.168.1.0/24): ").strip()

    try:
        devices = enumerate_devices(ip_range)

        print("\nDevices Found:")
        print(f"{'IP Address':<20}{'MAC Address':<20}")
        print("=" * 40)
        for device in devices:
            print(f"{device['ip']:<20}{device['mac']:<20}")
    except Exception as e:
        print(f"An error occurred: {e}")

