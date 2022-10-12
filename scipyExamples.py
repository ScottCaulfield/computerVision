from PIL import Image
from numpy import *
from scipy.ndimage import *
from pylab import *
import scipy.misc

""" Blurring greyscale images """

# im = array(Image.open('Images/ClashOfCosmos.png').convert('L'))
# im2 = gaussian_filter(im, 1)

""" Blurring colour images """

# # Difference here is that Gaussian blurring is applied to each colour channel
# im = array(Image.open('Images/ClashOfCosmos.png'))
# im2 = zeros(im.shape)
# for i in range(3):
#     im2[:,:,i] = gaussian_filter(im[:,:,i],5)
# im2 = uint8(im2)

""" Binary morphology """

# Load image and threshold to make sure it is binary
im = array(Image.open('Images/tshirts.png').convert('L'))
im = 1*(im<255)

labels, numObjects = label(im)
print("Number of objects:", numObjects)

# Opening to separate objects better
imOpen = binary_opening(im, ones((9,5)), iterations=2)

labelsOpen, numObjectsOpen = label(imOpen)
print("Number of objects:", numObjectsOpen)

imshow(imOpen)
imsave("binaryMorph.png", imOpen)
show()