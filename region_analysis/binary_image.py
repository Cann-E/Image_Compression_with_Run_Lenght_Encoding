from dip import *

class BinaryImage:
    def __init__(self):
        pass

    def compute_histogram(self, image):
        """ Computes the histogram of the input image
        takes as input:
        image: a greyscale image
        returns a histogram as a list """

        hist = [0]*256
        hei, wid = image.shape
        for i in range(hei):
            for j in range(wid):
                hist[image[i][j]] += 1

        return hist

    def find_otsu_threshold(self, hist):
        """ Analyses a histogram to find the otsu's threshold assuming that the input histogram is bimodal
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value (otsu's threshold) """

        threshold = 0
        total = sum(hist)
        sumB = 0.0
        wB = 0.0
        maximum = 0.0
        sum1 = sum(i * hist[i] for i in range(256))

        for i in range(256):
            wB += hist[i]
            if wB == 0:
                continue
            wF = total - wB
            if wF == 0:
                break
            sumB += i * hist[i]
            mB = sumB / wB
            mF = (sum1 - sumB) / wF
            between = wB * wF * (mB - mF) ** 2
            if between > maximum:
                maximum = between
                threshold = i

        return threshold

    def binarize(self, image, threshold):
        """ Comptues the binary image of the input image based on histogram analysis and thresholding
        take as input
        image: a greyscale image
        threshold: the threshold used in binarization
        returns: a binary image """

        hei, wid = image.shape
        bin_img = zeros((hei, wid), uint8)
        for i in range(hei):
            for j in range(wid):
                if image[i][j] < threshold:
                    bin_img[i][j] = 255
                else:
                    bin_img[i][j] = 0

        return bin_img
