import socket
from _thread import *
import sys

server = "192.168.0.11"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, server started.")

def threaded_client(connection):
    reply = ""
    while True:
        try:
            data = connection.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("received: ", reply)
                print("sending: ", reply)
            connection.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    connection.close()

while True:
    connection, address = s.accept()
    print("Connected to:", address)

    start_new_thread(threaded_client, (connection,))