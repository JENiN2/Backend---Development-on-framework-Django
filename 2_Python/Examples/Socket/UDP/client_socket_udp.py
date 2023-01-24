import socket as sc

sock = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)
sock.sendto(b'Hello socket', ('127.0.0.1', 8087))

