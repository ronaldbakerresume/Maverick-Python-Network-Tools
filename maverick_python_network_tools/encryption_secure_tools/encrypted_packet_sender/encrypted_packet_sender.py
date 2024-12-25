"""
Encrypted Packet Sender
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

This script encrypts and sends data packets over the network using AES encryption.

Instructions:
1. Run the script from the terminal.
2. Specify the target IP, port, and message to send.
3. The script will encrypt the message and send it to the destination.

Required Libraries:
- cryptography (Install with `pip install cryptography`)
- socket (Standard Python library, no installation required)

Usage:
python3 encrypted_packet_sender.py
"""

import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def encrypt_message(message, key):
    """
    Encrypts a message using AES encryption.

    :param message: The plaintext message to encrypt.
    :param key: The encryption key (16 bytes).
    :return: The encrypted message.
    """
    iv = os.urandom(16)  # Generate a random IV
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Apply PKCS7 padding
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_message = padder.update(message.encode()) + padder.finalize()

    # Encrypt the padded message
    encrypted_message = encryptor.update(padded_message) + encryptor.finalize()
    return iv + encrypted_message  # Include IV for decryption

def send_packet(target_ip, target_port, encrypted_message):
    """
    Sends an encrypted packet to the specified target.

    :param target_ip: The destination IP address.
    :param target_port: The destination port.
    :param encrypted_message: The encrypted payload to send.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(encrypted_message, (target_ip, target_port))
        print(f"Encrypted message sent to {target_ip}:{target_port}")
    except Exception as e:
        print(f"Error sending packet: {e}")

if __name__ == "__main__":
    print("Welcome to the Encrypted Packet Sender.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input target details
    target_ip = input("Enter the target IP address: ").strip()
    target_port = int(input("Enter the target port: ").strip())
    message = input("Enter the message to send: ").strip()

    # Generate a 16-byte AES key
    key = os.urandom(16)
    print(f"Generated AES key: {key.hex()} (Share this key with the receiver for decryption)")

    # Encrypt and send the message
    try:
        encrypted_message = encrypt_message(message, key)
        send_packet(target_ip, target_port, encrypted_message)
    except Exception as e:
        print(f"An error occurred: {e}")

