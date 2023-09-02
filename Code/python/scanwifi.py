import os
import scapy

from scapy.all import ARP, Ether, srp

def scan_wifi_devices(interface):
    # Create an ARP request packet to broadcast to all devices on the network
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.1.0/24")

    # Send the packet and capture responses
    ans, _ = srp(arp_request, timeout=2, iface=interface, verbose=False)

    # Dictionary to store IP and MAC addresses of connected devices
    devices = {}

    # Process the responses
    for _, rcv in ans:
        devices[rcv.psrc] = rcv.hwsrc

    return devices

if __name__ == "__main__":
    # Replace "wlan0" with the name of your Wi-Fi interface (e.g., "eth0" for Ethernet)
    wifi_interface = "wlan0"

    print("Scanning connected devices on the Wi-Fi network...")
    connected_devices = scan_wifi_devices(wifi_interface)

    # Print the connected device details
    print("\nConnected Devices:")
    for ip, mac in connected_devices.items():
        print(f"IP: {ip} - MAC Address: {mac}")
