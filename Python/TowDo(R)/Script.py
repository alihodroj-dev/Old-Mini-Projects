# imports
import tkinter as gui
from tkinter import filedialog
from tkinter import ttk
import os

# Preparing
file = open("SongNames")
songpathnumber = 0
index = 0
songpaths = []
songnames = []
songs = []
for songpath in file.readlines():
    songpaths.append(songpath)
    songpathnumber += 1
if len(songpaths) > 1:
    for ite1 in range(1, songpathnumber):
        pathstr = ""
        patharr = []
        path = songpaths[index]
        for letter1 in path:
            patharr.append(letter1)
        for ite2 in range(0, len(path) - 1):
            pathstr += str(patharr[ite2])
        songs.append(pathstr)
        index += 1
    songs.append(songpaths[len(songpaths)-1])
elif len(songpaths) == 1:
    songs.append(songpaths[0])

# Functions
def play_music():
    pass

def stop_music():
    pass

def backwards():
    pass

def forward():
    pass

def add_song():
    pass

def delete_song():
    try:
        if len(songs) > 1:
            songstowrite = []
            cursarr = []
            for letter2 in songs_box.curselection():
                cursarr.append(letter2)
            cursstr = int(cursarr[0])
            songs_box.delete(songs_box.curselection())
            songs.remove(songs[cursstr])
            for x in range(0, len(songs) - 1):
                songstowrite.append(songs[x] + "\n")
            songstowrite.append(songs[len(songs) - 1])
            filetowriteto2 = open("SongNames", "w")
            for y in songstowrite:
                filetowriteto2.write(y)
        elif len(songs) == 1:
            songstowrite = []
            cursarr = []
            for letter2 in songs_box.curselection():
                cursarr.append(letter2)
            cursstr = int(cursarr[0])
            songs_box.delete(songs_box.curselection())
            songs.remove(songs[cursstr])
            filetowriteto2 = open("SongNames", "w")
    except:
        pass

# Variables
# main window
root_window = gui.Tk()
root_window.title("TowDo Music Player")
root_window.iconbitmap(r"App_Icon.ico")
root_window.geometry("1100x707")
root_window.configure(background="black")
root_window.resizable(False, False)

# Recommended songs pictures
first_recommended_song_pic = gui.PhotoImage(file="UI_Pictures\song_sign.png")
second_recommended_song_pic = gui.PhotoImage(file="UI_Pictures\song_sign.png")
third_recommended_song_pic = gui.PhotoImage(file="UI_Pictures\song_sign.png")

# UI Pictures
add_btn_pic = gui.PhotoImage(file=r"UI_Pictures\add.png")
delete_btn_pic = gui.PhotoImage(file=r"UI_Pictures\delete.png")
song_pic = gui.PhotoImage(file=r"UI_Pictures\mp3.png")
play_pause_btn_pic = gui.PhotoImage(file=r"UI_Pictures\play.png")
backward_btn_pic = gui.PhotoImage(file=r"UI_Pictures\backward.png")
forward_btn_pic = gui.PhotoImage(file=r"UI_Pictures\forward.png")

# LeftSideFrame
left_frame = gui.Frame(root_window)
left_frame.configure(bg="black")
left_frame.pack(side="left", fill="y")

# leftframe title
songs_label = gui.Label(left_frame, text="Songs")
songs_label.configure(fg="#00FF49", background="black", font=("Arial", 13))
songs_label.grid(row=0, column=0)

# Song ListBox
songs_box = gui.Listbox(left_frame)
songs_box.configure(height=36, width=32, background="#00FF49", borderwidth=0, font=("Arial", 11), fg="black")
songs_box.grid(row=1, column=0)
for song in songs:
    songs_box.insert(songs.index(song), song)
# Add btn
add_btn = gui.Button(left_frame, image=add_btn_pic, command=add_song)
add_btn.configure(background="black", width=130, height=30, borderwidth=0)
add_btn.grid(row=2, column=0, sticky="W")

# delete btn
delete_btn = gui.Button(left_frame, image=delete_btn_pic, command=delete_song)
delete_btn.configure(background="black", width=127, height=30, borderwidth=0)
delete_btn.grid(row=2, column=0, sticky="E")

# RightSideFrame
right_frame = gui.Frame(root_window)
right_frame.configure(bg="black")
right_frame.pack(side="top", padx=40)

# song name
song_name = gui.Label(right_frame, text="Welcome")
song_name.configure(fg="#00FF49", background="black", font="Helvetica 15")
song_name.grid(row=0, column=1, pady= 15)

# song picture
song_pic_label = gui.Label(right_frame, image=song_pic)
song_pic_label.configure(width=400, height=350, background="black")
song_pic_label.grid(row=1, column=1, padx=70)

# play_pause_btn
play_pause_btn = gui.Button(right_frame, image=play_pause_btn_pic)
play_pause_btn.configure(background="black", relief="flat", borderwidth=0)
play_pause_btn.grid(row=2, column=1, pady=5)

# backwards btn
backward_btn = gui.Button(right_frame, image=backward_btn_pic)
backward_btn.configure(background="black", relief="flat", borderwidth=0)
backward_btn.grid(row=1, column=0)

# forward btn
forward_btn = gui.Button(right_frame, image=forward_btn_pic)
forward_btn.configure(background="black", relief="flat", borderwidth=0)
forward_btn.grid(row=1, column=2)

# BottomSideFrame
bottom_frame = gui.Frame(root_window)
bottom_frame.configure(bg="#00FF49")
bottom_frame.pack(side="bottom", fill="x")

# 1st recommended song
first_recommended_song = gui.Button(bottom_frame, image=first_recommended_song_pic)
first_recommended_song.configure(width=170, height=160, borderwidth=0, bg="black")
first_recommended_song.grid(row=0, column=0, padx=60, pady=10)

# 2nd recommended song
second_recommended_song = gui.Button(bottom_frame, image=second_recommended_song_pic)
second_recommended_song.configure(width=170, height=160, borderwidth=0, bg="black")
second_recommended_song.grid(row=0, column=1, padx=40, pady=10)

# 3rd recommended song
third_recommended_song = gui.Button(bottom_frame, image=third_recommended_song_pic)
third_recommended_song.configure(width=170, height=160, borderwidth=0, bg="black")
third_recommended_song.grid(row=0, column=2, padx=60, pady=10)


# Firing
if __name__ == "__main__":
    root_window.mainloop()
