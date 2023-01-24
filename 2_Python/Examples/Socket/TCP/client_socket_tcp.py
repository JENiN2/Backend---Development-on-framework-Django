import socket as sc

sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
sock.connect(('127.0.0.1', 8081))

while True:
    message = input('Input message: ')
    sock.send(message.encode('UTF-8'))
    if message == 'quit':
        sock.close()
        break
