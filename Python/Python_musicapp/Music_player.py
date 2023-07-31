from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer
import os

#Application GUI
root=Tk()
root.title("MusicMuserAI")
root.geometry("1080x1920")
root.configure(bg="green")
root.resizable
mixer.init()

#Functions for playing and adding music
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

    #Icon & logo
    Icon_Image = PhotoImage(file="logo.png")
    root.iconphoto(False, Icon_Image= PhotoImage(file="logo.png"))

    Top_Image = PhotoImage(file="top.png")
    Label(root, image=Top_Image, bg="green").pack()

    #Logo
    Logo_Image = PhotoImage(file="logo.png")
    Label(root, image=Logo_Image, bg="green").place(x=65, y=115)

    #Button creation
    Button_Play = PhotoImage(file="play.png")
    Button(root, image=Button_Play, bg="green", bd=0, command=play_music).place(x=100,y=400)

    Button_Stop = PhotoImage(file="stop.png")
    Button(root, image=Button_Stop, bg="green", bd=0, command=mixer.music.stop).place(x=30,y=500)

    Button_Resume = PhotoImage(file="resume.png")
    Button(root, image=Button_Resume, bg="green", bd=0, command=mixer.music.unpause).place(x=115,y=500)

    Button_Pause = PhotoImage(file="pause.png")
    Button(root, image=Button_Pause, bg="green", bd=0, command=mixer.music.pause).place(x=200,y=500)

    #Music
    