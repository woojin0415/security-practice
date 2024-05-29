import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(('10.0.2.69', 9090))

tcp.sendall((b'Hello Server!\n'))
tcp.sendall((b"Heelo Again!\n"))

tcp.close()