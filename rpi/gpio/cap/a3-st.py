import numpy as np
import matplotlib.pyplot as plt
import time

def decToBinList(decNumber):
    ans = bin(decNumber)
    ans = list(ans)
    ans = ans[2:]
    ans = [int(i) for i in ans]
    ans = [0]*8+ans
    ans = ans[-8:]

    return ans

def sinus(timeq, frequency, samplingFrequency):
    times = np.arange(0, 6.28*samplingFrequency, timeq*frequency)
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
        print(decToBinList(int(ndarray[i])), int(ndarray[i]), i)
        time.sleep(frequency**(-1))

sinus(20, 5, 10)