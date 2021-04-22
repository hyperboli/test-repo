import RPi.GPIO as GPIO
import time
 
chan_list = (26, 19, 13, 6, 5, 11, 9, 10)
GPIO.setmode (GPIO.BCM)
GPIO.setup (chan_list, GPIO.OUT) 
 
def decToBinList (decNumber):
    if decNumber < 0 or decNumber > 255:
        raise ValueError
    return [(decNumber & (1 << i)) >> i for i in range (7, -1, -1)]
 
def num2dac (value):
    x = decToBinList (value)
    GPIO.output (chan_list, tuple (x))
 
while True:
    try:
        value = int(input ("Enter value (-1 to exit):"))
        if value < -1 or value > 255:
            print ("N not in [0; 255] :(((")
            continue
    except ValueError:
        print ("Not number")
    else:
        if value == -1:
            break
        num2dac(value)

GPIO.output (chan_list, 0)
GPIO.cleanup (chan_list)