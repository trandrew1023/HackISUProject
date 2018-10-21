import RPi.GPIO as GPIO
import os
import sys
sys.path.append('/home/pi')
from RandomChar.CharArray import AddChar

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21,GPIO.OUT, initial=GPIO.LOW)


class gpioget:
    def __init__(self):
        self

    def get16(self):
        GPIO.output(24, GPIO.HIGH)
        rand = AddChar()
        while len(rand.get16()) <= 16:
            bit0 = GPIO.input(26) * 1
            bit1 = GPIO.input(19) * 2
            bit2 = GPIO.input(13) * 4
            bit3 = GPIO.input(6) * 8
            bit4 = GPIO.input(17) * 16
            bit5 = GPIO.input(18) * 32
            bit6 = GPIO.input(22) * 64
            bit7 = GPIO.input(23) * 128
            byte = bit0 + bit1 + bit2 + bit3 + bit4 + bit5 + bit6 + bit7
            rand.addchar(byte)
        GPIO.output(24, GPIO.LOW)
        return rand.get16()

    def get32(self):
        GPIO.output(20, GPIO.HIGH)
        while len(rand.get32()) <= 32:
            bit0 = GPIO.input(26) * 1
            bit1 = GPIO.input(19) * 2
            bit2 = GPIO.input(13) * 4
            bit3 = GPIO.input(6) * 8
            bit4 = GPIO.input(17) * 16
            bit5 = GPIO.input(18) * 32
            bit6 = GPIO.input(22) * 64
            bit7 = GPIO.input(23) * 128
            byte = bit0 + bit1 + bit2 + bit3 + bit4 + bit5 + bit6 + bit7
            rand.addchar(byte)
        GPIO.output(20, GPIO.LOW)
        return rand.get32()

temp = gpioget()
print(temp.get16())
print(temp.get32())