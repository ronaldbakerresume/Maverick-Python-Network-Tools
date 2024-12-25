#!/usr/bin/env bash
#
# organize_files.sh
# Moves all top-level .py files into the desired subdirectory structure
# where each script resides in its own subfolder.

# An associative array mapping "filename.py" => "target/subfolder".
# Each target path is relative to the top-level directory where you run this script.
# Adjust the paths if you want a different layout.

declare -A FILE_TO_DIR=(
  # ----------------------
  # 1) Network Scanning & Enumeration
  # ----------------------
  ["local_network_scanner.py"]="src/my_python_network_tools/network_scanning_enumeration/local_network_scanner"
  ["wifi_scanner.py"]="src/my_python_network_tools/network_scanning_enumeration/wifi_scanner"
  ["wireless_network_scanner.py"]="src/my_python_network_tools/network_scanning_enumeration/wireless_network_scanner"
  ["ip_mac_scanner.py"]="src/my_python_network_tools/network_scanning_enumeration/ip_mac_scanner"
  ["ip_geolocation_tracker.py"]="src/my_python_network_tools/network_scanning_enumeration/ip_geolocation_tracker"
  ["subdomain_enum.py"]="src/my_python_network_tools/network_scanning_enumeration/subdomain_enum"
  ["port_scanner.py"]="src/my_python_network_tools/network_scanning_enumeration/port_scanner"
  ["network_port_scanner.py"]="src/my_python_network_tools/network_scanning_enumeration/network_port_scanner"
  ["network_device_enumerator.py"]="src/my_python_network_tools/network_scanning_enumeration/network_device_enumerator"

  # ----------------------
  # 2) Network Monitoring & Analysis
  # ----------------------
  ["bandwidth_usage_monitor.py"]="src/my_python_network_tools/network_monitoring_analysis/bandwidth_usage_monitor"
  ["bandwidth_usage_tracker.py"]="src/my_python_network_tools/network_monitoring_analysis/bandwidth_usage_tracker"
  ["network_activity_logger.py"]="src/my_python_network_tools/network_monitoring_analysis/network_activity_logger"
  ["network_bandwidth_monitor.py"]="src/my_python_network_tools/network_monitoring_analysis/network_bandwidth_monitor"
  ["network_bandwidth_throttler.py"]="src/my_python_network_tools/network_monitoring_analysis/network_bandwidth_throttler"
  ["network_connection_tracker.py"]="src/my_python_network_tools/network_monitoring_analysis/network_connection_tracker"
  ["network_intrusion_detection.py"]="src/my_python_network_tools/network_monitoring_analysis/network_intrusion_detection"
  ["network_intrusion_detection_system.py"]="src/my_python_network_tools/network_monitoring_analysis/network_intrusion_detection_system"
  ["network_latency_tool.py"]="src/my_python_network_tools/network_monitoring_analysis/network_latency_tool"
  ["network_packet_aggregator.py"]="src/my_python_network_tools/network_monitoring_analysis/network_packet_aggregator"
  ["network_packet_analyzer.py"]="src/my_python_network_tools/network_monitoring_analysis/network_packet_analyzer"
  ["network_packet_delay_simulator.py"]="src/my_python_network_tools/network_monitoring_analysis/network_packet_delay_simulator"
  ["network_packet_loss_monitor.py"]="src/my_python_network_tools/network_monitoring_analysis/network_packet_loss_monitor"
  ["network_ping_sweep.py"]="src/my_python_network_tools/network_monitoring_analysis/network_ping_sweep"
  ["network_ping_sweeper.py"]="src/my_python_network_tools/network_monitoring_analysis/network_ping_sweeper"
  ["network_traffic_encryption_analyzer.py"]="src/my_python_network_tools/network_monitoring_analysis/network_traffic_encryption_analyzer"
  ["network_traffic_logger.py"]="src/my_python_network_tools/network_monitoring_analysis/network_traffic_logger"
  ["network_traffic_statistics.py"]="src/my_python_network_tools/network_monitoring_analysis/network_traffic_statistics"
  ["network_traffic_visualizer.py"]="src/my_python_network_tools/network_monitoring_analysis/network_traffic_visualizer"
  ["packet_sniffer.py"]="src/my_python_network_tools/network_monitoring_analysis/packet_sniffer"
  ["packet_sniffer_protocol_analysis.py"]="src/my_python_network_tools/network_monitoring_analysis/packet_sniffer_protocol_analysis"
  ["remote_command_execution_monitor.py"]="src/my_python_network_tools/network_monitoring_analysis/remote_command_execution_monitor"
  ["advanced_port_knocking_framework.py"]="src/my_python_network_tools/network_monitoring_analysis/advanced_port_knocking_framework"
  ["dynamic_traffic_throttling_tool.py"]="src/my_python_network_tools/network_monitoring_analysis/dynamic_traffic_throttling_tool"

  # ----------------------
  # 3) DNS Tools
  # ----------------------
  ["dns_lookup.py"]="src/my_python_network_tools/dns_tools/dns_lookup"
  ["dns_query_logger.py"]="src/my_python_network_tools/dns_tools/dns_query_logger"
  ["dns_request_interceptor.py"]="src/my_python_network_tools/dns_tools/dns_request_interceptor"
  ["dns_spoofing_detection.py"]="src/my_python_network_tools/dns_tools/dns_spoofing_detection"
  ["dns_spoofing_tool.py"]="src/my_python_network_tools/dns_tools/dns_spoofing_tool"

  # ----------------------
  # 4) ARP & MAC Tools
  # ----------------------
  ["arp_spoofing_detection.py"]="src/my_python_network_tools/arp_mac_tools/arp_spoofing_detection"
  ["arp_spoofing_tool.py"]="src/my_python_network_tools/arp_mac_tools/arp_spoofing_tool"
  ["mac_address_spoofer.py"]="src/my_python_network_tools/arp_mac_tools/mac_address_spoofer"

  # ----------------------
  # 5) HTTP & Protocol Tools
  # ----------------------
  ["http_proxy_server.py"]="src/my_python_network_tools/http_protocol_tools/http_proxy_server"
  ["http_request_logger.py"]="src/my_python_network_tools/http_protocol_tools/http_request_logger"
  ["http_traffic_monitor.py"]="src/my_python_network_tools/http_protocol_tools/http_traffic_monitor"
  ["banner_grabber.py"]="src/my_python_network_tools/http_protocol_tools/banner_grabber"
  ["protocol_analyzer.py"]="src/my_python_network_tools/http_protocol_tools/protocol_analyzer"
  ["websocket_traffic_logger.py"]="src/my_python_network_tools/http_protocol_tools/websocket_traffic_logger"

  # ----------------------
  # 6) Network Attacks & Exploit Simulation
  # ----------------------
  ["slowloris_attack_simulator.py"]="src/my_python_network_tools/attacks_exploits/slowloris_attack_simulator"
  ["wifi_deauth_attack_tool.py"]="src/my_python_network_tools/attacks_exploits/wifi_deauth_attack_tool"
  ["firewall_evasion_tool.py"]="src/my_python_network_tools/attacks_exploits/firewall_evasion_tool"
  ["tcp_syn_flood_detection.py"]="src/my_python_network_tools/attacks_exploits/tcp_syn_flood_detection"
  ["ssl_strip_tool.py"]="src/my_python_network_tools/attacks_exploits/ssl_strip_tool"
  ["port_forwarding_tool.py"]="src/my_python_network_tools/attacks_exploits/port_forwarding_tool"

  # ----------------------
  # 7) Security & Vulnerability Scanning
  # ----------------------
  ["automated_exploit_framework.py"]="src/my_python_network_tools/security_vuln_scanning/automated_exploit_framework"
  ["automated_recon.py"]="src/my_python_network_tools/security_vuln_scanning/automated_recon"
  ["vulnerability_scanner.py"]="src/my_python_network_tools/security_vuln_scanning/vulnerability_scanner"
  ["iot_vulnerability_scanner.py"]="src/my_python_network_tools/security_vuln_scanning/iot_vulnerability_scanner"
  ["cloud_security_auditor.py"]="src/my_python_network_tools/security_vuln_scanning/cloud_security_auditor"

  # ----------------------
  # 8) Traffic Replaying & Shaping
  # ----------------------
  ["network_traffic_replayer.py"]="src/my_python_network_tools/traffic_replay_shaping/network_traffic_replayer"
  ["packet_replay_tool.py"]="src/my_python_network_tools/traffic_replay_shaping/packet_replay_tool"
  ["network_traffic_shaper.py"]="src/my_python_network_tools/traffic_replay_shaping/network_traffic_shaper"

  # ----------------------
  # 9) Encryption & Secure Tools
  # ----------------------
  ["encrypted_packet_sender.py"]="src/my_python_network_tools/encryption_secure_tools/encrypted_packet_sender"
  ["secure_file_transfer_tool.py"]="src/my_python_network_tools/encryption_secure_tools/secure_file_transfer_tool"
  ["secure_shell_traffic_logger.py"]="src/my_python_network_tools/encryption_secure_tools/secure_shell_traffic_logger"
  ["tls_ssl_tester.py"]="src/my_python_network_tools/encryption_secure_tools/tls_ssl_tester"

  # ----------------------
  # 10) Misc
  # ----------------------
  ["wifi_signal_mapper.py"]="src/my_python_network_tools/misc/wifi_signal_mapper"
  ["wireless_signal_strength_monitor.py"]="src/my_python_network_tools/misc/wireless_signal_strength_monitor"
)

# Loop over the mapping
for FILE in "${!FILE_TO_DIR[@]}"; do
    # If the file exists in the current (top-level) directory
    if [ -f "$FILE" ]; then
        DEST_DIR="${FILE_TO_DIR[$FILE]}"
        
        # Create the destination directory if it doesn't exist
        mkdir -p "$DEST_DIR"

        # Move the file into that directory
        mv "$FILE" "$DEST_DIR"

        # Print what we did
        echo "Moved $FILE → $DEST_DIR"
    else
        echo "Skipping $FILE (not found at top level)."
    fi
done

echo "File organization complete!"

