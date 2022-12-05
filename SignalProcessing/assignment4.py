import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv


def draw():
    rRange = np.linspace(0.1, 10, 11, endpoint=True)
    for r in rRange:
        x = np.linspace(-r, r, 1000)
        y_posi = np.sqrt(r ** 2 - x ** 2)
        y_nega = -np.sqrt(r ** 2 - x ** 2)
        plt.plot(x, y_posi, c="k", linewidth=5)
        plt.plot(x, y_nega, c="k", linewidth=5)
    plt.axis("off")
    plt.xticks([])
    plt.yticks([])
    plt.savefig("assignment4.jpg")
    plt.show()


def fft():
    img = cv.imread("assignment4.jpg", 0)
    print(img.shape)
    f = np.fft.fft2(img)
    f = np.log(np.abs(np.fft.fftshift(f)))

    plt.subplot(121)
    plt.imshow(img, "gray")
    plt.title("Original")
    plt.axis("off")

    plt.subplot(122)
    plt.imshow(f, "gray")
    plt.title("Fourier")
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    plt.figure(figsize=(10,10))
    draw()
    fft()
