from sklearn.cluster import KMeans
import numpy as np

# Sample data
X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])

# Create and fit the KMeans model
# Note: n_init should be an integer, representing the number of time the k-means algorithm will be run
# with different centroid seeds. The final results will be the best output of n_init consecutive runs in terms of inertia.
kmeans = KMeans(n_clusters=2, random_state=0, n_init=10).fit(X)

# Printing the labels of each point
print(kmeans.labels_)  # Correct syntax to access the labels of each point

# Predict the closest cluster each sample in X belongs to
print(kmeans.predict([[0, 0], [12, 3]]))  # Correct syntax to predict the cluster of new points

# Printing the coordinates of cluster centers
print(kmeans.cluster_centers_)  # Correct syntax to access the cluster centers
