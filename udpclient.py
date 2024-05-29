import socket
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = b'Hello, Server 10.9.0.5\n'
udp.sendto(data, ("10.9.0.5",9090))

data = b'Hello, Server 10.9.0.6\n'
udp.sendto(data, ("10.9.0.6", 9091))