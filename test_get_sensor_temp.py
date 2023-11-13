from machine import ADC
import time

sensor = ADC(4)

while True:
    reading = sensor.read_u16()
    voltage = reading * (3.3 / 65535)
    temperature = 27 - (voltage - 0.706) / 0.001721
    print('Temperature: ', temperature)
    time.sleep(2)
