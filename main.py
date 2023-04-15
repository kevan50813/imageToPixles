from PIL import Image
import matplotlib.pyplot as plt

#open image
img=Image.open('photo of me.PNG')

plt.imshow(img)
plt.show()