import pygame as pg
import time
import math

points = []
size = 4
pointSize = 5 * size
gravity = 0.75 * size
deltaTime = 0.1
bounce = 0.3
background = 145, 190, 235
force = 0.4 * size

class Point():
    def __init__(self, x, y, near, far):
        self.x = x
        self.y = y
        self.px = x
        self.py = y

        self.near = near * size
        self.far = far * size
        self.color = (232, 28, 58)

def ScreenInit():
    pg.init()
    fps = 30
    width = 720
    height = 720
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Fluid Simulation")
    screen.fill(background)
    return screen

def Start():
    for x in range(100):
        points.append(Point(x + 100, 100, 8, 12))

def Distance(a, b):
    dx = a.x - b.x
    dy = a.y - b.y
    return math.sqrt(dx ** 2 + dy ** 2)

def Calculate():
    for point in points:
        px, py = point.x, point.y
        point.x, point.y = [2 * point.x - point.px, 2 * point.y - point.py]
        point.y += gravity * deltaTime

        if point.x < 0:
            point.x = 0
            px += 2 * (point.x - point.px) * bounce
        elif point.x > 720:
            point.x = 720
            px += 2 * (point.x - point.px) * bounce
        if point.y < 0:
            point.y = 0
            py += 2 * (point.y - point.py) * bounce
        elif point.y > 720:
            point.y = 720
            py += 2 * (point.y - point.py) * bounce

        for other in points:
            if other != point:
                if Distance(point, other) < point.far:
                    if other.x > point.x:
                        other.x += force
                        point.x -= force
                    elif point.x > other.x:
                        point.x += force
                        other.x -= force

                    if other.y > point.y:
                        other.y += force
                        point.y -= force
                    elif point.y > other.y:
                        point.y += force
                        other.y -= force
                elif Distance(point, other) < point.near:
                    if other.x < point.x:
                        other.x += force
                        point.x -= force
                    elif point.x < other.x:
                        point.x += force
                        other.x -= force

                    if other.y < point.y:
                        other.y += force
                        point.y -= force
                    elif point.y < other.y:
                        point.y += force
                        other.y -= force

        point.px, point.py = px, py

def Render(screen):
    screen.fill(background)
    for point in points:
        pg.draw.circle(screen, point.color, (point.x, point.y), pointSize)

def main():
    screen = ScreenInit()
    Start()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return None
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    return None

        time.sleep(0.01)
        Calculate()
        Render(screen)
        pg.display.update()

main()
pg.quit
