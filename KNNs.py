# Import libraries
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
# define data, split to train & test, create model and fit data
X = Variables
Y = Classes
Model = KNeighborsClassifier(n_neighbors = 4, otherparams).fit(X, Y)
# Predict new classes
Y_predict = Model.Predict(X_test)
# Score model
accuracy_score(Y_test, Y_predict)
