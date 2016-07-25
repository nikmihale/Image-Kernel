# Image-Kernel
Image processing using an arbitrary matrix.
This program takes a picture called 'original.jpg' and a text file called 'kernel.txt', which contains a rectangular matrix, to output a picture called 'convoluted.jpg'

Instead of splitting the original picture into RGB, here it is split into YCbCr, and convolution is applied only to luma. Boundary points are ignored: they indergo no transformation.
