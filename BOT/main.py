import cv2 as cv 
import os 
from Windowscapture import * 
from multiOBJ import * 

''' Check path  '''
print(os.getcwd())
nameOfapp = "LDPlayer"
Cap = WindowCapture(nameOfapp)

screen = Cap.screenshot()
search = MultiOBJ(screen , "image\g.PNG", "obj")
target  = search.matchTemp( method='cv.TM_CCOEFF_NORMED', threshold=0.89 , showname=True , Debug=True)
print(target)