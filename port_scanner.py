import socket
ip = "127.0.0.1" #localhost
for port in range(1,101):
 #AF_INET=> IPv4
 sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 sock.settimeout(0.5) #delay
 result = sock.connect_ex((ip,port))
 if result == 0:
   print("port open")
 sock.close()