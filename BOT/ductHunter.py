import cv2 as cv 
import os 
import pyautogui as auto
from Windowscapture import * 
from multiOBJ import * 

''' Check path  '''
# print(os.getcwd())


try:
    # https://www.crazygames.com/game/duck-hunt
    nameOfapp = "Duck Hunt 🕹️ Play on CrazyGames — Mozilla Firefox"
    Cap = WindowCapture(nameOfapp)
    while(True):
        nameofscreen = nameOfapp
        screen = Cap.screenshot()
        mulobj = {
            "Enemy1" : "image/duck1.PNG",
            "Enemy2" : "image/duck2.PNG",
            "Enemy3" : "image/duck3.PNG",
            "Enemy4" : "image/duck4.PNG",
            "Enemy5" : "image/duck5.PNG",
            "Enemy6" : "image/duck6.PNG",
            "Enemy7" : "image/duck7.PNG",
            "Enemy8" : "image/duck8.PNG",
        }
        for Ntar , pathEnemy in mulobj.items(): 
            search = MultiOBJ(Path_image=screen , Path_target=pathEnemy,nameOftarget=Ntar , nameofscreen = nameofscreen)
            target  = search.matchTemp( method='cv.TM_CCOEFF_NORMED', threshold=0.67 , showname=False , Debug=True)
            # search.mourse_cursor()
            for pos in target: 
                auto.click(button="left",x= pos[0] , y = pos[1])

        if cv.waitKey(1) == ord('q'):
            break
except KeyboardInterrupt as e:
    print(e)

