import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
from time import strftime
import adafruit_rgb_display.st7789 as st7789
from mpyg321.MPyg123Player import MPyg123Player
import csv
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

# player = MPyg123Player()
# player.play_song("/home/pi/Documents/idd/Interactive-Lab-Hub/Lab 2/songs/StillGoin.mp3")
cur_episode_scroll_position = 0
total_episodes_scroll_position = 0

scroll_speed = 3  # Adjust this for desired scrolling speed

# Load Office data from CSV
episodes = []
with open('office_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        episodes.append(row)

# Initialize counters
episode_index = 0
elapsed_seconds = 0
while True:
    # Update elapsed time
    elapsed_seconds += 1

    # Convert episode duration from minutes to seconds
    episode_duration_seconds = int(episodes[episode_index]['Duration']) * 60

    # Check if we need to move to the next episode
    while episode_index < len(episodes) and elapsed_seconds >= episode_duration_seconds:
        elapsed_seconds -= episode_duration_seconds
        episode_index += 1
        if episode_index < len(episodes):
            episode_duration_seconds = int(episodes[episode_index]['Duration']) * 60

    # Calculate current episode and percentage watched
    if episode_index < len(episodes):
        cur_episode_holder = "Current Episode: " + episodes[episode_index]['EpisodeTitle']
        percent_watched = "Percent Complete: {:.2f}%".format((elapsed_seconds / episode_duration_seconds) * 100)
    else:
        cur_episode_holder = "You've watched all episodes!"
        percent_watched = "Percent Complete: 100%"

    total_episodes = "You've Watched: " + str(episode_index) + ' episodes'

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=(23,69,157))
    
    # Check if scrolling is needed for cur_episode_holder
    text_width = draw.textlength(cur_episode_holder, font)
    if text_width > width:
        draw.text((x - cur_episode_scroll_position, -2), cur_episode_holder, font=font, fill="#FFFFFF")
        draw.text((x - cur_episode_scroll_position + text_width + 10, -2), cur_episode_holder, font=font, fill="#FFFFFF")
        cur_episode_scroll_position = (cur_episode_scroll_position + scroll_speed) % (text_width + 10)
    else:
        draw.text((x, -2), cur_episode_holder, font=font, fill="#FFFFFF")

    draw.text((x, 30), percent_watched, font=font, fill="#FFFFFF")

    # Check if scrolling is needed for total_episodes
    text_width = draw.textlength(total_episodes, font)
    if text_width > width:
        draw.text((x - total_episodes_scroll_position, 60), total_episodes, font=font, fill="#FFFFFF")
        draw.text((x - total_episodes_scroll_position + text_width + 10, 60), total_episodes, font=font, fill="#FFFFFF")
        total_episodes_scroll_position = (total_episodes_scroll_position + scroll_speed) % (text_width + 10)
    else:
        draw.text((x, 60), total_episodes, font=font, fill="#FFFFFF")

    # Display image.
    disp.image(image, rotation)
    time.sleep(1)

