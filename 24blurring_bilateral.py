import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# "image"
# "kernel" - diameter of our pixel neighborhood
# "color" - larger means that more colors in the neighborhood will be considered when computing the blur
# "space" - larger means that pixels farther out from the central pixel will influence the blurring calculation, provided that their colors are similar enough

blurred = np.hstack([
	cv2.bilateralFilter(image, 5, 21, 21),
	cv2.bilateralFilter(image, 7, 31, 31),
	cv2.bilateralFilter(image, 9, 41, 41)])
cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)