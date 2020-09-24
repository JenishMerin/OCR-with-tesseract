from PIL import Image

image1 = Image.open(r'handwritten.jpg')
im1 = image1.convert('RGB')
im1.save(r'handwritten.pdf')