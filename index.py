
import random
import time

import variate
import speech
import spotlink

import indexHandler

name = "Thomas"

speechCount = 0
def speakText(text):
    global speechCount
    speechCount += 1
    text = variate.VaryString(text)
    lngth = speech.Speak(text, speechCount)
    return lngth

def pickRandom(data):
    lngth = len(data)
    num = random.randint(0,lngth-1)
    return data[num]

def IsDecade(string):
    try:
        asNum = int(string)
        if asNum:
            return True
        else:
            return False
    except:
        return False

index = 0
def GetOptionMsg(option):
    global index
    index += 1
    starts = ["Moving on, let's check out ", "Now, let's check out ", "Now, let's move on to "]
    if index == 1:
        starts = ["First, let's begin with ", "To start, let's begin with ","Let's begin with "]
    rests = ["something"]
    if option == "recent":
        rests = ["some songs you've been listening to lately", "some songs you've had on repeat lately", "a few songs you've listened to recently", "some of your recently played songs", "a few of your recently played songs", "some of your most played songs recently"]
    elif IsDecade(option) == True:
        rests = ["some "+option+"s classics", "a collection of songs you might know from the "+option+"s", "a few songs that were popular in the "+option+"s", "some songs that were all the rage in the "+option+"s", "some songs you might reckognise from the "+option+"s"]
    return pickRandom(starts) + pickRandom(rests)

def SetOrder(index):
    options = ["recent", #General
               "1980", "1990", "2000","2010" #Decades
               ]

    wanted = 5
    for i in range(wanted):
        if indexHandler.CheckIndex(index) == False:
            return

        option = pickRandom(options)
        dialouge = GetOptionMsg(option)
        extra = ''
        if option == 'recent':
            delay, song, artist = spotlink.PlayTop(index)
            song = variate.FixAccuracy(song)
            extra = ', starting with ' + song + ', from ' + artist
        elif IsDecade(option) == True:
            delay, song, artist = spotlink.PlayDecade(int(option),index)
            song = variate.FixAccuracy(song)
            extra = ', starting with ' + song + ', from ' + artist
        print(option)
        speekLength = speakText(dialouge + extra)
        time.sleep(delay+(speekLength-5))
        spotlink.Pause()
        
def Start():
    index = indexHandler.SetIndex()
    spotlink.Verify()
    spotlink.Pause()
    greetings = ["Hello", "Hey", "Hi"]
    greet = pickRandom(greetings)
    if random.randint(0,1) == 0:
        greet = greet + ' ' + name
    rest = "! Welcome to Radiate, your personal radio show."
    speakText(greet + rest)
    SetOrder(index)


Start()