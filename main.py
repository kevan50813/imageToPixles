from PIL import Image
import cv2
import matplotlib.pyplot as plt

'''
def pixleateImage(img):
    height, width = img.shape[:2]

    temp = cv2.resize(input, (8, 8), interpolation=cv2.INTER_LINEAR)
    small_img=cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    return small_img
'''

def imageToSketch(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    sketch_img = cv2.divide(img_gray, 255 - img_smoothing, scale=255)
    return sketch_img


def displayImages():
    img=cv2.imread('photo of me.PNG')
    img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
  #  small_img = pixleateImage(img)
    sketch_img = imageToSketch(img)

    plt.figure(figsize=(20,20))
    plt.subplot(1,5,1)
    plt.title("Original Image")
    plt.imshow(img)
    plt.axis("off")

    plt.subplot(1,5,2)
    plt.title("Pixleated Image")
    #plt.imshow(small_img)
    plt.axis("off")

    plt.subplot(1,5,3)
    plt.title("sketch Image")
    plt.imshow(sketch_img,cmap="gray",vmin=0,vmax=255)
    plt.axis("off")

    plt.show()

displayImages()