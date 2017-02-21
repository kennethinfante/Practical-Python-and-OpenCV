import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# extract image starting at (240, 30) and ending at (335, 120)
# remember that cv2 represents images as numpy arrays with height first , width second
cropped = image[30:120, 240:335]

cv2.imshow("Irish Face", cropped)
cv2.waitKey(0)

