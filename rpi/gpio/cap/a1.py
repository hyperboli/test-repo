import RPi.GPIO as GPIO
import time
#import sample as sa

N = 8 #количество пинов
channel = range(N) #берём номер пина на плате из классического  (от 0 до 7) номера пина
#pins = [21,20,16,12,7,8,25,24][24, 25, 8, 7, 12, 16, 20, 21]
pins = [26, 19, 13, 6, 5, 11, 9, 10]
pins = pins[::-1]


GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)

#GPIO.output(,)

#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOI

def darkness():
    GPIO.output(pins, 0) #прямое действие

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

def decToBinList(decNumber):
    ans = bin(decNumber)
    ans = list(ans)
    ans = ans[2:]
    ans = [int(i) for i in ans]
    ans = [0]*8+ans
    ans = ans[-8:]

    return ans

def lightNumber(number):
    d = decToBinList(number)
    print(d)
    for i in range(N):
        if d[i]==1:
            GPIO.output(pins[N-i-1], 1)

#    time.sleep(2)
#    darkness()


#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOI


def main():
    s = None
    k = None

    def num2dac(value):
        lightNumber(value)

    darkness()

    while True:
        s = input()
        try:
            k = int(s)
        except ValueError:
            print("Это не похоже на число")
            continue
        if k==-1:
            darkness()
            raise SystemExit(1)
        elif not(k>=0 and k<=256):
            print("Число выходит за рамки 256")
            continue
        darkness()
        num2dac(k)
        
try:
    main()
finally:
    GPIO.output(pins, 0)
    GPIO.cleanup(pins)