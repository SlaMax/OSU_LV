import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from PIL import Image

model = keras.models.load_model("model_mnist.h5")

img_path = "test.png"
img = Image.open(img_path).convert("L") 

plt.imshow(img, cmap="gray")
plt.title("Originalna slika")
plt.axis("off")
plt.show()

img_resized = img.resize((28, 28))
img_resized = np.array(img_resized).reshape((1,28, 28, 1))
img_array = np.array(img_resized).astype("float32") / 255.0  
  

img_array = img_array.reshape((28*28))  


prediction = model.predict(np.array(img_resized))
predicted_class = np.argmax(prediction)

print("Predviđena oznaka:", predicted_class)
