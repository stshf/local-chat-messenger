import socket
import os
import sys

def display_menu():
    menu = f"""Please select an option by entering the corresponding number:
0: Get fake Japanese Person data.
1: Get random color
2: Get random Emoji"""
    print(menu)

def create_socket():
    return socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

def connect_to_server(sock, server_address):
    try:
        sock.connect(server_address)
    except socket.error as err:
        print(err)
        sys.exit(1)

def send_request(sock, request):
    sock.sendall(request.encode())

def receive_response(sock):
    sock.settimeout(5)
    response = b''
    try:
        while True:
            data = sock.recv(32)
            if data:
                response += data
            else:
                break
        return response.decode('utf-8')
    except TimeoutError:
        print('Socket timeout, ending listening for server messages')
        return None

def main():
    server_address = 'socket_file'
    sock = create_socket()

    connect_to_server(sock, server_address)

    try:
        display_menu()
        user_input = input()

        send_request(sock, user_input)
        response = receive_response(sock)
        if response:
            print('Complete response: {}'.format(response))

    finally:
        print('Closing socket')
        sock.close()

if __name__ == "__main__":
    main()