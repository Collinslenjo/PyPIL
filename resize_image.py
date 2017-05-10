import PIL
from PIL import Image
# Resizing Images With Python
basewidth = 500
img = Image.open('Imgs/bmw.jpg')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1] * float(wpercent))))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save('resized.jpg')
# The below inbuilt  method is used in creation of thumbnails
# im.thumbnail(size,Image.ANTIALIAS) 
