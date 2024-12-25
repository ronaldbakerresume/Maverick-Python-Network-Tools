"""
Wi-Fi Signal Mapper
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

This script maps nearby Wi-Fi networks, logging their signal strength and other details.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for wireless monitoring).
2. Specify the wireless interface in monitor mode.
3. The script will scan nearby Wi-Fi networks and log their details.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 wifi_signal_mapper.py
"""

from scapy.all import sniff, Dot11
import time

def log_wifi_signal(packet, detected_networks):
    """
    Logs Wi-Fi signal information from captured packets.

    :param packet: The captured network packet.
    :param detected_networks: Dictionary of detected networks to avoid duplicates.
    """
    if packet.haslayer(Dot11) and packet.type == 0 and packet.subtype == 8:  # Beacon frames
        ssid = packet.info.decode('utf-8', errors='ignore') if packet.info else "Hidden Network"
        bssid = packet.addr2
        signal_strength = packet.dBm_AntSignal if hasattr(packet, 'dBm_AntSignal') else "N/A"
        channel = packet[Dot11].channel if hasattr(packet, 'channel') else "N/A"

        if bssid not in detected_networks:
            detected_networks[bssid] = {"SSID": ssid, "Signal": signal_strength, "Channel": channel}
            print(f"Detected Network: SSID={ssid}, BSSID={bssid}, Signal={signal_strength}, Channel={channel}")

if __name__ == "__main__":
    print("Welcome to the Wi-Fi Signal Mapper.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input wireless interface
    interface = input("Enter the wireless interface in monitor mode (e.g., 'wlan0mon'): ").strip()
    detected_networks = {}

    try:
        print(f"Scanning Wi-Fi networks on interface {interface}. Press Ctrl+C to stop.")
        sniff(iface=interface, prn=lambda pkt: log_wifi_signal(pkt, detected_networks), store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nWi-Fi Signal Mapping Complete.")
        print("\nDetected Networks:")
        for bssid, details in detected_networks.items():
            print(f"BSSID: {bssid} | SSID: {details['SSID']} | Signal: {details['Signal']} | Channel: {details['Channel']}")
    except Exception as e:
        print(f"An error occurred: {e}")

