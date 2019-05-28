import socket, os
import time


host = '10.0.15.105'
porta = 8000

clienteTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clienteUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clienteTCP.connect((host, porta))

testes = ['teste1', 'teste2', 'seu cu viado', 'xsdcfvgbhn', 'fvtgybhun']

for teste in testes:
    clienteTCP.send(teste.encode())

percaTCP = clienteTCP.recv(1024).decode()
print(percaTCP)
latenciaTCP = clienteTCP.recv(1024).decode()


for teste in testes:
    clienteUDP.sendto('teste'.encode(), (host, porta))

percaUDP = clienteUDP.recv(1024).decode()
latenciaUDP = clienteUDP.recv(1025).decode()


img = open('C:\\Users\\FILIPE~1\\Documents\\ShareApp\\tcp\\origem\\miranha.jpg', 'rb')
data = img.readlines()

if percaTCP < percaUDP:
    for line in data:
        clienteTCP.send(line)

    EOF = '\n\r##'
    clienteTCP.send(EOF.encode())

    resposta = clienteTCP.recv(4896)
    resposta = resposta.decode()

    print(resposta)
elif percaUDP < percaTCP:
    for line in data:
        clienteUDP.sendto(line, (host, porta))

    EOF = '\n\r##'
    clienteUDP.sendto(EOF.encode(), (host, porta))
elif latenciaTCP < latenciaUDP:
    for line in data:
        clienteTCP.send(line)

    EOF = '\n\r##'
    clienteTCP.send(EOF.encode())

    resposta = clienteTCP.recv(4896)
    resposta = resposta.decode()

    print(resposta)
else:
    for line in data:
        clienteUDP.sendto(line, (host, porta))

    EOF = '\n\r##'
    clienteUDP.sendto(EOF.encode(), (host, porta))

img.close()

