import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from KNN import knn

df = datasets.load_iris()

X, y = df.data, df.target

X_train, x_test, Y_train, y_test = train_test_split(X, y, train_size = 0.75, random_state =42)


Model = knn()
Model.fit(X_train, Y_train)
y_preds = Model.predict(x_test)

# Model accuracy score
print(f"model accuracy score is,  {accuracy_score(y_test, y_preds)}")



