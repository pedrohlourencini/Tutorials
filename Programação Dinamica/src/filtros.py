from PIL import Image, ImageFilter
from math import sqrt
from utils import in_file, out_file, show_vertical, show_horizontal
import numpy as np
import os

def show_vertical(im1, im2):
    im = Image.fromarray(np.vstack((np.array(im1), np.array(im2))))
    im.show()

DATA_DIR = os.path.join('filtros', 'data')

#img = Image.open(os.path.join(DATA_DIR, 'youtube.jpg'))
img = Image.open(in_file('Firefox_wallpaper.png'))

#filtered = img.filter(ImageFilter.BLUR)
filtered = img.filter(ImageFilter.CONTOUR)
filtered2 = img.filter(ImageFilter.GaussianBlur)

#img.show()
#filtered.show()
#show_vertical(filtered, filtered2)

def show_box_blur(filename, r = 1):
    '''Aplica um filtro BoxBlur a Imagem, exibe e salva o resultado'''
    original = Image.open(in_file('wallhaven-96ovxx.jpg'))
    filtered = original.filter(ImageFilter.BoxBlur(r))

    show_horizontal(original, filtered)
    filtered.save(out_file('{}_boxblur_{}.jpg'.format(filename[:filename.index('.')], r)))

def show_edges(filename, direction= 'x', offset = 0):
    '''Aplica um filtro Sobel a Imagem, exibe e salva o resultado'''
    original = Image.open(in_file('wallhaven-96ovxx.jpg')).convert('L') #converte para escala de cinza

    XSOBEL = ImageFilter.Kernel(
        (3, 3),
        [
            -1, 0, 1,
            -2, 0, 2,
            -1, 0, 1
        ], 1, offset
    )

    YSOBEL = ImageFilter.Kernel(
        (3, 3),
        [
            -1, -2, -1,
            0, 0, 0,
            1, 2, 1
        ], 1, offset
    )

    if direction == 'x':
        filtered = original.filter(XSOBEL)
    elif direction == 'y':
        filtered = original.filter(YSOBEL)
    else:
        vsobel = original.filter(XSOBEL)
        hsobel = original.filter(YSOBEL)
        w, h = original.size
        filtered = Image.new('L', (w, h))

        for i in range(w):
            for j in range(h):
                value = sqrt(vsobel.getpixel((i, j)) **2 + hsobel.getpixel((i, j))**2)
                value = int(min(value, 255))
                filtered.putpixel((i, j), value)

    #filtered = original.filter(ImageFilter.Kernel(
    #                                                (3, 3), [-1, 0, 1,
    #                                                         -2, 0, 2,
    #                                                         -1, 0, 1], 1, offset))

    show_horizontal(original, filtered)
    filtered.save(out_file('{}_{}sobel_{}.jpg'.format(
        filename[:filename.index('.')],
        direction,
        offset)))


if __name__ == '__main__':
    #show_box_blur('wallhaven-96ovxx.jpg', 3)
    show_edges('wallhaven-96ovxx.jpg', 'a', 128)

