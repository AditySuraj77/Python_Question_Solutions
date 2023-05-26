print('Program to Find the Size (Resolution) of an Image')

from PIL import Image

img = Image.open('forest.jfif')

width,height = img.size

print('The Image size is = ',width ,'X',height)