#!/bin/sh

if [[ ! -f pre_translate_en.wav ]]; then
    echo 'You will have 8 seconds to record a single phrase to be translated. You must speak continuously in English. You may begin after the beep.' | piper \
    --model en_US-lessac-medium \
    --output_file pre_translate_en.wav
fi
aplay pre_translate_en.wav
aplay beep.wav
timeout 8s python -u microphone_complete_results.py -m en 2>/dev/null > to_translate.txt
aplay beep.wav
cat to_translate.txt | python translator_to_es.py | piper \
  --model es_ES-davefx-medium.onnx \
  --output_file translated_toes.wav

aplay translated_toes.wav