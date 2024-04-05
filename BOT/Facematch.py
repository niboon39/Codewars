import cv2 as cv 

class Facematch : 

    def __init__(self , Path_image , Path_target , nameOftarget) -> None:
        self.image = cv.imread(Path_image , cv.IMREAD_ANYCOLOR)
        assert self.image is not None, "file could not be read, check with os.path.exists()"
        self.target = cv.imread(Path_target , cv.IMREAD_ANYCOLOR)
        assert self.target is not None, "file could not be read, check with os.path.exists()"
        self.name = nameOftarget 

    def matchTemp (self , method):
        '''
        ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
        '''
        fmatch =  cv.matchTemplate(self.image , self.target , eval(method) )
        minval , maxval , minloc , maxloc = cv.minMaxLoc(fmatch)
        print("Name of the target : {}".format(self.name))
        print("Min : {} , Minloc : {} , Max : {} , Maxloc : {}".format(minval , minloc , maxval , maxloc))

        W,H,_ = self.target.shape
        # thershold = 0.85
        # if maxval >= thershold:
        #     topleft = maxloc
        topleft = maxloc
        buttomright = (topleft[0] + H , topleft[1] + W)
        cv.rectangle(self.image,topleft , buttomright , color = (0,255,0) , thickness = 4 , lineType = cv.LINE_4)
        cv.putText(self.image ,self.name , (topleft[0]+10,topleft[1]-10) , cv.FONT_ITALIC,fontScale=1 ,color=(255,0,0) , thickness=2  )
        cv.imshow(self.name,self.image)
        cv.waitKey(0)
        cv.destroyAllWindows()

character = ['anya','sontaya','yur','bond',]
target_name = character[3]
Path_tar = f"image/{target_name}.png"
Path_img = "image/spy.png"

mybot = Facematch(Path_image =Path_img  , Path_target=Path_tar , nameOftarget= target_name )
mybot.matchTemp(method='cv.TM_CCORR_NORMED')
