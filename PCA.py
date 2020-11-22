# Import libraries
from sklearn.decomposition import PCA
# define data, create model, fit and transform data
# X here has very high dimensionality
X = Variables/features
PCA_Model = PCA(n_components = 5).fit(X)
# Check explain variance from components
PCA_Model.explained_variance_ratio_
# Transform data if you like the explained variance
T_X = PCA_Model.transform(X)
