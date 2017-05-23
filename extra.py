'''
This will cover almost all manipulations but not all though
'''
from PIL import Image
import os

# Showing an image
#image1 = Image.open('resized.jpg')
# image1.show();

# Convert an image to an png format
# image1.save('res.png') this is only for one file

# for multiple files

size_300 = (300,300)
size_700 = (700,700)

for f in os.listdir('.'):
	if f.endswith('.jpg'):
		i = Image.open(f)
		fn, fext = os.path.splitext(f)
		# thumbnail size
		i.thumbnail(size_700)
		i.save('700/{}700{}'.format(fn,fext))

		# thumbnail size
		i.thumbnail(size_300)
		i.save('300/{}_300{}'.format(fn,fext))
		
	#	i.save('pngs/{}.png'.format(fn))