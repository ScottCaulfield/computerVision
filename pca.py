from PIL import Image
from numpy import *

def pca(X):
    """ Principal Component Analysis 
        input: X, matrix with training data stored as flattened arrays in rows
        return: projection matrix (with important dimensions first), variance and mean """
    # Get dimensions
    numData, dim = X.shape

    # Centre data
    meanX = X.mean(axis=0)
    X = X - meanX

    if(dim > numData):
        # PCA - Compact trick used
        M = dot(X, X.T) # Covariance matrix
        e, EV = linalg.eigh(M) # Eigenvalues and eigenvectors
        tmp = dot(X.t, EV).T # This is the compact trick
        V = tmp[::-1] # Reverse since last eigenvectors are the ones we want
        S = sqrt(e)[::-1] # Reverse since eigenvalues are in increasing order
        for i in range(V.shape[1]):
            V[:,i] /= S
    else:
        # PCA -  SVD used
        U,S,V = linalg.svd(X)
        V = V[:numData] # Return only the first numData

    # Return the projection matrix, variance and mean
    return V, S, meanX