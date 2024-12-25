"""
Secure File Transfer Tool
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

This script encrypts and securely transfers files between machines.

Instructions:
1. Run the script in "send" mode on the sending machine.
2. Run the script in "receive" mode on the receiving machine.
3. Files will be encrypted and transferred securely.

Required Libraries:
- cryptography (Install with `pip install cryptography`)
- socket (Standard Python library, no installation required)

Usage:
python3 secure_file_transfer_tool.py
"""

import socket
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def encrypt_file(file_path, key):
    """
    Encrypts a file using AES encryption.

    :param file_path: The path of the file to encrypt.
    :param key: The encryption key (16 bytes).
    :return: Encrypted data with IV prepended.
    """
    with open(file_path, "rb") as f:
        data = f.read()

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()
    return iv + encrypted_data

def decrypt_file(encrypted_data, key):
    """
    Decrypts AES-encrypted data.

    :param encrypted_data: The encrypted data with IV prepended.
    :param key: The encryption key (16 bytes).
    :return: Decrypted data.
    """
    iv = encrypted_data[:16]
    encrypted_payload = encrypted_data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(encrypted_payload) + decryptor.finalize()

def send_file(file_path, target_ip, target_port, key):
    """
    Sends an encrypted file to a target machine.

    :param file_path: The path of the file to send.
    :param target_ip: The target machine's IP address.
    :param target_port: The target machine's port.
    :param key: The encryption key (16 bytes).
    """
    encrypted_data = encrypt_file(file_path, key)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((target_ip, target_port))
        s.sendall(encrypted_data)
        print(f"Encrypted file sent to {target_ip}:{target_port}")

def receive_file(save_path, listen_port, key):
    """
    Receives an encrypted file and saves it after decryption.

    :param save_path: The path to save the decrypted file.
    :param listen_port: The port to listen for incoming files.
    :param key: The encryption key (16 bytes).
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", listen_port))
        s.listen(1)
        print(f"Listening for incoming file on port {listen_port}...")
        conn, addr = s.accept()
        with conn:
            print(f"Connection from {addr}")
            encrypted_data = conn.recv(1024 * 1024)  # Receive up to 1MB
            decrypted_data = decrypt_file(encrypted_data, key)
            with open(save_path, "wb") as f:
                f.write(decrypted_data)
            print(f"File saved to {save_path}")

if __name__ == "__main__":
    print("Welcome to the Secure File Transfer Tool.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    mode = input("Enter mode ('send' or 'receive'): ").strip().lower()
    key = os.urandom(16)  # Generate a 16-byte AES key
    print(f"Generated AES key: {key.hex()} (Share this key with the receiver for decryption)")

    if mode == "send":
        file_path = input("Enter the path of the file to send: ").strip()
        target_ip = input("Enter the target IP address: ").strip()
        target_port = int(input("Enter the target port: ").strip())
        send_file(file_path, target_ip, target_port, key)
    elif mode == "receive":
        save_path = input("Enter the path to save the received file: ").strip()
        listen_port = int(input("Enter the listening port: ").strip())
        receive_file(save_path, listen_port, key)
    else:
        print("Invalid mode. Exiting.")

