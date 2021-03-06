import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help = "Path to the image")
args = vars(ap.parse_args())

# Loads the image
image = cv2.imread(args["image"])

# Print the weight, height and the channels
print("Width: ", image.shape[1])
print("Height: ", image.shape[0])
print("Channels: ", image.shape[2])

# Remind: RGB order BGR in OpenCV | Pixels, [x,y], are indexed from top left
# Access pixel values
(blue, green, red) = image[0,0]
print(blue, green, red)

# Access portion of the Image
corner = image[0:100, 0:100]

# Draw a line
startPoint = (0, 0)
endPoint = (300, 300)
greenColor = (0, 255, 0)
thickness = 3
cv2.line(image, startPoint, endPoint, greenColor, thickness)

# Draw rectangle
cv2.rectangle(image, startPoint, endPoint, greenColor, thickness)
# negative thickness fills the rectangle

# Draw circle
radius = 25
cv2.circle(image, startPoint, radius, thickness)

cv2.imshow("Shown Image", image)
cv2.waitKey()
