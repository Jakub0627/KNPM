from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

X, y = load_breast_cancer(return_X_y=True)
print(X[1])

X_train, X_test, y_train, y_test = train_test_split(test_size=0.1, random_state=42)
model = GaussianNB()

y_pred = model.fit(X_train, y_train).predict(X_test)

# tutaj są własne testy