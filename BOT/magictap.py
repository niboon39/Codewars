import cv2 as cv 
import os , time , keyboard
from Windowscapture import * 
from multiOBJ import * 
from Classclick import Click 

''' Check path  '''
# print(os.getcwd())

magictap = {

    (64, 814) : 'z',
    (196,814) : 'x',
    (341 , 814) : 'c',
    (487 , 814): 'v',
    }
time.sleep(2)
try:
    nameOfapp = "LDPlayer"
    name0fclass = 'LDPlayerMainFrame' 
    ExnameOdclass = 'RenderWindow' 
    caption = 'TheRender'
    Cap = WindowCapture(nameOfapp)
    while(True):
        nameofscreen = nameOfapp
        screen = Cap.screenshot()
        # print(screen)
        
        search = MultiOBJ(Path_image=screen  , nameofscreen = nameofscreen)
        
        for l,k in magictap.items():
            # print(search.get_color(l[0],l[1],"0x000000") )
            result = search.get_color(l[0],l[1], color='0x000000')
            if result[1] <= 50 or result[0] :
                # print(l[0] , l[1] , k)
                # keyboard.press(k)
                click = Click(nameOfapp , l[0] , l[1] , name0fclass , ExnameOdclass , caption )
                click.controlClick()
            else:
                # keyboard.release(k)
                pass 

except KeyboardInterrupt as e:
    print(e)
