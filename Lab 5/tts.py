from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def text_to_speech(text, output_file, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save(output_file)
    return output_file

def play_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    play(audio)

def say_hello_world():
    output_file = 'hello_world.mp3'  # Output file name
    hello_text = "Hello world"  # The text you want to convert to speech
    lang = 'en'  # Language code for English

    # Convert text to speech and save the audio file
    text_to_speech(hello_text, output_file, lang)

    # Play the audio file
    play_audio(output_file)

if __name__ == "__main__":
    say_hello_world()
