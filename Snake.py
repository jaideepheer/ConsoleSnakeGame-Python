from AutoAI import AutoAI
class Snake:
    ai = AutoAI()
    length=0
    body = list()
    bodyChar="O"
    deadChar = "X"
    headChar = "0"
    head = (0,0)
    # >0 = up
    # <0 = down
    yMotion = 0.0
    ySpeed = 0.0
    # <0 = left
    # >0 = right
    xMotion = 0.0
    xSpeed = 0.0
    mode = "Normal"

    # "side" or "up" or "none"
    moving = "none"

    xtoySpeedRatio = 0.5
    def __init__(self,bodyChar,deadChar,xtoySpeedRatio,mode):
        self.xtoySpeedRatio = xtoySpeedRatio
        self.bodyChar = bodyChar
        self.deadChar = deadChar
        self.mode=mode
    def collisionCheck(self,asciicanvas):
        if self.head in self.body or not asciicanvas.isInCanvas(self.head[0],self.head[1]):
            return True
        return False
    def isMovable(self,x,y,asciicanvas):
        return (x,y) not in self.body and asciicanvas.isInCanvas(x,y)
    def updateMotion(self):
        if self.xMotion >= 1:
            self.xMotion = self.xMotion - 1
        elif self.xMotion <= -1:
            self.xMotion = self.xMotion + 1
        else:
            self.xMotion = self.xMotion + self.xSpeed
        if self.yMotion >= 1:
            self.yMotion = self.yMotion - 1
        elif self.yMotion <= -1:
            self.yMotion = self.yMotion + 1
        else:
            self.yMotion = self.yMotion + self.ySpeed
    def update(self,asciicanvas,foodspawner):
        #self.ai.update(self,foodspawner.foodList,asciicanvas)
        self.updateMotion()
        if int(self.xMotion) is 0 and int(self.yMotion) is 0:
            #stopped
            self.renderSnake(asciicanvas)
            return True
        
        # Move head
        prevHead = (self.head[0],self.head[1])
        self.head = (self.head[0]+int(self.xMotion),self.head[1]+int(self.yMotion))
        
        # Check for collision
        if self.collisionCheck(asciicanvas):
            self.head = prevHead
            self.setMotion(0,0)
            # Collided
            if self.mode is "Trap":
                if not self.isMovable(self.head[0],self.head[1]+1,asciicanvas) and not self.isMovable(self.head[0]-1,self.head[1],asciicanvas) and not self.isMovable(self.head[0],self.head[1]-1,asciicanvas) and not self.isMovable(self.head[0]+1,self.head[1],asciicanvas):
                    # Trapped
                    self.renderSnake(asciicanvas)
                    asciicanvas.writeToRenderCache(self.deadChar,self.head[0],self.head[1])
                    return False
            else:
                # Game Over
                self.renderSnake(asciicanvas)
                asciicanvas.writeToRenderCache(self.deadChar,self.head[0],self.head[1])
                return False
            return True
        
        # Update moving state
        if int(self.xMotion) is not 0:
            self.moving = "side"
        else:
            self.moving = "up"
        if prevHead not in self.body:self.body.append(prevHead)
        
        # Remove shadow
        if(len(self.body)>self.length):
            _=self.body.pop(0)

        # Render Snake
        self.renderSnake(asciicanvas)
        
        # Grow if food eaten.
        if foodspawner.hasFood(self.head[0],self.head[1]):
            self.length = self.length+1
            foodspawner.popFood(self.head[0],self.head[1])
        
        return True
    def renderSnake(self,asciicanvas):
        asciicanvas.writeToRenderCache(self.headChar,self.head[0],self.head[1])
        for l in self.body:
            asciicanvas.writeToRenderCache(self.bodyChar,l[0],l[1])
    def addLength(self,lenth):
        self.length = self.length+length
    def setMotion(self,up,side):
        self.xMotion = 0
        self.yMotion = 0
        if up is not 0:
            if self.moving is not "up":
                self.ySpeed = up*self.xtoySpeedRatio
                self.xSpeed = 0.0
        elif side is not 0:
            if self.moving is not "side":
                self.xSpeed = side
                self.ySpeed = 0.0
        elif up is 0 and side is 0:
            self.xSpeed = self.ySpeed = 0.0
