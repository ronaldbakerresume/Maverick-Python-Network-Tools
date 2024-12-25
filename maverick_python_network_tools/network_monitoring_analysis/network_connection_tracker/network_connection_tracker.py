"""
Network Connection Tracker
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

This script tracks active network connections in real-time.

Instructions:
1. Run the script from the terminal.
2. Specify the refresh interval.
3. The script will display a real-time list of active network connections.

Required Libraries:
- psutil (Install with `pip install psutil`)

Usage:
python3 network_connection_tracker.py
"""

import psutil
import time

def track_connections(interval):
    """
    Tracks and displays active network connections.

    :param interval: The refresh interval in seconds.
    """
    try:
        print("Tracking active network connections. Press Ctrl+C to stop.\n")
        while True:
            connections = psutil.net_connections(kind='inet')
            print(f"{'Proto':<6}{'Local Address':<25}{'Remote Address':<25}{'Status':<15}")
            print("=" * 70)
            for conn in connections:
                proto = "TCP" if conn.type == psutil.SOCK_STREAM else "UDP"
                local_addr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "-"
                remote_addr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "-"
                status = conn.status if conn.status else "N/A"
                print(f"{proto:<6}{local_addr:<25}{remote_addr:<25}{status:<15}")
            print("\nRefreshing in {} seconds...\n".format(interval))
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopping network connection tracker.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the Network Connection Tracker.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input refresh interval
    interval = float(input("Enter the refresh interval (seconds, e.g., 2): ").strip())

    try:
        track_connections(interval)
    except Exception as e:
        print(f"An error occurred: {e}")

