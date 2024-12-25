"""
IP Geolocation and Tracker
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

This script uses an API to fetch geolocation data for IP addresses and display detailed results.

Instructions:
1. Run the script from the terminal.
2. Enter the IP addresses to lookup, separated by commas.
3. The script will query a geolocation API and display results.

Required Libraries:
- requests (Install with `pip install requests`)

Usage:
python3 ip_geolocation_tracker.py
"""

import requests

def get_geolocation(ip_addresses, api_url, api_key):
    """
    Fetches geolocation data for a list of IP addresses.

    :param ip_addresses: A list of IP addresses to lookup.
    :param api_url: The geolocation API endpoint.
    :param api_key: The API key for authentication.
    """
    for ip in ip_addresses:
        try:
            print(f"\nFetching geolocation for IP: {ip}")
            response = requests.get(f"{api_url}/{ip}", params={"apikey": api_key}, timeout=10)
            if response.status_code == 200:
                data = response.json()
                print(f"IP Address: {ip}")
                print(f"  Country: {data.get('country_name', 'N/A')}")
                print(f"  City: {data.get('city', 'N/A')}")
                print(f"  Latitude: {data.get('latitude', 'N/A')}")
                print(f"  Longitude: {data.get('longitude', 'N/A')}")
            else:
                print(f"Failed to fetch geolocation for {ip}. Status Code: {response.status_code}")
        except Exception as e:
            print(f"Error fetching geolocation for {ip}: {e}")

if __name__ == "__main__":
    print("Welcome to the IP Geolocation and Tracker.")
    print("Developer: Ronald Baker")
    print("Company: Mavericks Umbrella LLC\n")

    # Input IP addresses
    ip_input = input("Enter IP addresses to lookup (comma-separated): ").strip()
    ip_addresses = [ip.strip() for ip in ip_input.split(",")]

    # API settings
    api_url = "https://api.ipgeolocation.io/ipgeo"  # Replace with your preferred geolocation API endpoint
    api_key = input("Enter your API key: ").strip()

    # Perform geolocation lookup
    get_geolocation(ip_addresses, api_url, api_key)

