import socket 
import threading


HEADER = 64
PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DESCONECTADO!"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NUEVA CONEXIÓN] {addr} conectado.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:   
            msg_length = int(msg_length)
            print(f"[{addr}] {msg}")
            conn.send("Mensaje recibido".encode(FORMAT))
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

    conn.close()


def start():
    server.listen()
    print(f"[ESCUCHANDO] El servidor está sobre {SERVER}")
    connected = True
    while connected:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[CONEXIONES ACTIVAS] {threading.active_count() - 1}")

print("[INICIALIZANDO] El servidor se está inicializando...")
start()