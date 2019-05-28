import socket

HOST = '127.0.0.1'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

img = open('C:\\Users\\FILIPE~1\\Documents\\ShareApp\\udp\\origem\\miranha.jpg', 'rb')
data = img.readlines()

for line in data:
    udp.sendto(line, dest)

EOF = '\n\r##'
udp.sendto(EOF.encode(), dest)

img.close()

udp.close()