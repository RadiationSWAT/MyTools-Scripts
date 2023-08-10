from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer
import os

#Application GUI
root=Tk()
root.title("MuserMusic")
root.geometry("640x480")
root.configure(bg="#545454")
root.resizable(False,False)
mixer.init()

#Functions for playing and adding music
def add_music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)


def play_music():
    Music_Name= Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

os.chdir("C:\\Users\\radia\\Documents\\MyTools-Scripts\\Python\\MusicMuser\\Icons")

#Icon
icon_image = PhotoImage(file=os.path.join(os.getcwd(), "MuserMusicwithoutfont.png"))
root.iconphoto(False, icon_image)

#Logo
Logo_Image = PhotoImage(file=os.path.join(os.getcwd(), "MuserMusicwithfont.png"))
Logo_reduce = Logo_Image.subsample(2)
Label(root, image=Logo_reduce,bg="#545454").place(x=-60, y=-60)

#Button creation
Button_prev = PhotoImage(file=os.path.join(os.getcwd(),"Previous.png"))
prev_reduce = Button_prev.subsample(4)
Button(root, image=prev_reduce, bg="#545454", bd=0, command=play_music).place(x=10,y=200)

#Button_next = PhotoImage(file=os.path.join(os.getcwd(),"Next.png"))
#Button(root, image=Button_next, bg="#0f1a2b", bd=0, command=mixer.music.stop).place(x=30,y=500)

#Button_Resume = PhotoImage(file=os.path.join(os.getcwd(),"Play.png"))
#Button(root, image=Button_Resume, bg="#0f1a2b", bd=0, command=mixer.music.unpause).place(x=115,y=500)

#Button_Pause = PhotoImage(file=os.path.join(os.getcwd(),"Pause.png"))
#Button(root, image=Button_Pause, bg="#0f1a2b", bd=0, command=mixer.music.pause).place(x=200,y=500)

#Music
#Frame_Music = Frame(root, bd=2 ,relief=RIDGE)
#Frame_Music.place(x=330,y=350,width=560,height=250)

#Button(root,text="Add Music",width=15,height=2,font=("times new roman",12,"bold"),fg="black",bg="#21b3de",command=add_music).place(x=330,y=300)

#Scroll = Scrollbar(Frame_Music)
#Playlist = Listbox(Frame_Music,width=100,font=("times new roman",10),bg="#333333",fg="grey",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=Scroll.set)
#Scroll.config(command=Playlist.yview)
#Scroll.pack(side=RIGHT,fill=Y)
#Playlist.pack(side=LEFT,fill=BOTH)

root.mainloop()