class AutoAI:
    def update(self,snake,foodList,asciicanvas):
        pathFind(snake,)
        return
    def pathFind(self,snake,frm,to,asciicanvas):
        if not asciicanvas.isInCanvas(frm[0],frm[1]) or not asciicanvas.isInCanvas(to[0],to[1]):
            # end points not in canvas.
            return
        if frm[0] < to[0]:
            snake.setMotion(0,-1)
        elif frm[0] > to[0]:
            snake.setMotion(0,1)
        else:
            if frm[1] < to[1]:
                snake.setMotion(1,0)
            elif frm[1] > to[1]:
                snake.setMotion(-1,0)
        return
