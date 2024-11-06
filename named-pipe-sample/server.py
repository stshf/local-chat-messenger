import os
import json

config = json.load(open('config.json'))

# すでに同じ名前のパイプが存在する場合はそれを削除
if os.path.exists(config['filepath']):
    os.remove(config['filepath'])

# os.mkfifo: 指定したパスに名前付きパイプを作成
# 0o600: permition mode, 読み書き可能
os.mkfifo(config['filepath'], 0o600)

print("FIFO named '%s' is created successfully." % config['filepath'])

# ユーザーからの入力を取得し、名前付きパイプに書き込む
# 'exit'が入力されるまでこの操作を繰り返す
flag = True

while flag:
    print("Type in what you would like to send to clients  or exit")
    inputstr = input()

    if (inputstr == 'exit'):
        flag = False
    else:
        # 'with'文のコンテキスト内では、ファイルは自動的にクローズされる
        with open(config['filepath'], 'w') as f:
            f.write(inputstr)

# programの終了時に名前付きパイプを削除
os.remove(config['filepath'])