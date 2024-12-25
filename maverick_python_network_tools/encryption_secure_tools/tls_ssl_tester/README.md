# TLS/SSL Security Tester

**Developer**: Ronald Baker  

## Description

This script tests the TLS/SSL configuration of a target server and checks for:

- Supported TLS protocols (e.g., TLS 1.2, TLS 1.3)  
- Cipher suite information  
- Certificate validity (expiration date, issuer, subject)  
- Hostname mismatch (if any)

It connects to the specified domain and port using a secure socket, retrieves the certificate, and displays its validity period along with other useful details.

## Requirements

- **Python 3**
- Standard libraries:  
  - **ssl**  
  - **socket**  
- **pyOpenSSL** (install with `pip install pyOpenSSL`) for detailed certificate checks

## Usage

1. **Run**:
   ```bash
   python3 tls_ssl_tester.py
   ```
2. **Enter**:
   - **Target domain** (e.g., `example.com`)
   - **Target port** (e.g., `443`, or press Enter for the default)
3. The script attempts a secure connection, reports the TLS version, cipher suite details, and checks certificate validity.

**Example session**:
```
Welcome to the TLS/SSL Security Tester.
Developer: Ronald Baker

Enter the target domain (e.g., example.com): example.com
Enter the target port (default: 443): 
Connected to example.com:443 with TLSv1.3
  Cipher Suite: TLS_AES_256_GCM_SHA384 (Protocol: TLSv1.3, Bits: 256)

Certificate Information:
  Subject: {b'CN': b'example.com'}
  Issuer: {b'C': b'US', b'O': b'Example CA', b'CN': b'Example CA Root'}
  Valid From: 2024-01-01 12:00:00
  Valid To: 2025-01-01 12:00:00
  Certificate is valid.
```

## Author

Ronald Baker  

## License & Disclaimer

This script is provided "as-is" for testing and educational purposes. Use at your own risk.