import time
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime

from adafruit_lsm6ds.lsm6ds3 import LSM6DS3

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = LSM6DS3(i2c)

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

wall_pos = [240, 120, 0]
speed = 5
jump_height = 7
jump_count = 16
jumps = 0

line_width = 3

game_over = False
lost_msg_1 = "GAME OVER"
lost_msg_2 = "PRESS DOWN TO RESET"

ball_pos = [[40, 100], [60, 120]]

bgrnd_clr = "#000000"
objct_clr = "#FFFFFF"

start = time.time()
current = start

i = 0
i_max = 0

while True:
    current = time.time()
    
    draw.rectangle((0, 0, width, height), outline=0, fill=bgrnd_clr)
    draw.line([(0, 120), (240, 120)], fill=objct_clr, width=3)

    draw.text((20, 10), "TIME", font=font, fill=objct_clr)
    draw.text((20, 30), str(i), font=font, fill=objct_clr)
    draw.text((160, 10), "HIGH", font=font, fill=objct_clr)
    draw.text((160, 30), str(i_max), font=font, fill=objct_clr)

    if jumps == 0 and not buttonA.value:
        jumps = jump_count

    if jumps > jump_count // 2:
        ball_pos[0][1] -= jump_height
        ball_pos[1][1] -= jump_height
        jumps -= 1
    elif jumps > 0:
        ball_pos[0][1] += jump_height
        ball_pos[1][1] += jump_height
        jumps -= 1

    draw.ellipse([tuple(x) for x in ball_pos], fill=objct_clr, width=line_width)

    wall_poses = [[(240 - wall_pos[k], 80), (240 - wall_pos[k], 120)] for k in range(3)]

    for k in range(3):
        
        wall_pos[k] = (wall_pos[k] + speed) % 240
        draw.line(wall_poses[k], fill=objct_clr, width=line_width)
        if (ball_pos[0][0] < 240 - wall_pos[k] < ball_pos[1][0] or \
             ball_pos[0][0] < 240 - wall_pos[k] + line_width < ball_pos[1][0]) and \
            ball_pos[1][1] >= 80:
            draw.rectangle((0, 0, width, height), outline=0, fill=bgrnd_clr)
            draw.text((60, 40), lost_msg_1, font=font, fill=objct_clr)
            draw.text((10, 60), lost_msg_2, font=font, fill=objct_clr)
            draw.text((60, 80), "SCORE: " + str(i), font=font, fill=objct_clr)
            disp.image(image, rotation)
            game_over = True

    if game_over:
        while game_over:
            if not buttonB.value:
                i_max = max(i_max, i)
                i = 0
                start = time.time()
                current = start
                jumps = 0
                wall_pos = [240, 120, 0]
                ball_pos = [[40, 100], [60, 120]]
                game_over = False

    else:
        i = int(current - start)

        # Display image.
        disp.image(image, rotation)
