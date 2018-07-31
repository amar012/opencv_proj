import cv2
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", nargs='+', required=True,
	help="image file path(s)\nseparate consecutive paths with a space")

args = ap.parse_args()

def im_show(img_path_list):

    for img_path in args.images:
        if not os.path.exists(img_path) or not os.path.isfile(img_path):
            print("The image path: '%s' is not a valid path/file" % (img_path))
        else:
            img = cv2.imread(img_path)
            cv2.imshow(img_path, img)
            cv2.waitKey(0)


cv2.destroyAllWindows()

if __name__ == '__main__' :

    im_show(args.images)