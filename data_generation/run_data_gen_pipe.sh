#!/bin/bash
set -e

sudo -v

echo "Running the Data Generation pipeline"

python3 target.py > target_logs.txt 2>&1 &
TARGET_PID=$!

echo "Target launched with PID: $TARGET_PID"

sudo python3 hook_network_info.py --pid "$TARGET_PID"
