import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image file")
args = vars(ap.parse_args())

#carregando img
image = cv2.imread(args["image"])

#loop pelo angulos de rotacao
for angle in np.arange(0, 360, 15):
    #15 modificacoes de angulo
    rotated = imutils.rotate(image, angle)
    cv2.imshow("Rotated (correct)", rotated)
    cv2.waitKey(0)

