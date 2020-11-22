# Import libraries
from sklearn.linear_model import LogisticRegression
# define data, create model and fit data
X = Variables
Y = Classes
Model = LogisticRegression(params).fit(X, Y)
# Score model
Model.score(X, y)
# Predict new class probs
NewY = Model.Predict(NewX)
