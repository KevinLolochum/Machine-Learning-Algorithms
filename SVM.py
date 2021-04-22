import numpy as np

# Check MIT lecture on youtube for the math
# Lecture name: 16. Learning: Support Vector Machines

class svm:

    def __init__(self, learning_rate = 0.001, alpha_param = 0.01, n_iters = 1000):
        self.w = None
        self.b = None
        self.lr = learning_rate
        self.n_iters = n_iters
        self.alpha_param = alpha_param

    def fit(self, X, y):
        ''' Optimizes the objective function that puts samples into clusters
            by adjusting weights params(w,b) based on constraint'''
        n_samples, n_features = X.shape

        # make y (classes to -1, 1) so that it is in line with the constraint.

        y_ = np.where(y <= 0, -1, 1)

        #Initialize the weights vector and the bias

        self.w = np.zeros(n_features)
        self.b = 0

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                constraint = y_[idx]*(np.dot(x_i, self.w) + self.b) >= 1

                # Adjusting params
                # If contraint is satisfied, use current weights for this x

                if constraint:
                    self.w -= self.lr*(2*self.alpha_param*self.w)


                # If not, update w and b
                else:
                    self.w -= self.lr*(2*self.alpha_param*self.w- np.dot(x_i, y_[idx]))
                    self.b -= self.lr*y_[idx]


    def predict(self, X):
        pred = np.dot(X, self.w)-self.b
        return np.sign(pred)
            
        
        
