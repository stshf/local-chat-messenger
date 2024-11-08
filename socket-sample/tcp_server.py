import socket
import os

# UNIX Socketをstreamモード(TCP)で作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# サーバーが接続を待つUNIX SocketのPathを設定
server_address = 'tmp/socket_file'

# 以前の接続が残っていた場合、サーバアドレスをunlink(削除)する
try:
    os.unlink(server_address) # os.remove()と同じ
# サーバアドレスが存在しない場合、例外を無視
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))

# サーバアドレスにソケットをBind(接続)
sock.bind(server_address)

# socketが接続要求を待機するようにする
sock.listen()

# 無限ループでクライアントからの接続を待つ
while True:
    # クライアントからの接続を受け入れる
    # return
    #   conn   :接続を通じてデータの送受信を行うための 新しい ソケットオブジェクト
    #   adresss:接続先でソケットにbindしているアドレス
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # サーバが新しいデータを待ち続けるためのループ
        while True:
            # サーバは接続からデータを読み込む
            # 16は一度に読み込むデータの最大バイト数
            data = connection.recv(16)

            # 受け取ったデータはbinary形式なので、文字列に変換
            data_str = data.decode('utf-8')

            # 受け取ったデータを表示
            print('Received: ' + data_str)

            # もしデータがあれば以下の処理を行う
            if data:
                # 受け取ったメッセージを処理
                response = 'Processing: ' + data_str

                # 処理したメッセージをクライアントに送り返す
                # メッセージをbinary形式(encode)に戻してから送信
                connection.sendall(response.encode())
            else:
                # clientからデータが送られてこなければ、ループを終了
                print('no data from ', client_address)
                break
    
    # 最終的に接続を閉じる
    finally:
        print('Closing current connection')
        connection.close()