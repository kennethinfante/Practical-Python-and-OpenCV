import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("Image", image)

edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edges", edged)

# ARGUMENTS:
# first - edged image, a copy only since this function is destructive
# second - type of contour
# third - how we want to approximate the contour

(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print "I cound %d coins in this image" % (len(cnts))

coins = image.copy()

# ARGUMENTS:
# first - we want to draw contour on the image copy
# second - list of contours
# third - contour index, in this case negative since we want to draw all contours. We could supply an index i which would be the i'th contour in cnts
# fourth - thickness of the line we are drawing

cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)

cv2.imshow("Coins", coins)
cv2.waitKey(0)


for (i, c) in enumerate(cnts):
	(x, y, w, h) = cv2.boundingRect(c)

	print "Coin #%d" % (i + 1)
	coin = image[y:y + h, x:x + w]
	cv2.imshow("Coin", coin)

	mask = np.zeros(image.shape[:2], dtype = "uint8")
	((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
	cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
	mask = mask[y:y + h, x:x + w]

	cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask = mask))
	cv2.waitKey(0)

