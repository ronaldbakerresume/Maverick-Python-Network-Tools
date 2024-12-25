"""
HTTP/HTTPS Request Logger
Developer: Ronald Baker

This script sets up a proxy server to capture and log HTTP/HTTPS requests.
It displays details such as:
- Request URL
- HTTP Method
- Headers
- Body Content (if available)

Instructions:
1. Run the script with `python3`.
2. Configure your device to use the proxy server (IP: localhost, Port: 8080).
3. The script will log HTTP/HTTPS requests passing through the proxy.

Required Libraries:
- mitmproxy (Install with `pip install mitmproxy`)

Usage:
python3 http_request_logger.py
"""

from mitmproxy import http

def request(flow: http.HTTPFlow):
    """
    Callback to log HTTP/HTTPS requests passing through the proxy.

    :param flow: The HTTPFlow object containing request and response details.
    """
    try:
        # Log request details
        print(f"Request URL: {flow.request.pretty_url}")
        print(f"HTTP Method: {flow.request.method}")
        print("Headers:")
        for header, value in flow.request.headers.items():
            print(f"  {header}: {value}")
        
        # Log request body if available
        if flow.request.content:
            print(f"Body: {flow.request.content.decode('utf-8', errors='ignore')}")
        print("-" * 50)
    except Exception as e:
        print(f"Error processing request: {e}")

def start():
    """
    Entry point for the mitmproxy addon.
    """
    print("HTTP/HTTPS Request Logger initialized. Listening on port 8080.")
    return [request]

