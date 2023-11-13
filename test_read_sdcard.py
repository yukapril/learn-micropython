from machine import Pin, SPI, I2C
import sdcard
import os
from ssd1306 import SSD1306_I2C

sdcard_spi_id = 0
sdcard_cs = Pin(17)
sdcard_sck = Pin(18)
sdcard_mosi = Pin(19)
sdcard_miso = Pin(16)

ssd1305_spi_id = 0
ssd1306_sda = Pin(20)
ssd1306_scl = Pin(21)
ssd1306_width = 128
ssd1306_height = 64


def mount_sdcard():
    spi = SPI(id=sdcard_spi_id,
              baudrate=1000000,
              polarity=0,
              phase=0,
              bits=8,
              firstbit=SPI.MSB,
              sck=sdcard_sck,
              mosi=sdcard_mosi,
              miso=sdcard_miso)
    sd = sdcard.SDCard(spi, sdcard_cs)
    vfs = os.VfsFat(sd)
    os.mount(vfs, "/sd")


def write_sdcard_data():
    with open("/sd/sdtest.txt", "w") as file:
        file.write("Hello World!\r\n")
        file.write("This is a test\r\n")


def get_sdcard_data():
    with open("/sd/sdtest.txt", "r") as file:
        return file.read()


def ssd1306_show(data):
    i2c = I2C(id=ssd1305_spi_id,
              sda=ssd1306_sda,
              scl=ssd1306_scl,
              freq=400000)
    oled = SSD1306_I2C(ssd1306_width, ssd1306_height, i2c)
    for index, item in enumerate(data.split("\r\n")):
        oled.text(item, 0, index * 10)
    oled.show()


def main():
    mount_sdcard()
    data = get_sdcard_data()
    print("== sdcard data ==")
    print(data)
    ssd1306_show(data)


if (__name__ == '__main__'):
    main()
