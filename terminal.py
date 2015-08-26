import graphics


class Terminal():

    def __init__(self):
        self.create_terminal_window()

    def create_terminal_window(self):
        win = graphics.GraphWin("Testing", 890, 408)
        win.setBackground("black")
        s = "0123456789" * 8
        i = 0
        x = 446
        y = 12
        height = 16
        fontSize = 14
        for i in range(0, 25):
            t = graphics.Text(graphics.Point(x, y), s)
            t.setSize(fontSize)
            t.setFace("courier")
            t.setTextColor("white")
            t.draw(win)
            y = y + height
        win.getMouse()
        win.close()