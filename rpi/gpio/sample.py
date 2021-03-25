import RPi.GPIO as GPIO
import time

N = 8 #количество пинов
channel = range(N) #берём номер пина на плате из классического  (от 0 до 7) номера пина
#pins = [21,20,16,12,7,8,25,24]
pins = [24, 25, 8, 7, 12, 16, 20, 21]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)

#GPIO.output(,)

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

def  runningPatternContinue(pattern, direction, period):
    d = decToBinList(pattern)
    print(d)
    for j in range(direction):
        #lightNumberPro(pattern, period)
        for i in range(8):
            d = d[1:]+d[0:1]
            print(d)
            for s in range(N):
                if d[s]==1:
                    GPIO.output(pins[N-s-1], 1)
                         #chis = pattern%(2**(N-i))*(2**i)+pattern//(2**(N-i))
            time.sleep(period)
            darkness()

    #pattern1 = pattern
    #for j in range(direction):
     #   for i in range(8):
     #       lightNumberPro(pattern, period)
     #       pattern = pattern>>1
     #   pattern = pattern1<<8
      #  for i in range(8):
      #      lightNumberPro(pattern, period)
      #      pattern = pattern>>1
    #lightNumberPro(pattern, period)

#direction - смещаем в одну
def  runningPattern(pattern, direction):
    if direction==1:
        pattern = pattern>>1
    else:
        pattern = pattern

    lightNumber(pattern)

def lightNumberPro(number, period):
    d = decToBinList(number)
    #print(d)
    for i in range(N):
        if d[i]==1:
            GPIO.output(pins[N-i-1], 1)

    time.sleep(period)
    darkness()


def lightNumber(number):
    d = decToBinList(number)
    print(d)
    for i in range(N):
        if d[i]==1:
            GPIO.output(pins[N-i-1], 1)

    time.sleep(2)
    darkness()

def shim(period):

    #без библиотек - каждая итерация цикла - 0.01 секунды
    #распределяем это время на вкл и выкл

    i = 0
    step = 1000/(period*100)
    while i<1000:
        GPIO.output(pins, 1) #прямое действие
        time.sleep(i/100000)
        GPIO.output(pins, 0) #прямое действие
        time.sleep((1000-i)/100000)
        i+=step

    GPIO.output(pins, 1) #прямое действие
    time.sleep(1)

    i = 0
    while i<1000:
            GPIO.output(pins, 1) #прямое действие
            time.sleep((1000-i)/100000)
            GPIO.output(pins, 0) #прямое действие
            time.sleep(i/100000)
            i+=step


    #for i in range(255):
    #GPIO.output(pins, 1) #прямое действие
    #time.sleep(2)
    #GPIO.output(pins, 0) #прямое действие
        #time.sleep(0.005)
        #GPIO.output(pins, 0) #прямое действие
        #time.sleep(0.005)


#lightUp(4, 2)
#blink(1, 5, 0.1)
#runningDark(2, 0.1)
#shim(10)
m = 5 #число, которое я показываю
runningPatternContinue(m, 2, 0.5)
#runningPatternContinue(m, 0, 0.5)
#print(p2)
#lightNumber(m)
#lightNumber(p1)
#lightNumber(p2)
#runningDark(10, 0.5)

darkness()

GPIO.cleanup()