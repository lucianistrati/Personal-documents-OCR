import helper
import get_text
import image_deskew
import process_dipf
import process_dipv
#import color_detection
#import tensorflow as tf 
import numpy as np 
import matplotlib.pyplot as plt 
import myEastTextDetector
#import seabons as sns 
import imutils
import sklearn
import cv2	
import cv
import levi
import houghLines

def main():
	
	frontPath = "C:\\Users\\Istrati Lucian\\Admitere-OCR\\images\\dipf_2.png"
	img = cv2.imread(frontPath, 0)     # queryImage
	template_bac_front = cv2.imread("C:\\Users\\Istrati Lucian\\Admitere-OCR\\images\\template\\TEMPLATE_FATA_BAC.PNG", 0) # template for the front of the Baccalaureate diploma
	
	#template_bac_back = cv2.imread("C:\\Users\\Istrati Lucian\\Admitere-OCR\\images\\template\\TEMPLATE_SPATE_BAC.PNG",0) # template for the back of the Baccalaureate diploma
  	

	img = imutils.resize(img, width=1200)
	final_image = image_deskew.get_final_image(img, template_bac_front)

	cv2.imwrite('C:\\Users\\Istrati Lucian\\Admitere-OCR\\lena_opencv_red_front.jpg', final_image)
	houghLines.convertToHoughLines('C:\\Users\\Istrati Lucian\\Admitere-OCR\\lena_opencv_red_front.jpg')
	#cv2.imshow("images", final_image)
	
	#cv2.waitKey(0)  
	
	if final_image is not None:
	    cnp = process_dipf.getCNP(final_image)
	    name = process_dipf.getName(final_image)

	    print("-"*10)
	    print("CNP: ",cnp)
	    print("Nume: ",name)
	    print("-"*10)
	print('done for the front of the diploma')


	#####################################################################################
	#####################################################################################
	#####################################################################################
	
	backPath = "C:\\Users\\Istrati Lucian\\Admitere-OCR\\images\\dipv_4.png"
	img = cv2.imread(backPath, 0)
	
	template_bac_back = cv2.imread("C:\\Users\\Istrati Lucian\\Admitere-OCR\\images\\template\\myverso.jpg",0) # template for the back of the Baccalaureate diploma
	img = imutils.resize(img, width=1200)
	final_image = image_deskew.get_final_image(img, template_bac_back)
	cv2.imwrite('C:\\Users\\Istrati Lucian\\Admitere-OCR\\lena_opencv_red.jpg', final_image)
	cv2.imshow("images2", final_image)
	#myEastTextDetector.eastTextDetector(final_image)
	#myEastTextDetector.OpenCVtextDetection(final_image)
	houghLines.convertToHoughLines('C:\\Users\\Istrati Lucian\\Admitere-OCR\\lena_opencv_red.jpg')
	houghLines.convertProbabilisticToHoughLines('C:\\Users\\Istrati Lucian\\Admitere-OCR\\lena_opencv_red.jpg')
	#process_dipv.imageToBoxes(final_image) 

	#all_text = process_dipv.getAll(final_image)
	#print(all_text)
	if final_image is not None:
	    subject = process_dipv.getSubject(final_image)
	    allMarks = process_dipv.getAllMarks(final_image)
	    print(allMarks)
	    print(subject)
	    if subject!=None and (levi.iterative_levenshtein(subject,'MATEMATICA')>=6 or levi.iterative_levenshtein(subject,'MATEMATICA - scris')>=9):
	    	ok=False
	    	
	    	bacMark = process_dipv.getBacMark(final_image)
	    	print("-"*10)	
	    	#print(levi.iterative_levenshtein(subject,"Limba si literatura romana - scris"))
	    	if subject!="" and levi.iterative_levenshtein(subject,"Limba si literatura romana - scris")<=10 or subject!="" or (subject!="" and levi.howManySpaces(subject)>=3):
	    		subject = process_dipv.getSubjectInCaseSubjectRomanianLanguage(final_image)
	    		print("Subject: ",subject)
	    		if subject!="" and (levi.iterative_levenshtein(subject,'MATEMATICA')<=6 or levi.iterative_levenshtein(subject,'MATEMATICA - scris')>=9):
	    			mathMark = process_dipv.getMathMark(final_image)	
	    			bacMark = process_dipv.getBacMark(final_image)	
	    			print("Baccalaureate Mark: ",bacMark)
	    			print("Math Bac Mark:", mathMark)
	    			ok=True
	    			print("-"*10)
	    		else: 
	    			bacMark = process_dipv.getBacMarkInCaseSubjectRomanianLanguage(final_image)
	    			print("Baccalaureate Mark: ",bacMark)
	    	else:
	    		print("Baccalaureate Mark: ",bacMark)
	    	if ok==False:
	    		print("The candidat had no exam at mathematics")
	    	print("-"*10)
	    else:
	    	mathMark = process_dipv.getMathMark(final_image)
	    	bacMark = process_dipv.getBacMark(final_image)
	    	print("-"*10)
	    	print("Subject: ",subject)
	    	print("Baccalaureate Mark: ", bacMark)
	    	print("Math Bac Mark:", mathMark)
	    	print("-"*10)
	   
	print('done for the back of the diploma')
	
	
if __name__=="__main__":
	main()
