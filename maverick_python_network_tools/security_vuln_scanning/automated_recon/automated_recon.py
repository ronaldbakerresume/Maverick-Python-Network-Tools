"""
Automated Recon Tool with Visualization
Developer: Ronald Baker

This script performs automated reconnaissance on a target domain or IP address.
It includes:
- Subdomain enumeration
- Open port scanning
- Service banner grabbing
- Visualization of results

Instructions:
1. Run the script from the terminal.
2. Enter the target domain or IP address.
3. The script will perform reconnaissance and display the results.
4. Modify this script to extend functionality as needed.

Required Libraries:
- socket (Standard Python library, no installation required)

Optional Libraries:
- matplotlib (Install with `pip install matplotlib` for visualization)

Usage:
python3 automated_recon.py
"""

import socket
import matplotlib.pyplot as plt

def subdomain_enumeration(domain, wordlist):
    """
    Performs subdomain enumeration for the given domain.

    :param domain: The target domain (e.g., example.com).
    :param wordlist: A list of subdomains to check.
    :return: A list of active subdomains.
    """
    print("\nStarting Subdomain Enumeration...")
    active_subdomains = []

    for sub in wordlist:
        subdomain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(subdomain)
            print(f"[ACTIVE] {subdomain} -> {ip}")
            active_subdomains.append(subdomain)
        except socket.gaierror:
            pass

    return active_subdomains

def port_scanner(target_ip, ports):
    """
    Scans open ports on the target IP.

    :param target_ip: The target IP address.
    :param ports: A list of ports to scan.
    :return: A dictionary of open ports and their banners.
    """
    print("\nStarting Port Scanning...")
    open_ports = {}

    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((target_ip, port))
                if result == 0:
                    s.sendall(b"\r\n")
                    banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
                    open_ports[port] = banner if banner else "No banner"
                    print(f"[OPEN] Port {port}: {open_ports[port]}")
        except socket.timeout:
            pass
        except Exception as e:
            print(f"Error on port {port}: {e}")

    return open_ports

def visualize_results(results):
    """
    Visualizes the reconnaissance results using a bar chart.

    :param results: A dictionary of ports and banners.
    """
    print("\nVisualizing Results...")
    ports = list(results.keys())
    banners = list(results.values())

    plt.bar(ports, [1] * len(ports), tick_label=banners)
    plt.title("Open Ports and Banners")
    plt.xlabel("Ports")
    plt.ylabel("Banner Presence")
    plt.show()

if __name__ == "__main__":
    print("Welcome to the Automated Recon Tool.")
    print("Developer: Ronald Baker\n")

    # Input target
    target = input("Enter the target domain or IP address: ")

    # Example wordlist for subdomains
    wordlist = ["www", "api", "mail", "ftp", "admin"]

    # Subdomain enumeration
    active_subdomains = subdomain_enumeration(target, wordlist)

    # Port scanning
    target_ip = socket.gethostbyname(target)
    ports_to_scan = range(20, 101)  # Example port range
    open_ports = port_scanner(target_ip, ports_to_scan)

    # Visualize results
    if open_ports:
        visualize_results(open_ports)
    else:
        print("\nNo open ports detected.")

