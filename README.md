# MP3_Music_Player
The objective of this project is to create a GUI based python music player from scratch using python. For this project, you will need intermediate knowledge of the Tkinter widgets, basic knowledge about tkinter.filedialog, pygame.mixer, and os libraries.

# Project Prerequisites
To create this music player python project, you will need intermediate understanding of Python Tkinter, and basic knowledge about the Pygame and ttkwidgets libraries.

Tkinter – To create the GUI for the project.

Pygame.mixer – This is a pygame module that is used to load and play music.

OS – To fetch the playlist of songs from the specified directories.

Not all the libraries come pre-installed with Python, so you will have to run the following command to install the required libraries.

[python -m pip install pygame](url)

# Elements of Mixer Module
To make python music player project, we will use some elements in the music file of the mixer module. Those elements are:

.load(filename) – This method is used to load a file so that other actions can be performed on that file. The argument it takes is a file of a supported audio format [.wav, .mp3, .ogg].
.play() – This method is used to play the music file that was loaded by the .load() method.
.stop() – This method can stop the loaded file such that it cannot be resumed again.
.pause() – This method is used to pause a loaded file, at least with this option, it can be played again before needing to be loaded again.
.unpause() – This method is used to unpause a loaded audio file, also known as the resume option.
