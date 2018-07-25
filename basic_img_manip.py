import argparse
import cv2
import imutils
import os.path

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to image file is required")

args = vars(ap.parse_args())
if not os.path.exists(args["image"]) or not os.path.isfile(args["image"]):
    print("The image file mentioned does not exist!\n Exiting the app")
    exit(1)

img = cv2.imread(args["image"])
img_sm = imutils.resize(img, width=300)
img_sm_gray = cv2.cvtColor(img_sm, cv2.COLOR_BGR2GRAY)
img_sm_blur = cv2.GaussianBlur(img_sm_gray, (5, 5), 0)


cv2.imshow("Image", img)
cv2.imshow("Blurred Smaller Image", img_sm_blur)
cv2.waitKey(0)
