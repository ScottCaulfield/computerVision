from PIL import Image

originalImage = Image.open('Images/ClashOfCosmos.png')

""" Uncomment the individual parts to see what they do """

# greyImage = Image.open('Images/ClashOfCosmos.png').convert('L')
# greyImage.show()

# Creates a thumbnail of the image preserving aspect ratios with 128x128 max resolution
# originalImage.thumbnail((128, 28))

# Defines a region of the image (left, upper, right, lower) and crops to that region
# box = (100, 100, 400, 400)
# region = originalImage.crop(box)

# Rotates the cropped region by 180 degrees and places it back on the image
# region = region.transpose(Image.ROTATE_180)
# originalImage.paste(region, box)

# Resizes the image and rotates it
# originalImage = originalImage.resize((1280, 1280))
# originalImage = originalImage.rotate(45)

originalImage.show()