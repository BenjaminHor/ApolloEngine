from Scene import Scene
import keyboard


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, point):
        self.x += point.x
        self.y += point.y

    def copy(self):
        return Vector2(self.x, self.y)


class PythonScene(Scene):
    def __init__(self):
        self.direction = Vector2(0, 0)
        self.snakePos = Vector2(0, 0)

        self.tail = "#"
        self.head = "@"

        self.tailQueue = []

        self.lastDir = ""

    def process(self, displayBuffer):
        if keyboard.is_pressed("esc"):
            quit()

        # Handle player input
        elif keyboard.is_pressed("down") and self.lastDir != "up":
            self.lastDir = "down"
            self.direction.x = 0
            self.direction.y = 1
        elif keyboard.is_pressed("up") and self.lastDir != "down":
            self.lastDir = "up"
            self.direction.x = 0
            self.direction.y = -1
        elif keyboard.is_pressed("left") and self.lastDir != "right":
            self.lastDir = "left"
            self.direction.x = -1
            self.direction.y = 0
        elif keyboard.is_pressed("right") and self.lastDir != "left":
            self.lastDir = "right"
            self.direction.x = 1
            self.direction.y = 0

        self.snakePos.add(self.direction)

        # Need to cap the position
        self.snakePos.x = self.constrain(self.snakePos.x, 0, displayBuffer.width - 1)
        self.snakePos.y = self.constrain(self.snakePos.y, 0, displayBuffer.height - 1)

        self.tailQueue.insert(0, self.snakePos.copy())
        if len(self.tailQueue) > 50:
            self.tailQueue.pop()

    def render(self, displayBuffer):
        displayBuffer.clear()
        for t in self.tailQueue:
            displayBuffer.drawAt(t.y, t.x, self.tail)
        displayBuffer.drawAt(self.snakePos.y, self.snakePos.x, self.head)
        displayBuffer.renderBuffer()

    def constrain(self, x, low, high):
        if x < low:
            return low
        elif x > high:
            return high
        return x
