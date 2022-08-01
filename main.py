import proprioception
import visual
import tkinter
import time
import data_recorder

class controller():
    def __init__(self):
        #             visual proprioception
        self.modes = {'proprioception': False, 'visual': False} #[False, False] # enable a given stimulus
        self.window = tkinter.Tk()
        self.window.attributes('-fullscreen', True)
        self.dr = data_recorder.DataRecorder(1, 'COM6') # hard code for our setup
        self.dr.begin_recording()
        self.visualstim = visual.controller(self.window, .02)
        self.propstim = proprioception.controller(self.dr.insert_marker)

    def set_participant_name(self, name):
        self.dr.trial_name = name

    def iterate(self):
        self.propstim.iterate(self.modes['proprioception'])
        self.visualstim.iterate(self.modes['visual'])

    # control functions to be connected to gui

    def enable(self, mode):
        self.modes[mode] = True

    def disable(self, mode):
        self.modes[mode] = False

    def stop(self):
        self.dr.finish()
        self.window.destroy()

    def new_recording(self):
        self.dr.end_recording()
        self.dr.save_data()
        self.dr.begin_recording()

def main():
    control = controller()
    control.enable('proprioception')
    control.enable('visual')
    while True:
        control.iterate()
        time.sleep(.15)

if __name__ == '__main__':
    main()

