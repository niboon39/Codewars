import cv2 as cv 
import os 
from Windowscapture import * 
from multiOBJ import * 

''' Check path  '''
# print(os.getcwd())
nameOfapp = "LDPlayer"
Cap = WindowCapture(nameOfapp)
while(1):
    nameofscreen = nameOfapp
    target = "obj"
    screen = Cap.screenshot()
    search = MultiOBJ(Path_image=screen , Path_target="image\ldst.PNG",nameOftarget=target , nameofscreen = nameofscreen)
    target  = search.matchTemp( method='cv.TM_CCOEFF_NORMED', threshold=0.89 , showname=False , Debug=True)
    print(target)

    if cv.waitKey(1) == ord('q'):
        break