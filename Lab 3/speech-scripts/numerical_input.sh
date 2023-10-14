echo 'What is your social security number? Dont worry! I wont tell anyone. Hehe' | piper \
  --model en_US-lessac-medium \
  --output_file output.wav
aplay output.wav
python microphone_complete_results.py -m en
