"""
Remote Command Execution Monitor
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

This script monitors network traffic for suspicious payloads indicative of remote command execution.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for packet capture).
2. Specify the network interface to monitor.
3. The script will analyze traffic payloads for signs of unauthorized command execution.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 remote_command_execution_monitor.py
"""

from scapy.all import sniff, IP, TCP, Raw
import re

# Patterns indicative of command execution attempts
SUSPICIOUS_PATTERNS = [
    r"bash",
    r"sh",
    r"python",
    r"perl",
    r"wget",
    r"curl",
    r"/bin/",
    r"nc ",
    r"&&",
    r"||",
    r";",
]

def analyze_packet(packet):
    """
    Analyzes packet payloads for suspicious patterns.

    :param packet: The captured network packet.
    """
    if packet.haslayer(Raw):
        payload = packet[Raw].load.decode('utf-8', errors='ignore')

        for pattern in SUSPICIOUS_PATTERNS:
            if re.search(pattern, payload, re.IGNORECASE):
                print("\nALERT: Potential Remote Command Execution Detected!")
                print(f"Source IP: {packet[IP].src}")
                print(f"Destination IP: {packet[IP].dst}")
                print(f"Payload: {payload}")
                return

if __name__ == "__main__":
    print("Welcome to the Remote Command Execution Monitor.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface
    interface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ").strip()

    try:
        print(f"Monitoring traffic on interface {interface}. Press Ctrl+C to stop.")
        sniff(iface=interface, filter="tcp", prn=analyze_packet, store=0)
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except KeyboardInterrupt:
        print("\nStopping command execution monitor.")
    except Exception as e:
        print(f"An error occurred: {e}")

