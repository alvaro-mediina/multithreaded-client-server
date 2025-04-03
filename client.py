import socket

HEADER = 64
PORT = 8080
SERVER = "127.0.1.1"
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DESCONECTADO!"
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048))

send("Hello World!")
send("Hola Mundo!")
send("Hola Santi!")
input(str(input("Ingresar ->")))
input(str(input("Ingresar ->")))
send(DISCONNECT_MESSAGE)