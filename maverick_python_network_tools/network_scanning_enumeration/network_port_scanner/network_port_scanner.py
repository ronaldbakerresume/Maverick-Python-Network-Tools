"""
Network Port Scanner
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

This script scans a target IP or range of IPs for open ports and displays results.

Instructions:
1. Run the script from the terminal.
2. Specify the target IP, port range, and timeout for scanning.
3. The script will identify open ports and display results.

Required Libraries:
- socket (Standard Python library, no installation required)

Usage:
python3 network_port_scanner.py
"""

import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port, timeout):
    """
    Scans a single port on the target IP.

    :param ip: The target IP address.
    :param port: The port number to scan.
    :param timeout: The timeout value for the connection attempt.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            if s.connect_ex((ip, port)) == 0:
                print(f"Open port found: {ip}:{port}")
    except Exception as e:
        print(f"Error scanning port {port} on {ip}: {e}")

def scan_range(ip, start_port, end_port, timeout, threads):
    """
    Scans a range of ports on the target IP using multithreading.

    :param ip: The target IP address.
    :param start_port: The starting port number.
    :param end_port: The ending port number.
    :param timeout: The timeout value for the connection attempts.
    :param threads: Number of threads for scanning.
    """
    print(f"Scanning {ip} for open ports in range {start_port}-{end_port}...")
    with ThreadPoolExecutor(max_workers=threads) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port, timeout)

if __name__ == "__main__":
    print("Welcome to the Network Port Scanner.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input target IP, port range, and timeout
    target_ip = input("Enter the target IP address or hostname: ").strip()
    start_port = int(input("Enter the starting port number: ").strip())
    end_port = int(input("Enter the ending port number: ").strip())
    timeout = float(input("Enter the timeout value (seconds): ").strip())
    threads = int(input("Enter the number of threads (e.g., 10): ").strip())

    try:
        scan_range(target_ip, start_port, end_port, timeout, threads)
    except Exception as e:
        print(f"An error occurred: {e}")

