import socket
import os

# UNIX SocketをDGRAMモード(UDP)で作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

# serverが接続を待つUNIX SocketのPathを設定
server_address = 'tmp/udp_socket_file'

# 以前の接続が残っていた場合、サーバアドレスをunlink(削除)する
try:
    os.unlink(server_address)
# サーバアドレスが存在しない場合、例外を無視
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))

# server addressにsocketをbind
sock.bind(server_address)

# UDPソケットサーバーはデータの受信を永遠に待ち続ける
while True:
    # サーバが新しいデータを待ち続けるループ
    while True:
        # データを接続から読み込む
        # 最大4096byte
        data, client_address = sock.recvfrom(4096)

        # dataはbinary形式なので、文字列に変換
        data_str = data.decode('utf-8')

        print('Received {} bytes from {} '.format(len(data), client_address))
        print(data_str)

        # もしデータがあれば受け取ったメッセージを送り返す
        if data:
            # 受け取ったメッセージを処理
            response = 'Processing: ' + data_str

            # 処理したメッセージをクライアントに送り返す
            # メッセージを文字列→binaryに変換して送る
            sock.sendto(response.encode(), client_address)