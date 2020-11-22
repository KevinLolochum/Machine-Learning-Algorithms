# Import libraries
from xgboost import XGBClassifier
# define data, split to train & test, create model and fit data
X = Variables
Y = Classes
model = XGBClassifier(objective = loss_func, 
                      n_estimators = num_of_base_estimators, params).fit(X, Y)
# Predict new classes
Y_predict = Model.Predict(X_test)
# Score model
accuracy_score(Y_test, Y_predict)
