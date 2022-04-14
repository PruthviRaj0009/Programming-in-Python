'''
Generate PDF file of your 3rd Semester Mark-sheet
'''
# Pruthvi Raj
# 20CS068

import img2pdf
from PIL import Image

# Importing the image file
imp_path = "C:\\Users\\praj7\\Downloads\\20CS068.jpg"

# creating a pdf file.
pdf_path = "C:\\Users\\praj7\\Downloads\\20CS068topdf.pdf"

# creating a image file
image = Image.open(imp_path)

# creating a pdf from the image.
pdf_bytes = img2pdf.convert(image.filename)

# opening file
file = open(pdf_path, "wb")

# writing the file.
file.write(pdf_bytes)

# closing an image.
image.close()

# closing an file.
file.close()
print("Success!!")
