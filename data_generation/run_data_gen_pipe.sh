#!/bin/bash
set -e
sudo -v

echo "Running the Data Generation pipeline"
python3 gen_connection.py --num-conn 1000 > ./data/target_logs.txt 2>&1 &

TARGET_PID=$!
echo "Target launched with PID: $TARGET_PID"

sudo python3 hook_network.py --pid "$TARGET_PID"
