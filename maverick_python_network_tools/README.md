# Maverick Python Network Tools

**Maverick Python Network Tools** is a comprehensive collection of Python scripts and modules designed for a wide range of networking, security, and analysis tasks. Each directory below represents a category of tools, and each subfolder corresponds to a specific script or set of scripts.

---

## Table of Contents
- [arp_mac_tools](#arp_mac_tools)
- [attacks_exploits](#attacks_exploits)
- [dns_tools](#dns_tools)
- [encryption_secure_tools](#encryption_secure_tools)
- [http_protocol_tools](#http_protocol_tools)
- [misc](#misc)
- [network_monitoring_analysis](#network_monitoring_analysis)
- [network_scanning_enumeration](#network_scanning_enumeration)
- [security_vuln_scanning](#security_vuln_scanning)
- [traffic_replay_shaping](#traffic_replay_shaping)

---

## arp_mac_tools

[**arp_mac_tools/**](./arp_mac_tools/) contains utilities for working with ARP (Address Resolution Protocol) and MAC address manipulation.

- [arp_spoofing_detection/](./arp_mac_tools/arp_spoofing_detection/):  
  Script(s) to analyze ARP traffic for detecting malicious ARP spoofing attempts on a network.
- [arp_spoofing_tool/](./arp_mac_tools/arp_spoofing_tool/):  
  Tools to **initiate** ARP spoofing, typically used for testing or red-team exercises.
- [mac_address_spoofer/](./arp_mac_tools/mac_address_spoofer/):  
  Utility to change (spoof) your network interface’s MAC address to evade detection or for privacy tests.

---

## attacks_exploits

[**attacks_exploits/**](./attacks_exploits/) houses scripts that simulate or help demonstrate offensive security techniques.

- [firewall_evasion_tool/](./attacks_exploits/firewall_evasion_tool/):  
  Methods to bypass certain firewall rules or network filtering.
- [port_forwarding_tool/](./attacks_exploits/port_forwarding_tool/):  
  Helps with redirecting traffic from one port to another, which can aid in pivoting or bypassing security controls.
- [slowloris_attack_simulator/](./attacks_exploits/slowloris_attack_simulator/):  
  Simulates the Slowloris DoS attack, used for testing server resilience to Layer 7 slow-HTTP attacks.
- [ssl_strip_tool/](./attacks_exploits/ssl_strip_tool/):  
  Attempts to downgrade HTTPS to HTTP in order to capture or modify traffic that would otherwise be encrypted.
- [tcp_syn_flood_detection/](./attacks_exploits/tcp_syn_flood_detection/):  
  Detects suspicious levels of TCP SYN packets, indicating possible SYN flood attacks.
- [wifi_deauth_attack_tool/](./attacks_exploits/wifi_deauth_attack_tool/):  
  Sends Wi-Fi deauthentication frames to forcibly disconnect devices, often used in penetration testing of wireless networks.

---

## dns_tools

[**dns_tools/**](./dns_tools/) deals with Domain Name System lookups, logging, spoofing, and interception.

- [dns_lookup/](./dns_tools/dns_lookup/):  
  Basic DNS resolution tool to query different DNS records.
- [dns_query_logger/](./dns_tools/dns_query_logger/):  
  Logs DNS queries passing through the network for analysis or auditing.
- [dns_request_interceptor/](./dns_tools/dns_request_interceptor/):  
  Intercepts and potentially modifies DNS requests in transit.
- [dns_spoofing_detection/](./dns_tools/dns_spoofing_detection/):  
  Monitors DNS responses to detect spoofing or tampering attempts.
- [dns_spoofing_tool/](./dns_tools/dns_spoofing_tool/):  
  Scripts to perform DNS spoofing attacks for penetration testing.

---

## encryption_secure_tools

[**encryption_secure_tools/**](./encryption_secure_tools/) provides scripts for secure communication and encryption.

- [encrypted_packet_sender/](./encryption_secure_tools/encrypted_packet_sender/):  
  Sends network packets with encryption, ensuring data confidentiality in transit.
- [secure_file_transfer_tool/](./encryption_secure_tools/secure_file_transfer_tool/):  
  Transfers files securely over encrypted channels, minimizing the risk of interception.
- [secure_shell_traffic_logger/](./encryption_secure_tools/secure_shell_traffic_logger/):  
  Monitors and logs SSH (Secure Shell) traffic for auditing or intrusion detection.
- [tls_ssl_tester/](./encryption_secure_tools/tls_ssl_tester/):  
  Checks TLS/SSL configurations for potential vulnerabilities or misconfigurations.

---

## http_protocol_tools

[**http_protocol_tools/**](./http_protocol_tools/) includes utilities around HTTP/HTTPS traffic, including proxies and traffic analysis.

- [banner_grabber/](./http_protocol_tools/banner_grabber/):  
  Retrieves banners or server information from open ports, often used in reconnaissance.
- [http_proxy_server/](./http_protocol_tools/http_proxy_server/):  
  Sets up a basic HTTP proxy that can be used for traffic redirection or filtering.
- [http_request_logger/](./http_protocol_tools/http_request_logger/):  
  Logs HTTP requests for debugging, analysis, or auditing.
- [http_traffic_monitor/](./http_protocol_tools/http_traffic_monitor/):  
  Monitors HTTP traffic in real-time, useful for performance monitoring or threat detection.
- [protocol_analyzer/](./http_protocol_tools/protocol_analyzer/):  
  Analyzes the structure and flow of network protocols, not limited to HTTP.
- [websocket_traffic_logger/](./http_protocol_tools/websocket_traffic_logger/):  
  Captures and logs messages exchanged over a WebSocket connection.

---

## misc

[**misc/**](./misc/) holds assorted scripts or tools that don’t fit neatly elsewhere.

- [wifi_signal_mapper/](./misc/wifi_signal_mapper/):  
  Maps Wi-Fi signals to geographic or indoor locations to visualize coverage.
- [wireless_signal_strength_monitor/](./misc/wireless_signal_strength_monitor/):  
  Monitors the signal strength of wireless networks over time, useful for troubleshooting or site surveys.

---

## network_monitoring_analysis

[**network_monitoring_analysis/**](./network_monitoring_analysis/) focuses on tools for gathering stats, logging activity, measuring performance, or detecting intrusions.

- [advanced_port_knocking_framework/](./network_monitoring_analysis/advanced_port_knocking_framework/):  
  Implements an advanced approach to port knocking, allowing secure but stealthy server access.
- [bandwidth_usage_monitor/](./network_monitoring_analysis/bandwidth_usage_monitor/):  
  Tracks real-time bandwidth consumption.
- [bandwidth_usage_tracker/](./network_monitoring_analysis/bandwidth_usage_tracker/):  
  Records and charts bandwidth usage over longer periods.
- [dynamic_traffic_throttling_tool/](./network_monitoring_analysis/dynamic_traffic_throttling_tool/):  
  Dynamically limits or shapes traffic based on usage thresholds or policies.
- [network_activity_logger/](./network_monitoring_analysis/network_activity_logger/):  
  Logs network connections or data flows for auditing.
- [network_bandwidth_monitor/](./network_monitoring_analysis/network_bandwidth_monitor/):  
  Observes network bandwidth in different time intervals.
- [network_bandwidth_throttler/](./network_monitoring_analysis/network_bandwidth_throttler/):  
  Enforces bandwidth caps or rate limiting.
- [network_connection_tracker/](./network_monitoring_analysis/network_connection_tracker/):  
  Tracks active connections, IP endpoints, and sessions on a system or network.
- [network_intrusion_detection/](./network_monitoring_analysis/network_intrusion_detection/):  
  Simple intrusion detection logic, analyzing packet patterns for suspicious behavior.
- [network_intrusion_detection_system/](./network_monitoring_analysis/network_intrusion_detection_system/):  
  More robust IDS implementation with signature or anomaly-based detection.
- [network_latency_tool/](./network_monitoring_analysis/network_latency_tool/):  
  Measures round-trip times or latency between hosts, helps diagnose slow connections.
- [network_packet_aggregator/](./network_monitoring_analysis/network_packet_aggregator/):  
  Consolidates packets from multiple sources for aggregated analysis.
- [network_packet_analyzer/](./network_monitoring_analysis/network_packet_analyzer/):  
  Dissects packet headers and payloads to identify protocols or suspicious data.
- [network_packet_delay_simulator/](./network_monitoring_analysis/network_packet_delay_simulator/):  
  Injects artificial delays into network streams for testing high-latency scenarios.
- [network_packet_loss_monitor/](./network_monitoring_analysis/network_packet_loss_monitor/):  
  Observes traffic for dropped packets, often crucial for VoIP or streaming.
- [network_ping_sweep/](./network_monitoring_analysis/network_ping_sweep/):  
  Pings multiple IP addresses to discover live hosts.
- [network_ping_sweeper/](./network_monitoring_analysis/network_ping_sweeper/):  
  Variation on ping sweep with extra features (e.g., parallel checks).
- [network_traffic_encryption_analyzer/](./network_monitoring_analysis/network_traffic_encryption_analyzer/):  
  Evaluates whether traffic is properly encrypted or attempts to detect weaker ciphers.
- [network_traffic_logger/](./network_monitoring_analysis/network_traffic_logger/):  
  Passively records packet information for offline review.
- [network_traffic_statistics/](./network_monitoring_analysis/network_traffic_statistics/):  
  Gathers metrics (bandwidth usage, connection counts, etc.) for analysis.
- [network_traffic_visualizer/](./network_monitoring_analysis/network_traffic_visualizer/):  
  Visualizes network flows or topologies using charts or graphs.
- [packet_sniffer/](./network_monitoring_analysis/packet_sniffer/):  
  Captures raw packets from the network interface for real-time analysis.
- [packet_sniffer_protocol_analysis/](./network_monitoring_analysis/packet_sniffer_protocol_analysis/):  
  Extends packet sniffing with detailed protocol breakdowns.
- [remote_command_execution_monitor/](./network_monitoring_analysis/remote_command_execution_monitor/):  
  Observes or alerts on possible remote command executions across the network.

---

## network_scanning_enumeration

[**network_scanning_enumeration/**](./network_scanning_enumeration/) contains tools for discovering hosts, ports, subdomains, and other network assets.

- [ip_geolocation_tracker/](./network_scanning_enumeration/ip_geolocation_tracker/):  
  Attempts to map IP addresses to geographic locations.
- [ip_mac_scanner/](./network_scanning_enumeration/ip_mac_scanner/):  
  Scans a network for IP and MAC addresses of connected devices.
- [local_network_scanner/](./network_scanning_enumeration/local_network_scanner/):  
  Identifies active hosts and services on the local LAN.
- [network_device_enumerator/](./network_scanning_enumeration/network_device_enumerator/):  
  Enumerates network devices and collects basic info (OS, open ports).
- [network_port_scanner/](./network_scanning_enumeration/network_port_scanner/):  
  Searches for open ports across a range of IPs, useful for vulnerability assessment.
- [port_scanner/](./network_scanning_enumeration/port_scanner/):  
  A simpler or alternative port scanner variant focusing on single hosts or custom tasks.
- [subdomain_enum/](./network_scanning_enumeration/subdomain_enum/):  
  Finds subdomains for a given domain to expand the attack surface.
- [wifi_scanner/](./network_scanning_enumeration/wifi_scanner/):  
  Scans Wi-Fi channels and SSIDs, listing available networks.
- [wireless_network_scanner/](./network_scanning_enumeration/wireless_network_scanner/):  
  Similar to `wifi_scanner`, but may include extended features or band support.

---

## security_vuln_scanning

[**security_vuln_scanning/**](./security_vuln_scanning/) focuses on scripts for discovering vulnerabilities, automating exploits, and performing reconnaissance.

- [automated_exploit_framework/](./security_vuln_scanning/automated_exploit_framework/):  
  A framework to streamline exploit selection and execution.
- [automated_recon/](./security_vuln_scanning/automated_recon/):  
  Automates data gathering about hosts or domains for penetration testing.
- [cloud_security_auditor/](./security_vuln_scanning/cloud_security_auditor/):  
  Checks common misconfigurations or vulnerabilities in cloud-based services.
- [iot_vulnerability_scanner/](./security_vuln_scanning/iot_vulnerability_scanner/):  
  Identifies potential weaknesses in IoT devices, such as default credentials or open ports.
- [vulnerability_scanner/](./security_vuln_scanning/vulnerability_scanner/):  
  General-purpose vulnerability scanner that probes systems for known CVEs or misconfigurations.

---

## traffic_replay_shaping

[**traffic_replay_shaping/**](./traffic_replay_shaping/) contains tools for replaying previously captured network traffic or shaping (limiting/modifying) traffic in real time.

- [network_traffic_replayer/](./traffic_replay_shaping/network_traffic_replayer/):  
  Replays recorded packets, useful for testing IDS/IPS or debugging production issues.
- [network_traffic_shaper/](./traffic_replay_shaping/network_traffic_shaper/):  
  Adjusts and throttles throughput, latency, or packet loss to simulate various network conditions.
- [packet_replay_tool/](./traffic_replay_shaping/packet_replay_tool/):  
  Focuses on replaying specific packet captures, possibly with modifications or timing controls.

---

## Get Started

1. **Install Dependencies**: Check each subdirectory’s `README.md` for any required Python libraries (e.g., `scapy`, `requests`, `numpy`).
2. **Run Scripts**: Most tools can be used standalone:
   ```bash
   python local_network_scanner.py
