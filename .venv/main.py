import os
from game_data import data
from art import logo, vs
import random


# Create a function to generate random numbers

def generate_random_index(data):
    random_index = random.sample(range(len(data)), 2)
    return random_index


def game_start():
    print(logo)
    score = 0
    continue_game = True
    while continue_game:
        index = generate_random_index(data)

        name = data[index[0]]["name"]
        description = data[index[0]]["description"]
        country = data[index[0]]["country"]
        follower_A = data[index[0]]["follower_count"]
        print(f"Compare A: {name}, a {description}, from {country}, with followers: {follower_A}")

        print(vs)

        name1 = data[index[1]]["name"]
        description1 = data[index[1]]["description"]
        country1 = data[index[1]]["country"]
        follower_A1 = data[index[1]]["follower_count"]

        print(f"Against B: {name1}, a {description1}, from {country1}, with followers: {follower_A1}")

        user_choice = input("Who has more followers? Type 'A' or 'B':").upper()
        if (user_choice == "A" and follower_A > follower_A1) or (user_choice == "B" and follower_A1 > follower_A):
            score += 1
            print(f"You're right! Current score: {score}")
            os.system("clear")
        elif (user_choice == "A" and follower_A < follower_A1) or (user_choice == "B" and follower_A1 < follower_A):
            continue_game = False

    if not continue_game:
        os.system("clear")
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")


game_start()

