import socket
target = "scanme.nmap.org"
for port in range(1,101):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target,port))
    if result == 0:
        print(f"\n{port} open")
        try:
            sock.send(b"Hello\r\n")
            banner = sock.recv(1024)
            print("banner:")
            print(banner.decode(errors = "ignore"))
        except:
            print("no banner")
        finally:
            sock.close()