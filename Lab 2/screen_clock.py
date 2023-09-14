import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep

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

while True: # main game loop

    wall_pos = [240, 120, 0]
    speed = 5
    jump_height = 7
    jump_count = 16
    jumps = 0

    line_width = 3

    game_over = False

    ball_pos = [[40, 100], [60, 120]]

    bgrnd_clr = "#000000"
    objct_clr = "#FFFFFF"

    i = 0
    i_max = 0

    chosen = False
    difficulty = 0

    draw.rectangle((0, 0, width, height), outline=0, fill=bgrnd_clr)
    disp.image(image, rotation)
    sleep(0.5)

    while not chosen:
        draw.rectangle((0, 0, width, height), outline=0, fill=bgrnd_clr)

        if not buttonB.value:
            difficulty = (difficulty + 1) % 3

        if not buttonA.value:
            chosen = True

        draw.text((20, 50 + difficulty * 20), "-", font=font, fill=objct_clr)

        draw.text((60, 10), "TIME KILLER", font=font, fill=objct_clr)
        draw.text((40, 50), "EASY", font=font, fill=objct_clr)
        draw.text((40, 70), "MEDIUM", font=font, fill=objct_clr)
        draw.text((40, 90), "HARD", font=font, fill=objct_clr)

        disp.image(image, rotation)
        sleep(0.1)

    draw.rectangle((0, 0, width, height), outline=0, fill=bgrnd_clr)
    draw.text((70, 40), "GO!", font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 48), fill=objct_clr)
    disp.image(image, rotation)
    sleep(1)

    start = time.time()
    current = start
    game = True

    while game:
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
                draw.text((60, 20), "GAME OVER", font=font, fill=objct_clr)
                draw.text((60, 40), "SCORE: " + str(i), font=font, fill=objct_clr)
                draw.text((60, 80), "A TO REPLAY", font=font, fill=objct_clr)
                draw.text((0, 100), "B TO CHANGE DIFFICULTY", font=font, fill=objct_clr)
                
                disp.image(image, rotation)
                game_over = True

        if game_over:
            while game_over:
                if not buttonB.value:
                    game = False
                    break
                if not buttonA.value:
                    i_max = max(i_max, i)
                    i = 0
                    start = time.time()
                    current = start
                    jumps = 0
                    wall_pos = [240, 120, 0]
                    ball_pos = [[40, 100], [60, 120]]
                    game_over = False
                    draw.rectangle((0, 0, width, height), outline=0, fill=bgrnd_clr)
                    draw.text((70, 40), "GO!", font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 48), fill=objct_clr)
                    disp.image(image, rotation)
                    sleep(0.5)

        else:
            i = int(current - start)

            # Display image.
            disp.image(image, rotation)

        sleep(0.01 + (2 - difficulty) * 0.05)
