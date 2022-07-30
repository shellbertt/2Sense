# controls the proprioceptive stimulators via arduino

import pyfirmata
import time

class controller():
    def __init__(self):
        self.board = pyfirmata.Arduino('COM5')
        self.pin = self.board.get_pin('d:13:o')
        self.it = pyfirmata.util.Iterator(self.board)
        self.it.start()
        self.board.analog[0].enable_reporting()
    def iterate(self):
        reading = self.board.analog[0].read()
        if reading is None: return
        print(reading)
        self.board.digital[13].write(1 if reading > .9 else 0)
        self.board.digital[8].write(1 if reading > .9 else 0)

if __name__ == '__main__':
    c = controller()
    while True:
        c.iterate()
        time.sleep(.15)

