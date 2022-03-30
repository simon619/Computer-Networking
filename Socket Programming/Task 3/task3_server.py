import socket
import threading

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'END'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_clients(conn, addr):
    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                conn.send('Goodbye'.encode(FORMAT))
            else:
                v = 'aeiouAEIOU'
                count = 0
                for i in msg:
                    if i in v:
                        count += 1

                if count == 0:
                    conn.send('Not Enough Vowels'.encode(FORMAT))
                elif 0 <= count <= 2:
                    conn.send('Enough vowels I guess'.encode(FORMAT))
                elif count < 2:
                    conn.send('Too Many Vowel'.encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print('Server is Listening')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clients, args=(conn, addr))
        thread.start()
        print(f'Total Client Connected Currently: {threading.active_count() - 1}')


start()


