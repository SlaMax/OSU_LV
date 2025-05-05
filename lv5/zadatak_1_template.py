import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report



X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)



# Prikaz podataka za učenje i testiranje
plt.figure()
# Trening skup (krugovi)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='bwr', edgecolor='k', label='Train')
# Testni skup (x markeri)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='bwr', marker='x', label='Test')
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Podaci za učenje i testiranje")
plt.show()



model = LogisticRegression()
model.fit(X_train, y_train)



theta0 = model.intercept_[0]
theta1, theta2 = model.coef_[0]

x_vals = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
y_vals = -(theta0 + theta1 * x_vals) / theta2

plt.figure()
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='bwr', edgecolor='k', label='Train')
plt.plot(x_vals, y_vals, 'k--', label='Granica odluke')
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Granica odluke logističke regresije")
plt.show()


y_test_p = model.predict(X_test)

disp = ConfusionMatrixDisplay(confusion_matrix(y_test , y_test_p))
disp.plot()
plt.show()
print(classification_report(y_test , y_test_p))

#Pod e
y1 = (y_test==y_test_p)
y0 = (y_test!=y_test_p)

X_false = []

for i in range(len(y_test)):
    if y_test[i] != y_test_p[i]:
        X_false.append([X_test[i, 0], X_test[i, 1]])

X_false = np.array(X_false)
print(X_false)

plt.scatter(X_test[:,0], X_test[:, 1])
plt.scatter(X_false[:,0], X_false[:,1], color='green')
plt.show()