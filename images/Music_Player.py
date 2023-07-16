from ast import Lambda
from asyncio import current_task
from asyncore import loop
from re import A
import tkinter
from tkinter import *
from tkinter import ttk
#from tkinter import _Relief
from PIL import Image, ImageTk  # import image
import os  # song path name
import time
from mutagen.mp3 import MP3   # get music length
import tkinter.ttk as ttk
import tkinter.messagebox  # messagebox
from tkinter import filedialog
from matplotlib.pyplot import text
from pygame import mixer
import pygame  # music mixer
import time

mixer.init()


class musicplayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock's Music player")
        # self.root.iconbitmap("icon.ico")
        self.root.maxsize(width=900, height=640)
        self.root.minsize(width=900, height=640)
        self.root.configure(background="white")

        # adding label
        self.fieldlabel = Label(
            text="Let's Select And Play", bg="black", fg="white", font=22, width=50)
        self.fieldlabel.place(x=20, y=11)

        def songinfo():
            self.fieldlabel['text'] = "Current Music :- " + \
                os.path.basename(filename)

        # adding rightside_image
        self.R_photo = ImageTk.PhotoImage(file="D:\python\MUSIC_PLAYER\Music Player\images\music3.jpg")
        self.Photo = Label(self.root, image=self.R_photo, bg="white", width=500).place(
            x=420, y=40, width=610, height=400)

        # #adding image
        # self.photo = ImageTk.PhotoImage(file="musicwp.jpg")
        # self.Photo = Label(self.root,image=self.photo,bg="white").place(x=20 , y=45,width=553)

        self.song_box = Listbox(root, bg="black", fg="green", font=22,selectbackground="white", selectforeground="black")
        self.song_box.place(x=20, y=51, width=557,  height=390)

        # label
        self.label1 = Label(self.root, text="Let's Play It!!",bg="black", fg="white", font=22)

        self.label1.pack(side=BOTTOM, fill=X)

        # openfile function

        def openfile():
            global filename
            filename = filedialog.askopenfilename(
                initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))

            # strip out the directory info and .mp3 extention from the song name
            #song = filename
            filename = filename.replace("D:/songs/", "")
            filename = filename.replace(".mp3", "")

            # add song to list box
            self.song_box.insert(END, filename)

        # add many song to play list:
        def add_many_songs():
            global filename
            filenames = filedialog.askopenfilenames(
                initialdir='audio/', title="Choose Multiple Songs", filetypes=(("mp3 Files", "*.mp3"), ))
            # print("hello")

            # loop through song list and replace directory info and mp3for
            for filename in filenames:
                filename = filename.replace("D:/songs/", "")
                filename = filename.replace(".mp3", "")
                self.song_box.insert(END, filename)

           # print("bye")

        # Menu
        self.menubar = Menu(self.root)
        self.root.configure(menu=self.menubar)

        self.submenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Add Song", menu=self.submenu)
        self.submenu.add_command(label="Open Single song", command=openfile)
        self.submenu.add_command(
            label="Open Many Songs", command=add_many_songs)
        self.submenu.add_command(label="Exit", command=self.root.destroy)

        # about function

        def about():
            tkinter.messagebox.showinfo(
                "About us", "Music Player Is Created By Neel Patel")

        self.submenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.submenu)
        self.submenu.add_command(label="About", command=about)

        # song time info
        def play_time():
            global filename
            # grab current song Elapsed time
            current_time = int(pygame.mixer.music.get_pos() / 1000)

            # #check
            # self.slider_label.config(text=f'Slider : {int(self.my_slider.get())} and Song position : {int(current_time)}')

            # converted to time format
            converted_current_time = time.strftime(
                '%M:%S', time.gmtime(current_time))

            # get the currently playing song
            current_song = self.song_box.curselection()
            # #collect song from playlist
            filename = self.song_box.get(current_song)
            # #add directory structure and mp3 to song title
            filename = f"D:/songs/{filename}.mp3"

            # get length with mutagen
            song_mut = MP3(filename)

            # get song length
            global song_length
            song_length = song_mut.info.length

            # converted to time format
            converted_song_length = time.strftime(
                '%M:%S', time.gmtime(song_length))

            # increase current time by one second
            current_time += 1

            if int(self.my_slider.get()) == int(song_length):
                # output time to status bar
                self.status_bar.config(
                    text=f' Time Elapsed : {converted_song_length} ')
            elif paused:
                pass
            elif int(self.my_slider.get()) == int(current_time):
                # slider hasn't been moved
                # Update Slider to current possition
                self.slider_position = int(song_length)
                self.my_slider.config(
                    to=self.slider_position, value=int(current_time))
            else:
                # slider has been moved!!
                # Update Slider to current possition
                self.slider_position = int(song_length)
                self.my_slider.config(
                    to=self.slider_position, value=int(self.my_slider.get()))

                # converted to time format
                converted_current_time = time.strftime(
                    '%M:%S', time.gmtime(int(self.my_slider.get())))

                # output time to status bar
                self.status_bar.config(
                    text=f' Time Elapsed : {converted_current_time}  of  {converted_song_length}  ')

                # Move this things along by one second
                self.next_time = int(self.my_slider.get()) + 1
                self.my_slider.config(value=self.next_time)

            # # output time to status bar
            # self.status_bar.config(
            #     text=f' Time Elapsed.  {converted_current_time}  of  {converted_song_length}  ')

            # update slider position value to current song position
            # self.my_slider.config(value=int(current_time))

            # Update Slider to current possition
            #self.slider_position = int(song_length)
            #self.my_slider.config(to=self.slider_position , value=int(current_time))

            # Update time
            self.status_bar.after(1000, play_time)

        # label for length bar :
        self.status_bar = Label(self.root, text="", bd=3,
                                relief=GROOVE, anchor=E)
        self.status_bar.pack(fill=X, side=BOTTOM, ipady=2)

        # functions
        def playmusic():
            global filename
            try:

                if paused:
                    # set Slider andRe Status Bar
                    self.status_bar.config(text='')
                    self.my_slider.config(value=0)

                filename = self.song_box.get(ACTIVE)
                songinfo()
                filename = f"D:/songs/{filename}.mp3"
                mixer.music.load(filename)
                mixer.music.play()
                play_time()

                # #Update Slider to current possition
                # self.slider_position = int(song_length)
                # self.my_slider.config(to=self.slider_position , value=0)

                # print(filename)
                self.label1["text"] = "Music is Palying..."

                if(filename == " "):
                    tkinter.messagebox.showerror(
                        "Error", "File Could Not Found, Please Try Again..")

            except:
                tkinter.messagebox.showerror(
                    "Error", "Something goes wrong, Please Try Again..")

            # else :
            #     mixer.music.unpause()
            #     #self.song_box.select_clear(DISABLED)
            #     #self.label1["text"] = "Music unpaused"
            #     self.label1["text"] = "Music is Palying..."

        #global declaration
        global paused
        paused = False

        def pausemusic(is_paused):
            global paused
            paused = is_paused
            # self.song_box.select_clear(ACTIVE)
            if paused:
                # unpaused
                mixer.music.unpause()
                self.label1["text"] = "Music is Palying..."
                paused = False
            else:
                # paused
                mixer.music.pause()
                self.label1["text"] = "Music Paused"
                paused = True

        # paly next song :

        def next_song():
            global filename

            # set Slider andRe Status Bar
            self.status_bar.config(text='')
            self.my_slider.config(value=0)

            # get the current song tuple number
            next_one = self.song_box.curselection()
            # add one to the current song
            next_one = next_one[0]+1
            # print(next_one)
            # #collect song from playlist
            filename = self.song_box.get(next_one)
            songinfo()
            # #print(song)
            # #add directory structure and mp3 to song title
            filename = f"D:/songs/{filename}.mp3"
            mixer.music.load(filename)
            mixer.music.play()
            play_time()

            # # clear active bar in playlist
            self.song_box.selection_clear(0, END)

            # #Active new song bar
            self.song_box.activate(next_one)

            # #set active bar to next song
            self.song_box.selection_set(next_one)

        # paly previoius song :

        def previous_song():
            global filename

            # Reset Slider and Status Bar
            self.status_bar.config(text='')
            self.my_slider.config(value=0)

            # get the current song tuple number
            next_one = self.song_box.curselection()
            # minus one to the current song
            next_one = next_one[0]-1
            # print(next_one)
            # #collect song from playlist
            filename = self.song_box.get(next_one)
            songinfo()
            # #print(song)
            # #add directory structure and mp3 to song title
            filename = f"D:/songs/{filename}.mp3"
            mixer.music.load(filename)
            mixer.music.play()
            play_time()

            # # clear active bar in playlist
            self.song_box.selection_clear(0, END)

            # #Active new song bar
            self.song_box.activate(next_one)

            # #set active bar to next song
            self.song_box.selection_set(next_one)

        # making button_play
        self.Play_photo = ImageTk.PhotoImage(file="D:\python\MUSIC_PLAYER\Music Player\images\play.gif")
        self.button = Button(self.root, image=self.Play_photo, bg="black",
                             command=playmusic).place(x=20, y=470, width=50, height=50)

        # # making button_previous
        self.previous_photo = ImageTk.PhotoImage(file="D:\python\MUSIC_PLAYER\Music Player\images\previous.gif")
        self.button = Button(self.root, image=self.previous_photo, bg="black",
                             command=previous_song).place(x=95, y=470, width=50, height=50)

        # # making button_next
        self.next_photo = ImageTk.PhotoImage(file="D:\python\MUSIC_PLAYER\Music Player\images\my_next.gif")
        self.button = Button(self.root, image=self.next_photo, bg="black",
                             command=next_song).place(x=220, y=470, width=50, height=50)

        # making button_pause
        self.pause_photo = ImageTk.PhotoImage(file="D:\python\MUSIC_PLAYER\Music Player\images\pause.gif")
        self.button = Button(self.root, image=self.pause_photo,
                             bg="black", command=lambda: pausemusic(paused))
        self.button.place(x=157, y=470, width=50, height=50)

       
        # #Annimation
        # self.img1 = ImageTk.PhotoImage(file="")
        # self.img1 = ImageTk.PhotoImage(file="")
        # self.img1 = ImageTk.PhotoImage(file="")

        # mute_volume:

        def volume_mute():
            self.scale.set(0)
            self.mute = Image.open("mutevolume.jpg")
            # Resize the image using resize() method
            self.resize_image = self.mute.resize((35, 35))
            self.img = ImageTk.PhotoImage(self.resize_image)
            volume_button = Button(image=self.img, bg="black", command=unmute)
            volume_button.place(x=395, y=472)

        # Read the Image
        self.image = Image.open("D:\python\MUSIC_PLAYER\Music Player\images\my_vol.jpg")
        # Resize the image using resize() method
        self.resize_image = self.image.resize((35, 35))
        self.img = ImageTk.PhotoImage(self.resize_image)
        volume_button = Button(image=self.img, bg="black", command=volume_mute)
        volume_button.place(x=395, y=472)

        # function_volume
        def volume(vol):
            volume = int(vol)/100
            mixer.music.set_volume(volume)

        # unmute_volume :

        def unmute():
            self.scale.set(50)
            self.unmute = Image.open("D:\python\MUSIC_PLAYER\Music Player\images\my_vol.jpg")
            # Resize the image using resize() method
            self.resize_image = self.unmute.resize((35, 35))
            self.img = ImageTk.PhotoImage(self.resize_image)
            volume_button = Button(
                image=self.img, bg="black", command=volume_mute)
            volume_button.place(x=395, y=472)

        # volume control
        self.scale = Scale(self.root, from_=0, to=100, orient=HORIZONTAL,
                           bg="black", length=130, command=volume, fg="white")
        self.scale.set(50)
        self.scale.place(x=440, y=470)

        # create  slider function
        def slide(X):
            #self.slider_label.config(text=f'{int(self.my_slider.get())} of {int(song_length)}')
            filename = self.song_box.get(ACTIVE)
            filename = f"D:/songs/{filename}.mp3"
            mixer.music.load(filename)
            mixer.music.play(start=int(self.my_slider.get()))

        # create Music Position Slider

        # style = ttk.Style()
        # style.configure("TButton")

        self.my_slider = ttk.Scale(
            self.root, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=560)
        self.my_slider.place(x=20, y=540)

        # # #create Temporary Slider label
        # self.slider_label = Label(self.root,text="0")
        # self.slider_label.place(x=600,y=550)


root = Tk()
obj = musicplayer(root)
root.mainloop()
