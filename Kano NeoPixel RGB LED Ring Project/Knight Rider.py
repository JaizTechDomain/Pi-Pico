from neopixel import Neopixel
import utime

numpix = 10
strip = Neopixel(numpix, 0, 28, "RGB")

delay = 0.040

utime.sleep(delay)

red = (0, 255, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (255, 0, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (0, 175, 255)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

strip.brightness(47)
blank = (0,0,0)

 

while True:
 
    strip.show()
  ############ Left to Right ##################  
    for x in range(10):
        strip.set_pixel(x, violet)
        strip.show()
        utime.sleep(delay)
        strip.set_pixel(x, violet)
        strip.show()
        utime.sleep(delay)
        strip.set_pixel(x, violet)
        strip.show()
        utime.sleep(delay)
        strip.set_pixel(x, blank)
        utime.sleep(delay)
        strip.set_pixel(x, blank)
        utime.sleep(delay)
        strip.set_pixel(x, blank)
        strip.show()
        
          
        

        
  ############ Left to Right ##################  
    for x in reversed(range(9)):       
        strip.set_pixel(x, violet)
        utime.sleep(delay)
        strip.show()
        strip.set_pixel(x, violet)
        utime.sleep(delay)
        strip.show()
        strip.set_pixel(x, violet)
        utime.sleep(delay)
        strip.show()
        utime.sleep(delay)
        strip.set_pixel(x, blank)
        utime.sleep(delay)
        strip.set_pixel(x, blank)
        utime.sleep(delay)
        strip.set_pixel(x, blank)
        strip.show()
        
          

