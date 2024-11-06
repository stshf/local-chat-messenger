import socket
import os 
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

# 送信先のサーバアドレスを定義
server_address = 'tmp/udp_socket_file'

# clientのアドレスを定義
# serverはこのclientアドレスにメッセージを返信する
client_address = 'tmp/udp_client_socket_file'

# 以前の接続が残っていた場合、clientアドレスをunlink(削除)する
try:
    os.unlink(client_address)
# サーバアドレスが存在しない場合、例外を無視
except FileNotFoundError:
    pass

print('bind to {}'.format(client_address))
try:
    sock.bind(client_address)
except socket.error as err:
    print(err)
    sys.exit(1)

# sendto() recvfrom()でデータの送受信を行う
try:
    print('Type what in your message or exit')
    input_str = input()
    
    sock.sendto(input_str.encode(), server_address)

    # サーバからの応答時間に対する待機
    sock.settimeout(2)

    try:
        # return
        # data: binary format
        # server: server address
        data, server = sock.recvfrom(4096)

        data_str = data.decode('utf-8')

        if data:
            print('Response from {} : {!r}'.format(server, data_str))
            print('Response from {} : {!r}'.format(server, data))
    except(TimeoutError):
        print('Socket timeout')

finally:
    sock.close()