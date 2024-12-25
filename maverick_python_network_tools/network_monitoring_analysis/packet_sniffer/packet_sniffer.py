"""
Packet Sniffer and Analyzer
Developer: Ronald Baker

This script captures and analyzes network packets in real-time.
It displays details such as:
- Source IP
- Destination IP
- Protocol
- Raw Packet Data

Instructions:
1. Run the script with `sudo` (superuser privileges are required for sniffing).
2. Enter the network interface to sniff on (e.g., 'eth0', 'wlan0').
3. The script will capture packets and display their details in real-time.
4. Modify this script to extend functionality as needed.

Required Library:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 packet_sniffer.py
"""

from scapy.all import sniff, IP, TCP, UDP, ARP

def process_packet(packet):
    """
    Processes and displays details about a captured packet.

    :param packet: The captured packet object.
    """
    try:
        # Identify the type of packet
        if packet.haslayer(IP):
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            protocol = "TCP" if packet.haslayer(TCP) else "UDP" if packet.haslayer(UDP) else "Other"

            print(f"[IP Packet] Source: {ip_src}, Destination: {ip_dst}, Protocol: {protocol}")
        elif packet.haslayer(ARP):
            print(f"[ARP Packet] Source: {packet[ARP].psrc}, Destination: {packet[ARP].pdst}")
        else:
            print("[Unknown Packet Type]")
        
        # Display raw packet data (optional, can be verbose)
        print(f"Raw Data: {bytes(packet)[:50]}...\n")  # Display the first 50 bytes
    except Exception as e:
        print(f"Error processing packet: {e}")

def start_sniffer(interface):
    """
    Starts the packet sniffer on the specified network interface.

    :param interface: The network interface to sniff on (e.g., 'eth0', 'wlan0').
    """
    print(f"Starting packet sniffer on interface: {interface}")
    print("Press Ctrl+C to stop sniffing.\n")

    try:
        # Start sniffing and process each packet
        sniff(iface=interface, prn=process_packet, store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the Packet Sniffer and Analyzer.")
    print("Developer: Ronald Baker\n")

    # Prompt the user to input the network interface
    iface = input("Enter the network interface to sniff on (e.g., 'eth0', 'wlan0'): ")

    # Start the sniffer
    try:
        start_sniffer(iface)
    except Exception as e:
        print(f"An error occurred: {e}")

