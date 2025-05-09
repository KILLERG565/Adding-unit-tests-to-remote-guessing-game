def receive_data(sock):
    return sock.recv(1024).decode().strip()

def send_data(sock, msg):
    sock.sendall(msg.encode())

def is_correct_reply(msg):
    return "CORRECT!" in msg
# this is the function