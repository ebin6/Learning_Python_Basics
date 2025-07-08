from tkinter import *
from gtts import gTTS
import os 
window=Tk()
def PlaymyNote():
    g=gTTS(text=note.get(),lang='en')
    g.save('sample.mp3')
    os.system('start sample.mp3')

note=Entry(window)
note.grid(row=0,column=0)
Button(text="Play",command=PlaymyNote).grid(row=0,column=1)
window.mainloop()

