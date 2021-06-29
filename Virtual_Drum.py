import cv2
import numpy as np
import pyautogui
import imutils

def Press(key):
	pyautogui.press(key)


cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	frame = cv2.flip(frame,1)
	frame = imutils.resize(frame, height=700, width=900)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lowred = np.array([131, 90, 106])
	highred = np.array([255, 255, 255])

	lowblue = np.array([40, 150, 166])
	highblue = np.array([255, 255, 255])


	red_mask = cv2.inRange(hsv, lowred, highred)
	blue_mask = cv2.inRange(hsv, lowblue, highblue)

	cv2.rectangle(frame, (0,580), (200,700), (255,0,0),1)
	cv2.putText(frame,'TOM HI',(50,640),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
	cv2.rectangle(frame, (210,580), (430,700), (0,0,255),1)
	cv2.putText(frame,'TOM MID',(250,640),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)
	cv2.rectangle(frame, (440,580), (650,700), (255,0,0),1)
	cv2.putText(frame,'TOM LOW',(480,640),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
	cv2.rectangle(frame, (660,580), (900,700), (0,0,255),1)
	cv2.putText(frame,'KICK',(740,640),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)    
	
   
    


	contours, hierachy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)


	for cnt in contours:
		(x,y,w,h) = cv2.boundingRect(cnt)
		cv2.rectangle(frame, (x,y), (x+w, y+h),(0, 255, 0), 2)
		print(x,y)

		if x > 0 and y > 580 and x < 200 and y < 700:
		   Press('q') #TOM HI
		   break      
		if x > 210 and y > 580 and x < 430 and y < 700:
		   Press('w') #TOM MID
		   break      
		if x > 440 and y > 580 and x < 650 and x < 700:
		   Press('e') #TOM LOW 
		   break      
		if x > 660 and y > 580 and x < 900 and y < 700:
		   Press('1') #HIT HAT OPEN 
		   break

		break

	contours, hierachy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)


	for cnt in contours:
		(x,y,w,h) = cv2.boundingRect(cnt)
		cv2.rectangle(frame, (x,y), (x+w, y+h),(0, 255, 0), 2)
		print(x,y)
		break
	

	cv2.imshow('Frame', frame)

	key = cv2.waitKey(1)

	if key == 27:
		break
cap.release()
cv2.destroyAllWindows()