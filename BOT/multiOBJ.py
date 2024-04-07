import cv2 as cv 
import numpy as np 

class MultiOBJ : 

    def __init__(self , Path_image , Path_target , nameOftarget,nameofscreen) -> None:
        # self.image = cv.imread(Path_image , cv.IMREAD_ANYCOLOR) # Type od cv.imread is numpy array 
        self.image = Path_image
        # print(type(cv.imread(Path_image , cv.IMREAD_ANYCOLOR)) )
        assert self.image is not None, "file could not be read, check with os.path.exists()"
        self.target = cv.imread(Path_target , cv.IMREAD_ANYCOLOR)
        assert self.target is not None, "file could not be read, check with os.path.exists()"
        self.nameOftarget = nameOftarget
        self.nameOfscreen = nameofscreen
        self.Height , self.Width, _ = self.target.shape
        if self.target.shape[0] > self.image.shape[0] or self.target.shape[1] > self.image.shape[1] : 
            self.target = cv.resize(self.target , (self.image.shape[1] , self.image.shape[0]))

    def matchTemp (self , method , showname = False , threshold = 0.9 , Debug = False):
        '''
                            METHODS
        ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
        '''

        fmatch =  cv.matchTemplate(self.image , self.target , eval(method) )

        minval , maxval , minloc , maxloc = cv.minMaxLoc(fmatch)
        print("Name of the target : {}".format( self.nameOftarget))
        print("Min : {} , Minloc : {} , Max : {} , Maxloc : {}".format(minval , minloc , maxval , maxloc))

        # Locations 
        locs = np.where(fmatch >= threshold)
        locs = list(zip(*locs[::-1]))

        ''' Group rectangles '''
        recs = []
        for  l in locs : 
            # recs.append([l[0] , l[1] , self.Width , self.Height])
            recs.append([int(l[0]) , int(l[1]) , self.Width , self.Height])
            recs.append([int(l[0]) , int(l[1]) , self.Width , self.Height])


        recs = cv.groupRectangles(recs , groupThreshold=1 , eps=0.2)
        position = [[x,y] for x,y,_,_ in recs[0]]
        # print(position)
        if len(locs) == 0 :
            print(f"Adjust threshold, NO OBJECT DETECTED : {len(position)}")
        else:
            if Debug : 
                print(f"Total of the objects are : {len(position)}")
                for loc in position :       
                    buttomright = (loc[0]+self.Width , loc[1]+ self.Height)
                    cv.rectangle(self.image,loc , buttomright , color = (0,0,255) , thickness = 2 , lineType = cv.LINE_4)

                    ''' Centre of the picture '''
                    centerX = loc[0] + int(self.Width / 2 )
                    centerY = loc[1] + int(self.Height / 2 )
                    cv.drawMarker(self.image , (centerX , centerY) , color=(0,255,0) , markerSize=5 ,markerType=cv.MARKER_STAR )
                    if showname  : 
                        cv.putText(self.image , self.nameOftarget , (loc[0]+10,loc[1]-10) , cv.FONT_ITALIC,fontScale=1 ,color=(255,0,0) , thickness=1  )
        if Debug : 
            cv.imshow(self.nameOfscreen,self.image)
            # cv.waitKey(0)
            # cv.destroyAllWindows()

        return position

if __name__ == '__main__' : 
    pass 
    # character = ['coin','A','wifi']
    # target_name = character[0]
    # Path_tar = f"image/{target_name}.PNG"
    # Path_img = "image/mario.PNG"

    # myobj  = MultiOBJ(Path_img , Path_tar ,target_name )
    # positions = myobj.matchTemp(method='cv.TM_CCOEFF_NORMED',threshold=0.8,showname=False , Debug=True)
    # print(positions)
    # for pos in positions : 
    #     x = pos[0]
    #     y = pos[1]
    #     print(x,y)