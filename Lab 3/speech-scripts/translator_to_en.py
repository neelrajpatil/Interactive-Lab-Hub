import sys
from translate import Translator

input_text = sys.stdin.read().strip()

translator = Translator(to_lang="en", from_lang="es")
translation = translator.translate(input_text)

print(translation)
