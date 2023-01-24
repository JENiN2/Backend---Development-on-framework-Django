import socket as sc

sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
sock.bind(('localhost', 8081))
sock.listen(2)

# sock.setblocking(False)  # True is default == sock.settimeout(None). False like sock.settimeout(0)
sock.settimeout(4)

while True:
    try:
        client, addr = sock.accept()
    except sc.error:
        print('No connection')
    else:
        while True:
            result = client.recv(1024)
            if result.decode('UTF-8') == 'quit':
                client.close()
                break
            print(f'Message {addr}: {result.decode("UTF-8")}')
