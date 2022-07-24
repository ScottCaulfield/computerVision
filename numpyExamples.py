from PIL import Image
from pylab import *
from numpy import *
import imtools

""" Information about images """

# # Prints shape and datatype of image. Default is uint8
# im = array(Image.open('Images/ClashOfCosmos.png'))
# print(im.shape, im.dtype)

# # f forces the datatype to be float32
# im = array(Image.open('Images/ClashOfCosmos.png').convert('L'))#, 'f')
# print(im.shape, im.dtype)

""" Greylevel transforms """

# im = array(Image.open('Images/Octopus.png').convert('L'))
# print (int(im.min()), int(im.max()))
# imshow(im)

# # Inverts
# im2 = 255 - im
# print (int(im2.min()), int(im2.max()))
# imshow(im2)

# # Clamps to interval 100-200
# im3 = (100/255) * im + 100
# print (int(im3.min()), int(im3.max()))
# imshow(im3)

# # Squared, which lowers values of the darker pixels
# im4 = 255 * (im/255)**2
# print (int(im4.min()), int(im4.max()))
# imshow(im4)

# # Reverse of the array() transformation - gets an image from an array. The datatype should be uint8 before doing this, so you can cast it to be safe
# imFromArray = Image.fromarray(uint8(im))

""" Histogram equalisation """

# im = array(Image.open('Images/ClashOfCosmos.png').convert('L'))
# im2, cdf = imtools.histEq(im)

# hist(im.flatten(), 256)
# hist(im2.flatten(), 256)

# imshow(im)

show()