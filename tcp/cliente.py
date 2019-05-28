import socket

host = '127.0.0.1'
porta = 8000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((host, porta))

img = open('C:\\Users\\FILIPE~1\\Documents\\ShareApp\\tcp\\origem\\miranha.jpg', 'rb')
data = img.readlines()

for line in data:
    cliente.send(line)

EOF = '\n\r##'
cliente.send(EOF.encode())

img.close()

resposta = cliente.recv(4896)
resposta = resposta.decode()

print(resposta)