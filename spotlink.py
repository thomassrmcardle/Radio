import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import random
import subprocess

import speech
import indexHandler

sp = 0
def Verify():
    global sp
    scope = "playlist-read-private user-library-read user-modify-playback-state user-read-playback-state user-top-read playlist-read-collaborative"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,client_id='7a25aca7e2cf40b098fc32032f65f4ad',client_secret='087f65cd665e49ebbd30fd24043896fd',redirect_uri='http://localhost:8888/callback'))

def Play(Id):
    Verify()
    devices = sp.devices()
    for device in devices['devices']:
        sp.start_playback(uris=[Id],device_id=device['id'])
        break

def Pause():
    try:
        Verify()
        devices = sp.devices()
        if devices and len(devices['devices']) > 0:
            sp.pause_playback()
    except:
        print("Not listening")

def TopTracks(offset,index):
    Verify()
    top_tracks = sp.current_user_top_tracks(time_range='short_term', limit=5, offset=offset)
    time.sleep(5)
    for idx, track in enumerate(top_tracks['items']):
        if indexHandler.CheckIndex(index) == False:
            return
        track_id = track['id']
        duration = sp.track(track_id)['duration_ms']/1000
        Play('spotify:track:'+track_id)
        time.sleep(duration)

def PlayTop(index):
    offset = random.randint(0,5)
    top_tracks = sp.current_user_top_tracks(time_range='short_term', limit=5, offset=offset)
    total = 0
    firstSong = ''
    firstArtist = ''

    for idx, track in enumerate(top_tracks['items']):
        firstSong = track['name']
        firstArtist = track["artists"][0]['name']
        break

    for idx, track in enumerate(top_tracks['items']):
        track_id = track['id']
        duration = sp.track(track_id)['duration_ms']/1000
        total += duration

    subprocess.Popen(['python', '-c', 'import spotlink; spotlink.TopTracks(' + str(offset) + ', "' + str(index) + '")'])
    return total, firstSong, firstArtist


def TopDecade(Offset, Start,index):
    Verify()
    results = sp.search(q="year:" + str(Start) + "-" + str(Start+9), type="track", limit=5, offset=Offset)
    tracks = results['tracks']['items']
    time.sleep(5)

    for i, track in enumerate(tracks):
        if indexHandler.CheckIndex(index) == False:
            return
        track_id = track['id']
        duration = sp.track(track_id)['duration_ms']/1000
        Play('spotify:track:'+track_id)
        time.sleep(duration)

def PlayDecade(Start,index):
    offset = random.randint(0,10)
    results = sp.search(q="year:" + str(Start) + "-" + str(Start+9), type="track", limit=5, offset=offset)
    tracks = results['tracks']['items']

    total = 0
    firstSong = ''
    firstArtist = ''

    for i, track in enumerate(tracks):
        firstSong = track['name']
        firstArtist = track['artists'][0]['name']
        break

    for i, track in enumerate(tracks):
        track_id = track['id']
        duration = sp.track(track_id)['duration_ms']/1000
        total += duration

    subprocess.Popen(['python', '-c', 'import spotlink; spotlink.TopDecade(' + str(offset) + ', ' + str(Start) + ', "' + str(index) + '")'])
    return total, firstSong, firstArtist