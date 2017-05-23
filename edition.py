'''
Continue manipulating the images
'''
from PIL import Image, ImageFilter
import os

# Rotation of imades
image1 = Image.open('Imgs/carrot.jpg')
image1.rotate(-90).save('rotated.jpg')

#make the image black and white
image1.convert(mode="L").save('black_white.jpg')

# Blur my Image
image1.filter(ImageFilter.GaussianBlur(15)).save('blur.jpg')