#!/usr/bin/python
# -*- coding: utf-8 -*-

import helper
import get_text
import cv2
import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image
#import cv
def getCNP(image):

    # get gender

    #img = helper.cut_image(image, 80, 245, 277, 295) good
    img = helper.cut_image(image, 89, 245, 277, 295)
    #160 pixels, 13*12
    text = ""
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    for i in range(89,234,12):
        digit = helper.cut_image(image,i,i+9,277,293)
        path = "C:\\Users\\Istrati Lucian\\Admitere-OCR\\DIGIT"+str(i)+".jpg"
        cv2.imwrite(path,digit)
        t = get_text.get_text_from_image(digit)
        #t = pytesseract.image_to_string(Image.open(path))
        print(t,end=" ")
        text+=t
    """
    vertical = img
    vertical = cv.bitwise_not(vertical)
    show_wait_destroy("vertical_bit", vertical)
    
    Extract edges and smooth image according to the logic
    1. extract edges
    2. dilate(edges)
    3. src.copyTo(smooth)
    4. blur smooth img
    5. smooth.copyTo(src, edges)
    '''
    # Step 1
    edges = cv.adaptiveThreshold(vertical, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 3, -2)
    show_wait_destroy("edges", edges)
    # Step 2
    kernel = np.ones((2, 2), np.uint8)
    edges = cv.dilate(edges, kernel)
    show_wait_destroy("dilate", edges)
    # Step 3
    smooth = np.copy(vertical)
    # Step 4
    smooth = cv.blur(smooth, (2, 2))
    # Step 5
    (rows, cols) = np.where(edges != 0)
    vertical[rows, cols] = smooth[rows, cols]
    # Show final result
    show_wait_destroy("smooth - final", vertical)
    """
        

    #text = get_text.get_text_from_image(img)
    return text


def getName(image):
    final_image = helper.cut_image(image, 100, 385, 166, 184)
    text = get_text.get_text_from_image(final_image)
    return text




      
