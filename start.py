# The ratio of width to height of characters in the console.
XYCONSOLERATIO = 0.35
# The character representing the snake's body
SNAKEBODY = "O"
# The character shown at the snake's death point
DEATHPOINT = "X"

print("Snake Game")
print("Select mode:-\n\t1)Normal mode: You die on collision.\n\t2)Trap Death: You die only when you can't move.")
try:
    mode = int(input("Your choice:"))
except:
    mode = 1
if mode is 1:
    mode = "Normal"
elif mode is 2:
    mode = "Trap"
ch = input("Do you want to configure settings?(y/n)")
if "y" is ch[0] or "Y" is ch[0]:
    fps = int(input("Enter desired game speed (FPS):"))
    maxfood = int(input("Enter max no. of food points on map:"))
    width = int(input("Enter width of map:"))
    height = int(input("Enter height of the map:"))
else:
    fps=30
    maxfood=20
    width = 40
    height=20

from ASCIICanvas import ASCIICanvas
import time
from FoodSpawner import FoodSpawner
from Snake import Snake
import msvcrt

canvas = ASCIICanvas(width,height)
sn = Snake(SNAKEBODY,DEATHPOINT,XYCONSOLERATIO,mode)
fs = FoodSpawner(maxfood,"*")
game = True
def inputSnake(s):
    # Input
    if msvcrt.kbhit()>0 :
        c = msvcrt.getch()
        if c== b'\xe0':
            # Arrow Key
            c = msvcrt.getch()
            if c is b'H':
                # Uparrow
                s.setMotion(1,0)
            elif c is b'P':
                # Downarrow
                s.setMotion(-1,0)
            else:
                if c is b'K':
                    # Leftarrow
                    s.setMotion(0,-1)
                elif c in b'M':
                    # Rightarrow
                    s.setMotion(0,1)
    # [END] Input
def waitForTick(tickStartTime,targetFPS):
    delta = time.monotonic() - tickStartTime
    delta = (1.0/targetFPS)-delta
    if delta>0:time.sleep(delta)
# Game Loop
tickStartTime = 0
while game:
    tickStartTime = time.monotonic()
    inputSnake(sn)
    fs.update(canvas)
    if not sn.update(canvas,fs):
        game = False
    canvas.update()
    print("Score:",sn.length)
    print(mode,"Mode")
    print("\nFood:",len(fs.foodList),"/",maxfood)
    waitForTick(tickStartTime,fps)
    print("FPS:",1/(time.monotonic() - tickStartTime))

print("\n\tGame Over")
_=input()
