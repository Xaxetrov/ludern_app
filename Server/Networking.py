def send_message(conn, message, needs_answer=False):
    if needs_answer:
        sent_message = message + '&needs_answer=1'
    else:
        sent_message = message + '&needs_answer=0'
    print('to ' + str(conn.getpeername()) + ' sending: ' + sent_message)
    conn.send(sent_message.encode())


def send_message_to_all(c1, c2, message, needs_answer = False):
    send_message(c1, message, needs_answer)
    send_message(c2, message, needs_answer)


def receive_message(conn, max_size=1024):
    message = conn.recv(max_size).decode()
    if not message:
        return 'USER_DISCONNECTED'
    print('from ' + str(conn.getpeername()) + ' received: ' + message)
    return message


def receive_message_from_all(c1, c2, max_size=1024):
    m1 = receive_message(c1, max_size)
    m2 = receive_message(c2, max_size)
    return m1, m2
