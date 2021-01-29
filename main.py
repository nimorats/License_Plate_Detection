import cv2
import os
import imutils
import numpy as np
import pytesseract
from LPR import lpr
try:
    from PIL import Image
except ImportError:
    import Image

for root, dirs, files in os.walk("media/"):  
    for filename in files:
        path = "media/{}".format(filename)
        img = cv2.imread(path, 1)
        res = lpr(img, filename)
        print(res)

#OCR
#setting tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/user/Desktop/pythonpro/llt/Tesseract-OCR/tesseract'

for root, dirs, files in os.walk("ocr/"):  
    for filename in files:
        #fetching license plate number
        print(pytesseract.image_to_string(Image.open("ocr/"+filename)))



    
