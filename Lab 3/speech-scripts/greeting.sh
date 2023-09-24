#!/bin/sh
echo 'Hello, Zack. My name is Piper.' | piper \
  --model en_US-lessac-medium \
  --output_file greeting.wav
