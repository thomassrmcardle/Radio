import gtts
import os
from gtts import gTTS
import time

import mutagen
from mutagen import mp3

def Speak(Text, index):
    directory = "speech" + str(index) + '.mp3'
    tts = gTTS(Text, lang='en', tld='co.uk')
    tts.save(directory)
    os.system("start " + directory)

    audio = mp3.MP3(directory)
    lngth = audio.info.length
    time.sleep(lngth)
    return lngth
