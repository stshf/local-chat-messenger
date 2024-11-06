# pipeの留意点
プロセスごとにfile descriptor tableは独立しており、同じ数字のfdでも異なるリソースを指している可能性がある

例: fd=3はプロセス1とプロセス2で異なるファイルを指している
- プロセス1 (PID:1234)
```bash
$ ls -l /proc/1234/fd
```
0 -> /dev/pts/0  # stdin
1 -> /dev/pts/0  # stdout
2 -> /dev/pts/0  # stderr
3 -> /path/to/fileA  # プロセス1が開いたファイル

- プロセス2 (PID:1235)
```bash
$ ls -l /proc/1235/fd
```
0 -> /dev/pts/1  # 別の端末のstdin
1 -> /dev/pts/1  # 別の端末のstdout
2 -> /dev/pts/1  # 別の端末のstderr
3 -> /path/to/fileB  # プロセス2が開いた別のファイル

# パイプを共有するための方法
- 1. fork()で子プロセスを作る(この場合、親のfd tableが子にコピーされる)
- 2. 名前付きパイプを使う
- 3. UNIXドメインソケットを使う

# 2. 名前付きパイプ(named pipe)を取り扱う
named pipe: 特定のパス名を持つpipe. UNIX系OSではFIFOといわれ、ファイルの一種であり、ファイルのように操作をすることが可能
同一システム上で動作している任意のプロセス間でデータのやり取りが可能となる
名前付きパイプは永続的で、プロセスが消滅しても存在し続けるので、使わなくなったら削除する必要がある

# ファイル説明
- *.py
    - pythonのosモジュールでnamed pipe(fifo)を扱う
- config.json
    - *.pyからpipeのfilepathをjson形式で読み込む用に作成
- *.sh
    - bashコマンドでnamed pipe(fifo)を扱う

# 使用方法
- *.py
    別々のターミナルで実行
    ```bash
    python3 client.py
    ```
    ```bash
    python3 server.py
    ```
- *.sh
    別々のターミナルで実行
    ```bash
    ./client.sh
    ```
    ```bash
    ./server.sh
    ```


