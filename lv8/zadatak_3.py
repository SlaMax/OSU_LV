import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from PIL import Image

# Učitaj prethodno izgrađeni model
model = keras.models.load_model("model_mnist.h5")

# Učitaj sliku s diska
img_path = "test.png"
img = Image.open(img_path).convert("L")  # Konverzija u grayscale

# Prikaz originalne slike
plt.imshow(img, cmap="gray")
plt.title("Originalna slika")
plt.axis("off")
plt.show()

# Prilagodi veličinu i format slike
img_resized = img.resize((28, 28))  # Promjena veličine na 28x28 piksela
img_array = np.array(img_resized).astype("float32") / 255.0  # Skaliranje u [0,1]
img_array = 1.0 - img_array  # Inverzija boja ako je broj crn na bijeloj podlozi

# Oblikuj u batch veličine 1 s kanalom
img_array = np.expand_dims(img_array, axis=-1)  # Dodaj kanal (28, 28, 1)
img_array = np.expand_dims(img_array, axis=0)   # Dodaj batch dimenziju (1, 28, 28, 1)

# Predikcija
prediction = model.predict(img_array)
predicted_class = np.argmax(prediction)

# Ispis rezultata
print("Predviđena oznaka:", predicted_class)
