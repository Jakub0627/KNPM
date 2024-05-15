from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

X, y = load_breast_cancer(return_X_y=True)
print(X[1])

gnb = GaussianNB()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

y_pred = gnb.fit(X_train, y_train).predict(X_test)

num_mislabeled = (y_test != y_pred).sum()
total_points = X_test.shape[0]
print(f"Number of mislabeled points out of a total {total_points} points : {num_mislabeled}")

accuracy = accuracy_score(y_test, y_pred) * 100
print(f"Accuracy: {accuracy}%")
