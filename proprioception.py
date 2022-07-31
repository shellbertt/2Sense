# controls the proprioceptive stimulators via arduino

import pyfirmata
import time

class controller():
    def __init__(self):
        self.board = pyfirmata.Arduino('COM5')
        self.it = pyfirmata.util.Iterator(self.board)
        self.it.start()
        self.board.analog[0].enable_reporting()

    def iterate(self, on):
        reading = self.board.analog[0].read()
        if reading is None: return # first reading may be None, can just ignore it
        if on:
            self.board.digital[8].write(1 if reading > .9 else 0)

if __name__ == '__main__':
    c = controller()
    while True:
        c.iterate()
        time.sleep(.15)

