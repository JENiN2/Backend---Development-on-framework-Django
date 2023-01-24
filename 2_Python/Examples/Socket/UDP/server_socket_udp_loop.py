import socket as sc

sock = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)  # IP4, UDP
sock.bind(('127.0.0.1', 8087))

while True:
    try:
        result = sock.recv(1024)
    except sc.error as e:
        print('Принять сообщение не удалось.')
        print(e)
    except:
        sock.close()
    else:
        print(f'Result: {result.decode("UTF-8")}')
