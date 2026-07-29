from gtts import gTTS
from playsound import playsound
import os

def text_to_speech(text):
    filename = "response.mp3"

    tts = gTTS(text=text, lang="en")
    tts.save(filename)

    playsound(filename)

    if os.path.exists(filename):
        os.remove(filename)