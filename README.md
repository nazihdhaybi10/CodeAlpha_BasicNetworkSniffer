# Advanced Network Sniffer

## 🔐 Cyber Security Internship Project

A professional Python-based network packet sniffer using Scapy that captures and analyzes real-time network traffic.

---

## 🚀 Features

- Real-time packet capturing
- Source & Destination IP tracking
- Protocol detection (TCP / UDP / ICMP)
- Port analysis (Source & Destination)
- Packet size monitoring
- Timestamp logging
- Start / Stop control system
- Automatic log saving

---

## 🛠️ Technologies Used

- Python 3
- Scapy
- Kali Linux
- VirtualBox (for testing environment)

---

## 📦 Installation

Install dependencies:

```bash
sudo apt update
sudo apt install python3-scapy -y
```

---

## ▶️ Usage

Run the tool:

```bash
sudo python3 sniffer.py
```

### Menu Options:

1. Start Sniffer  
2. Stop Sniffer  
3. Exit  

---

## 📊 Example Output

```text
[2026-06-24 15:22:10] 192.168.1.10:52344 -> 142.250.184.78:443 | TCP | Size: 74 bytes
```

---

## 📁 Log File

All captured packets are saved in:

```text
sniffer_log.txt
```

---

## 🎯 Learning Outcomes

- Network packet analysis
- Understanding TCP/IP model
- Traffic monitoring
- Scapy library usage
- Cybersecurity fundamentals

---

## ⚠️ Disclaimer

This tool is for educational and authorized testing purposes only.

---

## 👨‍💻 Author

Nazih El Dhaybi 