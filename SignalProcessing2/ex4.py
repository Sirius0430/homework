import numpy as np
import math

def gaussianFilter(size,sigma):
    GF = np.zeros([size,size])
    center = int(size/2)
    for x in range(size):
        for y in range(size):
            GF[x,y] = math.exp((-(np.square(x-center) + np.square(y-center)))/(2*math.pi*sigma**2))
    GF /= np.sum(GF)
    return GF

if __name__ == '__main__':
    GF = gaussianFilter(7,1)
    print(GF)
