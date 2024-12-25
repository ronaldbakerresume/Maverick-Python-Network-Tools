"""
Packet Replay Tool
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

This script captures network packets and replays them to a target network.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet capture).
2. Capture packets and save them to a file.
3. Replay the captured packets to a target network.
4. Modify this script to extend functionality as needed.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 packet_replay_tool.py
"""

from scapy.all import sniff, wrpcap, rdpcap, sendp

def capture_packets(output_file, iface):
    """
    Captures network packets and saves them to a file.

    :param output_file: The name of the file to save packets.
    :param iface: The network interface to sniff on.
    """
    print(f"Capturing packets on interface {iface}. Press Ctrl+C to stop.\n")
    try:
        packets = sniff(iface=iface, timeout=60)  # Capture packets for 60 seconds
        wrpcap(output_file, packets)
        print(f"Packets saved to {output_file}.")
    except Exception as e:
        print(f"Error capturing packets: {e}")

def replay_packets(input_file, iface):
    """
    Replays packets from a file to a network.

    :param input_file: The name of the file containing packets.
    :param iface: The network interface to send packets on.
    """
    print(f"Replaying packets from {input_file} on interface {iface}...\n")
    try:
        packets = rdpcap(input_file)
        sendp(packets, iface=iface, verbose=1)
        print("Packet replay complete.")
    except Exception as e:
        print(f"Error replaying packets: {e}")

if __name__ == "__main__":
    print("Welcome to the Packet Replay Tool.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input mode: capture or replay
    print("Choose an operation:")
    print("1. Capture Packets")
    print("2. Replay Packets")
    choice = input("Enter your choice (1/2): ")

    # Input network interface
    iface = input("Enter the network interface to use (e.g., 'eth0', 'wlan0'): ")

    # Execute the chosen operation
    try:
        if choice == "1":
            output_file = input("Enter the output file name for captured packets (e.g., 'capture.pcap'): ")
            capture_packets(output_file, iface)
        elif choice == "2":
            input_file = input("Enter the input file name for replaying packets (e.g., 'capture.pcap'): ")
            replay_packets(input_file, iface)
        else:
            print("Invalid choice. Exiting.")
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except Exception as e:
        print(f"An error occurred: {e}")

