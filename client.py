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

def print_colored_response(response):
    if response.startswith('#') and len(response) == 7:
        # ANSI escape code for colored text
        print(f'\033[38;2;{int(response[1:3], 16)};{int(response[3:5], 16)};{int(response[5:7], 16)}m Response from server: {response}\033[0m')
    else:
        print('Response from server: {}'.format(response))

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
            if user_input == '1':
                print_colored_response(response)
            else:
                print('Response from server: {}'.format(response))

    finally:
        print('Closing socket')
        sock.close()

if __name__ == "__main__":
    main()