#!/bin/bash

# end flag
running=true

function cleanup() {
    echo "End server..."
    echo "Delete fifo"
    rm myfifo
    running=false
}

# よく使用されるシグナル
# EXIT   - スクリプトが終了する時（正常終了も異常終了も）
# SIGINT - Ctrl+Cが押された時（割り込み）
# SIGTERM - killコマンドでプロセスを終了する時
trap cleanup SIGINT SIGTERM

if [ ! -e myfifo ]; then
    mkfifo  myfifo
fi

while $running; do
    echo "Current time: $(date)" > myfifo
    sleep 2
done

