import RPi.GPIO as GPIO
import time

delay = 2

pin_4 = 4
pin_18 = 18
pin_23 = 23
pin_24 = 24

GPIO.setmode(GPIO.BCM)

class Uln2003AN():
    def init(self):
        GPIO.setwarnings(False)
        GPIO.setup(pin_4, GPIO.OUT)
        GPIO.setup(pin_18, GPIO.OUT)
        GPIO.setup(pin_23, GPIO.OUT)
        GPIO.setup(pin_24, GPIO.OUT)

    def forward(self,delay):
        self.setStep(1,0,0,0)
        time.sleep(delay)
        self.setStep(0,1,0,0)
        time.sleep(delay)
        self.setStep(0,0,1,0)
        time.sleep(delay)
        self.setStep(0,0,0,1)
        time.sleep(delay)

    def setStep(self,w1,w2,w3,w4):
        GPIO.output(pin_4, w1)
        GPIO.output(pin_18, w2)
        GPIO.output(pin_23, w3)
        GPIO.output(pin_24, w4)


if __name__ == "__main__":
    uln2003 = Uln2003AN()
    uln2003.init()
    while True:
        uln2003.forward(int(delay)/ 1000.0)


