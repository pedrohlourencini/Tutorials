#executar o pip install --upgrade scikit-image
from skimage.measure import compare_ssim #SSIM means Structural Similarity Index
import argparse
import imutils
import cv2

#construindo o argument parse
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True, help="first input image")
ap.add_argument("-s", "--second", required=True, help="second input image")
args = vars(ap.parse_args())

#carregando imagens
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])

#convertendo para GS
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

#verifica o SSIM entre as duas imagens, e retorna a imagem
#é calculado o score, valor que diz a proximidade entre as imagens
#diff é a imagem resultado, é necessário converter a mesma para 8bit
(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))

#destaca as diferenças
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

#loop pelos contornos
for c in cnts:
    #calcula a box do contorno e desenha a mesma sobre as imagens, onde há diferença
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

#mostra o resultado
cv2.imshow("Original", imageA)
cv2.imshow("Modified", imageB)
cv2.imshow("Diff", diff)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)