# Encrypted Packet Sender

**Developer**: Ronald Baker  
**Company**: Mavericks Umbrella LLC  

## Disclaimer

This software is provided by Mavericks Umbrella LLC "as-is" and without any warranties or conditions,  
express or implied, including but not limited to the implied warranties of merchantability and fitness for a particular purpose.  
In no event shall Mavericks Umbrella LLC or its contributors be liable for any direct, indirect, incidental,  
special, exemplary, or consequential damages (including but not limited to procurement of substitute goods or services;  
loss of use, data, or profits; or business interruption) however caused and on any theory of liability,  
whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of  
the use of this software, even if advised of the possibility of such damage.

## Description

This script encrypts a plaintext message using AES (CFB mode) and sends the encrypted bytes as a UDP packet to a specified host and port. The script automatically generates a 16-byte AES key (shared secret) and prepends the IV to the ciphertext for the receiver to decrypt.

## Requirements

- **Python 3**  
- **cryptography** (Install with `pip install cryptography`)
- **socket** (part of the standard library)

## Usage

1. **Run**:
   ```bash
   python3 encrypted_packet_sender.py
   ```
2. **Provide**:
   - Target IP address (e.g., `192.168.1.10`)
   - Target port (e.g., `9999`)
   - Message to send

The script generates a **16-byte AES key** and uses it to encrypt your message in AES-CFB mode. The **IV** is automatically included at the start of the encrypted payload.

Example session:
```
Welcome to the Encrypted Packet Sender.
Developer: Ronald Baker
Company: Mavericks Umbrella LLC

Enter the target IP address: 192.168.1.10
Enter the target port: 9999
Enter the message to send: Hello, world!
Generated AES key: 931ac4ad7d2a4f73bf633eeb3db5eece (Share this key with the receiver for decryption)
Encrypted message sent to 192.168.1.10:9999
```

## Author

Ronald Baker  
Mavericks Umbrella LLC

## License & Warranty

See the **Disclaimer** above. This script is provided without warranties of any kind. Use at your own risk.
```