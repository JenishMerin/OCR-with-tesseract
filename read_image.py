from PIL import Image
import pytesseract

im = Image.open("data-entry.jpg")

text = pytesseract.image_to_string(im, lang = 'eng')

print(text)