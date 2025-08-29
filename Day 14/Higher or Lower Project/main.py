# Display art
from art import logo, vs
from game_data import data
import random

def celebrity_data(celebrity):
# display the data in a printable format as seen in the result
    celebrity_name = celebrity["name"]
    celebrity_description = celebrity["description"]
    celebrity_country = celebrity["country"]
    return(f"{celebrity_name}, a {celebrity_description} from {celebrity_country}")

def result(choice, a_celebrity_followers, b_celebrity_followers):
    if a_celebrity_followers > b_celebrity_followers:
        return choice == "a"
    else:
        return choice == "b"
print(logo)
score = 0
gaming = True
b_celebrity = random.choice(data)
while gaming:
    # Generate a random account from the game_data
    a_celebrity = b_celebrity
    b_celebrity = random.choice(data)

    if a_celebrity == b_celebrity:
        b_celebrity = random.choice(data)

    print(f"Compare A: {celebrity_data(a_celebrity)}")
    print(vs)
    print(f"Against B: {celebrity_data(b_celebrity)}")

    # Ask user who has more followers
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    #clear screen
    print("\n" * 20)
    print(logo)
    # check if user is correct
    a_celebrity_followers = a_celebrity["follower_count"]
    b_celebrity_followers = b_celebrity["follower_count"]
    correct_choice = result(choice, a_celebrity_followers, b_celebrity_followers)
    # Give feedback to the user for correct or incorrect
    if correct_choice:
        score += 1
        print(f"You are right ! correct score: {score}")
    else:
        print(f"Sorry that is wrong. Final score: {score}")
        gaming = False
# If user is correct let the game continue with the winning person as A and repeatable



