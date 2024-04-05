import cv2 as cv 
import os 
from Windowscapture import * 
from multiOBJ import * 

nameOfapp = "LDPlayer"
Cap = WindowCapture(nameOfapp)
screen = Cap.screenshot()
# print(os.getcwd())
# cv.imshow("LD" , screen)
# cv.waitKey(0)
# cv.destroyAllWindows()

search = MultiOBJ(screen , "image\wifi.PNG", "obj")

target  = search.matchTemp( method ='cv.TM_CCORR_NORMED',  Debug=True)