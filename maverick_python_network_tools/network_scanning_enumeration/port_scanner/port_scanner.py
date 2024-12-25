"""
Open Port Scanner
Developer: Ronald Baker

This script scans a target IP address for open TCP or UDP ports within a specified range.

Instructions:
1. Run the script from the terminal.
2. Enter the target IP address to scan.
3. Enter the range of ports to scan (e.g., 1-1000).
4. The script will display all open ports and their statuses.
5. Modify this script to extend functionality as needed.

Required Library:
- socket (Standard Python library, no installation required)

Usage:
python3 port_scanner.py
"""

import socket

def port_scanner(target_ip, start_port, end_port):
    """
    Scans the specified range of ports on a target IP address for open ports.

    :param target_ip: The IP address to scan.
    :param start_port: The starting port of the range.
    :param end_port: The ending port of the range.
    """
    print(f"Scanning {target_ip} for open ports in range {start_port}-{end_port}...")
    print("This may take a few seconds.\n")

    # Iterate through the specified port range
    for port in range(start_port, end_port + 1):
        try:
            # Create a socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)  # Set timeout for connection attempts
                # Attempt to connect to the port
                result = s.connect_ex((target_ip, port))
                if result == 0:  # If connection is successful
                    print(f"Port {port}: OPEN")
        except KeyboardInterrupt:
            print("\nScan aborted by user.")
            break
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

    print("\nPort scan complete. Consider extending this script for UDP scanning or saving results.")

if __name__ == "__main__":
    print("Welcome to the Open Port Scanner.")
    print("Developer: Ronald Baker\n")

    # Prompt the user to input the target IP address
    target = input("Enter the target IP address: ")

    # Prompt the user to input the port range
    port_range = input("Enter the port range to scan (e.g., 1-1000): ")
    try:
        start, end = map(int, port_range.split("-"))
    except ValueError:
        print("Error: Invalid port range format. Use the format 'start-end' (e.g., 1-1000).")
        exit(1)

    # Run the port scanner
    try:
        port_scanner(target, start, end)
    except Exception as e:
        print(f"An error occurred: {e}")

