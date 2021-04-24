import numpy as np
from collections import Counter

# Prepared using MIT lecture and my notes on KNN explanation
# Lecture name: 10. Introduction to Learning, Nearest Neighbors

# Distance function
def Eucledian(x_i, x_j):
    Dist = np.sqrt(np.sum((x_i - x_j)**2))
    return Dist

# Function to count the most common class/label
def common(ar):
    counter = Counter(ar)
    return counter.most_common(1)[0][0]



class knn:

    def __init__(self, k = 5):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def get_neighbors(self, x):
        distances = [Eucledian(x, x_train) for x_train in self.X_train]

        # Sort by distance and return closest neighbors
        k_idx = np.argsort(distances)[:self.k]

        # The labels of the k most closest neighbors
        labels = [self.y_train[i] for i in k_idx]
        return common(labels)
        
        
        
    def predict(self, X):
        preds =  [self.get_neighbors(x) for x in X]
        return np.array(preds)
