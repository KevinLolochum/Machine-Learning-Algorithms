import numpy as np

# Sigmoid function


class LogisticRegression:

    def __init__(self, lr=0.0001, n_iter = 1000):
        self.lr = lr
        self.n_iter = n_iter
        self.w = None
        self.b = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        #params
        self.w = np.zeros(n_features)
        self.b = 0

        #gradient descent

        for _ in range(self.n_iters):

            # Predict y using, X, w and b
            linear_model = np.dot(X, self.w)+ b
            
            #Apply sigmoid function
            y_pred = self._sigmoid(linear_model)

            #Compute gradients
            dw = (1/n_samples)*np.dot(X.T, (ypred-y))
            db = (1/n_samples)*np.sum(y_pred-y)

            #Update parameters
            self.w -= self.lr * dw
            self.b -= self.lr * db
    def predict(self, X):
        linear_model = np.dot(X, self.w) + self.b
        y_pred = self._sigmoid(linear_model)
        y_pred_cls = [1 if i > 0.5 else 0 for i in y_pred]

        return np.array(y_pred_cls)

    def _sigmoid(self, x):
        return 1/(1 + np.exp(-x))
            

        
        
    
