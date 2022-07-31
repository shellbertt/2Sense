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

var = StringVar()
label = Label(window, textvariable=var, relief=RAISED, padx=20, pady=20)

var.set("Instructions:" + "\n" + "\n" + "No Stimulation: No visual stimulation; foot fall does NOT start vibration" + "\n" + "Visual Stimulation only: Visual stimulation turned ON; foot fall does NOT start vibration" + "\n" +
            "Vibration only: No visual stimulation; foot fall triggers vibration on ankle" + "\n" + "Both: Visual stimulation ON; foot fall triggers vibration on ankle")
label.place(x=250, y=200)

stim = main.controller()

#introFrame = Frame(window, width=Width, height=Height, bg="white")
#introFrame.pack()

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
#add stuff to stop stimulation

# label with the logo is on the second frame 
label = Label(window, image = bg)
label.place(x=0, y=25)

#introLabel= Label(introFrame, )

NoStimButton = Button(window, text = "No Stimulation", command=NoStimulation).place(x=25, y=400)
VisButton = Button(window, text = "Visual Only", command=VisualOnly).place(x=300, y=400)
VibButton = Button(window, text = "Vibration Only", command=VibrationOnly).place(x=600, y=400)
BothButton = Button(window, text = "Both On", command=BothOn).place(x=900, y=400)
StopButton = Button(window, text="Stop Stimulation", command=StopStim).place(x=450, y=500)

while True:
    stim.iterate()
    time.sleep(.01)

window.mainloop()
