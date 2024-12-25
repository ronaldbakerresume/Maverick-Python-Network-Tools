# Network Monitoring & Analysis

These scripts log, analyze, and measure network activity for performance insights, intrusion detection, and more.

## Subdirectories

- [advanced_port_knocking_framework/](./advanced_port_knocking_framework/)  
  Implements a stealthy server-access method using port knocking.

- [bandwidth_usage_monitor/](./bandwidth_usage_monitor/)  
  Observes current bandwidth usage across interfaces.

- [bandwidth_usage_tracker/](./bandwidth_usage_tracker/)  
  Tracks bandwidth usage over time, creating logs or charts.

- [dynamic_traffic_throttling_tool/](./dynamic_traffic_throttling_tool/)  
  Adjusts traffic flow on-the-fly to enforce rate limits or simulate congestion.

- [network_activity_logger/](./network_activity_logger/)  
  Captures high-level network events, like connections or disconnections, for auditing.

- [network_bandwidth_monitor/](./network_bandwidth_monitor/)  
  Another approach to bandwidth monitoring, sometimes with additional reporting.

- [network_bandwidth_throttler/](./network_bandwidth_throttler/)  
  Specifically enforces a maximum throughput to control usage.

- [network_connection_tracker/](./network_connection_tracker/)  
  Watches active TCP/UDP sessions and logs new or closed connections.

- [network_intrusion_detection/](./network_intrusion_detection/)  
  Basic intrusion detection logic—can be signature-based or anomaly-based.

- [network_intrusion_detection_system/](./network_intrusion_detection_system/)  
  A more feature-complete IDS implementation.

- [network_latency_tool/](./network_latency_tool/)  
  Measures ping times or round-trip latency to identify possible bottlenecks.

- [network_packet_aggregator/](./network_packet_aggregator/)  
  Collects packets from multiple sources or interfaces for centralized analysis.

- [network_packet_analyzer/](./network_packet_analyzer/)  
  Dissects packet data (headers, payloads) for deeper inspection.

- [network_packet_delay_simulator/](./network_packet_delay_simulator/)  
  Injects artificial delay to test how applications behave in high-latency conditions.

- [network_packet_loss_monitor/](./network_packet_loss_monitor/)  
  Observes the rate of dropped packets or retransmissions.

- [network_ping_sweep/](./network_ping_sweep/)  
  Pings a range of IP addresses to discover which hosts respond.

- [network_ping_sweeper/](./network_ping_sweeper/)  
  Similar to `network_ping_sweep`, possibly with additional parallel or scheduling capabilities.

- [network_traffic_encryption_analyzer/](./network_traffic_encryption_analyzer/)  
  Checks whether traffic is encrypted properly or if weak ciphers are in use.

- [network_traffic_logger/](./network_traffic_logger/)  
  Captures packets or connection events to disk for offline review.

- [network_traffic_statistics/](./network_traffic_statistics/)  
  Summarizes traffic volume, protocols used, or top talkers on the network.

- [network_traffic_visualizer/](./network_traffic_visualizer/)  
  Creates graphs or diagrams representing network flows or topologies.

- [packet_sniffer/](./packet_sniffer/)  
  Captures packets in real time from a specified interface.

- [packet_sniffer_protocol_analysis/](./packet_sniffer_protocol_analysis/)  
  Extends the basic sniffer with deeper protocol dissection.

- [remote_command_execution_monitor/](./remote_command_execution_monitor/)  
  Identifies possible remote command executions by analyzing traffic or system logs.

