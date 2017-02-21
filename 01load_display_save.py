import argparse
import cv2

# handle parsing of command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])
print "width: %d pixels" % (image.shape[1])
print "height: %d pxiesl" % (image.shape[0])
print "channels: %d" % (image.shape[2])

# show the image
image.shape
cv2.imshow("Image", image)
cv2.waitKey(0)

cv2.imwrite("newimage.jpg", image)
