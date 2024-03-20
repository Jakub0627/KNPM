from time import time
from sklearn import metrics
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def bench_k_means(kmeans, name, data, labels):
    """
    Benchmark to evaluate the KMeans initialization methods.

    Parameters
    ----------
    kmeans : KMeans instance
        A :class:`~sklearn.cluster.KMeans` instance with the initialization
        already set.
    name : str
        Name given to the strategy. It will be used to show the results in a
        table.
    data : ndarray of shape (n_samples, n_features)
        The data to cluster.
    labels : ndarray of shape (n_samples,)
        The labels used to compute the clustering metrics which requires some
        supervision.
    """
    # Start timing the fit process
    t0 = time()
    # Create a pipeline that standardizes the data and applies KMeans clustering
    estimator = make_pipeline(StandardScaler(), kmeans).fit(data)
    # Calculate the time taken to fit the model
    fit_time = time() - t0
    # Initialize the results list with the method name, fit time, and inertia
    # (sum of squared distances to the closest cluster center)
    results = [name, fit_time, estimator[-1].inertia_]

    # Define the metrics that require true labels and estimator labels
    clustering_metrics = [
        metrics.homogeneity_score,
        metrics.completeness_score,
        metrics.v_measure_score,
        metrics.adjusted_rand_score,
        metrics.adjusted_mutual_info_score,
    ]
    # Compute and add the clustering metrics to the results
    results += [m(labels, estimator[-1].labels_) for m in clustering_metrics]

    # Compute and add the silhouette score to the results.
    # The silhouette score measures how similar an object is to its own cluster compared to other clusters.
    results += [
        metrics.silhouette_score(
            data,
            estimator[-1].labels_,
            metric="euclidean",
            sample_size=300,
        )
    ]

    # Format and print the results.
    # The results include the method name, fit time, inertia, and various clustering quality metrics.
    formatter_result = (
        "{:9s}\t{:.3f}s\t{:.0f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}"
    )
    print(formatter_result.format(*results))
