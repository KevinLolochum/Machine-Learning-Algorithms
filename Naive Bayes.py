# Import libraries
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
# define data, create model and fit data
X = Variables
Y = Classes
Model = GaussianNB(params).fit(X, Y)
# Score model
Model.score(X, Y)
# Predict new classes
NewY = Model.Predict(NewX)
