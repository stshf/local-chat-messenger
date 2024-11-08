import socket
import os
from faker import Faker

# response用にfaker objectを生成
fake_en = Faker(['en-US'])
fake_jp = Faker(['ja-JP'])

def generate_response(request):
    if not isinstance(request, int):
        return "Invalid request type. Expected an integer."

    match request:
        case 0:
            return generate_fake_jp_person()
        case 1:
            return generate_random_color()
        case 2:
            return generate_random_emoji()
        case _:
            return "Invalid request value. Expected 0, 1, or 2."

def generate_fake_jp_person():
    return f"""
    name        : {fake_jp.name()}
    address     : {fake_jp.address()}
    company     : {fake_jp.company()}
    email       : {fake_jp.email()}
    phone number: {fake_jp.phone_number()}
    """

def generate_fake_en_person():
    return fake_en.profile()

def generate_random_color():
    return fake_en.color()

def generate_random_emoji():
    return fake_en.emoji()

def create_socket():
    return socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

def bind_server(sock, server_address):
    # 以前の接続が残っていた場合、server addressをunlink(削除)する
    try:
        os.unlink(server_address)
    # server addressが存在しない場合、例外を無視
    except FileNotFoundError:
        pass

    # socketをserver addressにbind(接続)
    sock.bind(server_address)

def handle_client_connection(connection):
    try:
        print('Connection accepted')

        # serverが新しいデータを待ち続けるためのループ
        while True:
            # serverは接続からデータを読み込む
            data = connection.recv(16)
            
            if not data:
                # clientからのデータがなければ、ループを終了
                print('No data from client')
                break

            # 受け取ったデータはbinary形式なので文字列に変換
            data_str = data.decode('utf-8')
            print('Received: {}'.format(data_str))

            try:
                request = int(data_str)
                response = generate_response(request)
            except ValueError:
                response = "Invalid request format. Expected an integer."

            # responseを表示
            print('Sending response: {}'.format(response))

            # responseをbinary形式にして、clientへ返信
            connection.sendall(response.encode('utf-8'))

            # データ送信後に接続を閉じる
            break

    except Exception as e:
        print(f'Error handling client connection: {e}')
    finally:
        print('Closing current connection')
        connection.close()

def main():
    # サーバーが接続を待つUNIX SocketのPathを設定
    server_address = 'socket_file'

    sock = create_socket()
    bind_server(sock, server_address)
    print('Starting up on {}'.format(server_address))
    # socketが接続要求を待機するようにする
    sock.listen()

    # 無限ループでclientからの応答を待つ
    while True:
        # clientからの接続を受け入れる
        connection, _ = sock.accept()
        handle_client_connection(connection)

if __name__ == "__main__":
    main()