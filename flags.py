import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from skimage import io
from skimage import img_as_float, img_as_ubyte
from skimage.transform import PiecewiseAffineTransform, warp
from PIL import Image, ImageDraw
from skimage import data
from random import randint as rn
from skimage.transform import resize
import os

def fl(name):
    i = Image.open(name)
    i = i.convert('RGBA')

    p = name[:-3]+"png"
    os.remove(name)
    i.save(p)

    imageS = io.imread(p)
    os.remove(p)
    image = resize(imageS,(500,800))


    rows, cols = image.shape[0], image.shape[1]

    src_cols = np.linspace(0, cols, 20)
    src_rows = np.linspace(0, rows, 10)
    src_rows, src_cols = np.meshgrid(src_rows, src_cols)
    src = np.dstack([src_cols.flat, src_rows.flat])[0]

    # add sinusoidal oscillation to row coordinates
    k = rn(2,5)
    dst_rows = src[:, 1] - np.sin(np.linspace(0, k * np.pi, src.shape[0])) * 50
    dst_cols = src[:, 0]
    dst_rows *= 1.5
    dst_rows -= 1.5 * 50
    dst = np.vstack([dst_cols, dst_rows]).T


    tform = PiecewiseAffineTransform()
    tform.estimate(src, dst)

    out_rows = image.shape[0] - 1.5 * 50

    out = warp(image, tform, output_shape=(out_rows, cols))

    imgF= img_as_ubyte(out)
    io.imsave("FS"+p, imgF)
    v = rn(1, 5)
    if v == 1:
        fon = Image.open('imagesForFlags/Whome.jpg')
        img = Image.open("FS"+p)
        img = img.convert('RGBA')
        fon.paste(img, (1928, 490), mask=img)
        fon = fon.convert('RGB')
        fon.save(name)
    elif v == 2:
        fon = Image.open('imagesForFlags/Kreml.jpg')
        imgS = Image.open("FS"+p)
        img = imgS.resize((333, 167))
        img = img.convert('RGBA')
        fon.paste(img, (552, 10), mask=img)
        fon = fon.convert('RGB')
        fon.save(name)
    elif v == 3:
        fon = Image.open('imagesForFlags/Soviet.jpg')
        imgS = Image.open("FS"+p)
        imgK = imgS.resize((400, 380))
        imgP = imgK.transpose(Image.FLIP_LEFT_RIGHT)
        img = imgP.rotate(47.5, expand=True)
        img = img.convert('RGBA')
        fon.paste(img, (65, 210), mask=img)
        fon = fon.convert('RGB')
        fon.save(name)
    elif v == 4:
        fon = Image.open('imagesForFlags/moon.jpg')
        imgS = Image.open("FS"+p)
        imgK = imgS.resize((500, 313))
        imgP = imgK.transpose(Image.FLIP_LEFT_RIGHT)
        img = imgP.rotate(-2.5, expand=True)
        img = img.convert('RGBA')
        fon.paste(img, (664, 200), mask=img)
        fon = fon.convert('RGB')
        fon.save(name)
    elif v == 5:
        fon = Image.open('imagesForFlags/tank.jpg')
        imgS = Image.open("FS"+p)
        imgK = imgS.resize((400, 250))
        imgP = imgK.transpose(Image.FLIP_LEFT_RIGHT)
        img = imgP.rotate(5, expand=True)
        img = img.convert('RGBA')
        fon.paste(img, (656, 63), mask=img)
        fon = fon.convert('RGB')
        fon.save(name)
    os.remove("FS"+p)

# matrix = np.array([[1, 0.5, 0],
#                    [0, 1, 0],
#                    [0,    0.0025, 1]])
# tform2 = transform.ProjectiveTransform(matrix=matrix)
# tf_img2 = transform.warp(img, tform2.inverse)
#
#
# fig, ax = plt.subplots(2,1)
#
# ax[0].imshow(tf_img)
# ax[1].imshow(tf_img2)
#
#
#
# io.imsave("123.png",tf_img2)
"""
[    сжатие по x        | tg угла сжимания -\ x  |  смещение по x]
[угол сжимания  по y \- |      сжатие по y       |  смещение по y]
[угол открывания дверь  | угол поднятия багажник | уменьшение к (0,0)]
"""
