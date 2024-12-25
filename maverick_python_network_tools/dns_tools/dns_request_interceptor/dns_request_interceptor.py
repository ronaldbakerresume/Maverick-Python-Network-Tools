"""
DNS Request Interceptor
Developer: Ronald Baker

This script intercepts DNS requests and logs queried domains. It can also redirect
specific domains to a user-specified IP address for testing or analysis.

Instructions:
1. Run the script with `sudo` (superuser privileges are required for DNS interception).
2. Configure your device or router to use this script's IP as the DNS server.
3. The script will log all DNS queries in real-time.
4. Modify this script to extend functionality as needed.

Required Libraries:
- dnslib (Install with `pip install dnslib`)

Usage:
sudo python3 dns_request_interceptor.py
"""

from dnslib import DNSRecord, RR, QTYPE
from socketserver import UDPServer, BaseRequestHandler

# Define the IP to redirect specific domains (optional)
REDIRECT_IP = "192.168.1.100"  # Replace with desired redirection IP

class DNSHandler(BaseRequestHandler):
    """
    Handles incoming DNS requests and logs queried domains.
    Redirects specific domains to a predefined IP address if needed.
    """

    def handle(self):
        # Receive the DNS request
        data, socket = self.request
        request = DNSRecord.parse(data)

        # Extract the queried domain
        qname = str(request.q.qname)
        qtype = QTYPE[request.q.qtype]
        print(f"Received DNS Query: {qname} ({qtype})")

        # Prepare the DNS response
        reply = request.reply()
        if "example.com" in qname:  # Replace with domain to redirect
            print(f"Redirecting {qname} to {REDIRECT_IP}")
            reply.add_answer(RR(qname, QTYPE.A, rdata=REDIRECT_IP))
        else:
            # Respond with no answer
            reply.header.rcode = 3  # NXDOMAIN (Non-Existent Domain)

        # Send the response back to the client
        socket.sendto(reply.pack(), self.client_address)

if __name__ == "__main__":
    print("Welcome to the DNS Request Interceptor.")
    print("Developer: Ronald Baker\n")

    # Define the server address and port
    server_address = ("0.0.0.0", 53)  # Bind to all interfaces on port 53 (DNS)

    try:
        # Start the DNS server
        with UDPServer(server_address, DNSHandler) as server:
            print(f"DNS server running on {server_address[0]}:{server_address[1]}")
            print("Intercepting DNS queries. Press Ctrl+C to stop.\n")
            server.serve_forever()
    except PermissionError:
        print("Error: Permission denied. Please run this script with sudo.")
    except Exception as e:
        print(f"An error occurred: {e}")

