"""
Network Latency Measurement Tool
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

This script measures latency to a specified host using ICMP echo requests (ping).

Instructions:
1. Run the script with `sudo` (superuser privileges are required for ICMP requests).
2. Specify the target host and interval between pings.
3. The script will measure latency and log results.

Required Libraries:
- scapy (Install with `pip install scapy`)

Usage:
sudo python3 network_latency_tool.py
"""

from scapy.all import IP, ICMP, sr1
import time
import datetime

def measure_latency(target, interval, log_file):
    """
    Measures the latency to a target host at regular intervals.

    :param target: The target host to ping.
    :param interval: Time between pings in seconds.
    :param log_file: The path to the log file.
    """
    print(f"Measuring latency to {target} every {interval} seconds...")
    print("Press Ctrl+C to stop.\n")

    with open(log_file, "a") as log:
        log.write(f"Latency Measurement to {target}\n")
        log.write("=" * 40 + "\n")

    try:
        while True:
            start_time = time.time()
            packet = IP(dst=target) / ICMP()
            reply = sr1(packet, timeout=1, verbose=0)

            if reply:
                rtt = (time.time() - start_time) * 1000  # Convert to milliseconds
                print(f"{datetime.datetime.now()} | Reply from {target}: {rtt:.2f} ms")
                with open(log_file, "a") as log:
                    log.write(f"{datetime.datetime.now()} | Reply from {target}: {rtt:.2f} ms\n")
            else:
                print(f"{datetime.datetime.now()} | Request to {target} timed out.")
                with open(log_file, "a") as log:
                    log.write(f"{datetime.datetime.now()} | Request to {target} timed out.\n")

            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopping latency measurement.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the Network Latency Measurement Tool.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input target host and interval
    target = input("Enter the target host (e.g., google.com or 8.8.8.8): ").strip()
    interval = float(input("Enter the interval between pings (seconds, e.g., 1): ").strip())
    log_file = input("Enter the path to save the log file (e.g., 'latency_log.txt'): ").strip()

    try:
        measure_latency(target, interval, log_file)
    except Exception as e:
        print(f"An error occurred: {e}")

