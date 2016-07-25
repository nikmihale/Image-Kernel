from PIL import Image, ImageDraw
import re

kernel = open('kernel.txt')

ker = kernel.read()
ker = [re.findall(r'[-]?\d+\.?\d*', item) for item in ker.split('\n')]
ker = [line for line in ker if line]
image = Image.open("original.jpg")
Y, Cb, Cr = image.convert("YCbCr").split()
new_image = Y.copy()
draw = ImageDraw.Draw(new_image)
width = image.size[0]
height = image.size[1]
pix = Y.load()
Kheight = len(ker) 
Kwidth = len(ker[0])

if Kheight*Kwidth % 2 == 0:
	print "Invalid kernel: height and width must both be odd"
	kernel.close()
	del draw
	raise SystemExit


#Convolution itself starts here
sum = 0
for i in range(Kheight):
	for j in range(Kwidth):
		sum += float(ker[i][j])
if sum == 0 :
	sum = 1

for i in range(height):
	for j in range(width):
		Sy = 0
		for k in range(Kheight):
			for l in range(Kwidth):
				pixelposX = i + k - ( Kwidth / 2 )
				pixelposY = j + l - ( Kheight / 2 )
				if pixelposX < 0 or pixelposX >= width or pixelposY < 0 or pixelposY >= height :
					continue				
				Sy += pix[pixelposX, pixelposY] * float( ker[k][l] ) / sum
		draw.point( (i, j), int(Sy) )
kernel.close()
new_image = Image.merge("YCbCr", (new_image, Cb, Cr) )
new_image.save("convoluted.jpg", "JPEG")
del draw