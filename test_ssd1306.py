from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

sda = Pin(20)
scl = Pin(21)

width = 128
height = 64

i2c = I2C(0, sda=sda, scl=scl, freq=400000)
oled = SSD1306_I2C(width, height, i2c)
oled.text("Pico", 0, 0)
oled.show()
