import proprioception
import visual
import tkinter
import time

class controller():
    def __init__(self):
        #             visual proprioception
        self.modes = {'proprioception': False, 'visual': False} #[False, False] # enable a given stimulus
        self.window = tkinter.Tk()
        self.window.attributes('-fullscreen', True)
        self.visualstim = visual.controller(self.window, .02)
        self.propstim = proprioception.controller()

    def iterate(self):
        self.propstim.iterate(self.modes['proprioception'])
        self.visualstim.iterate(self.modes['visual'])

    # control functions to be connected to gui

    def enable(self, mode):
        self.modes[mode] = True

    def disable(self, mode):
        self.modes[mode] = False

    def stop(self):
        self.window.destroy()
        exit()

def main():
    control = controller()
    control.enable('proprioception')
    control.enable('visual')
    while True:
        control.iterate()
        time.sleep(.01)

if __name__ == '__main__':
    main()

