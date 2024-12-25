"""
Wireless Signal Strength Monitor
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

This script monitors the signal strength of nearby wireless networks in real-time.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for wireless monitoring).
2. Specify the wireless interface to monitor.
3. The script will display real-time signal strength and network information.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 wireless_signal_strength_monitor.py
"""

from scapy.all import sniff, Dot11

# Dictionary to track networks and signal strengths
networks = {}

def monitor_signal(packet):
    """
    Captures and displays signal strength for wireless networks.

    :param packet: The captured packet.
    """
    if packet.haslayer(Dot11):
        ssid = packet.info.decode("utf-8", errors="ignore") if packet.info else "Hidden Network"
        bssid = packet.addr2
        signal_strength = packet.dBm_AntSignal if hasattr(packet, "dBm_AntSignal") else "N/A"
        channel = int(ord(packet[Dot11Elt:3].info)) if packet.haslayer(Dot11Elt) else "N/A"

        if bssid not in networks:
            networks[bssid] = {"SSID": ssid, "Signal Strength": signal_strength, "Channel": channel}
            print(f"Detected Network: SSID={ssid}, BSSID={bssid}, Signal={signal_strength} dBm, Channel={channel}")
        else:
            networks[bssid]["Signal Strength"] = signal_strength

if __name__ == "__main__":
    print("Welcome to the Wireless Signal Strength Monitor.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input wireless interface
    interface = input("Enter the wireless interface to monitor (e.g., 'wlan0mon'): ").strip()

    try:
        print(f"Monitoring wireless signals on interface {interface}. Press Ctrl+C to stop.")
        sniff(iface=interface, prn=monitor_signal, store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping wireless signal strength monitor.")
    except Exception as e:
        print(f"An error occurred: {e}")

