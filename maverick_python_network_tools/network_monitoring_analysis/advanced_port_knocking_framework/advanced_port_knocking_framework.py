"""
Advanced Port Knocking Framework
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

This script simulates port knocking by sending sequences of packets to predefined ports on a target server.

Instructions:
1. Run the script from the terminal.
2. Enter the target server's IP and the sequence of ports.
3. The script will send the packet sequence and display results.
4. Modify this script to extend functionality as needed.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
python3 advanced_port_knocking_framework.py
"""

from scapy.all import IP, TCP, send

def send_knock_sequence(target, port_sequence):
    """
    Sends a sequence of TCP packets to the specified ports on the target.

    :param target: The target server's IP address.
    :param port_sequence: A list of ports to knock.
    """
    print(f"\nSending port knocking sequence to {target}...")
    for port in port_sequence:
        packet = IP(dst=target)/TCP(dport=port, flags="S")
        send(packet, verbose=0)
        print(f"Knocked on port {port}")
    print("Port knocking sequence complete.")

if __name__ == "__main__":
    print("Welcome to the Advanced Port Knocking Framework.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input target server IP
    target_ip = input("Enter the target server's IP address: ")

    # Input port sequence
    port_sequence_input = input(
        "Enter the port sequence (comma-separated, e.g., 1234,5678,9100): "
    )
    try:
        port_sequence = [int(port.strip()) for port in port_sequence_input.split(",")]
    except ValueError:
        print("Error: Invalid port sequence format. Exiting.")
        exit(1)

    # Send port knocking sequence
    try:
        send_knock_sequence(target_ip, port_sequence)
    except Exception as e:
        print(f"An error occurred: {e}")

