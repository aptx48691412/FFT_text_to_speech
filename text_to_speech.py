from gtts import gTTS 
from playsound import playsound
import sys
sys.path.append('/Users/shotaro-y/Library/Python/3.8/lib/python/site-packages')
sys.path.append('/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/site-packages')
import cv2
import librosa

myText = "やはりショパンの英雄ポロネーズは美しいですね。何度でも聴きたくなる。"
language ='ja'
output = gTTS(text=myText, lang=language, slow=False)
output.save("output.mp3")

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret_,threshold=cv2.threshold(gray,0,255,cv2.THRESH_OTSU)
    cv2.imshow('frame',threshold)
    key=cv2.waitKey(1)

    if key==27:
        playsound('output.mp3')
        break


#playsound('output.mp3')
