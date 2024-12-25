"""
Network Bandwidth Monitor
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

This script monitors network bandwidth usage in real-time.

Instructions:
1. Run the script from the terminal.
2. Specify the network interface to monitor.
3. The script will display real-time upload and download rates.

Required Libraries:
- psutil (Install with `pip install psutil`)

Usage:
python3 network_bandwidth_monitor.py
"""

import psutil
import time

def get_network_stats(interface):
    """
    Retrieves network statistics for the specified interface.

    :param interface: The network interface name.
    :return: Bytes sent and received as a tuple.
    """
    stats = psutil.net_io_counters(pernic=True)
    if interface in stats:
        return stats[interface].bytes_sent, stats[interface].bytes_recv
    else:
        raise ValueError(f"Interface {interface} not found. Please check the interface name.")

def monitor_bandwidth(interface, interval):
    """
    Monitors network bandwidth usage in real-time.

    :param interface: The network interface to monitor.
    :param interval: Time interval for updates in seconds.
    """
    try:
        print(f"Monitoring bandwidth usage on interface {interface}. Press Ctrl+C to stop.\n")
        prev_sent, prev_recv = get_network_stats(interface)

        while True:
            time.sleep(interval)
            curr_sent, curr_recv = get_network_stats(interface)

            upload_rate = (curr_sent - prev_sent) / interval / 1024  # Convert to KB/s
            download_rate = (curr_recv - prev_recv) / interval / 1024  # Convert to KB/s

            print(f"Upload: {upload_rate:.2f} KB/s | Download: {download_rate:.2f} KB/s")

            prev_sent, prev_recv = curr_sent, curr_recv
    except KeyboardInterrupt:
        print("\nStopping bandwidth monitor.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the Network Bandwidth Monitor.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input network interface and monitoring interval
    interface = input("Enter the network interface to monitor (e.g., 'eth0', 'wlan0'): ").strip()
    interval = float(input("Enter the time interval for updates (seconds, e.g., 1): ").strip())

    try:
        monitor_bandwidth(interface, interval)
    except Exception as e:
        print(f"An error occurred: {e}")

