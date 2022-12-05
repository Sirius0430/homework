import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import random


def add_noise(img, salt, pepper=None):
    img = img.copy()
    if pepper == None: pepper = 1 - salt
    row, col = img.shape

    for x in range(row):
        for y in range(col):
            r = random.random()
            if r > salt:
                img[x][y] = 255
            elif r < pepper:
                img[x][y] = 0
            else:
                img[x][y] = img[x][y]

    return img


def clip(xMin, xMax, yMin, yMax, img):
    img = img[xMin:xMax, yMin:yMax]
    cv.imwrite("5_sample.jpg", img)
    return img


def match(target, sample):
    result = cv.matchTemplate(target, sample, cv.TM_SQDIFF_NORMED)
    cv.normalize(result, result, 0, 1, cv.NORM_MINMAX, -1)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    return min_loc


def show(origin, noise, result, sample, min_loc):
    sheight, swidth = sample.shape
    fig = plt.figure()
    ax=fig.add_subplot(221)
    ax.set_title("Sample")
    ax.imshow(sample,"gray")
    ax = fig.add_subplot(222)
    ax.set_title("Noise")
    ax.imshow(noise, "gray")
    ax = fig.add_subplot(223)
    ax.set_title("Origin")
    ax.imshow(origin, "gray")
    rect = plt.Rectangle((145,118),30,15,linewidth=1,edgecolor='r',facecolor='none')
    ax.add_patch(rect)
    ax = fig.add_subplot(224)
    ax.set_title("Result")
    ax.imshow(result, "gray")
    rect = plt.Rectangle(min_loc,swidth,sheight,linewidth=1,edgecolor='r',facecolor='none')
    ax.add_patch(rect)
    fig.tight_layout()
    plt.show()
    # plt.Rectangle(min_loc, max_loc[0] - min_loc[0], max_loc[1] - min_loc[1])


if __name__ == '__main__':
    img = cv.imread("5_target.jpg", 0)
    sample = cv.imread("5_sample.jpg", 0)
    # sample = clip(118,133,145,175,img)    #截取sample
    img_noise = add_noise(img, salt=0.9)  # 添加椒盐噪声
    img_blur = cv.blur(img_noise, (5, 5))  # 均值滤波
    min_loc = match(img_blur, sample)  # 图像匹配
    show(img,img_noise,img_blur,sample,min_loc)


