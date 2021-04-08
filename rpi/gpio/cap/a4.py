import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt
import time
#import sample as sa

N = 8 #количество пинов
channel = range(N) #берём номер пина на плате из классического  (от 0 до 7) номера пина
#pins = [21,20,16,12,7,8,25,24]
pins = [24, 25, 8, 7, 12, 16, 20, 21]

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
    #print(d)
    for i in range(N):
        if d[i]==1:
            GPIO.output(pins[N-i-1], 1)

#    time.sleep(2)
#    darkness()


#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOI


s = None
k = None

def num2dac(value):
    lightNumber(value)

def blade_runner(repetitionsNumber):
    r = repetitionsNumber
    for j in range(r):
        for i in range(256):
            num2dac(i)
            time.sleep(0.1)
            darkness():
        for i in range(256, -1, -1):
            num2dac(i)
            time.sleep(0.05)
            darkness():


def sinus(timeq, frequency, samplingFrequency):
    times = np.arange(0, timeq, samplingFrequency**(-1))
    ndarray = np.sin(times)
    for i in range(len(ndarray)):
        ndarray[i] = (ndarray[i]+1)*255/2
    
    #print(ndarray)


    plt.plot(times, ndarray)
    plt.title('Синус')
    plt.xlabel('Время')
    plt.ylabel('Амплитуда sin(time)')
    plt.show()

    for i in range(timeq*frequency):
        num2dac(int(ndarray[i]))
        time.sleep(frequency**(-1))



while True:
    print("Введите число повторений:")
    s = input()
    try:
        k = int(s)
    except ValueError:
        print("Это не похоже на число")
        continue
    if k==-1:
        exit()
    if k<0:
        print("Число повторений не может быть отрицательным")
        continue
    blade_runner(k)
    break