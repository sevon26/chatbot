import numpy as np
import cv2
from flask import g, jsonify
import hashlib, random, requests, json

@staticmethod
def face_detect(image_name):
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	img = cv2.imread(img_name)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	count = 0
	for (x,y,w,h) in faces:
		count = count +1
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
		font = cv2.FONT_HERSHEY_SIMPLEX	 
		roi_gray = gray[y:y+h//2, x:x+w]
		roi_color = img[y:y+h//2, x:x+w]
	print(count)
	cv2.imshow('face_detected_1.jpg',img)
	cv2.imwrite('face_detected_1.jpg',img)

	return count