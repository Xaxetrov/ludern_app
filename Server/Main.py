import socket
from Server.GameManager import *
from Server.Networking import *


if __name__ == '__main__':

    # create a socket object (listener)
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # My adress
    host = '0.0.0.0'
    port = 12345
    print('My local adress is : {}'.format(host))
    print('My port is : {}'.format(port))

    # bind the socket to the port
    serversocket.bind((host, port))

    # Listen to someone
    serversocket.listen(1)
    # establish a connection
    conn1, addr = serversocket.accept()
    print('Got a connection from {}'.format(addr))
    send_message(conn1, "Hello, player 1. Waiting for a second player...")
    conn2, addr2 = serversocket.accept()
    print('Got a connection from {}'.format(addr))

    send_message(conn1, "Player 2 found !")
    send_message(conn2, "Hello, player 2")

    # Begin to play !
    begin_party(conn1, conn2)

    # Close connection
    send_message_to_all(conn1, conn2, 'end_of_com')
    conn1.close()
