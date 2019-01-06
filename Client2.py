import socket

from pip._vendor.distlib.compat import raw_input

## To create Socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to connect")
    sys.exit();

print("[CLIENT]Socket Created")

## To declare the host and port
host = "192.168.43.85"
port = 9000

## Function to connect
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print("[CLIENT]Hostname could not be resolved")
    sys.exit();

print("[CLIENT]IP Address: " + remote_ip)

s.connect((remote_ip, port))

while True:
    print("Send 'q' to exit\n")
    message = input("-> ")


    s.send(bytes(message,'UTF8'))
    data = s.recv(4056)
    data.decode("utf-8")

    Operations = input(str(data))
    s.send(bytes(Operations,'UTF8'))

    statement = s.recv(1024).decode()
    print(statement)
    value = input()
    s.send(bytes(value, 'UTF8'))
    ##num = int(raw_input("Enter number: "))
    ##s.send(bytes(num,'UTF8'))

    statement2 = s.recv(1024).decode()
    print(statement2)
    value2 = input()
    s.send(bytes(value2, 'UTF8'))
    ##num2 = int(raw_input("Enter number: "))
    ##s.send(bytes(num2,'UTF8'))
    if statement2 == "exit":
        print("Connection Lost")
        exit(0)
    else:
        total = s.recv(1024).decode()
        print("Total value is :",total)
    
    
    statement2 = s.recv(1024).decode()
    print(statement2)
    value2 = input()
    s.send(bytes(value2, 'UTF8'))
    if statement2 == "exit":
        print("Connection Lost")
        exit(0)
    
    statement2 = s.recv(1024).decode()
    print(statement2)
    value2 = input()
    s.send(bytes(value2, 'UTF8'))
    if statement2 == "exit":
        print("Connection Lost")
        exit(0)
    

    s.close()

