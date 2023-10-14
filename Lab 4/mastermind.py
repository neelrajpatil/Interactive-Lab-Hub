# Create a list of fruits
fruits = ["apple", "banana", "orange", "pear"]

# Assign a unique keyboard key to each fruit
to_fruit_dict = {
    "0": "apple",
    "1": "banana",
    "2": "orange",
    "3": "pear"
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

## Get the codemaker and codebreaker players ##
codemaker = input("Enter the codemaker's name: ")
codebreaker = input("Enter the codebreaker's name: ")

## Codemaker chooses the secret code ##
secret_code = [[None, None], [None, None]]
for _ in range(4):
    # for j in range(2):
    i, j = get_position(signal)
    secret_code[i][j] = get_codemaker_input(i, j)

## Set the limit on the number of guesses ##
guess_limit = 5
## Initialize the number of guesses the codebreaker has made ##
num_guesses = 0

print('secret code:', secret_code)

player_guess = [[None, None], [None, None]]

## Game loop ##
while True:

    ## Codebreaker's turn ##
    print("Codebreaker's turn:")
    for _ in range(2):
        #for j in range(2):
        i, j = get_position(signal)
        player_guess[i][j] = get_codebreaker_guess(i,j)#input(f"{codebreaker}, enter your guess for row {i+1} and column {j+1}: ")
    
    if num_guesses >= guess_limit:
        print("Sorry, you have run out of guesses. The codemaker wins!")
        break

    print('player guess:', player_guess)

    ## Check for correctness ##
    if player_guess == secret_code:
        print("Congratulations! You guessed the correct code!")
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

    print(f"You have {num_correct_items} correct items and {num_correct_positions} correct positions.")
    print(f"You have {guess_limit-num_guesses} tries left")

## Determine the winner ##
if player_guess == secret_code:
    print(f"{codebreaker} wins!")
else:
    print(f"{codemaker} wins!")