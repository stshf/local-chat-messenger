import os
import sys
import socket
# 1. socket()はソケット（ファイルディスクリプタ）を作成します。
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# 2. connect()はリモートのソケットに接続します。
server_address = 'tmp/socket_file'

print('connecting to {}'.format(server_address))

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    # sys.exitを使うとpythonプログラムを終了させる
    # 引数1はプログラムがエラーで終了したことを示すステータスコード
    sys.exit(1)

# 3.4 send()/receive()はデータの送受信を行います。
try:
    print('Type what in your message or exit')
    input_str = input()

    sock.sendall(input_str.encode())

    # サーバからの応答に対する待機時間
    # この時間が過ぎても応答がない場合、プログラムは次のステップへ進む
    sock.settimeout(2)

    # サーバからの応答を待ち、応答があればそれを表示する
    try:
        while True:
            # サーバからのデータを受け取る
            # 受け取るデータの最大量は32byte
            data = sock.recv(32)

            data_str = data.decode('utf-8')

            # データがあれば表示し、なければループを終了
            if data:
                print('Server response: ' + data_str)
            else:
                break
    # 2秒間サーバからの応答がなければ、タイムアウトエラーとなり、エラーメッセージを表示
    except(TimeoutError):
        print('Socket timeout, ending listening for server messages')

# すべての操作が完了したらsocketを閉じる
finally: 
    print('closing socket')
    sock.close()



# 5. close()ではソケットをクローズし、ファイルディスクリプタも削除します。
sock.close()