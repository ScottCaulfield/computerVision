from PIL import Image
from pylab import *
import os

def getImList(path):
    """ Returns a list of filenames for all jpg images in a directory """
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.png')]

def imresize(im, size):
    """ Resize an image array using PIL """
    pilIm = Image.fromarray(uint8(im))

    return array(pilIm.resize(size))

def histEq(im, numBins=256):
    """ Histogram equalisation of a greyscale image """
    # Get image histogram
    imHist, bins = histogram(im.flatten(), numBins)
    cdf = imHist.cumsum() # Cumulative distribution function
    cdf = 255 * cdf/cdf[-1] # Normalise

    # Use linear interpolation of cdf to find new pixel values
    im2 = interp(im.flatten(), bins[:-1], cdf)

    return im2.reshape(im.shape), cdf

def computeAverage(imList):
    """ Compute the average of a list of images """
    # Open first image and make into array of type float
    averageIm = array(Image.open(imList[0]), 'f')

    for imName in imList[1:]:
        try:
            averageIm += array(Image.open(imName))
        except:
            print(imName + "...skipped")
    averageIm /= len(imList)

    # Return average as uint8
    return array(averageIm, 'uint8')