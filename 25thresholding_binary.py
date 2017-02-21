import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Image", image)

# image - that we wish to threshold
# threshold value
# maximum value applied - any pixel intensity p that is greater than T, is set to this value
# thresholding method

(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Threshold Binary Inverse", threshInv)
cv2.imshow("Coins", cv2.bitwise_and(image, image, mask = threshInv))
cv2.waitKey(0)


