from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
digits = load_digits()
plt.gray()
plt.matshow(digits.images[0])
plt.show()