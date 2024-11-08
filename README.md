# Local Chat Messenger

Local Chat Messengerは、シンプルなクライアント-サーバーアプリケーションで、Pythonを使用してローカル環境で動作します。
サーバーはFakerライブラリを使用してランダムなデータを生成し、クライアントはそのデータをリクエストして表示します。

## 使用方法

### 前提条件
- Python 3.x のインストール
- Faker パッケージのインストール
  ```bash
  pip install faker
  ```

### 仮想環境の構築
本プロジェクトではvenvを使用して、pythonの仮想環境を構築しております。
参考までに手順を記載します
1. 仮想環境の作成
    ```bash
    python3 -m venv venv
    ```
2. 仮想環境のアクティベート
- windows:
    ```bash
    source venv/bin/activate
    ```
3. 必要なパッケージをインストール
    ```bash
    pip install faker
    ```
4. 終了時
    ```bash
    deactivate
    ```

### 実行

#### サーバーの起動
まず、サーバーを起動します。
```bash
python3 server.py
```

#### クライアントの起動
次に、クライアントを起動します。
```bash
python3 client.py
```

### Client側でのCLI入出力

#### 例1:
入力
```
0
```
出力
```
 Response from server: 
    name        : 佐藤 美加子
    address     : 山形県横浜市磯子区独鈷沢34丁目24番9号 竜泉コート428
    company     : 高橋農林株式会社
    email       : mituru24@example.net
    phone number: 04-9089-8604
```

#### 例2:
入力
```
1
```
出力 (terminalでは#colorhex色付きで出力される)
```
 Response from server: #e28c96
```

#### 例3:
入力
```
2
```
出力
```
 Response from server: 🎢
```

#### 例4:
入力
```
other string
```
出力
```
 Response from server: Invalid request format. Expected an integer.
```

## プロジェクトの背景
本プロジェクトは、[Recursion](https://recursionist.io/dashboard/course/31/lesson/1099)のソケットプログラミングの学習の一環で作成しております。