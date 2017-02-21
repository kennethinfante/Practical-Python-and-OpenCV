import numpy as numpy
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

r = 150.0/image.shape[1] # new width/old width
dim = (150, int(image.shape[0]*r))

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width) Area", resized)
# cv2.waitKey(0)


resized = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)
cv2.imshow("Resized (Width) Linear", resized)
# cv2.waitKey(0)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)
cv2.imshow("Resized (Width) Cubic", resized)
# cv2.waitKey(0)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_NEAREST)
cv2.imshow("Resized (Width) Nearest", resized)
# cv2.waitKey(0)

# resize by specifying the height

# r = 50.0/image.shape[0]
# dim = (int(image.shape[1] * r), 50)

# resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
# cv2.imshow("Resized (Height)", resized)
# cv2.waitKey(0)





