import gtts
import os
from gtts import gTTS
import time

import mutagen
from mutagen import mp3

import fileManager

def Speak(Text, index):
    baseDirectory = fileManager.GetBaseDirectory("audio_cache/speech")
    # Ensure the directory exists before writing the readme file
    os.makedirs(baseDirectory, exist_ok=True)
    
    directory = fileManager.formatPath(baseDirectory + "/speech" + str(index) + '.mp3')
    tts = gTTS(Text, lang='en', tld='co.uk')
    tts.save(directory)
    os.system("start " + directory)

    try:
        audio = mp3.MP3(directory)
        lngth = audio.info.length
    except Exception as e:
        print(f"Error reading audio file: {e}")
        lngth = 0
    
    time.sleep(lngth)
    return lngth
