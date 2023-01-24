import socket as sc

sock = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)  # IP4, UDP
sock.bind(('127.0.0.1', 8087))
result = sock.recv(1024)
print(f'Result: {result.decode("UTF-8")}')
