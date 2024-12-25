"""
Service Banner Grabbing Tool
Developer: Ronald Baker

This script connects to a specified IP address and port to retrieve the service banner.
It is useful for identifying the services running on open ports.

Instructions:
1. Run the script from the terminal.
2. Enter the target IP address and port when prompted.
3. The script will attempt to retrieve the banner of the service running on the specified port.
4. Modify this script to extend functionality as needed.

Required Libraries:
- socket (Standard Python library, no installation required)

Usage:
python3 banner_grabber.py
"""

import socket

def banner_grabber(target_ip, target_port):
    """
    Connects to a target IP and port to retrieve the service banner.

    :param target_ip: The IP address of the target (e.g., '192.168.1.1').
    :param target_port: The port number to connect to (e.g., 80).
    """
    print(f"Connecting to {target_ip}:{target_port}...\n")

    try:
        # Create a socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)  # Set a timeout for the connection
            # Connect to the target IP and port
            s.connect((target_ip, target_port))
            # Send a blank request (if required by the protocol)
            s.sendall(b"\r\n")
            # Receive and decode the banner
            banner = s.recv(1024).decode('utf-8', errors='ignore')
            print(f"Banner retrieved from {target_ip}:{target_port}:\n")
            print(banner)
    except socket.timeout:
        print("Connection timed out. The port may not be open or is unresponsive.")
    except ConnectionRefusedError:
        print("Connection refused. The port may be closed or blocked by a firewall.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the Service Banner Grabbing Tool.")
    print("Developer: Ronald Baker\n")

    # Prompt the user to input the target IP address
    target = input("Enter the target IP address (e.g., '192.168.1.1'): ")

    # Prompt the user to input the target port
    try:
        port = int(input("Enter the target port (e.g., 80): "))
    except ValueError:
        print("Error: Invalid port number. Please enter a valid integer.")
        exit(1)

    # Run the banner grabber
    try:
        banner_grabber(target, port)
    except Exception as e:
        print(f"An error occurred: {e}")

