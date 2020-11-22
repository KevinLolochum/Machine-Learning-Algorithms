# Import libraries
from sklearn.cluster import KMeans
# Create and fit model
Model = KMeans(n_clusters=4).fit(X)
# Cluster centres
Model.cluster_centers_
# Predict clusters of new data
Means = Model.predict(NewX)
