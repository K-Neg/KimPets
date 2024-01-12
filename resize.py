from PIL import Image 
import os


def res(p):
	im = Image.open(p) 
	im2 = im.resize((300,300))
	im2.save(p.lower())


images = os.listdir('images')

for i in images:
	res('images//'+i)



