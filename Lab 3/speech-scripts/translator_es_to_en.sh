#!/bin/sh
sleep 2
if [[ ! -f pre_translate_es.wav ]]; then
  echo 'Vas a tener 8 segundos para grabar una respuesta que será traducida al inglés. Tienes que hablar continuamente en español. Empieza después del tono.' | piper \
  --model es_ES-davefx-medium.onnx \
  --output_file pre_translate_es.wav
fi
aplay pre_translate_es.wav
aplay beep.wav
timeout 8s python -u microphone_complete_results.py -m es 2>/dev/null > to_translate.txt
aplay beep.wav
cat to_translate.txt | python translator_to_en.py | piper \
  --model en_US-lessac-medium \
  --output_file translated_toen.wav

aplay translated_toen.wav