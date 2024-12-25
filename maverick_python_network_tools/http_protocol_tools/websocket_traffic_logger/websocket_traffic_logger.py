"""
WebSocket Traffic Logger
Developer: Ronald Baker

This script acts as a proxy server to intercept and log WebSocket traffic.
It displays:
- WebSocket handshake details
- Messages sent by the client
- Messages received from the server

Instructions:
1. Run the script with `python3`.
2. Configure your WebSocket client to connect through this proxy.
3. The script will log WebSocket traffic in real-time.

Required Libraries:
- websocket-server (Install with `pip install websocket-server`)

Usage:
python3 websocket_traffic_logger.py
"""

from websocket_server import WebsocketServer

def new_client(client, server):
    """
    Handles a new WebSocket connection.
    Logs the client's connection details.

    :param client: Client information (IP, port).
    :param server: The WebSocket server instance.
    """
    print(f"New client connected: {client['address']}")

def client_left(client, server):
    """
    Handles a client disconnection.
    Logs the client's disconnection details.

    :param client: Client information (IP, port).
    :param server: The WebSocket server instance.
    """
    print(f"Client disconnected: {client['address']}")

def message_received(client, server, message):
    """
    Handles messages sent by the client.
    Logs the content of the message.

    :param client: Client information (IP, port).
    :param server: The WebSocket server instance.
    :param message: The message sent by the client.
    """
    print(f"Message from {client['address']}: {message}")
    # Echo the message back to the client
    server.send_message(client, f"Server received: {message}")

if __name__ == "__main__":
    print("Welcome to the WebSocket Traffic Logger.")
    print("Developer: Ronald Baker\n")

    # Configure WebSocket server
    host = "0.0.0.0"
    port = 8081

    try:
        # Start the WebSocket server
        server = WebsocketServer(host=host, port=port)
        server.set_fn_new_client(new_client)
        server.set_fn_client_left(client_left)
        server.set_fn_message_received(message_received)

        print(f"WebSocket server running on ws://{host}:{port}")
        print("Waiting for connections...\n")
        server.run_forever()
    except Exception as e:
        print(f"An error occurred: {e}")

