# controls the proprioceptive stimulators via arduino

import pyfirmata
import time

class controller():
    # mark_step notes the stimulus in the data
    def __init__(self, mark_step):
        self.mark_step = mark_step
        self.board = pyfirmata.Arduino('COM5')
        self.it = pyfirmata.util.Iterator(self.board)
        self.it.start()
        self.board.analog[0].enable_reporting()
        self.wait = 15 # wait some cycles inbetween activation
        self.waited = 15

    def iterate(self, on):
        reading = self.board.analog[0].read()
        if reading is None: return # first reading may be None, can just ignore it
        if reading > .9 and on and self.waited >= self.wait:
            self.waited = 0
            self.mark_step(1)
            self.board.digital[8].write(1)
        else:
            self.board.digital[8].write(0)
            if self.waited < 15:
                self.waited += 1

def passer(trash):
    pass

if __name__ == '__main__':
    c = controller(passer)
    while True:
        c.iterate(True)
        time.sleep(.15)

