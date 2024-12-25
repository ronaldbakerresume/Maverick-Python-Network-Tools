"""
MAC Address Spoofer
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

This script changes the MAC address of a specified network interface temporarily.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for modifying network settings).
2. Specify the network interface and the new MAC address.
3. The script will apply the new MAC address temporarily.

Required Libraries:
- None (Standard Python libraries are used)

Usage:
sudo python3 mac_address_spoofer.py
"""

import os
import random
import re
import subprocess

def get_current_mac(interface):
    """
    Retrieves the current MAC address of the specified interface.

    :param interface: The network interface name.
    :return: The current MAC address or None if not found.
    """
    try:
        output = subprocess.check_output(["ifconfig", interface], universal_newlines=True)
        mac_address = re.search(r"ether ([0-9a-fA-F:]{17})", output)
        return mac_address.group(1) if mac_address else None
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving MAC address: {e}")
        return None

def change_mac(interface, new_mac):
    """
    Changes the MAC address of the specified interface.

    :param interface: The network interface name.
    :param new_mac: The new MAC address to set.
    """
    try:
        print(f"Changing MAC address of {interface} to {new_mac}...")
        os.system(f"sudo ifconfig {interface} down")
        os.system(f"sudo ifconfig {interface} hw ether {new_mac}")
        os.system(f"sudo ifconfig {interface} up")
        print(f"MAC address changed successfully to {new_mac}.")
    except Exception as e:
        print(f"Error changing MAC address: {e}")

def generate_random_mac():
    """
    Generates a random MAC address.

    :return: A randomly generated MAC address.
    """
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: f"{x:02x}", mac))

if __name__ == "__main__":
    print("Welcome to the MAC Address Spoofer.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface and MAC address
    interface = input("Enter the network interface (e.g., 'eth0', 'wlan0'): ").strip()
    current_mac = get_current_mac(interface)
    if current_mac:
        print(f"Current MAC address of {interface}: {current_mac}")

    use_random = input("Do you want to generate a random MAC address? (yes/no): ").strip().lower()
    new_mac = generate_random_mac() if use_random == "yes" else input("Enter the new MAC address: ").strip()

    if re.match(r"^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$", new_mac):
        change_mac(interface, new_mac)
    else:
        print("Invalid MAC address format.")

