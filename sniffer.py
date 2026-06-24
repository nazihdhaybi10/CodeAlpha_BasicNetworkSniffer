from scapy.all import *
from datetime import datetime
import threading

running = False
sniff_thread = None

LOG_FILE = "sniffer_log.txt"


def get_protocol_name(packet):
    if packet.haslayer(TCP):
        return "TCP"
    elif packet.haslayer(UDP):
        return "UDP"
    elif packet.haslayer(ICMP):
        return "ICMP"
    else:
        return "OTHER"


def packet_callback(packet):
    if not running:
        return

    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = get_protocol_name(packet)
        time_now = datetime.now().strftime("%H:%M:%S")
        size = len(packet)

        src_port = "-"
        dst_port = "-"

        if packet.haslayer(TCP):
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif packet.haslayer(UDP):
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        line = f"[{time_now}] {ip_src}:{src_port} -> {ip_dst}:{dst_port} | {proto} | Size: {size} bytes"

        print(line)

        with open(LOG_FILE, "a") as f:
            f.write(line + "\n")


def start_sniff():
    global running
    running = True

    print("\n[+] Sniffer STARTED...\n")

    sniff(
        prn=packet_callback,
        store=False,
        stop_filter=lambda x: not running
    )


def stop_sniff():
    global running
    running = False
    print("\n[-] Sniffer STOPPED...\n")


def menu():
    global sniff_thread

    while True:
        print("\n===== ADVANCED SNIFFER MENU =====")
        print("1. Start Sniffer")
        print("2. Stop Sniffer")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            if sniff_thread is None or not sniff_thread.is_alive():
                sniff_thread = threading.Thread(target=start_sniff, daemon=True)
                sniff_thread.start()
            else:
                print("[!] Sniffer already running")

        elif choice == "2":
            stop_sniff()

        elif choice == "3":
            stop_sniff()
            print("Exiting...")
            break

        else:
            print("Invalid choice")


print("=== ADVANCED MINI WIRESHARK ===")
menu()