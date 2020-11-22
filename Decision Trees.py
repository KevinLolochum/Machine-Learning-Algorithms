# Import libraries
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
# define data, split to train & test, create model and fit data
X = Variables
Y = Classes
Model = DecisionTreeClassifier(params).fit(X, Y)
# Predict new classes
Y_predict = Model.Predict(X_test)
# Score model
accuracy_score(Y_test, Y_predict)
