import socket, time

HOST = ''
PORT = 8000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)

udp.bind(orig)
print('Aguardando')

while True:

    data = b''
    erros = 0
    total_partes = 0

    while (data[-4:] != '\n\r##'.encode()):
        total_partes += 1
        try:
            data += udp.recv(1600)
        except:
            erros += 1

    perda = ((total_partes * erros) / 100)


    img = open('img_out.jpg', 'wb')
    img.write(data)
    img.close()

    udp.close()

