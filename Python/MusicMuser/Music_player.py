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
prev_reduce = Button_prev.subsample(5)
Button(root, image=prev_reduce, bg="#545454", bd=0, command=mixer.music.queue).place(x=10,y=200)

Button_next = PhotoImage(file=os.path.join(os.getcwd(),"Next.png"))
next_reduce = Button_next.subsample(5)
Button(root, image=next_reduce, bg="#545454", bd=0, command=mixer.music.unpause).place(x=250,y=200)

Button_Resume = PhotoImage(file=os.path.join(os.getcwd(),"Play.png"))
play_reduce = Button_Resume.subsample(5)
Button(root, image=play_reduce, bg="#545454", bd=0, command=play_music).place(x=165,y=200)

Button_Pause = PhotoImage(file=os.path.join(os.getcwd(),"Pause.png"))
pause_reduce = Button_Pause.subsample(5)
Button(root, image=pause_reduce, bg="#545454", bd=0, command=mixer.music.pause).place(x=90,y=200)

#Music
Frame_Music = Frame(root, bd=2 ,relief=RIDGE,bg="#83fe9a")
Frame_Music.place(x=350,y=20,width=270,height=450)

Button(root,text="Add Music",width=15,height=2,font=("sans-serif",12,"bold"),fg="black",bg="#83fe9a",command=add_music).place(x=180,y=300)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music,width=100,font=("times new roman",10),bg="#83fe9a",fg="#545454",selectbackground="#545454",cursor="hand2",bd=0,yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT,fill=Y)
Playlist.pack(side=LEFT,fill=BOTH)

root.mainloop()