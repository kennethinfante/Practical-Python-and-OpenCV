import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# dim = (w,h)
# 0 - around the x-axis
# 1 - around the y-axis
# -1 - both axes

flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)
# cv2.waitKey(0)

flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)

