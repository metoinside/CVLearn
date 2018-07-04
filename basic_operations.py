import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True,
                help = "Path to the image")
#ap.add_argument("-t","--translate", metavar = "X", nargs = "2", required=False,help = "Push or pull the pixel size")

ap.add_argument("-r","--rotate", type=int, required=False,
                help = "Rotate from the center with given degree")
ap.add_argument("-re","--resize", type=int, required=False,
                help = "Resize it through given percentage")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

def translate(image, xPush, yPush):
    M = np.float32([[1, 0, xPush],[0, 1, yPush]])
    dsize = (image.shape[1],image.shape[0])
    return cv2.warpAffine(image,M,dsize)

def rotate(image, degree, scale = 1.0):
    (h, w) = image.shape[:2]
    center = (h//2, w//2)

    M = cv2.getRotationMatrix2D(center,degree,scale)
    dsize = (image.shape[1],image.shape[0])
    return cv2.warpAffine(image, M, dsize)

def resize(image, percent):
    newWidth = image.shape[0] * percent // 100
    newHeight = image.shape[1] * percent //100
    return cv2.resize(image,(newHeight,newWidth))

if (args["rotate"]!=None):
    result = rotate(image, args["rotate"])
elif (args["resize"]!=None):
    result = resize(image, args["resize"])


cv2.imshow("Result", result)
cv2.waitKey(0)
