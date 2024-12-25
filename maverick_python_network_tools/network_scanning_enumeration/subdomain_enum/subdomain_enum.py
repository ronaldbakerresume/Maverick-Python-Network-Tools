"""
Subdomain Enumeration Tool
Developer: Ronald Baker

This script identifies subdomains for a given target domain by using a wordlist.
It resolves the subdomains through DNS lookups and displays active ones.

Instructions:
1. Provide a target domain to scan.
2. Provide a path to a wordlist file (or use the default example wordlist).
3. The script will resolve subdomains and display the active ones.
4. Modify this script to extend functionality as needed.

Required Libraries:
- socket (Standard Python library, no installation required)

Usage:
python3 subdomain_enum.py
"""

import socket

def subdomain_enum(domain, wordlist_file):
    """
    Enumerates subdomains for a given domain using a wordlist.

    :param domain: The target domain to scan (e.g., 'example.com').
    :param wordlist_file: Path to the wordlist file containing subdomain prefixes.
    """
    print(f"Starting subdomain enumeration for: {domain}\n")

    try:
        # Open the wordlist file
        with open(wordlist_file, 'r') as f:
            subdomains = f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: Wordlist file '{wordlist_file}' not found.")
        return

    print(f"Loaded {len(subdomains)} subdomains from wordlist.")
    print("Resolving subdomains...\n")

    active_subdomains = []

    # Check each subdomain
    for subdomain in subdomains:
        full_domain = f"{subdomain}.{domain}"
        try:
            # Perform DNS resolution
            resolved_ip = socket.gethostbyname(full_domain)
            print(f"[ACTIVE] {full_domain} -> {resolved_ip}")
            active_subdomains.append(full_domain)
        except socket.gaierror:
            # Ignore subdomains that don't resolve
            pass

    print("\nEnumeration complete.")
    if active_subdomains:
        print(f"Found {len(active_subdomains)} active subdomains:")
        for subdomain in active_subdomains:
            print(f"- {subdomain}")
    else:
        print("No active subdomains found.")

if __name__ == "__main__":
    print("Welcome to the Subdomain Enumeration Tool.")
    print("Developer: Ronald Baker\n")

    # Prompt the user to input the target domain
    target_domain = input("Enter the target domain (e.g., 'example.com'): ")

    # Prompt the user to input the wordlist file path or use a default one
    wordlist_path = input("Enter the path to the wordlist file (or press Enter to use the default): ")
    if not wordlist_path:
        # Example default wordlist (can be extended or replaced with a larger list)
        default_wordlist = "subdomains.txt"
        print(f"No wordlist specified. Using default: {default_wordlist}")
        wordlist_path = default_wordlist

        # Create a simple default wordlist file if it doesn't exist
        with open(default_wordlist, 'w') as f:
            f.write("www\napi\nmail\nftp\nadmin\nportal\n")

    # Run the subdomain enumeration
    try:
        subdomain_enum(target_domain, wordlist_path)
    except Exception as e:
        print(f"An error occurred: {e}")

