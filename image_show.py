import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to image file")

vars = ap.parse_args()

img = cv2.imread(vars.image)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()