import os

def getImList(path):
    """ Returns a list of filenames for all jpg images in a directory """
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.png')]