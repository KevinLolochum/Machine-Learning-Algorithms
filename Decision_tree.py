import numpy as np



def Gini(y):
    p = count(class_values)/count(rows)
    return np.sum(p*(1-P)*(group_size/no_samples)

def split(dataset):
    class_values = list(set(row[-1] for row in dataset))


class Node:

    def __init__(self, *, left = None, right = None, feature = None, threshold = None, value =None):
        slef.left = left
        self.right = right
        self.feature = feature
        self.threshold = threshold
        self.value = value
        
    def leaf_node(self):
        return self.value is not None

    
class Dtree:

    def __init__(self, *, max_depth = 20, min_samples_split = 2, max_features = None, random_state = None):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.max_features = max_features
        self.randdom_state = random_state
        self.root = None
        


    def fit(self, X, y, sample_weight = None):
        self.X_train = X
        self.Y_train = y


    def predict(x):



        return self.classes_.take(np.argmin(proba, axis = 1), axis = 0)

        return y
