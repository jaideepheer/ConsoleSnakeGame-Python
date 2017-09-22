from random import random
class FoodSpawner:
    foodChar = "."
    maxFood = 10
    foodList = list()
    def __init__(self,maxFood=10,foodChar="."):
        self.maxFood = maxFood
        self.foodChar = foodChar
    def update(self,asciicanvas):
        if len(self.foodList)<self.maxFood:
            self.spawnFood(asciicanvas)
        self.renderFood(asciicanvas)
    def spawnFood(self,asciicanvas):
        pos = (int(asciicanvas.getX() + random()*(asciicanvas.getWidth())),int(asciicanvas.getY() + random()*(asciicanvas.getHeight())))
        if pos not in self.foodList:
            self.foodList.append(pos)
    def renderFood(self,asciicanvas):
        for l in self.foodList:
            asciicanvas.writeToRenderCache(self.foodChar,l[0],l[1])
    def hasFood(self,x,y):
        return (x,y) in self.foodList
    def popFood(self,x,y):
        self.foodList.remove((x,y))
