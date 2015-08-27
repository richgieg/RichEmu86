import graphics


class VideoController():
    """Represents a computer system's video controller."""
    
    def power_on(self):
        """Powers on this video controller."""
        print("VideoController.power_on()")
        self._create_terminal_window()

    def _create_terminal_window(self):
        # Creates the terminal window using John Zelle's graphics module.
        win = graphics.GraphWin("RichEmu86", 890, 408)
        win.setBackground("black")
        s = "RichEmu86 " * 8
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
