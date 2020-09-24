import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image file")
args = vars(ap.parse_args())

#carrega image
image = cv2.imread(args["image"])

#grayscale e blur na imagem
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)

#detecção de arestras
edge = cv2.Canny(gray, 20, 100)

#encontra os contornos nas arestras
cnts = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

#garante que pelo menos um contorno foi encontrado
if len(cnts) > 0:
    #pega o maior contorno, então desenha a mascara para o objeto
    c = max(cnts, key=cv2.contourArea)
    mask = np.zeros(gray.shape, dtype="uint8")
    cv2.drawContours(mask, [c], -1, 255, -1)

    #pega o bounding box, e aplica a mask
    (x, y, w, h) = cv2.boundingRect(c)
    imageROI = image[y:y + h, x:x + w]
    maskROI = mask[y:y + h, x:x + w]
    imageROI = cv2.bitwise_and(imageROI, imageROI, mask=maskROI)

    #loop pelos angulos de rotacao
    for angle in np.arange(0, 360, 15):
        rotated = imutils.rotate(imageROI, angle)
        cv2.imshow("Rotated (Problematic)", rotated)
        cv2.waitKey(0)

    #loop pelo angulos de rotacao novamente, desta vez de forma correta
    for angle in np.arange(0, 360, 15):
        rotated = imutils.rotate_bound(imageROI, angle)
        cv2.imshow("Rotated (Correct)", rotated)
        cv2.waitKey(0)