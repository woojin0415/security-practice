import socket

udp = socket.socket(socket.AF_INET, socker.SOCK_DGRAM)
udp.bind(("0.0.0.0", 9090))

while True:
    data, addr = udp.recvfrom(1024)
    print("From {}: {}".format(addr, data))