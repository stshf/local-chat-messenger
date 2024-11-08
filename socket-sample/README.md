# Socket
双方向のデータストリーム
socketはプログラム間の通信を行うためのインターフェースとして使用される
socketは特定の"socket domain"と"socket type"によって作成され、それぞれがソケットがどのように通信を行うかを決定する

# Socket Domain（アドレスファミリー）
## AF_UNIX (AF_LOCAL)
- 同じシステム上のプロセス間通信(IPC)を提供する、つまり同じマシン上で通信が可能になる
- UNIX Domain Socket, IPC Socketと呼ばれる
- ファイルシステム上のパスを使用してアドレス指定を行う
- AF_LOCALは、POSIX準拠のシステムでAF_UNIXの別名として使用される

## AF_INET
- インターネットプロトコルバージョン4(IPv4)を使用して、異なるコンピュータシステム上のプロセス間で通信を行う
- Network Socket とも呼ばれる
- IPアドレスとポート番号の組み合わせでアドレス指定を行う

## AF_INET6
- IPv6を使用して、異なるコンピュータシステム上のプロセス間で通信を行う
- より大きなアドレス空間と追加機能を提供
- IPv4との後方互換性も提供

# プロトコル（トランスポート層）
トランスポート層プロトコルは、異なるデバイス間でのデータ転送をどのように行うかを定義する一連のルールと手順

## TCP (Transmission Control Protocol)
- 信頼性の高いデータ転送を提供
- コネクション型（接続確立が必要）
- 順序保証
- フロー制御とエラー検出/訂正
- データの完全性が重要なアプリケーションに適している
  - 銀行アプリケーション
  - EC
  - ファイル転送
  - Webブラウジング（HTTP/HTTPS）

## UDP (User Datagram Protocol)
- 高速な通信を提供
- コネクションレス型（事前の接続確立不要）
- 順序保証なし
- 配信保証なし
- オーバーヘッドが少ない
- リアルタイムアプリケーションに適している
  - ビデオ会議
  - Online game
  - DNS
  - ストリーミング

# Socket Type
アプリケーションが通信する方法を決定する

## SOCK_STREAM
- TCPに対応
- TCPプロトコルを使用して、信頼性の高い、順序通りの、エラーのないバイトストリームの伝送を提供する
- 双方向の接続型通信
- バイトストリームベース（メッセージ境界なし）

## SOCK_DGRAM
- UDPに対応
- UDPプロトコルを使用して、データグラム(独立したパケット)の送受信を提供する
- 順序が入れ替わったり、重複する可能性もある
- メッセージ境界が保持される
- 最大メッセージサイズの制限がある

# その他のSocket Type
## SOCK_RAW
- 生のIPパケットへの直接アクセスを提供
- カスタムプロトコルの実装やネットワーク監視に使用

## SOCK_SEQPACKET
- SOCK_STREAMに似ているが、メッセージ境界を保持
- 信頼性のある順序付きパケット通信を提供

# 実装内容
ローカルシステムで動作するsimpleなチャットメッセンジャー
UNIX Domain Socketを介して、同じマシン上で動作するserverとclientを実装

## サーバサイドのフロー

1. socket()はソケット（ファイルディスクリプタ）を作成します。
2. bind()はソケットをローカルのアドレス（ソケットファイルやIP+ポート）にバインドします。
3. listen()はソケットに接続を待ち受けるように命令します。
4. accept()は外部からの接続に対して新しいソケットを作成します。
5.6 send()/receive()はデータの送受信を行います。
7 close()ではソケットをクローズし、ファイルディスクリプタも削除します。

## クライアントサイドのフロー

1. socket()はソケット（ファイルディスクリプタ）を作成します。
2. connect()はリモートのソケットに接続します。
3.4 send()/receive()はデータの送受信を行います。
5. close()ではソケットをクローズし、ファイルディスクリプタも削除します。