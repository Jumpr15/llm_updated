#!/bin/bash
set -e

sudo apt update
sudo apt install tmux

uv sync
uv add liger-kernel

cd src

uv run train.py

