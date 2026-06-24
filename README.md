# Network Sniffer

## Overview

Advanced Network Sniffer is a Python-based network monitoring tool developed using the Scapy library. It captures network packets in real time and displays useful information such as source IP, destination IP, protocol type, ports, packet size, and timestamp.

This project was created as part of a Cyber Security Internship task to demonstrate packet sniffing and network traffic analysis fundamentals.

---

## Features

- Real-time packet capture
- Source and destination IP detection
- Protocol identification (TCP, UDP, ICMP)
- Source and destination port detection
- Packet size monitoring
- Timestamp logging
- Start and Stop controls
- Log file generation
- View recent captured packets

---

## Technologies Used

- Python 3
- Scapy
- Kali Linux
- VirtualBox

---

## Installation

Install Scapy:

```bash
sudo apt update
sudo apt install python3-scapy -y
```

## Usage

Run the program:

```bash
sudo python3 sniffer.py
```

### Menu Options

1. Start Sniffer
2. Stop Sniffer
3. View Last 10 Logs
4. Exit

---

## Example Output

```text
[2026-06-24 15:22:10] 192.168.1.10:52431 -> 142.250.184.78:443 | TCP | Size: 74 bytes
```

---

## Log File

Captured packets are automatically saved in:

```text
sniffer_log.txt
```

---

## Learning Outcomes

- Understanding packet sniffing concepts
- Working with network protocols
- Analyzing network traffic
- Using Scapy for cybersecurity tasks
- Building practical security tools

---

## Disclaimer

This project is intended for educational and authorized testing purposes only.

---

## Author

Mahmoud Dhaybi
Cyber Security Internship Project