from osgeo import gdal
import numpy as np
from truncation import readTif
import cv2


def show(img,name,width,height):
    cv2.namedWindow(name, 0)
    cv2.resizeWindow(name, width,height)
    cv2.imshow(name, img)


def subSample(img):
    return cv2.pyrDown(img)

def lowPassFilter(img):
    return cv2.GaussianBlur(img,(5,5),9)

def interpolate(img,factor):
    return cv2.resize(img,dsize=None,fx=factor,fy=factor,interpolation=cv2.INTER_NEAREST)


if __name__ == '__main__':
    width, height, bands, data, geotrans, proj = readTif("D:\Codes\作业\SignalProcessing2\data.tif")
    img = cv2.merge([data[2], data[1], data[0]])
    ex1 = subSample(img)
    ex2 = lowPassFilter(img)
    ex2 = subSample(ex2)

    ex4 = interpolate(ex2,2)
    ex5 = subSample(ex1)
    ex6 = lowPassFilter(ex2)
    ex6 = subSample(ex6)

    ex8 = interpolate(ex6,4)

    show(ex8,"show",600,600)

    cv2.waitKey(0)