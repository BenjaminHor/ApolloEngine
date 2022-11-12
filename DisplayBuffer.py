import curses


class DisplayBuffer:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.screen = ["."] * (self.width * self.height)
        self.display = curses.initscr()

    # row is y
    # column is x
    def drawAt(self, row, column, val=chr(64)):
        if row >= self.height or row < 0 or column >= self.width or column < 0:
            return
        self.screen[row * self.width + column] = val

    def getPixel(self, row, column):
        if row >= self.height or row < 0 or column >= self.width or column < 0:
            return str(-1)
        return self.screen[row * self.width + column]

    def renderBuffer(self):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                row += str(self.screen[y * self.width + x])
                if x < self.width - 1:
                    row += " "
            self.display.addstr(y, 0, row)
        self.refresh()

    def clear(self):
        self.screen = ["."] * (self.width * self.height)

    def refresh(self):
        self.display.refresh()
