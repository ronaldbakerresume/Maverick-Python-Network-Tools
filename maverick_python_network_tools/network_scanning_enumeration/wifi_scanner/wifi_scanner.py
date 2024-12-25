"""
Wi-Fi Network Scanner
Developer: Ronald Baker

This script scans for nearby Wi-Fi networks and displays their details, such as:
- SSID (Network Name)
- BSSID (Access Point MAC Address)
- Signal Strength (in dBm)
- Channel (Wi-Fi frequency channel)

Instructions:
1. Run the script with `sudo` (superuser privileges are required for scanning).
2. Enter the wireless interface you wish to scan on (e.g., wlan0, en0).
3. The script will display detected Wi-Fi networks.
4. Modify this script to extend functionality as needed.

Required Library:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 wifi_scanner.py
"""

from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon, Dot11Elt

def wifi_scanner(interface):
    """
    Scans for nearby Wi-Fi networks and prints details to the console.

    :param interface: The name of the wireless interface to scan on (e.g., 'wlan0', 'en0').
    """
    # Dictionary to store discovered networks (prevents duplicates)
    networks = {}

    def packet_handler(packet):
        # Check if the packet is a Beacon frame
        if packet.haslayer(Dot11Beacon):
            ssid = packet[Dot11Elt].info.decode('utf-8', errors='ignore')  # Extract SSID
            bssid = packet[Dot11].addr2  # Extract BSSID (MAC Address)
            try:
                signal_strength = packet.dBm_AntSignal  # Extract signal strength in dBm
            except:
                signal_strength = "Unknown"  # Signal strength might not always be available
            try:
                channel = int(ord(packet[Dot11Elt:3].info))  # Extract channel
            except:
                channel = "Unknown"  # Channel might not always be extractable

            # Add to networks if not already recorded
            if bssid not in networks:
                networks[bssid] = (ssid, signal_strength, channel)
                print(f"SSID: {ssid}, BSSID: {bssid}, Signal: {signal_strength} dBm, Channel: {channel}")

    # Notify user about the scanning process
    print(f"Scanning for Wi-Fi networks on interface: {interface}...")
    print("Press Ctrl+C to stop scanning.\n")

    # Start sniffing packets on the specified interface
    sniff(iface=interface, prn=packet_handler, store=0)

if __name__ == "__main__":
    print("Welcome to the Wi-Fi Network Scanner.")
    print("Developer: Ronald Baker\n")

    # Prompt the user to input the wireless interface
    iface = input("Enter your wireless interface (e.g., wlan0, en0): ")

    # Run the scanner
    try:
        wifi_scanner(iface)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except Exception as e:
        print(f"An error occurred: {e}")

