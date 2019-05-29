import socket, pythonping


host = '127.0.0.1'
porta = 8000

clienteTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clienteUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clienteTCP.connect((host, porta))

latencia = pythonping.ping(host).rtt_avg_ms

print(latencia)

img = open('C:\\Users\\FILIPE~1\\Documents\\testeSoquete\\tcp\\origem\\miranha.jpg', 'rb')
data = img.readlines()

if latencia > 30:
    for line in data:
        clienteTCP.send(line)

    EOF = '\n\r##'
    clienteTCP.send(EOF.encode())


else:
    for line in data:
        clienteUDP.sendto(line, (host, porta))

    EOF = '\n\r##'
    clienteUDP.sendto(EOF.encode(), (host, porta))



img.close()

