import os
import time

# os.pipe(): 2つのファイル記述子を生成し、これらはpipeでつながれている
# ファイル記述子: file descripterとも呼ばれる
#                "どのファイルとつながっているか"を示す目印となる"番号"
# 下記はos.pipe()で生成されたファイルにつながっていることを示すファイル記述子
r, w = os.pipe() # r: 読み取り専用, w: 書き込み専用
# 0 - 2のファイル記述子は決まっているため、自分で開いたファイルには3以降が割り当てられる
# 0：標準入力
# 1：標準出力
# 2：標準エラー出力
print("file descripter r: ", r)
print("file descripter w: ", w)
# プロセスを複製
pid = os.fork()

# 親プロセス -> 子プロセスへPipeを通してメッセージを送る
if pid > 0:
    # 親プロセスでは読み取りを閉じる
    os.close(r)
    # 親プロセスからのメッセージを生成
    message = "Message from parent with pid {}".format(os.getpid())
    print("Parent, sending out the message - {}".format(message))
    os.write(w, message.encode('utf-8'))
    # 現在開いているfile descriptorを取得し、表示
    print("file descriptor: ")
    with os.scandir("/proc/{}/fd/".format(os.getpid())) as it:
        for entry in it:
            if not entry.name.startswith('.'):
                print(entry.name)
    print("-----")
else:
    # 子プロセスでは書き込みを閉じる
    os.close(w)
    # 子プロセスのPIDを表示
    print("Fork is 0, this is a Child PID: ", os.getpid())
    # 読み取りファイルディスクリプタを開き、openしたファイルオブジェクトを返す
    f = os.fdopen(r)
    # パイプから読み取ったmessageを表示
    print("incoming string: ", f.read())