import helper
import get_text
import cv2
import levi
import config.settings
import copy
from PIL import Image
import pytesseract
import houghLines
def cropFromOneHoughLineConversion(A,color):
    h, w = firstHough.shape
    red = color
    pixels = []
    allText = ""
    h, w = firstHough.shape
    for i in range(1,h-1):
        for j in range(1,w-1):
            if A[i][j]!=red and A[i-1][j]==red and A[i-1][j-1]==red and A[i][j-1]==red:
                pixels.append((i,j))
            if A[i][j]!=red and A[i-1][j]==red and A[i-1][j+1]==red and A[i][j+1]==red:
                pixels.append((i,j))
            if A[i][j]!=red and A[i+1][j-1]==red and A[i+1][j]==red and A[i][j-1]==red:
                pixels.append((i,j))
            if A[i][j]!=red and A[i+1][j]==red and A[i+1][j+1]==red and A[i][j+1]==red:
                pixels.append((i,j))
    for i in range(len(pixels)-3):
        if levi.canBeARectangle(pixels[i],pixels[i+1],pixels[i+4],pixels[i+3])==True:
            singleRectangelImage = helper.cut_image(image, pixels[i][1], pixels[i+1][1], pixels[i][0], pixels[i+3][0])
            text = get_text.get_text_from_image(singleRectangelImage)
            allText += text
            allText +='\n'            
    return allText
    
def cropImageUsingHoughLines(image,path):
    red = (0,0,255)
    green = (0,255,0)
    A = houghLines.convertToHoughLines(path, red)
    text = cropFromOneHoughLineConversion(A,color)
    print(text)
    print("#"*20)
    B = houghLines.convertProbabilisticToHoughLines(path, green)
    text = cropFromOneHoughLineConversion(A,color)
    print(text)
     
    
def extractMarkUsingLetters(myString):
	"""
	The string format might look like this
	'7.1G (SAPTE 16%)
	$.25 (CINCI 25%)
	"""
	first = ""
	second = ""
	for i in range(len(myString)):
		if myString[i]=='(':
			first = myString[:i-1]
			second = myString[i+1:len(myString)-2]
			break
	fnum = helper.get_numbers(first)
	integerPart = 0
	fractionalPart = 0.0
	for i in range(len(second)):
		if second[i]==' ':
			integerPart = config.settings.MarkToDigit[second[:i].upper()]
			fractionalPart = int(second[i+1:])
			break
	myMark = integerPart + fractionalPart/100.0
	return myMark

def getSubject(image):
	"""
	This function extracts the name of the subject for which the student had his 2nd exam in Baccalaureate
	The second exam may be either History or Mathematics, we need to extract the mark at maths, if he has one
	"""
	img = helper.cut_image(image, 35, 200, 338, 358)
	cv2.imwrite('C:\\Users\\Istrati Lucian\\Admitere-OCR\\subject.jpg', img)
	text = get_text.get_text_from_image(img)
	"""
	if text!=None and levi.iterative_levenshtein("Limba si literatura romana - scris",text)>=10:
		img = helper.cut_image(image, 35, 200, 370, 390)
		cv2.imwrite('C:\\Users\\Istrati Lucian\\Admitere-OCR\\subject.jpg', img)
		text = get_text.get_text_from_image(img)
	
	if text!=None and levi.iterative_levenshtein("Matematica",text)<=6 or levi.iterative_levenshtein("Istorie",text)<=6:
	"""
	return text

def getSubjectInCaseSubjectRomanianLanguage(image):
	img = helper.cut_image(image, 35, 200, 385, 407)
	cv2.imwrite('C:\\Users\\Istrati Lucian\\Admitere-OCR\\subject.jpg', img)
	text = get_text.get_text_from_image(img)
	return text

def getAll(image):
	return get_text.get_text_from_image(image)
def getMathMark(image):
	"""
	To be revised - coordonations
	"""
	img = helper.cut_image(image, 300, 475, 338, 358)
	cv2.imwrite('C:\\Users\\Istrati Lucian\\Admitere-OCR\\math.jpg', img)
	text = get_text.get_text_from_image(img)
	good = extractMarkUsingLetters(text)
	######
	"""
	img = helper.cut_image(image, 35, 200, 338, 358)
	cv2.imwrite('C:\\Users\\Istrati Lucian\\Admitere-OCR\\subject.jpg', img)
	text = get_text.get_text_from_image(img)
	
	if levi.iterative_levenshtein("Limba si literatura romana - scris",text)>=10:
		img = helper.cut_image(image, 35, 200, 350, 370)
		cv2.imwrite('C:\\Users\\Istrati Lucian\\Admitere-OCR\\subject.jpg', img)
		text = get_text.get_text_from_image(img)
	"""
	########

	return good

def getAllMarks(image):
	img = helper.cut_image(image, 330, 480, 335, 460)
	cv2.imwrite('C:\\Users\\Istrati Lucian\\Admitere-OCR\\bac.jpg', img)
	good = ""
	for i in range(335,436,25):
		singleMark = helper.cut_image(image,330, 480, i,i+25)
		cv2.imwrite('C:\\Users\\Istrati Lucian\\Admitere-OCR\\bac'+str((460-i)/25)+'.jpg', singleMark)
		text = get_text.get_text_from_image(singleMark)
		t = extractMarkUsingLetters(text)
		good+=str(t)+" "
	return good

def getBacMark(image):
	img = helper.cut_image(image, 300, 475, 390, 411 )
	cv2.imwrite('C:\\Users\\Istrati Lucian\\Admitere-OCR\\bac.jpg', img)
	text = get_text.get_text_from_image(img)
	good = extractMarkUsingLetters(text)
	return good
def getMathMarkInCaseSubjectRomanianLanguage(image):
	img = helper.cut_image(image, 300, 475, 384, 403)
	cv2.imwrite('C:\\Users\\Istrati Lucian\\Admitere-OCR\\math.jpg', img)
	text = get_text.get_text_from_image(img)
	good = extractMarkUsingLetters(text)
	return good
def getBacMarkInCaseSubjectRomanianLanguage(image):
	img = helper.cut_image(image, 300, 475, 434, 454 )
	cv2.imwrite('C:\\Users\\Istrati Lucian\\Admitere-OCR\\bac.jpg', img)
	text = get_text.get_text_from_image(img)
	good = extractMarkUsingLetters(text)
	return good

def imageToBoxes(img):
	copie = img.copy
	h, w  = copie.shape
	c = 1
	pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
	boxes = pytesseract.image_to_boxes(copie) 
	counter = 0 
	for b in boxes.splitlines():
		b = b.split(' ')
		copy = cv2.rectangle(copie, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
	#cv2.imshow('singleBox'+str(counter), img)
	cv2.imwrite('C:\\Users\\Istrati Lucian\\Admitere-OCR\\boxes'+str(counter)+'.jpg',copie)
	counter+=1

"""
def main():
	print(extractMarkUsingLetters("'7.1G (SAPTE 16%)"))
	print(extractMarkUsingLetters("$.25 (CINCI 25%)"))
if __name__=='__main__':
	main()
"""
