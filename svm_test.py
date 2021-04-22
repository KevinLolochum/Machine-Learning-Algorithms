
import numpy as np
from sklearn import datasets
from SVM import svm


# create testing data
X, y = datasets.make_blobs(n_samples = 100, n_features = 2, centers = 2, cluster_std = 1.05, random_state=42)

y = np.where(y==0, -1, 1)

# Fit data to model
Model = svm()
Model.fit(X, y)

# predict the cluster and compare with actual
print(f"actual:{y[7]}, predicted: {Model.predict(X[7])}")


