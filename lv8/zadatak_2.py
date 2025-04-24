import numpy as np
from tensorflow import keras
from tensorflow.keras import layers # type: ignore
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix


model=keras.models.load_model("model_mnist.h5")

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Skaliraj slike na raspon [0, 1]
x_test_s = x_test.astype("float32") / 255
x_test_s = np.expand_dims(x_test_s, -1)

# Pretvori labele u one-hot kodiranje
y_test_s = keras.utils.to_categorical(y_test, 10)

# Predviđanje na testnim podacima
y_pred = model.predict(x_test_s)

# Prebacivanje vjerojatnosti u klase
y_pred_classes = np.argmax(y_pred, axis=1)

# Identifikacija loše klasificiranih slika
incorrect = np.where(y_pred_classes != y_test)[0]

num_images = 20

plt.figure()
for i in range(num_images):
    index = incorrect[i] 
    plt.imshow(x_test[index], cmap="gray")    
    true_label = y_test[index]
    predicted_label = y_pred_classes[index]
    plt.title(f"True: {true_label}, Pred: {predicted_label}")
    plt.axis("off")
    plt.show()