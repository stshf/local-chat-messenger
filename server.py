import socket
import os
from faker import Faker

# response用にfaker objectを生成
fake_en = Faker(['en-US'])
fake_jp = Faker(['ja-JP'])

def generateResponse(request):
    if not isinstance(request, int):
        return "Invalid request type. Expected an integer."

    match request:
        case 0:
            return generateFakeJPPerson()
        case 1:
            return generateRandomColor()
        case 2:
            return generateRandomEmoji()
        case _:
            return "Invalid request value. Expected 0, 1, or 2."

def generateFakeJPPerson():
    return f"""
    name        : {fake_jp.name()}
    address     : {fake_jp.address()}
    company     : {fake_jp.company()}
    email       : {fake_jp.email()}
    phone number: {fake_jp.phone_number()}
    """

def generateFakeENPerson():
    return fake_en.profile()

def generateRandomColor():
    return fake_en.color()

def generateRandomEmoji():
    return fake_en.emoji()

# UNIX Socketをstreamモード(TCP)で作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# サーバーが接続を待つUNIX SocketのPathを設定
server_address = 'socket_file'

# 以前の接続が残っていた場合、server addressをunlink(削除)する
try:
    os.unlink(server_address)
# server addressが存在しない場合、例外を無視
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))

# socketをserver addressにbind(接続)
sock.bind(server_address)

# socketが接続要求を待機するようにする
sock.listen()

# 無限ループでclientからの応答を待つ
while True:
    # clientからの接続を受け入れる
    connection, client_address = sock.accept()

    try:
        print('Connection from {}'.format(client_address))

        # serverが新しいデータを待ち続けるためのループ
        while True:
            # serverは接続からデータを読み込む
            data = connection.recv(16)

            # 受け取ったデータはbinary形式なので文字列に変換
            data_str = data.decode('utf-8')

            # 受け取ったデータを表示
            print('Received: {}'.format(data_str))

            # もしデータがあれば以下の処理を行う
            if data:
                try:
                    request = int(data_str)
                except ValueError:
                    response = "Invalid request format. Expected an integer."
                else:
                    # 受け取ったメッセージを処理
                    response = generateResponse(request)

                # responseを表示
                print('Sending response: {}'.format(response))

                # responseをbinary形式にして、clientへ返信
                connection.sendall(response.encode('utf-8'))

                # データ送信後に接続を閉じる
                break
            else:
                # clientからのデータがなければ、ループを終了
                print('no data from {}'.format(client_address))
                break
    finally:
        print('Closing current connection')
        connection.close()

