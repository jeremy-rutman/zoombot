import socket
UDP_IP = "127.0.0.1"
UDP_IP = "178.128.26.70"
UDP_IP = "2a10:800c:380b:0:1c19:f06c:aa57:8d6b/64"
UDP_IP = "2a10:800c:380b:0:1c19:f06c:aa57:8d6b"
UDP_PORT = 5005
#s = socket.socket(family=socket.AF_INET6)
#sock = socket.socket(socket.AF_INET, # Internet
sock = socket.socket(socket.AF_INET6, # Internet
socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

print(f'sock {sock} ip {UDP_IP} port {UDP_PORT}')
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)
