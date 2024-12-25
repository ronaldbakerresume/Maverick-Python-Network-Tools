"""
Protocol Analyzer
Developer: Ronald Baker

This script captures network packets and analyzes specific protocols (HTTP, FTP, SMB).
It provides insights into:
- HTTP Requests and Responses
- FTP Commands
- SMB Protocol Details

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet capture).
2. Enter the network interface to sniff on (e.g., 'eth0', 'wlan0').
3. The script will analyze packets in real-time and display protocol-specific details.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 protocol_analyzer.py
"""

from scapy.all import sniff, TCP, IP, Raw

def process_http(packet):
    """
    Processes HTTP packets and extracts relevant details.

    :param packet: The captured HTTP packet.
    """
    try:
        if packet.haslayer(Raw):
            payload = packet[Raw].load.decode('utf-8', errors='ignore')
            if "HTTP" in payload:
                print(f"\n[HTTP Packet] Source: {packet[IP].src} -> Destination: {packet[IP].dst}")
                print(payload.splitlines()[0])  # Display the HTTP request or response line
    except Exception as e:
        print(f"Error processing HTTP packet: {e}")

def process_ftp(packet):
    """
    Processes FTP packets and extracts commands.

    :param packet: The captured FTP packet.
    """
    try:
        if packet.haslayer(Raw):
            payload = packet[Raw].load.decode('utf-8', errors='ignore')
            if payload.startswith(("USER", "PASS", "STOR", "RETR")):
                print(f"\n[FTP Packet] Source: {packet[IP].src} -> Destination: {packet[IP].dst}")
                print(f"FTP Command: {payload.strip()}")
    except Exception as e:
        print(f"Error processing FTP packet: {e}")

def process_smb(packet):
    """
    Processes SMB packets and identifies SMB communication.

    :param packet: The captured SMB packet.
    """
    try:
        if packet.haslayer(TCP) and packet[TCP].dport == 445:
            print(f"\n[SMB Packet] Source: {packet[IP].src} -> Destination: {packet[IP].dst}")
            print("SMB Protocol communication detected.")
    except Exception as e:
        print(f"Error processing SMB packet: {e}")

def packet_handler(packet):
    """
    Handles packets and routes them to the appropriate protocol analyzer.

    :param packet: The captured network packet.
    """
    if packet.haslayer(TCP):
        process_http(packet)
        process_ftp(packet)
        process_smb(packet)

if __name__ == "__main__":
    print("Welcome to the Protocol Analyzer.")
    print("Developer: Ronald Baker\n")

    # Prompt the user to input the network interface
    iface = input("Enter the network interface to sniff on (e.g., 'eth0', 'wlan0'): ")

    # Start packet sniffing
    try:
        print(f"Sniffing on interface: {iface}")
        print("Press Ctrl+C to stop.\n")
        sniff(iface=iface, prn=packet_handler, store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except Exception as e:
        print(f"An error occurred: {e}")

