"""
HTTP Proxy Server
Developer: Ronald Baker
Company: Mavericks Umbrella LLC

Disclaimer:
This software is provided by Mavericks Umbrella LLC "as-is" and without any warranties or conditions,
express or implied, including but not limited to the implied warranties of merchantability and fitness for a particular purpose.
In no event shall Mavericks Umbrella LLC or its contributors be liable for any direct, indirect, incidental,
special, exemplary, or consequential damages (including but not limited to procurement of substitute goods or services;
loss of use, data, or profits; or business interruption) however caused and on any theory of liability,
whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of
the use of this software, even if advised of the possibility of such damage.

This script creates an HTTP proxy server for logging HTTP requests and responses.

Instructions:
1. Run the script from the terminal.
2. Specify the port for the proxy server to listen on.
3. Configure your browser or application to use the proxy server.

Required Libraries:
- None (Standard Python libraries are used)

Usage:
python3 http_proxy_server.py
"""

import socket
import threading

def handle_client(client_socket):
    """
    Handles the client's request and forwards it to the target server.

    :param client_socket: The client's socket.
    """
    try:
        # Receive the request
        request = client_socket.recv(4096).decode()
        print(f"\n[Request]\n{request}")

        # Extract the target host and port
        first_line = request.split("\n")[0]
        url = first_line.split(" ")[1]

        # Default port to 80 if not specified
        http_pos = url.find("://")
        if http_pos != -1:
            url = url[(http_pos + 3):]
        port_pos = url.find(":")
        host = url[:port_pos] if port_pos != -1 else url.split("/")[0]
        port = int(url[(port_pos + 1):].split("/")[0]) if port_pos != -1 else 80

        # Create a socket to connect to the target server
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect((host, port))
        server_socket.send(request.encode())

        # Receive the response from the target server
        response = server_socket.recv(4096)
        print(f"\n[Response]\n{response.decode(errors='ignore')}")

        # Send the response back to the client
        client_socket.send(response)

        # Close the server connection
        server_socket.close()
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()

def start_proxy(port):
    """
    Starts the HTTP proxy server.

    :param port: The port for the proxy server to listen on.
    """
    try:
        # Create a listening socket
        proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        proxy_socket.bind(("0.0.0.0", port))
        proxy_socket.listen(5)
        print(f"HTTP Proxy Server running on port {port}")

        while True:
            client_socket, addr = proxy_socket.accept()
            print(f"Accepted connection from {addr}")
            # Handle each client in a separate thread
            threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()
    except KeyboardInterrupt:
        print("\nShutting down proxy server.")
    except Exception as e:
        print(f"Error starting proxy server: {e}")
    finally:
        proxy_socket.close()

if __name__ == "__main__":
    print("Welcome to the HTTP Proxy Server.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input proxy server port
    proxy_port = int(input("Enter the port for the proxy server (e.g., 8080): ").strip())

    start_proxy(proxy_port)

