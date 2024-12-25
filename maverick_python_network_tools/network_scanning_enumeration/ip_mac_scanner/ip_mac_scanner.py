"""
IP and MAC Address Scanner
Developer: Ronald Baker

This script scans a local network and retrieves the IP and MAC addresses of connected devices.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for ARP scanning).
2. Enter the target network range to scan (e.g., '192.168.1.0/24').
3. The script will display detected devices on the local network.
4. Modify this script to extend functionality as needed.

Required Library:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 ip_mac_scanner.py
"""

from scapy.all import ARP, Ether, srp

def ip_mac_scanner(network_range):
    """
    Scans the local network for connected devices and prints their IP and MAC addresses.

    :param network_range: The target network range to scan (e.g., '192.168.1.0/24').
    """
    print(f"Scanning the network: {network_range}")
    print("This might take a few seconds...\n")

    # Create an ARP request packet
    arp_request = ARP(pdst=network_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC address
    packet = broadcast / arp_request

    # Send the packet and receive responses
    answered, unanswered = srp(packet, timeout=2, verbose=0)

    print(f"{'IP Address':<20}{'MAC Address':<20}")
    print("-" * 40)

    # Iterate through the answered packets
    for sent, received in answered:
        print(f"{received.psrc:<20}{received.hwsrc:<20}")

    print("\nScan complete. Extend this script for additional functionality as needed.")

if __name__ == "__main__":
    print("Welcome to the IP and MAC Address Scanner.")
    print("Developer: Ronald Baker\n")

    # Prompt the user to input the target network range
    target_network = input("Enter the target network range (e.g., '192.168.1.0/24'): ")

    # Run the scanner
    try:
        ip_mac_scanner(target_network)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except Exception as e:
        print(f"An error occurred: {e}")

