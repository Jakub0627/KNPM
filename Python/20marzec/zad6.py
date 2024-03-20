from aeon.datasets import load_classification
X, y, meta_data = load_classification("BeetleFly")
print(" Shape of X = ", X.shape)
print(" Meta data = ", meta_data)

# uwaga to zostało nieskończone, tutaj należy rozgryźć aeon