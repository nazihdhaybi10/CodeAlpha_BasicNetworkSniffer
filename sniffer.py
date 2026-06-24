from scapy.all import *
from datetime import datetime

sniffer = None
LOG_FILE = "sniffer_log.txt"


def get_protocol_name(packet):
    if packet.haslayer(TCP):
        return "TCP"
    elif packet.haslayer(UDP):
        return "UDP"
    elif packet.haslayer(ICMP):
        return "ICMP"
    return "OTHER"


def packet_callback(packet):
    if packet.haslayer(IP):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        protocol = get_protocol_name(packet)
        size = len(packet)

        src_port = "-"
        dst_port = "-"

        if packet.haslayer(TCP):
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

        elif packet.haslayer(UDP):
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        line = (
            f"[{timestamp}] "
            f"{src_ip}:{src_port} -> "
            f"{dst_ip}:{dst_port} | "
            f"{protocol} | "
            f"Size: {size} bytes"
        )

        print(line)

        with open(LOG_FILE, "a") as log:
            log.write(line + "\n")


def start_sniffer():
    global sniffer

    if sniffer is not None:
        print("[!] Sniffer is already running.")
        return

    print("\n[+] Sniffer Started\n")

    sniffer = AsyncSniffer(
        prn=packet_callback,
        store=False
    )

    sniffer.start()


def stop_sniffer():
    global sniffer

    if sniffer is None:
        print("[!] Sniffer is not running.")
        return

    sniffer.stop()
    sniffer = None

    print("\n[-] Sniffer Stopped\n")


def show_log_file():
    try:
        with open(LOG_FILE, "r") as log:
            lines = log.readlines()

            if not lines:
                print("Log file is empty.")
                return

            print("\n===== LAST 10 ENTRIES =====\n")

            for line in lines[-10:]:
                print(line.strip())

    except FileNotFoundError:
        print("No log file found yet.")


def menu():
    while True:

        print("\n===== ADVANCED NETWORK SNIFFER =====")
        print("1. Start Sniffer")
        print("2. Stop Sniffer")
        print("3. View Last 10 Logs")
        print("4. Exit")

        choice = input("\nChoose: ")

        if choice == "1":
            start_sniffer()

        elif choice == "2":
            stop_sniffer()

        elif choice == "3":
            show_log_file()

        elif choice == "4":
            stop_sniffer()
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    print("=== PROFESSIONAL MINI WIRESHARK ===")
    menu()