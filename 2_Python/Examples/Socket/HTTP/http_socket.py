import socket as sc

sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
sock.connect(('example.com', 80))

content = [
    'GET / HTTP/1.1',
    'Host: example.com',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n',
]

request_http = '\n'.join(content)

print('Сформированный запрос')
print(request_http)
print('-' * 30)

sock.send(request_http.encode('UTF-8'))
result = sock.recv(65536)

print(result.decode('UTF-8'))
