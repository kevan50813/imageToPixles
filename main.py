from PIL import Image
import matplotlib.pyplot as plt

def pixleateImage():
    #open image
    img=Image.open('photo of me.PNG')

    plt.imshow(img)
    plt.show()

    small_img=img.resize((8,8),Image.BILINEAR)
    plt.imshow(small_img)
    plt.show()

pixleateImage()