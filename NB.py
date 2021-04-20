import numpy as np
from scipy.stats import norm
from numpy import mean, std
from sklearn.datasets import make_blobs
import pandas as pd


# Get the data and clean (In this case we are using already cleaned data)

X_values, Y_values = make_blobs(n_samples=10, centers=2, n_features=2, random_state=1, )

X = pd.DataFrame(X_values)
Y = pd.DataFrame(Y_values)

data = pd.concat([X, Y], axis = 1)
# Calculating summary stats                                          
def sum_stats(data):
    '''
    Returns the mean and variance for each x column
    '''
    self.mu = data.iloc[:, :-1].groupby(data.iloc[-1:]).apply(np.mean).to_numpy()
    self.var = data[:, :-1].groupby(data[:,-1]).apply(np.var).to_numpy()

    return self.mu, self.var

print(data.iloc[:,:-1])
