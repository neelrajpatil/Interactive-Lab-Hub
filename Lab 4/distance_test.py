import time
import board
import busio
import adafruit_vcnl4040

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vcnl4040.VCNL4040(i2c)
while True:
	print(sensor.proximity)
	time.sleep(0.1)