from PIL import Image
import cv2
import matplotlib.pyplot as plt



def pixleateImage(img):
    small_img=img.resize((8,8),Image.BILINEAR)
    return small_img

def imageToSketch():
    img=cv2.imread('photo of me.PNG')
    grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invert_img=cv2.bitwise_not(grey_img)
    blur_img=cv2.GaussianBlur(invert_img, (111,111),0)
    invblur_img=cv2.bitwise_not(blur_img)
    sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)
    return sketch_img

def displayImages():
    img=Image.open('photo of me.PNG')
    small_img=pixleateImage(img)
    sketch_img=imageToSketch()

    f, axarr = plt.subplots(2,2)
    axarr[0,0].imshow(img)

    axarr[0,1].imshow(small_img)
    
    axarr[1,0].imshow(sketch_img)

    plt.show()

displayImages()