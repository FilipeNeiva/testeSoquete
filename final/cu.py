import socket
import time

host = ''
porta = 8000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp.bind((host, porta))
tcp.listen(5)
print('Ouvindo data em %s:%d' %(host,porta))

conection,cliente = tcp.accept()
print('testando')

teste = []
erro = 0

start = time.perf_counter() * 1000

for i in range(0,4,1):
    try:
        teste.append(conection.recv(1024))
    except:
        erro += 1

end = time.perf_counter() * 1000
latencia = end - start
vazao = (1000/latencia)
perda = (5 * erro) / 100

latencia1 = bytes(latencia)
conection.send(latencia1)
