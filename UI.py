# control different stim modes with nice buttons

from asyncore import loop
from tkinter import *
from turtle import width
import pygame
from PIL import Image, ImageTk
import main
import time

pygame.mixer.init()

window = Tk()
window.geometry("1000x600")
window.title("2Sense_Stimulation")


bg = PhotoImage(file = "assets/LogoBanner.png") #adding an image as a background for later

Width = 1000
Height = 600

Logo = Label(window, image = bg)
Logo.pack()

text1 = StringVar()
NameLabel = Label(window, textvariable=text1, padx=20, pady=20)

text1.set("Enter Name of Participant:")
NameLabel.pack()

ID=StringVar()
UserName_input = Entry(window,bd=4,textvariable=ID)
UserName_input.pack()

Button_submit = Button(window, text = "SUBMIT", command=lambda: (UserName_input.pack_forget(), NameLabel.pack_forget(),Button_submit.pack_forget(), StimFrame()))
Button_submit.pack()

stim = main.controller()

def StimFrame():
    
    #Takes user to the Stimulation window when "Submit" is pressed

    Username = UserName_input.get()
    
    text2 = StringVar()
    NameDisplay = Label(window, textvariable=text2, padx=10,pady=20)

    text2.set("Participant Name: " + Username )
    NameDisplay.place(x=25, y=150)


    text3 = StringVar()
    Instruct = Label(window, textvariable=text3, relief=RAISED, padx=20, pady=20)

    text3.set("Instructions:" + "\n" + "\n" + "No Stimulation: No visual stimulation; foot fall does NOT start vibration" + "\n" + "Visual Stimulation only: Visual stimulation turned ON; foot fall does NOT start vibration" + "\n" +
                 "Vibration only: No visual stimulation; foot fall triggers vibration on ankle" + "\n" + "Both: Visual stimulation ON; foot fall triggers vibration on ankle")
    Instruct.place(x=250, y=200)


    NoStimButton = Button(window, text = "No Stimulation", command=NoStimulation).place(x=25, y=400)
    VisButton = Button(window, text = "Visual Only", command=VisualOnly).place(x=300, y=400)
    VibButton = Button(window, text = "Vibration Only", command=VibrationOnly).place(x=600, y=400)
    BothButton = Button(window, text = "Both On", command=BothOn).place(x=900, y=400)
    StopButton = Button(window, text="Stop Stimulation", command=StopStim).place(x=450, y=500)

def playBeep():
    pygame.mixer.music.load("assets/beep.wav")
    pygame.mixer.music.play(loops=0)

def NoStimulation():
    stim.disable("visual")
    stim.disable("proprioception")
     
def VisualOnly():
    stim.enable("visual")
    stim.disable("proprioception")
    
def VibrationOnly():
    stim.enable("proprioception")
    stim.disable("visual")
    
def BothOn():
    stim.enable("proprioception")
    stim.enable("visual")

def StopStim():
    stim.stop()
    print('ss')
    window.destrop()
    print('wd')
    exit()
    print('?')

window.protocol('WM_DELETE_WINDOW', StopStim)  #Stop stimulation when x button is pressed

while True:
    stim.iterate()
    time.sleep(.01)

window.mainloop()
