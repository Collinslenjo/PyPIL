from PIL import Image, ImageDraw, ImageFont
# Adding Watermarks in Python
image = Image.open('Imgs/shoe.jpg')
width, height = image.size
draw = ImageDraw.Draw(image)
text = "A watermark"
font = ImageFont.truetype('arial.ttf', 12)
textwidth, textheight = draw.textsize(text, font)
# calculate the x,y coordinates of the text
margin = 5
x = width - textwidth - margin
y = height - textheight - margin
# draw watermark in the bottom right corner
draw.text((x, y), text, font=font)
image.save('watermarked.jpg')
