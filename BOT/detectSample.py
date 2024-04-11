import cv2 as cv
import numpy as np 

character = ['anya','sontaya','yur','bond',]
target_image = character[2]
Path_img = "image/spy.png"
Path_target = f"image/{target_image}.png"

img = cv.imread(Path_img , cv.IMREAD_ANYCOLOR)
assert img is not None, "file could not be read, check with os.path.exists()"
target = cv.imread(Path_target , cv.IMREAD_ANYCOLOR)
assert target is not None, "file could not be read, check with os.path.exists()"

methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

fmatch = cv.matchTemplate(img , target , eval(methods[3]))

min , max , minloc , maxloc = cv.minMaxLoc(fmatch)

print(min , minloc , max , maxloc)

W,H,_ = target.shape

topleft = maxloc
buttomright = (topleft[0] + H , topleft[1] + W)
cv.rectangle(img,topleft , buttomright , color = (0,255,0) , thickness = 4 , lineType = cv.LINE_4)

cv.putText(img , target_image , (topleft[0]+10,topleft[1]-10) , cv.FONT_ITALIC,fontScale=1 ,color=(255,0,0) , thickness=2  )

cv.imshow('spy',img)

cv.waitKey(0)
cv.destroyAllWindows()

