import socket
import threading
import random

HEADER = 64
PORT = 6060
# SERVER = " 192.168.1.84"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "BYE"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn , addr):
    print(f"[Nueva conexion] {addr} conectado")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
         msg_length = int(msg_length)
         msg = conn.recv(msg_length).decode(FORMAT)
         if msg == DISCONNECT_MESSAGE:
             connected = False

        disordered_msg = disordered_message(msg)
        print(f"[{addr}] {msg} -> {disordered_msg}")
        conn.send(str(len(disordered_msg)).encode(FORMAT).ljust(HEADER))
        conn.send(disordered_msg.encode(FORMAT))

    conn.close()

def disordered_message(msg):
    msg_list = list(msg)
    random.shuffle(msg_list)
    return ''.join(msg_list)

def start():
    server.listen()
    print(f"[LISTENING] servidor escuchando en {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Conexiones activas] {threading.active_count()-1}")

print("[Iniciando] iniciando el servidor")
start()