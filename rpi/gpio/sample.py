import RPi.GPIO as GPIO
import time

N = 8 #количество пинов
channel = range(N) #берём номер пина на плате из классического  (от 0 до 7) номера пина
pins = [2, 3, 4, 17, 27, 22, 10, 9]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)

#GPIO.output(,)

def lightUpPro(ledNumber, period):
    n = pins[ledNumber]
    GPIO.output(n, 1) #прямое действие
    time.sleep(period)
    GPIO.output(n, 0) #прямое действие

def lightDownPro(ledNumber, period):
    n = pins[ledNumber]
    GPIO.output(n, 0) #прямое действие
    time.sleep(period)
    GPIO.output(n, 1) #прямое действие

def lightUp(ledNumber, period):
    lightUpPro(ledNumber, period)
    time.sleep(period)

def lightDown(ledNumber, period):
    lightDownPro(ledNumber, period)
    time.sleep(period)


def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range(blinkCount):
        lightUp(ledNumber, blinkPeriod)

def runningLight(count, period):
    channel = range(N)
    for j in range(count):
        for i in channel:
            lightUpPro(i, period)

def runningDark(count, period):
    channel = range(N)
    GPIO.output(pins, 1) #прямое действие
    for j in range(count):
        for i in channel:
            lightDownPro(i, period)
    GPIO.output(pins, 0) #прямое действие

def decToBinList(decNumber):
    ans = bin(decNumber)
    ans = list(ans)
    ans = ans[2:]
    ans = [int(i) for i in ans]
    ans = [0]*8+ans
    ans = ans[-8:]

    return ans

def  runningPattern(pattern, direction):
    return pattern<<direction

lightUp(0, 2)
blink(1, 5, 1)
runningLight(2, 1)
runningDark(2, 1)


GPIO.cleanup()