import cv2 as cv 
import time 
from Windowscapture import * 
from multiOBJ import * 
from Classclick import Click


try:
    nameOfapp = "Click speed test - CPS Test Online - Brave"
    nameOfclass = "Chrome_WidgetWin_1"
    Cap = WindowCapture(nameOfapp)
    Path_target = [
        "image/click.png",]
    while(True):
        screen = Cap.screenshot() 
        search = MultiOBJ(Path_image= screen , Path_target=Path_target[0] , nameOftarget="C" , nameofscreen="Click")
        ''' Searching object by image '''
        pos = search.matchTemp(method = 'cv.TM_CCOEFF_NORMED' , showname=False , threshold=.85 , Debug=True)
        # result = search.get_color( x = 322 , y = 631 , color="0x42B72A")[0]
        for p in pos : 
            B = Click(capPro=nameOfapp , x = p[0] , y = p[1] , nameOfclass=nameOfclass,Option=True)
            B.controlClick()
            
        if cv.waitKey(1) == ord('q'):
            break
except KeyboardInterrupt as e :
    print(e)  


