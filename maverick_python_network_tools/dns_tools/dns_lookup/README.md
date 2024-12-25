# Passive DNS Lookup Tool

**Developer**: Ronald Baker  

## Description

This script performs DNS lookups for a given domain and retrieves various DNS records:
- A (IP addresses)
- MX (Mail exchange servers)
- NS (Name servers)
- TXT (Text records)
- CNAME (Canonical name)

## Requirements

- Python 3  
- **dnspython** (Install with `pip install dnspython`)

## Usage

1. Run:
   ```bash
   python3 dns_lookup.py
   ```
2. Provide the **domain name** (e.g., `example.com`).
3. The script retrieves and displays DNS records (A, MX, NS, TXT, and CNAME).

**Example:**
```
Welcome to the Passive DNS Lookup Tool.
Developer: Ronald Baker

Enter the domain name to perform DNS lookups (e.g., 'example.com'): example.com

Performing DNS lookups for domain: example.com

A Records:
  - 93.184.216.34

MX Records:
  - No answer

NS Records:
  - sns.dns.icann.org.

TXT Records:
  - "v=spf1 +ip4:93.184.216.0/24 -all"

CNAME Records:
  - No answer
```

## Author

Ronald Baker  

## License & Disclaimer

This script is provided "as-is" for educational and informational purposes. Use at your own risk.
```