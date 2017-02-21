import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")
# cv2.imshow("Image", canvas)
# cv2.waitKey(0)

green = (0, 255, 0)
cv2.line(canvas, (0,0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

(centerX, centerY) = (canvas.shape[1]/2, canvas.shape[0]/2)
white = (255, 255, 255)

for r in xrange(0, 175, 25):
	cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)