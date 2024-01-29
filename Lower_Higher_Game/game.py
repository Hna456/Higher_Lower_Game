from data import game_data
from art import logo, vs
import os
import random


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


def random_account():
    """Return Data From Random Account"""
    return random.choice(game_data)


def account_info(account):
    """Format Account Into Printable Format: Name, Description And Country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}."


def comparing(guess, follower_a, follower_b):
    """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong."""
    if follower_a > follower_b:
        return guess == "A"
    else:
        return guess == "B"


def game():
    print(logo)
    score = 0
    game_on = True
    account_a = random_account()
    account_b = random_account()

    while game_on:
        account_a = account_b
        account_b = random_account()

        while account_a == account_b:
            account_b = random_account()

        print(f"Compare A: {account_info(account_a)}")
        print(vs)
        print(f"Compare B: {account_info(account_b)}")

        follower_a = account_a["follower_count"]
        follower_b = account_b["follower_count"]
        guess = input("Who has more followers? Type 'A' or 'B': ")

        checker = comparing(guess, follower_a, follower_b)

        clear()
        print(logo)
        if checker:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_on = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
