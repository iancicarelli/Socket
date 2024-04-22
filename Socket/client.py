import socket
import threading

HEADER = 64
PORT = 6060
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "BYE"
#server usar ip de la maquina
SERVER = "192.168.1.84"
ADDR= (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
   # print(client.recv(HEADER).decode(FORMAT))

def recv():
    while True:
        message_length = client.recv(HEADER).strip()
        if message_length:
            message_length = int(message_length.decode(FORMAT))
            message = client.recv(message_length).decode(FORMAT)
            print(f"[SERVER]: {message}")


def send_console_input():
    while True:
        msg = input("Ingrese el mensaje a enviar ('BYE' para salir): ")
        if msg.upper() == DISCONNECT_MESSAGE:
            send(DISCONNECT_MESSAGE)
            break
        send(msg)


thread_recv = threading.Thread(target=recv)
thread_recv.start()
send_console_input()
