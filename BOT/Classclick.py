import win32api , win32gui , win32con



class Click : 

    def __init__(self ,capPro="", x=0 , y=0 , nameOfclass="" , ExnameOfclass="" , caption="",Option=True) -> None:
        """
        If option is True (Click on browser) , If option is False (Click on Application). 

        """
        self.x = x 
        self.y = y 
        self.capPro = capPro 
        self.nameOfclass = nameOfclass 
        self.ExnameOfclass = ExnameOfclass
        self.caption = caption 
        self.option = Option

    def gethwid(self):
        # name0fclass = 'LDPlayerMainFrame'
        # ExnameOdclass = 'RenderWindow'
        # windows name (caption) = 'TheRender'
        hwid = win32gui.FindWindow(self.nameOfclass , self.capPro) # Get it form the Autoit
        childs = win32gui.FindWindowEx(hwid , None ,self.ExnameOfclass, self.caption)
        return childs

    def ClickBrowser(self):
        return win32gui.FindWindow(self.nameOfclass , self.capPro) # Get it form the Autoit
    
    def controlClick(self): 
        l_param = win32api.MAKELONG(self.x , self.y)
        if self.option:
            win32gui.SendMessage(self.ClickBrowser() , win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON,l_param)
            win32gui.SendMessage(self.ClickBrowser() , win32con.WM_LBUTTONUP,win32con.MK_LBUTTON , l_param)
        else:
            win32gui.SendMessage(self.gethwid() , win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON,l_param)
            win32gui.SendMessage(self.gethwid() , win32con.WM_LBUTTONUP,win32con.MK_LBUTTON , l_param)

if __name__ == '__main__': 
    pass