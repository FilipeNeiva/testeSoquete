import socket, time

HOST = ''
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)

udp.bind(orig)
print('Aguardando')

while True:

    data = b''
    erros = 0
    total_partes = 0
    tempo_total = 0

    ini2 = time.time()
    while (data[-4:] != '\n\r##'.encode()):
        total_partes += 1
        try:
            inicio = time.perf_counter()
            data += udp.recv(1600)
            fim = (time.perf_counter()) - inicio
            tempo_total += fim
        except:
            erros += 1
    fim2 = time.time()
    print(fim2-ini2)

    velocidade_bytes = (10000 / tempo_total) * (1550 * total_partes)
    perda = ((total_partes * erros) / 100)

    if (velocidade_bytes > 1000000):
        velocidade = '%.2f MB/s' % ((velocidade_bytes / 1000) / 1000)
    else:
        velocidade = '%.2f KB/s' % (velocidade_bytes / 1000)

    print('Vazão: %s Latência: %.3f ms (%.2f%% de perda)' % (velocidade, tempo_total, perda))

    img = open('img_out.jpg', 'wb')
    img.write(data)
    img.close()

    #udp.sendto('Deu certo'.encode(), cliente)

    udp.close()

