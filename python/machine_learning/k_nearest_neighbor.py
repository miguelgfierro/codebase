from sklearn.neighbors import NearestNeighbors
import numpy as np


def knn(X, Y, K):
    """Find the K nearest neighbor in X for each point in Y.
    Parameters:
        X (numpy array): A matrix, where the columns are the features and the rows are the examples.
        Y (numpy array): A matrix to query, where the columns are the features and the rows are the examples.
    Returns:
        distances (numpy array): Distance of the K nearest neighbor in X to Y.
        indices (numpy array): Indexes of the K nearest neighbor in X to Y.
    Examples:
        >>> np.random.seed(0)
        >>> X = np.random.randn(100000,512)
        >>> Y = np.random.randn(2,512)
        >>> dist, idx = knn(X,Y,5) #takes 5.78s
        >>> idx.shape
        (2, 5)
        >>> dist.shape
        (2, 5)

    """
    nbrs = NearestNeighbors(n_neighbors=K, algorithm='auto', metric='euclidean', n_jobs=-1).fit(X)
    distances, indices = nbrs.kneighbors(Y)
    return distances, indices


