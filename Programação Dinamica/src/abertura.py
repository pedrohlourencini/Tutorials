from PIL import Image
import os

#image = Image.open("/home/pedro/Documents/Python-Proj/processamento-imagens/wallhaven-2eq3gg.jpg")
#print(image.getpixel((500,500)))
#image.show()

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

#retorna o endereço relativo dentro da pasta 'input'
def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)

image = Image.open(in_path("/input/Firefox_wallpaper.png"))
print(image.getpixel((500,500)))

image.show()