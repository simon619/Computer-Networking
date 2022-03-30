import socket

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'END'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
print('Server is Listening')
conn, addr = server.accept()
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
            msg = int(msg)
            if msg <= 40:
                conn.send(f'You Have Earned 200 TK for working { msg } hours'.encode(FORMAT))
            if msg > 40:
                bonus = msg - 40
                bonus = 300 * bonus
                salary = 8000 + bonus
                conn.send(f'You Have Earned { salary } TK for working { msg } hours'.encode(FORMAT))

conn.close()
