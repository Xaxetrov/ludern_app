import socket


def parse(data):
    [message, needs_answer_p] = data.split('&needs_answer=')
    if needs_answer_p == '1':
        needs_answer = True
    else:
        needs_answer = False
    return message, needs_answer


if __name__ == '__main__':

    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Server location
    host = "127.0.0.1"  # input("host : ") # par défaut 127.0.0.1
    port = 12345  # int(input("port : "))

    # Connection to server
    s.connect((host, port))

    message_received = ''
    answer = ''
    # Stop if the user want to leave
    while answer != 'q' and message_received != 'end_of_com':

        # Receive message
        received = s.recv(1024).decode()
        # if received == 'end_of_com':
        #    break
        (message_received, needsAnswer) = parse(received)
        print(' <- ' + message_received)

        # Send message
        if needsAnswer:
            answer = input(" -> ")
            s.send(answer.encode())

    # Close the connection
    s.close()
