from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np


def color_quantization(img, k):
# Transform the image
  data = np.float32(img).reshape((-1, 3))

# Determine criteria
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

# Implementing K-Means
  ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
  center = np.uint8(center)
  result = center[label.flatten()]
  result = result.reshape(img.shape)
  return result

def pixleateImage(img):
    height, width = img.shape[:2]
    w,h=(32,32)
    temp = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)
    pixel_img=cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    return pixel_img

def imageToSketch(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    sketch_img = cv2.divide(img_gray, 255 - img_smoothing, scale=255)
    return sketch_img

def comicImage(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(img_gray, 7)
    edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 7)
    total_color = 9
    img = color_quantization(img, total_color)
    blurred = cv2.bilateralFilter(img, d=7, sigmaColor=200,sigmaSpace=200)
    cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)
    return cartoon


def displayImages():
    img=cv2.imread('images.jpg')
    img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    pixel_img  = pixleateImage(img)
    sketch_img = imageToSketch(img)
    cartoon_img = comicImage(img)

    plt.figure(figsize=(20,20))
    plt.subplot(1,5,1)
    plt.title("Original Image")
    plt.imshow(img)
    plt.axis("off")

    plt.subplot(1,5,2)
    plt.title("Pixleated Image")
    plt.imshow(pixel_img)
    plt.axis("off")

    plt.subplot(1,5,3)
    plt.title("cartoon Image")
    plt.imshow(cartoon_img)
    plt.axis("off")

    plt.subplot(1,5,4)
    plt.title("sketch Image")
    plt.imshow(sketch_img,cmap="gray",vmin=0,vmax=255)
    plt.axis("off")

    plt.show()
