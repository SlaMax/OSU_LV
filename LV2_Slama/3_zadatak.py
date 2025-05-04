import numpy as np
import matplotlib.pyplot as plt

image=plt.imread("road.jpg")

image_float = image.astype(np.float32) / 255.0  
brighter_image = image_float * 1.8
brighter_image = np.clip(brighter_image, 0, 1)

brighter_image_uint8 = (brighter_image * 255).astype(np.uint8)

plt.imshow(brighter_image)
plt.title("Posvijetljena slika")
plt.show()


width = len(image[0])  
quarter_width = int(width/4)  

plt.imshow(image[:, 1*quarter_width: 2*quarter_width , :])
plt.show()


rotated_image = np.rot90(image, 3)  
plt.imshow(rotated_image)
plt.show()


flipped_image = np.flip(image, 0) 
plt.imshow(flipped_image)
plt.show()
