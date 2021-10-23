from tkinter import *
from gtts import gTTS
import os
from playsound import playsound

window=Tk()
window.geometry("400x300")
window.title("Text To Speech")
window.configure(bg="grey")

l1=Label(window,text="TEXT_TO_SPEECH").pack()
l2=Label(window,text="Enter Text",width='20').place(x=20,y=60)

Msg=StringVar()
e1=Entry(window,textvariable=Msg,width='50').place(x=20,y=100)


def tts():
    message=Msg.get()
    speech=gTTS(text=message)
    speech.save('Speech1.mp3')
    playsound('Speech1.mp3')
    if os.path.exists('Speech1.mp3'):
        os.remove('Speech1.mp3')
    
    
def reset():
    Msg.set("")
Button(window,text="PLAY",command=tts,width='5').place(x=25,y=140)
Button(window,text="RESET",command=reset,width='5').place(x=100,y=140)
Button(window,text="EXIT",command=window.destroy,width='5').place(x=175,y=140)

window.mainloop()

