import random
from art import logo6, vs
from game_data import data


def format_data(account):
    """ Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess
   and returns True if they got it right.
   Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"


def game():
    print(logo6)
    score = 0
    a_account = random.choice(data)
    should_continue = True

    while should_continue:
        b_account = random.choice(data)

        if a_account == b_account:
            b_account = random.choice(data)
            print(f"Compare A: {format_data(a_account)}")
            print(vs)
            print(f"Against B: {format_data(b_account)}")
            guess = input("Who has more followers? Type 'A' or 'B': ").upper()
            a_followers_count = a_account["follower_count"]
            b_followers_count = b_account["follower_count"]
            is_correct = check_answer(guess, a_followers_count, b_followers_count)

            print(logo6)

            if is_correct:
                score += 1
                a_account = b_account
                print(f"You're right! Current score: {score}.")
            else:
                should_continue = False
                print(f"Sorry, that's wrong. Final score: {score}")


game()
