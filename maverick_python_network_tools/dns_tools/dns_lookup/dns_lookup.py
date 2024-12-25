"""
Passive DNS Lookup Tool
Developer: Ronald Baker

This script performs DNS lookups for a given domain and retrieves its DNS records:
- A (IP addresses)
- MX (Mail exchange servers)
- NS (Name servers)
- TXT (Text records)
- CNAME (Canonical name)

Instructions:
1. Run the script from the terminal.
2. Enter the domain name to perform DNS lookups.
3. The script will display DNS records for the provided domain.
4. Modify this script to extend functionality as needed.

Required Library:
- dnspython (Install with `pip install dnspython`)

Usage:
python3 dns_lookup.py
"""

import dns.resolver

def dns_lookup(domain):
    """
    Performs DNS lookups for the specified domain and retrieves various DNS records.

    :param domain: The domain name to perform DNS lookups on (e.g., 'example.com').
    """
    print(f"Performing DNS lookups for domain: {domain}\n")

    record_types = ['A', 'MX', 'NS', 'TXT', 'CNAME']
    results = {}

    for record_type in record_types:
        try:
            # Query DNS records of the specified type
            answers = dns.resolver.resolve(domain, record_type)
            results[record_type] = [str(rdata) for rdata in answers]
        except dns.resolver.NoAnswer:
            results[record_type] = ["No answer"]
        except dns.resolver.NXDOMAIN:
            print(f"Error: The domain '{domain}' does not exist.")
            return
        except Exception as e:
            results[record_type] = [f"Error: {str(e)}"]

    # Display results
    for record_type, records in results.items():
        print(f"{record_type} Records:")
        for record in records:
            print(f"  - {record}")
        print()

if __name__ == "__main__":
    print("Welcome to the Passive DNS Lookup Tool.")
    print("Developer: Ronald Baker\n")

    # Prompt the user to input the target domain
    target_domain = input("Enter the domain name to perform DNS lookups (e.g., 'example.com'): ")

    # Run the DNS lookup
    try:
        dns_lookup(target_domain)
    except Exception as e:
        print(f"An error occurred: {e}")

