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
            inicio = time.time() * 1000
            data += client_tcp.recv(1024)
            latencia = (time.time() * 1000) - inicio
            tempo_total += latencia
        except:
            erros += 1

    velocidade_bytes = (1000 / tempo_total) * (1024 * total_partes)
    perda = ((total_partes * erros) / 100)

    if (velocidade_bytes > 1000000):
        velocidade = '%.2f MB/s' % ((velocidade_bytes / 1000) / 1000)
    else:
        velocidade = '%.2f KB/s' % (velocidade_bytes / 1000)

    print('Vazão: %s Latência: %.3f ms (%.2f%% de perda)' % (velocidade, tempo_total, perda))

    img = open('img_out.jpg', 'wb')
    img.write(data)
    img.close()

    client_tcp.send('Deu certo'.encode())

    client_tcp.close()