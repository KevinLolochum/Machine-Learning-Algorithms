# Import libraries
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
# define data, split to train & test, create model and fit data
X = Variables
Y = Classes
Model = RandomForestClassifier(n_estimators = 10, params).fit(X, Y)
# Predict new classes
Y_predict = Model.Predict(X_test)
# Score model
accuracy_score(Y_test, Y_predict)
