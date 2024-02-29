from neopixel import Neopixel
import utime
import random

numpix = 10
strip = Neopixel(numpix, 0, 28, "RGB")

red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

delay = 0.5
strip.brightness(42)
blank = (0,0,0)

strip.setpixel(1, violet)
strip.show()
