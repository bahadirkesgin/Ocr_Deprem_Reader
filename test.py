from PIL import Image, ImageOps, ImageFilter
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Load the image using PIL
img = Image.open("../image.jpg")

# Binarize the image using ImageOps.binarize
img = ImageOps.grayscale(img)
img = ImageOps.colorize(img, black='black', white='white')

# Resize the image using Image.resize
img = img.resize((img.width * 2, img.height * 2), resample=Image.BILINEAR)

# Rotate the image using Image.rotate
img = img.rotate(0)

# Use pytesseract to extract the text from the image
text = pytesseract.image_to_string(img, lang='tur')

print(text)