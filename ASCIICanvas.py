import os
class ASCIICanvas:
    CLAERCONSOLECOMMAND = "cls"
    border="|"
    height=0
    width=0
    x=0
    y=0
    renderCache={}
    def writeToRenderCache(self,ch,x,y):
        if (x>=self.x+self.width or x<self.x) or (y>=self.y+self.height or y<self.y):
            # Out of Render Zone
            return
        self.renderCache[(x,y)] = ch
    def clearRenderCache(self):
        self.renderCache.clear()
    def getChar(self,x,y):
        c = " "
        try:
            c = self.renderCache[(x,y)]
        except:
            c = " "
        return c
    def __init__(self,width,height):
        self.setDimensions(width,height)
    def update(self):
        # Clear screen
        _=os.system(self.CLAERCONSOLECOMMAND)
        # Draw roof border
        print(" ",end="")
        for q in range(0,self.width):
            print(self.border,end="")
        print("")

        # X = x to x+width-1
        # Y = y+height-1 to y
        # Draw canvas
        for j in range(self.y+self.height-1,self.y-1,-1):
            print(self.border,end="")
            for i in range(self.x,self.x+self.width):
                print(self.getChar(i,j),end="")
            print(self.border)
            
        # Draw floor border
        print(" ",end="")
        for w in range(0,self.width):
            print(self.border,end="")
        print()
        self.clearRenderCache()
    def setDimensions(self,width,height):
        if(type(height) != type(0) or type(width)!=type(0)):
            return
        self.height=height
        self.width=width
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def isInCanvas(self,x,y):
        if x<self.x or x>=self.x+self.width or y<self.y or y>=self.y+self.height:
            return False
        return True
    def setPosition(self,x,y):
        if(type(x) != type(0) or type(y)!=type(0)):
            return
        self.x = x
        self.y = y
