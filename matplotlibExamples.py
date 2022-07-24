from PIL import Image
from pylab import *

# Read image to array
im = array(Image.open('Images/ClashOfCosmos.png').convert('L'))

""" Plotting points """

# # Plot image
# imshow(im)

# # Arbitrary points
# x = [100, 100, 400, 400]
# y = [200, 500, 200, 500]

# # Plot points with red star markers
# plot(x, y, 'r*')

# # Line plot connecting two of the points (in this case the first and third one)
# # w+: means white dashed line with pluses
# plot(x[::3], y[::3], 'w+:')

# # title("Plotting: 'ClashOfCosmos.png'")
# axis('off') # Comment as necessary

""" Contour image """

# # Create a new figure with no colours
# figure()
# gray()

# # Show contours with origin upper left corner
# contour(im, origin="image")
# axis('equal')
# axis('off')

""" Histogram """

# figure()

# # hist() takes a 1D array as input, so flatten() converts any array to a 1D array with values taken row-wise
hist(im.flatten(), 128)

""" Interactive annotation """

# imshow(im)
# print("Click 3 points")
# x = ginput(3)
# print("You clicked", x)

show()