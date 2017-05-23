'''
Continue manipulating the images
'''
from PIL import Image
import os

# Rotation of imades
image1 = Image.open('Imgs/carrot.jpg')
image1.rotate(-90).save('pup1_mod.jpg')

#make the image black and white
image1.convert(mode="L").save('pup1_mod.jpg')