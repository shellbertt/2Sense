import proprioception
import visual
import tkinter
import time

class controller():
    def __init__(self):
        #             visual proprioception
        self.modes = {'proprioception': True, 'visual': True] #[False, False] # enable a given stimulus
        self.visualstim = visual.controller(tkinter.Tk(), .02)
        self.propstim = proprioception.controller()

    def iterate(self):
        if self.modes[0]:
            self.visualstim.iterate()
        if self.modes[1]:
            self.propstim.iterate()

    # control functions to be connected to gui

    def enable(self, mode):
        self.modes[mode] = True

    def disable(self, mode):
        self.modes[mode] = False

    def stop(self):
        exit()

def main():
    control = controller()
    while True:
        control.iterate()
        time.sleep(.01)

if __name__ == '__main__':
    main()

