
import numpy as np
from scipy.stats import norm
from numpy import mean, std
from sklearn.datasets import make_blobs
import pandas as pd 


# Get the data and clean (In this case we are using already cleaned data)

X_values, Y_values = make_blobs(n_samples=100, centers=2, n_features=2, random_state=1)

# I will use pandas to make a few simplifications
X = pd.DataFrame(X_values)
Y = pd.DataFrame(Y_values)

data = pd.concat([X, Y], axis = 1)
# Calculating summary stats

def sum_stats(self, X_values, Y_values):
    '''
    Returns the mean and variance for each x column
    '''
    self.mu = X_values.groupby(Y_values).apply(np.mean).to_numpy()
    self.var = X_values.groupby(Y_values).apply(np.var).to_numpy()

    return self.mu, self.var
    
# Using guassian naive bayes
# Fit the data in a guassian pdf (write the function)

def guassian_pdf(self, class_idx, x):
    '''
    Returns probabilities of a guassian pdf
    '''
    mean = self.mean[class_idx]
    std = self.std[class_idx]
    numerator = np.exp((-1/2)*(((x-mean)/std)**2))
    denomenator = std*np.sqrt

    probability = numerator/denomator

    return probability
    

# Step 1. Calculating conditional probabilities (assuming independence for simplicity)

 # prior probabilities, step 2

def priors(self, X_values, Y_values):
     '''
        Parameters:
        X_values - array of shape(n_samples, n_features)
        Y_values - array of shape(n_samples)
        
        Returns:
        Prior Probabilities or frequency ratio of each class in the dataset
    '''
     self.priors = (X_values.groupby(Y_values).apply(lambda x: len(x))/len(self.rows)).to_numpy()

     return self.priors


# Posterior probabilities (Probabilities of samples belonging in a certain class)
# Will add the log of probabilities rather than multiplying to avoid numerical overflow

def posterior_probs(self, x):
    posteriors = []
    for i in range(self.count):
        prior = np.log(self.priors[i])
        conditional = np.sum(np.log(self.guassian_pdf(i,x)))
        posterior = priors + conditional
        posteriors.append(posterior)
    
    return self.classes[np.argmax(posteriors)]




# Fitting the model

def fit(self, X_values, Y_values):

    #Class variables
    self.classes = np.unique(Y_values)
    self.count = len(self.classes)
    self,feature_nums = Y_values.shape[1]
    self.rows = Y_values.shape[0]

    #Calculate statistics
    self.sum_stats(X_values, Y_values)
    self.priors(X_values, Y_values)


#Predicting values

def predict(self, X_values):
    '''
    Params:
    X-values array shape (n_samples, n_features)
    Returns:
    Y_values array shape (n_samples)
    '''
    preds = [self.posterior_probs(f) for f in X_values.to_numpy()]
    return preds

# Making actual predictions to test model

Xs, Ys = make_blobs(n_samples=6, centers=2, n_features=2, random_state=1)


