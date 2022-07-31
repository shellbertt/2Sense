import tkinter
import time
import visual
root = tkinter.Tk()
root.attributes('-fullscreen', True)
period = .02
V = visual.controller(root, period)
for i in range(360):
    V.iterate()
    #time.sleep(period)
root.mainloop()
