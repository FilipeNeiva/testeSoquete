import socket
import time

host = ''
porta = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, porta))
server.listen(5)

print('Ouvindo em %s:%d' % (host, porta))


while True:
    client_tcp, addr_tcp = server.accept()

    print('Conexão recebida por: %s:%d' % (addr_tcp[0], addr_tcp[1]))

    data = b''
    erros = 0
    total_partes = 0
    tempo_total = 0

    while (data[-4:] != "\n\r##".encode()):
        total_partes += 1
        try:
            data += client_tcp.recv(1024)
        except:
            erros += 1

    perda = ((total_partes * erros) / 100)


    img = open('img_out.jpg', 'wb')
    img.write(data)
    img.close()

    client_tcp.send('Deu certo'.encode())

    client_tcp.close()