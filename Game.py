import time
from DisplayBuffer import DisplayBuffer
from PythonScene import PythonScene

displayBuffer = DisplayBuffer(60, 40)
currentScene = PythonScene()


def gameLoop():
    global currentScene
    delta = 0.0
    prevTime = time.time_ns()
    fpsTime = time.time_ns()

    frames = 0
    ticks = 0

    while True:
        currTime = time.time_ns()
        delta += (currTime - prevTime) / (1000000000 / 60.0)
        prevTime = currTime

        while delta >= 1.0:
            currentScene.process(displayBuffer)
            ticks += 1
            delta -= 1.0
        currentScene.render(displayBuffer)
        frames += 1

        if time.time_ns() - fpsTime > (1000000000):
            displayBuffer.display.addstr(
                displayBuffer.height + 1, 0, f"{ticks} : {frames}"
            )
            ticks = 0
            frames = 0
            fpsTime = time.time_ns()


gameLoop()
