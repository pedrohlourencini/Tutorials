from PIL import Image, ImageFilter
import numpy as np
import os

INPUT_FOLDER = "/home/pedro/PycharmProjects/ProcessamentoImagens-ProgDin/input"
OUTPUT_FOLDER = "/home/pedro/PycharmProjects/ProcessamentoImagens-ProgDin/output"

#retorna o endereço relativo dentro da pasta 'input'
def in_file(filename):
    """ Retorna o caminho de um arquivo de entrada"""

    return os.path.join(INPUT_FOLDER, filename)

def out_file(filename):
    '''Retorna o caminho de um arquivo de saida'''
    return os.path.join(OUTPUT_FOLDER, filename)

def show_vertical(im1, im2):
    '''retorna as imagens concatenadas na vertical'''

    im = Image.fromarray(np.vstack((np.array(im1), np.array(im2))))
    im.show()
    return im

def show_horizontal(im1, im2):
    '''retorna as imagens concatenadas na horizontal'''
    im = Image.fromarray(np.hstack((np.array(im1), np.array(im2))))
    im.show()
    return im

