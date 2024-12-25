"""
Network Packet Analyzer with Detailed Protocol Breakdown
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

This script captures network packets and provides a detailed breakdown of their layers and protocols.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet capture).
2. Specify the network interface to monitor and log file path.
3. The script will display and log packet details.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 network_packet_analyzer.py
"""

from scapy.all import sniff, hexdump

def analyze_packet(packet, log_file):
    """
    Logs detailed packet analysis to a file.

    :param packet: The captured packet.
    :param log_file: The path to the log file.
    """
    packet_summary = packet.summary()
    packet_details = packet.show(dump=True)

    print("\nPacket Summary:")
    print(packet_summary)
    print("\nPacket Details:")
    print(packet_details)

    with open(log_file, "a") as f:
        f.write("\nPacket Summary:\n")
        f.write(packet_summary + "\n")
        f.write("\nPacket Details:\n")
        f.write(packet_details + "\n")
        f.write("=" * 50 + "\n")

if __name__ == "__main__":
    print("Welcome to the Network Packet Analyzer with Detailed Protocol Breakdown.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface and log file path
    interface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ").strip()
    log_file = input("Enter the path to save the log file (e.g., 'packet_log.txt'): ").strip()

    try:
        print(f"Analyzing packets on interface {interface}. Logging to {log_file}. Press Ctrl+C to stop.")
        sniff(iface=interface, prn=lambda pkt: analyze_packet(pkt, log_file), store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping packet analyzer.")
    except Exception as e:
        print(f"An error occurred: {e}")

