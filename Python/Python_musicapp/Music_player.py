from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer
import os

root=Tk()
root.title("MusicMuserAI")
root.geometry("1080x1920")
root.configure(bg="green")
root.resizable
mixer.init()

def add_music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdire(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)


def play_music():
    Music_Name= Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()