from PIL import Image, ImageFilter
import numpy as np
import skimage.io
from skimage import exposure

def blur_picture():
    img = Image.open('tmp/tmp_img_modified.png')
    img_blured = img.filter(ImageFilter.GaussianBlur(radius=1))
    img_blured = img_blured.save('tmp/tmp_img_modified.png', "PNG")
    return 'tmp/tmp_img_modified.png'


def sharpen_picture():
    img = Image.open('tmp/tmp_img_modified.png')
    img_sharpened = img.filter(ImageFilter.SHARPEN)
    img_sharpened=img_sharpened.save('tmp/tmp_img_modified.png', "PNG")
    return 'tmp/tmp_img_modified.png'


def contrast_streching():
    img = skimage.io.imread(fname='tmp/tmp_img_modified.png')
    # Contrast stretching
    p2, p98 = np.percentile(img, (2, 98))
    img_rescale = exposure.rescale_intensity(img, in_range=(p2, p98))
    skimage.io.imsave('tmp/tmp_img_modified.png', img_rescale)


def improve_picture():
    #blur_picture()
    contrast_streching()
    sharpen_picture()

    return 'tmp/tmp_img_modified.png'
