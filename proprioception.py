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
        self.wait = 5 # wait some cycles inbetween activation
        self.waited = self.wait
        self.ready = True

    def iterate(self, on):
        reading = self.board.analog[0].read()
        if reading is None: return # first reading may be None, can just ignore it
        print(reading, on, self.waited, self.wait,self.ready, end=': ')
        if reading > .9 and on and self.waited >= self.wait and self.ready:
            self.waited = 0
            self.mark_step(1) # step with simulus
            self.board.digital[8].write(1)
            self.ready = False
            print('GOooooooooooooooooooooooooooooooooooooooO!')
        else:
            if reading >.9 and self.waited >= self.wait and self.ready:
                self.mark_step(.5) # step without stimulus
                self.ready = False
                self.waited = 0
            if self.waited >= self.wait:
                self.board.digital[8].write(0)
            print('NO!')
        if reading < .65:
            self.ready = True
        if self.waited < self.wait:
            self.waited += 1

def passer(trash):
    pass

if __name__ == '__main__':
    c = controller(passer)
    while True:
        c.iterate(True)
        time.sleep(.15)

