import socket
import os
import sys

def printInputLine():
    content = f"""Input 0, 1, or 2.
0: Get fake Japanese Person data.
1: Get random color
2: Get random Emoji"""
    print(content)

# socketを作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# server addressのpathを設定
server_address = 'socket_file'

print('Connecting to {}'.format(server_address))
print()

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    printInputLine()
    input_str = input()

    sock.sendall(input_str.encode())

    sock.settimeout(5)

    try:
        response = b''
        while True:
            data = sock.recv(32)
            if data:
                response += data
            else:
                break
        print('Complete response: {}'.format(response.decode('utf-8')))
    except TimeoutError:
        print('Socket timeout, ending listening for server messages')
finally:
    print('Closing socket')
    sock.close()