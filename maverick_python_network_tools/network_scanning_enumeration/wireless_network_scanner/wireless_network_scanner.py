"""
Wireless Network Scanner
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

This script scans for nearby wireless networks and displays their details.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for wireless scanning).
2. Specify the wireless interface to monitor.
3. The script will display details of detected wireless networks.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 wireless_network_scanner.py
"""

from scapy.all import sniff, Dot11

# Dictionary to store detected networks
networks = {}

def process_packet(packet):
    """
    Processes each captured packet to extract wireless network details.

    :param packet: The captured packet.
    """
    if packet.haslayer(Dot11Beacon):
        ssid = packet.info.decode("utf-8", errors="ignore")
        bssid = packet.addr2
        channel = int(ord(packet[Dot11Elt:3].info))
        signal_strength = packet.dBm_AntSignal if hasattr(packet, 'dBm_AntSignal') else "N/A"

        if bssid not in networks:
            networks[bssid] = {
                "SSID": ssid,
                "Channel": channel,
                "Signal Strength": signal_strength,
            }
            print(f"Detected Network: SSID: {ssid}, BSSID: {bssid}, Channel: {channel}, Signal: {signal_strength} dBm")

if __name__ == "__main__":
    print("Welcome to the Wireless Network Scanner.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input wireless interface
    interface = input("Enter the wireless interface to monitor (e.g., 'wlan0mon'): ").strip()

    try:
        print(f"Scanning for wireless networks on interface {interface}. Press Ctrl+C to stop.")
        sniff(iface=interface, prn=process_packet, store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping wireless network scanner.")
    except Exception as e:
        print(f"An error occurred: {e}")

