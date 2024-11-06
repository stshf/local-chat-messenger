#!/bin/bash

function cleanup() {
    echo "Stop client..."
    exit 0
}

trap cleanup EXIT SIGINT SIGTERM


echo "Start client..."

while [ ! -p myfifo ]; do
    echo "Waiting for FIFO..."
    sleep 2
done

while read line < myfifo; do
    echo "Received: $line"
    sleep 2
done

