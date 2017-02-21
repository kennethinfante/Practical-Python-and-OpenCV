from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("'3D' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

hist = cv2.calcHist(image, [0, 1, 2], None, [8,8,8], [0, 256, 0, 256])
print "3D histogram shape: %s, with %d values" % (hist.shape, hist.flatten().shape[0])

plt.show()
cv2.waitKey(0)

