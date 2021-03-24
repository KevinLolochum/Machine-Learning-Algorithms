
import numpy as np
from scipy.stats import norm
from numpy import mean, std

# Before step one

# Get the data and clean




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
        Probabilities of belonging to each class
    '''
     self.priors = (X-values.groupby(Y_values).apply(lambda x: len(x))/len(self.rows)).to_numpy()

     return self.priors


 # Posterior probabilities

def posterior_probs(self, x):
    posteriors = []
    for i in range(self.count):
        prior = np.log(self.priors[i])
        conditional = np.sum(np.log(self.guassian_pdf(i,x)))
        posterior = priors + conditional
        posteriors.append(posterior)
    
    return self.classes[np.argmax(posteriors)]




