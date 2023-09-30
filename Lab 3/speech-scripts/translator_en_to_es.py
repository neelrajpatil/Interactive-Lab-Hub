import wave
from vosk import Model, KaldiRecognizer
from translate import Translator
import json
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

# Function to record audio using a microphone library (e.g., PyAudio)
def record_audio(driver, output_file_path, duration, lang):

    stream = driver.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
    )

    frames = []
    print("You will have 8 seconds to record a single phrase to be translated.")
    print(f"You must speak continuously in {lang}. You may begin after the beep.")

    for _ in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()

    with wave.open(output_file_path, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(driver.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(frames))

# Function to play audio using a library like pygame
def play_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    play(audio)

def recognize_speech(rec, audio_file_path):
    wf = wave.open(audio_file_path, "rb")

    results = []

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result["text"]
            results.append(text)

    result = json.loads(rec.FinalResult())
    text = result["text"]
    results.append(text)

    return " ".join(results)

def text_to_speech(text, output_file, lang):
    tts = gTTS(text=text, lang=lang)  # Specify the language (e.g., "es" for Spanish)
    tts.save(output_file)

def main():
    translator_en = Translator(to_lang="es")
    translator_es = Translator(to_lang="en", from_lang="es")
    audio_driver = pyaudio.PyAudio()
    model_en = Model(lang="en-us")
    rec_en = KaldiRecognizer(model_en, RATE)
    model_es = Model(lang="es")
    rec_es = KaldiRecognizer(model_es, RATE)

    en_audio_file = "english.wav"
    es_audio_file = "spanish.wav"

    while True:

        play_audio("beep.wav")
        record_audio(audio_driver, en_audio_file, 8, "English")
        play_audio("beep.wav")

        recognized_text_en = recognize_speech(rec_en, en_audio_file)
        print("Recognized text:", recognized_text_en)

        translated_text_en = translator_en.translate(recognized_text_en)
        print("Translated text:", translated_text_en)

        text_to_speech(translated_text_en, es_audio_file, "es")
        play_audio(es_audio_file)

        play_audio("beep.wav")
        record_audio(audio_driver, es_audio_file, 8, "Spanish")
        play_audio("beep.wav")

        recognized_text_es = recognize_speech(rec_es, es_audio_file)
        print("Recognized text:", recognized_text_es)

        translated_text_es = translator_es.translate(recognized_text_es)
        print("Translated text:", translated_text_es)

        text_to_speech(translated_text_es, en_audio_file, "en-us")
        play_audio(en_audio_file)

if __name__ == "__main__":
    main()
