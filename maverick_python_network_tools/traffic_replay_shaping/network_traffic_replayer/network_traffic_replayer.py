"""
Network Traffic Replayer
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

This script replays network traffic from a PCAP file onto the network.

Instructions:
1. Run the script with `sudo` (superuser privileges are required to send raw packets).
2. Specify the PCAP file and the network interface.
3. The script will replay all packets in the PCAP file.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 network_traffic_replayer.py
"""

from scapy.all import rdpcap, sendp

def replay_traffic(pcap_file, interface):
    """
    Replays network traffic from a PCAP file.

    :param pcap_file: Path to the PCAP file.
    :param interface: Network interface to replay traffic on.
    """
    try:
        print(f"Reading packets from {pcap_file}...")
        packets = rdpcap(pcap_file)
        print(f"Loaded {len(packets)} packets.")

        print(f"Replaying packets on interface {interface}...")
        sendp(packets, iface=interface, verbose=True)
        print("Replay complete.")
    except FileNotFoundError:
        print(f"Error: File {pcap_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the Network Traffic Replayer.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input PCAP file and interface
    pcap_file = input("Enter the path to the PCAP file (e.g., 'traffic.pcap'): ").strip()
    interface = input("Enter the network interface to replay traffic on (e.g., 'eth0', 'wlan0'): ").strip()

    try:
        replay_traffic(pcap_file, interface)
    except Exception as e:
        print(f"An error occurred: {e}")

