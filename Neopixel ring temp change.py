# Micro Python #

import machine
from neopixel import NeoPixel

# Define the LED pin and number of pixels
pin = machine.Pin(18)  # Adjust pin number if necessary
num_pixels = 10

# Initialize NeoPixel object
pixels = NeoPixel(pin, num_pixels)

# Define temperature thresholds and corresponding colors (adjust values as desired)
thresholds = [0, 20, 25]  # Temperature thresholds in Celsius
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]  # Corresponding colors (Blue, Green, Red)

def get_temperature():
  # Replace this function with your code to read temperature from your sensor
  # Example using a dummy sensor reading (replace with your actual sensor code)
  return 23.5

def set_led_color(temp):
  # Find the index of the threshold that the temperature falls within
  for i in range(len(thresholds) - 1):
    if temp >= thresholds[i] and temp < thresholds[i + 1]:
      return colors[i]
  # If temperature is outside the range, return the last color
  return colors[-1]

while True:
  # Read temperature
  temp = get_temperature()

  # Get the corresponding color based on temperature
  color = set_led_color(temp)

  # Set all LED colors
  for i in range(num_pixels):
    pixels[i] = color

  # Update LED strip
  pixels.write()

  # Delay for a bit
  time.sleep(1)
