# Automated Recon Tool with Visualization

**Developer**: Ronald Baker  

## Description

This script automates **reconnaissance** on a target domain or IP address. It performs:

1. **Subdomain Enumeration**  
2. **Open Port Scanning**  
3. **Service Banner Grabbing**  
4. (Optional) **Visualization** of scanned ports and banners using a bar chart  

## Requirements

- **Python 3**  
- **socket** (standard library, included with Python)  
- [Optional] **matplotlib** (`pip install matplotlib`) for visualization

## Usage

1. **Run** the script:
   ```bash
   python3 automated_recon.py
   ```
2. **Enter** the target domain or IP address (e.g., `example.com` or `192.168.1.10`).
3. The script will:
   - Enumerate potential subdomains (based on a small example wordlist).
   - Perform a **port scan** on a range of ports (20–100 by default).
   - Attempt to grab service banners on open ports.
   - If there are open ports, **visualize** the results in a bar chart (requires `matplotlib`).

**Example session**:
```
Welcome to the Automated Recon Tool.
Developer: Ronald Baker

Enter the target domain or IP address: example.com

Starting Subdomain Enumeration...
[ACTIVE] www.example.com -> 93.184.216.34
[ACTIVE] api.example.com -> 93.184.216.34

Starting Port Scanning...
[OPEN] Port 80: HTTP/1.1 200 OK
[OPEN] Port 25: No banner

Visualizing Results...
```

A **bar chart** appears with port numbers on the x-axis and a simple indicator of whether a banner was grabbed.

## Notes

- The **wordlist** for subdomains is a short, hardcoded list. Extend or replace it with a more robust dictionary for better coverage.
- The **port range** (20–100) can be adjusted as needed.
- You can **modify** the script to store results, integrate with other frameworks, or implement additional recon modules.

## Author

Ronald Baker  

## License & Disclaimer

Use at your own risk. This script is provided "as-is" for educational or demonstration purposes.