import RPi.GPIO as GPIO
import time
 
outstr = "{digital} = {analog}V"
maxV = 3.3

out_list = (26, 19, 13, 6, 5, 11, 9, 10)
in_chan = 4
V_chan = 17
GPIO.setmode (GPIO.BCM)
GPIO.setup (out_list, GPIO.OUT)
GPIO.setup (V_chan, GPIO.OUT) # светодиод к компаратору
GPIO.setup (in_chan, GPIO.IN)  
 
def decToBinList (decNumber):
    if decNumber < 0 or decNumber > 255:
        raise ValueError
    return [(decNumber & (1 << i)) >> i for i in range (7, -1, -1)]
 
def num2dac (value):
    x = decToBinList (value)
    GPIO.output (out_list, tuple (x))
 
GPIO.output (V_chan, 1)
while True:
    try:
        value = int(input ("Enter value (-1 to exit) > 25:"))
        if value < -1 or value > 255:
            print ("not [0, 255]")
            continue
    except ValueError:
        print ("not number")
    else:
        if value == -1:
            break
        an = maxV * value / 255.0
        print (value, "=", an, "В"))
        num2dac(int(value * 50 / 255))
        #num2dac(int(value * 50 / 255))

GPIO.output (out_list, 0)
GPIO.output (V_chan, 0)
GPIO.cleanup (out_list)
GPIO.cleanup (V_chan)
GPIO.cleanup (in_chan)