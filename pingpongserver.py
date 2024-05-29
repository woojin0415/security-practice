import socket

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(("0.0.0.0", 9090))

while True:
    data, (ip,port) = udp.recvfrom(1024)
    print("From {}:{} {}".format(ip, port, str(data, 'utf8')))

    udp.sendto(b'Thank you!\n', (ip,port))