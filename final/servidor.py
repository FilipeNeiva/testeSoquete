import socket
import time

host = ''
porta = 8000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tcp.bind((host, porta))
tcp.listen(5)

#udp.bind((host, porta))

print('Ouvindo data em %s:%d' %(host,porta))

while True:

    conection,cliente = tcp.accept()

    teste = []
    erro = 0

    start = time.perf_counter() * 1000

    for i in range(0,4,1):
        try:
            teste.append(conection.recv(1024))
        except:
            erro += 1

    end = time.perf_counter() * 1000
    latenciaTCP = end - start
    vazaoTCP = (1000/latenciaTCP)
    perdaTCP = (5 * erro) / 100

    print(latenciaTCP)
    print(perdaTCP)

    conection.send(('%f' % latenciaTCP).encode())
    conection.send(('%f' % perdaTCP).encode())

    # teste = []
    # erro = 0
    #
    # start = time.perf_counter() * 1000
    #
    # for i in range(0, 4, 1):
    #     try:
    #         teste.append(udp.recv(1024))
    #     except:
    #         erro += 1
    #
    # end = time.perf_counter() * 1000
    # latenciaUDP = end - start
    # vazaoUDP = (1000 / latenciaUDP)
    # perdaUDP = (5 * erro) / 100
    #
    #
    #
    # udp.sendto(('%f' % latenciaUDP).encode(), cliente)
    # udp.sendto(('%f' % perdaTCP).encode(), cliente)

    print('Conexão recebida por: %s:%d' % (cliente[0], cliente[1]))

    data = b''
    erros = 0
    total_partes = 0
    tempo_total = 0

    while (data[-4:] != "\n\r##".encode()):
        total_partes += 1
        try:
            inicio = time.time() * 1000
            data += conection.recv(1024)
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

    conection.send('Deu certo'.encode())

    conection.close()
