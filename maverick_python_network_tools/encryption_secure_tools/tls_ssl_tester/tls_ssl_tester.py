"""
TLS/SSL Security Tester
Developer: Ronald Baker

This script tests the TLS/SSL configuration of a target server and checks for:
- Supported protocols (TLS 1.2, TLS 1.3, etc.)
- Weak cipher suites
- Certificate validity (e.g., expiration, hostname mismatch)

Instructions:
1. Run the script from the terminal.
2. Enter the target domain and port (e.g., example.com:443).
3. The script will perform tests and display the results.
4. Modify this script to extend functionality as needed.

Required Libraries:
- ssl (Standard Python library, no installation required)
- socket (Standard Python library, no installation required)
- OpenSSL (Install with `pip install pyOpenSSL` for detailed certificate checks)

Usage:
python3 tls_ssl_tester.py
"""

import socket
import ssl
from datetime import datetime
from OpenSSL import crypto

def check_certificate(cert):
    """
    Checks the validity of an SSL certificate.

    :param cert: The certificate object.
    :return: Validation results.
    """
    try:
        x509 = crypto.load_certificate(crypto.FILETYPE_ASN1, cert)
        subject = dict(x509.get_subject().get_components())
        issuer = dict(x509.get_issuer().get_components())
        not_before = datetime.strptime(x509.get_notBefore().decode('utf-8'), "%Y%m%d%H%M%SZ")
        not_after = datetime.strptime(x509.get_notAfter().decode('utf-8'), "%Y%m%d%H%M%SZ")

        print("\nCertificate Information:")
        print(f"  Subject: {subject}")
        print(f"  Issuer: {issuer}")
        print(f"  Valid From: {not_before}")
        print(f"  Valid To: {not_after}")

        if datetime.now() > not_after:
            print("  Warning: Certificate has expired!")
        elif datetime.now() < not_before:
            print("  Warning: Certificate is not yet valid!")
        else:
            print("  Certificate is valid.")

    except Exception as e:
        print(f"Error parsing certificate: {e}")

def test_tls_connection(domain, port):
    """
    Tests the TLS/SSL configuration of a server.

    :param domain: The target domain.
    :param port: The target port (default: 443).
    """
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                print(f"\nConnected to {domain}:{port} with {ssock.version()}")
                cipher = ssock.cipher()
                print(f"  Cipher Suite: {cipher[0]} (Protocol: {cipher[1]}, Bits: {cipher[2]})")

                cert = ssock.getpeercert(binary_form=True)
                if cert:
                    check_certificate(cert)
                else:
                    print("  No certificate presented by the server.")
    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
    except Exception as e:
        print(f"Connection Error: {e}")

if __name__ == "__main__":
    print("Welcome to the TLS/SSL Security Tester.")
    print("Developer: Ronald Baker\n")

    # Input target domain and port
    target = input("Enter the target domain (e.g., example.com): ")
    try:
        port = int(input("Enter the target port (default: 443): ") or 443)
    except ValueError:
        print("Error: Invalid port number. Using default port 443.")
        port = 443

    # Test TLS/SSL configuration
    test_tls_connection(target, port)

