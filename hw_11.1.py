# Add some more data in the dictionary of the game

# For now our game only stores the number of attempts and the date.
# Let's also store the name of the player and the secret number in each game

import random
import json
import datetime

current_time = datetime.datetime.now()

secret = random.randint(1, 30)
attempts = 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

for score_dict in score_list:
    print(str(score_dict["attempts"]) + " attempts, player: ", str(score_dict["name"]) + ", secret number: " + str(score_dict["secret"]) + ", date: " + score_dict.get("date"))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        name = input("Please state your name for the score list: ")

        score_list.append({"attempts": attempts, "name": name, "secret": secret, "date": str(datetime.datetime.now())})

        with open ("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))


        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")