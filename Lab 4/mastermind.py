import time
import board
import busio

import adafruit_mpr121
import qwiic_oled_display

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

oled = qwiic_oled_display.QwiicOledDisplay()

def oled_print(str):
    oled.begin()

    oled.clear(oled.PAGE)  #  Clear the display's buffer

    oled.print(str)  #  Add "Hello World" to buffer

    #  To actually draw anything on the display, you must call the display() function. 
    oled.display()

oled_print("mastermind.py")

# Create a list of fruits
fruits = ["apple", "banana", "orange", "pear"]

# Assign a unique keyboard key to each fruit
to_fruit_dict = {
    8: "apple",
    9: "banana",
    10: "orange",
    11: "pear"
}

# Map a fruit to a keyboard key
def map_sensor_to_fruit(in_number):
    fruit = to_fruit_dict[in_number]
    return fruit

def get_codemaker_input(i, j):
    sensor_in = input(f"{codemaker}, enter your input for row {i+1} and column {j+1}: ")
    fruit = map_sensor_to_fruit(sensor_in)
    return fruit

def get_codebreaker_guess(i, j):
    sensor_in = input(f"{codebreaker}, enter your guess for row {i+1} and column {j+1}: ")
    fruit = map_sensor_to_fruit(sensor_in)
    return fruit

def get_position(signal):
    i = signal // 2
    j = signal % 2
    return i, j

def get_input():
    pos = None
    fruit = None
    while pos is None or fruit is None:
        for i in range(4):
            if mpr121[i].value:
                pos = i

        for j in range(8, 12):
            if mpr121[j].value:
                fruit = j

    return pos, fruit

## Get the codemaker and codebreaker players ##
codemaker = input("Enter the codemaker's name: ")
codebreaker = input("Enter the codebreaker's name: ")

## Codemaker chooses the secret code ##
secret_code = [[None, None], [None, None]]

for i in range(4):
    oled_print("Codemaker: touch it")
    pos, fruit = get_input()
    i, j = get_position(pos)
    secret_code[i][j] = map_sensor_to_fruit(fruit)
    oled_print(f"{to_fruit_dict[fruit]} at {pos}")
    time.sleep(1)

print(f"secret code: {secret_code}")


## Set the limit on the number of guesses ##
guess_limit = 5
## Initialize the number of guesses the codebreaker has made ##
num_guesses = 0

player_guess = [[None, None], [None, None]]

## Game loop ##
while True:

    ## Codebreaker's turn ##
    for i in range(4):
        oled_print("Codebreaker: touch it")
        pos, fruit = get_input()
        i, j = get_position(pos)
        player_guess[i][j] = map_sensor_to_fruit(fruit)
        oled_print(f"{to_fruit_dict[fruit]} at {pos}")
        time.sleep(1)
    
    if num_guesses >= guess_limit:
        oled_print("The codemaker wins!")
        break

    print('player guess:', player_guess)

    ## Check for correctness ##
    if player_guess == secret_code:
        oled_print("Congratulations!")
        break

    num_correct_items = 0
    num_correct_positions = 0
    for i in range(2):
        for j in range(2):
            if player_guess[i][j] == secret_code[i][j]:
                num_correct_items += 1
                num_correct_positions += 1
            elif player_guess[i][j] in secret_code and player_guess[i][j] != secret_code[i][j]:
                num_correct_items += 1

    num_guesses += 1

    oled_print(f"{num_correct_items} correct items and {num_correct_positions} correct positions.")
    oled_print(f"{guess_limit-num_guesses} tries left")

## Determine the winner ##
if player_guess == secret_code:
    print(f"{codebreaker} wins!")
else:
    print(f"{codemaker} wins!")